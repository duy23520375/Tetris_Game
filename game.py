import pygame.mixer
from grid import Grid
from blocks import IBlock, JBlock, LBlock, OBlock, SBlock, TBlock, ZBlock
import random
import time

GAME_UPDATE = pygame.USEREVENT

class Game:
    """
    Lớp đại diện cho trò chơi Tetris.
    Thuộc tính:
        grid (Grid): Lưới trò chơi.
        blocks (list): Danh sách các khối Tetris.
        game_over (bool): Trạng thái kết thúc trò chơi.
        current_block (Block): Khối hiện tại đang rơi.
        next_block (Block): Khối tiếp theo sẽ rơi.
        score (int): Điểm hiện tại của trò chơi.
        highest_score (int): Điểm cao nhất đạt được.
        level (int): Mức độ hiện tại của trò chơi.
        lines_cleared (int): Số dòng đã xóa.
        bomb_image (Surface): Hình ảnh của bom.
        bomb_explosion_image (Surface): Hình ảnh của vụ nổ bom.
        freeze_image (Surface): Hình ảnh của hiệu ứng đóng băng.
        next_special_event_score (int): Điểm số tiếp theo để kích hoạt sự kiện đặc biệt.
        special_event_toggle (bool): Trạng thái chuyển đổi giữa bom và đóng băng.
        background_music (Sound): Nhạc nền của trò chơi.
        gameover_music (Sound): Nhạc kết thúc trò chơi.
    Phương thức:
        random_block()
        draw(screen)
        move_left()
        move_right()
        move_down()
        block_inside()
        rotate()
        lock_block()
        reset()
        get_score(line_cleared)
        check_level_up()
        update_highest_score()
        check_special_event()
        trigger_bomb()
        trigger_freeze()
    """
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.game_over = False
        self.current_block = self.random_block()
        self.next_block = self.random_block()
        self.score = 0
        self.highest_score = 0
        self.level = 1
        self.lines_cleared = 0

        self.background_music = pygame.mixer.Sound("asset/tetris_theme.mp3")
        self.background_music.play(-1)

        self.gameover_music = pygame.mixer.Sound("asset/game-over.mp3")
        self.bomb_image = pygame.image.load("asset/bomb.png")
        self.bomb_explosion_image = pygame.image.load("asset/explosion.png")
        self.freeze_image = pygame.image.load("asset/snowflake.png")
        self.next_special_event_score = 500
        self.special_event_toggle = True

    def random_block(self):
        """
        Chọn ngẫu nhiên một khối Tetris từ danh sách và trả về khối đó.
        Return:
            Block: Khối Tetris ngẫu nhiên.
        """
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        if not self.game_over:
            block = random.choice(self.blocks)
            self.blocks.remove(block)
            return block

    def draw(self, screen):
        """
        Vẽ lưới trò chơi và các khối hiện tại và tiếp theo lên màn hình.
        Argument:
            screen (pygame.Surface): Màn hình để vẽ trò chơi.
        """
        self.grid.draw(screen)
        if not self.game_over:
            self.current_block.draw(screen, 0, 0)
        self.next_block.draw(screen, 370, 255)

    def move_left(self):
        """
        Di chuyển khối hiện tại sang trái, nếu không va chạm với các khối khác hoặc biên.
        """
        self.current_block.move(0, -1)
        if self.current_block.check_collision(self.grid):
            self.current_block.move(0, 1)

    def move_right(self):
        """
        Di chuyển khối hiện tại sang phải, nếu không va chạm với các khối khác hoặc biên.
        """
        self.current_block.move(0, 1)
        if self.current_block.check_collision(self.grid):
            self.current_block.move(0, -1)

    def move_down(self):
        """
        Di chuyển khối hiện tại xuống dưới, nếu va chạm với khối khác hoặc đáy thì khóa khối lại.
        """
        self.current_block.move(1, 0)
        if self.current_block.check_collision(self.grid):
            self.current_block.move(-1, 0)
            self.lock_block()

    def block_inside(self):
        """
        Kiểm tra xem khối hiện tại có nằm hoàn toàn trong lưới không.
        Return:
            bool: True nếu khối không va chạm, ngược lại False.
        """
        return not self.current_block.check_collision(self.grid)

    def rotate(self):
        """
        Xoay khối hiện tại, nếu va chạm thì quay lại trạng thái ban đầu.
        """
        self.current_block.rotate()
        if self.current_block.check_collision(self.grid):
            self.current_block.un_rotate()

    def lock_block(self):
        """
        Khóa khối hiện tại vào lưới và tạo khối mới. Kiểm tra và xóa dòng nếu cần.
        Kiểm tra level hiện tại, sự kiện đặc biệt, va chạm các khối.
        """
        tiles = self.current_block.get_cell_possition()
        for possition in tiles:
            self.grid.grid[possition.row][possition.col] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.random_block()
        line_cleared = self.grid.clear()
        self.lines_cleared += line_cleared
        self.get_score(line_cleared)
        self.check_level_up()
        self.check_special_event()
        if self.current_block.check_collision(self.grid):
            self.game_over = True
            self.background_music.stop()  # Stop the background music
            self.gameover_music.play()  # Play the game-over music
            self.update_highest_score()

    def reset(self):
        """
        Đặt lại trò chơi về trạng thái ban đầu.
        """
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.game_over = False
        self.current_block = self.random_block()
        self.next_block = self.random_block()
        self.score = 0
        self.lines_cleared = 0
        self.level = 1
        self.is_frozen = False
        self.next_special_event_score = 500
        self.special_event_toggle = True
        pygame.time.set_timer(GAME_UPDATE, 200)
        self.gameover_music.stop()
        self.background_music.play(-1)

    def get_score(self, line_cleared):
        """
        Tính điểm dựa trên số dòng đã xóa và phát âm thanh.
        Cập nhật high_score.
        Argument:
            line_cleared (int): Số dòng đã xóa.
        """
        if line_cleared == 1:
            self.score += 100
            pygame.mixer.Sound("asset/game-start-6104.mp3").play()
        elif line_cleared == 2:
            self.score += 200
            pygame.mixer.Sound("asset/game-start-6104.mp3").play()
        elif line_cleared == 3:
            self.score += 500
            pygame.mixer.Sound("asset/game-start-6104.mp3").play()
        self.update_highest_score()

    def check_level_up(self):
        """
        Kiểm tra và nâng cấp độ của trò chơi dựa trên số dòng đã xóa.
        """
        if self.lines_cleared >= 3:
            self.level += 1
            self.lines_cleared -= 1
            new_speed = max(50, 400 - (self.level - 1) * 30)
            pygame.time.set_timer(GAME_UPDATE, new_speed)

    def update_highest_score(self):
        """
        Cập nhật điểm cao nhất nếu điểm hiện tại cao hơn.
        """
        if self.score > self.highest_score:
            self.highest_score = self.score

    def check_special_event(self):
        """
        Kiểm tra và kích hoạt sự kiện đặc biệt dựa trên điểm số.
        """
        if self.score >= self.next_special_event_score:
            if self.special_event_toggle:
                self.trigger_bomb()
            else:
                self.trigger_freeze()
            self.special_event_toggle = not self.special_event_toggle
            self.next_special_event_score += 500

    def trigger_bomb(self):
        """
        Kích hoạt hiệu ứng bom, xóa tất cả các dòng và thêm điểm.
        """
        screen = pygame.display.get_surface()
        bomb_rect = self.bomb_image.get_rect(center=(150, -50))
        explosion_rect = self.bomb_explosion_image.get_rect(center=(250, 325))
        for y in range(-50, 325, 5):
            bomb_rect.centery = y
            screen.blit(self.bomb_image, bomb_rect)
            pygame.display.flip()
            pygame.time.delay(10)
        pygame.mixer.Sound("asset/explosion-42132.mp3").play()
        screen.blit(self.bomb_explosion_image, explosion_rect)
        pygame.display.flip()
        pygame.time.delay(300)
        font = pygame.font.Font(None, 50)
        text_surface = font.render("Bomb triggered!", True, (255, 0, 0))
        screen.blit(text_surface, (150, 300))
        pygame.display.flip()
        pygame.time.delay(1000)
        self.grid.clear_all()
        self.score += 100
        self.update_highest_score()

    def trigger_freeze(self):
        """
        Kích hoạt hiệu ứng đóng băng, làm chậm trò chơi và thêm điểm.
        """
        self.freeze_start_time = time.time()
        self.is_frozen = True
        pygame.time.set_timer(GAME_UPDATE, 800)
        screen = pygame.display.get_surface()
        freeze_rect = self.freeze_image.get_rect(center=(250, 325))
        for alpha in range(0, 256, 5):
            self.freeze_image.set_alpha(alpha)
            screen.blit(self.freeze_image, freeze_rect)
            pygame.display.flip()
            pygame.time.delay(10)
        pygame.mixer.Sound("asset/snow.mp3").play()
        font = pygame.font.Font(None, 50)
        text_surface = font.render("Freeze triggered!", True, (0, 0, 255))
        screen.blit(text_surface, (150, 400))
        pygame.display.flip()
        pygame.time.delay(1000)
