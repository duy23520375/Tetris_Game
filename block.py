from color import Colors
from location import Position
import pygame

class Block:
    """
        Lớp đại diện cho một khối trong trò chơi Tetris.
        Attributes:
            id (str): id của khối.
            cells (dict): Từ điển chứa các trạng thái xoay của khối.
            size (int): Kích thước của một ô trong khối.
            state (int): Trạng thái xoay hiện tại của khối.
            colors (dict): Từ điển chứa mã màu của các khối.
            rowNUM (int): Vị trí hàng hiện tại của khối.
            colNUM (int): Vị trí cột hiện tại của khối.
        Methods:
            draw(screen, x, y)
            move(row, col)
            get_cell_possition()
            rotate()
            un_rotate()
            check_collision(grid)
        """
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.size = 30
        self.state = 0
        self.colors = Colors.get_cell_colors()
        self.rowNUM = 0
        self.colNUM = 0
    def draw(self, screen, x, y):
        """
        Vẽ khối.
        Arguments:
            screen (pygame.Surface): Màn hình để vẽ khối.
            x (int): Tọa độ x của vị trí vẽ.
            y (int): Tọa độ y của vị trí vẽ.
                """
        tiles = self.get_cell_possition()
        for tile in tiles:
            t_rect = pygame.Rect(tile.col * self.size + x, tile.row * self.size + y, self.size - 1, self.size - 1)
            pygame.draw.rect(screen, self.colors[self.id], t_rect, 0, 7)
    def move(self, row, col):
        """
        Di chuyển khối theo hàng và cột đã chỉ định.
        Argument:
            row (int): Số hàng để di chuyển.
            col (int): Số cột để di chuyển.
                """
        self.rowNUM += row
        self.colNUM += col
    def get_cell_possition(self):
        """
        Lấy vị trí các ô của khối.
        Return:
            list[Position]: Danh sách các vị trí ô của khối.
                """
        tiles = self.cells[self.state]
        moved_tile = []
        for possition in tiles:
            possition = Position(possition.row + self.rowNUM, possition.col + self.colNUM)
            moved_tile.append(possition)
        return moved_tile

    def rotate(self):
        """
            Xoay khối .
                """
        self.state += 1
        if self.state == len(self.cells):
            self.state = 0
    def un_rotate(self):
        """
            Xoay khối theo hướng ngược lại.
                """
        self.state -= 1
        if self.state < 0:
            self.state = len(self.cells) - 1
    def check_collision(self, grid):
        """
            Kiểm tra xem khối có va chạm với biên lưới hoặc các khối khác không.
            Argument:
                grid (Grid): Lưới để kiểm tra va chạm.
            Return:
                True nếu có va chạm, ngược lại False.
                """
        for pos in self.get_cell_possition():
            if not grid.inside(pos.row, pos.col) or not grid.empty(pos.row, pos.col):
                return True
        return False
