import pygame.mixer
from grid import Grid
from blocks import IBlock, JBlock, LBlock, OBlock, SBlock, TBlock, ZBlock
import random

GAME_UPDATE = pygame.USEREVENT

class Game:
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
        pygame.mixer.Sound("asset/tetris-theme-korobeiniki-rearranged-arr-for-strings-185592.mp3").play()
        self.get_point = pygame.mixer.Sound("asset/game-start-6104.mp3")

    def random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        if not self.game_over:
            block = random.choice(self.blocks)
            self.blocks.remove(block)
            return block

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 1, 1)
        self.next_block.draw(screen, 340, 250)

    def move_left(self):
        self.current_block.move(0, -1)
        if self.current_block.check_collision(self.grid):
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if self.current_block.check_collision(self.grid):
            self.current_block.move(0, -1)

    def move_down(self):
        self.current_block.move(1, 0)
        if self.current_block.check_collision(self.grid):
            self.current_block.move(-1, 0)
            self.lock_block()

    def block_inside(self):
        return not self.current_block.check_collision(self.grid)

    def rotate(self):
        self.current_block.rotate()
        if self.current_block.check_collision(self.grid):
            self.current_block.un_rotate()

    def lock_block(self):
        tiles = self.current_block.get_cell_possition()
        for possition in tiles:
            self.grid.grid[possition.row][possition.col] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.random_block()
        line_cleared = self.grid.clear()
        self.lines_cleared += line_cleared
        self.get_score(line_cleared)
        self.check_level_up()
        if self.current_block.check_collision(self.grid):
            self.game_over = True
            self.update_highest_score()

    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.game_over = False
        self.current_block = self.random_block()
        self.next_block = self.random_block()
        self.score = 0
        self.lines_cleared = 0
        self.level = 1
        pygame.time.set_timer(GAME_UPDATE, 200)

    def get_score(self, line_cleared):
        self.get_point.play()
        if line_cleared == 1:
            self.score += 100
        elif line_cleared == 2:
            self.score += 200
        elif line_cleared == 3:
            self.score += 500
        self.update_highest_score()

    def check_level_up(self):
        if self.lines_cleared >= 2:
            self.level += 1
            self.lines_cleared -= 2
            new_speed = max(50, 300 - (self.level - 1) * 50)
            pygame.time.set_timer(GAME_UPDATE, new_speed)

    def update_highest_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
