import pygame
import random
from color import Colors

class Grid:
    """
        Lớp đại diện cho lưới trò chơi Tetris.
        Attributes:
            num_rows (int): Số hàng của lưới.
            num_cols (int): Số cột của lưới.
            size (int): Kích thước của mỗi ô trong lưới.
            grid (list): Ma trận đại diện cho lưới trò chơi.
            colors (list): Danh sách các mã màu RGB cho các ô khối.
        Methods:
            draw(screen)
            inside(row, col)
            empty(row, col)
            full(row)
            remove(row)
            move_row(row, num_rows)
            clear_line_effect(lines)
            clear()
            clear_all()
            reset()
        """
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.size = 30
        self.grid = [[0 for i in range(self.num_cols)] for j in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()
    def draw(self, screen):
        """
           Vẽ lưới.
           Argument:
               screen (pygame.Surface): Màn hình để vẽ lưới.
               """
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                val = self.grid[row][col]
                rect = pygame.Rect(col * self.size + 1, row * self.size + 1, self.size - 1, self.size - 1)
                pygame.draw.rect(screen, self.colors[val], rect)
    def inside(self, row, col):
        """
            Kiểm tra xem ô (row, col) có nằm trong lưới không.
            Argument:
                row (int): Chỉ số hàng.
                col (int): Chỉ số cột.
            Return:
                True nếu ô nằm trong lưới, ngược lại False.
                """
        return 0 <= row < self.num_rows and 0 <= col < self.num_cols
    def empty(self, row, col):
        """
            Kiểm tra xem ô (row, col) có trống không.
            Tham số:
                row (int): Chỉ số hàng.
                col (int): Chỉ số cột.
            Trả về:
                True nếu ô trống, ngược lại False.
                """
        return self.grid[row][col] == 0
    def full(self, row):
        """
            Kiểm tra xem hàng (row) có đủ các ô không.
            Argument:
                row (int): Chỉ số hàng.
            Return:
                True nếu hàng đầy, ngược lại False.
                """
        return all(self.grid[row][col] != 0 for col in range(self.num_cols))
    def remove(self, row):
        """
            Xóa tất cả các ô trong hàng (row).
            Argument:
                row (int): Chỉ số hàng.
                """
        for col in range(self.num_cols):
            self.grid[row][col] = 0
    def move_row(self, row, num_rows):
        """
            Di chuyển hàng (row) xuống dưới một số hàng (num_rows).
            Argument:
                row (int): Chỉ số hàng cần di chuyển.
                num_rows (int): Số lượng hàng để di chuyển.
                """
        for col in range(self.num_cols):
            self.grid[row + num_rows][col] = self.grid[row][col]
            self.grid[row][col] = 0
    def clear_line_effect(self, lines):
        """
            Tạo hiệu ứng xóa hàng.
            Argument:
                lines (list): Danh sách các hàng cần xóa.
                """
        screen = pygame.display.get_surface()
        for _ in range(5):
            for y in lines:
                self.grid[y] = [random.choice([0, 1]) for _ in range(self.num_cols)]
            self.draw(screen)
            pygame.display.update()
            pygame.time.delay(100)
    def clear(self):
        """
           Xóa tất cả các hàng đầy trong lưới và di chuyển các hàng còn lại xuống dưới.
           Return:
               int: Số lượng hàng đã xóa.
               """
        full = 0
        lines_to_clear = []
        for row in range(self.num_rows - 1, -1, -1):
            if self.full(row):
                lines_to_clear.append(row)
                full += 1
        if lines_to_clear:
            self.clear_line_effect(lines_to_clear)
            for row in sorted(lines_to_clear):
                self.remove(row)
                for move_row in range(row, 0, -1):
                    self.move_row(move_row - 1, 1)
        return full
    def clear_all(self):
        """
            Xóa tất cả các hàng trong lưới.
                """
        for row in range(self.num_rows):
            self.remove(row)
    def reset(self):
        """
            Đặt lại lưới về trạng thái ban đầu (tất cả các ô đều trống).
                """
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.grid[row][col] = 0
