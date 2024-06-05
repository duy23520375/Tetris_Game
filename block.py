from color import Colors
from location import Possition
import pygame

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.size = 30
        self.state = 0
        self.colors = Colors.get_cell_colors()
        self.rowNUM = 0
        self.colNUM = 0

    def draw(self, screen, x, y):
        tiles = self.get_cell_possition()
        for tile in tiles:
            t_rect = pygame.Rect(tile.col * self.size + x, tile.row * self.size + y, self.size - 1, self.size - 1)
            pygame.draw.rect(screen, self.colors[self.id], t_rect, 0, 7)

    def move(self, row, col):
        self.rowNUM += row
        self.colNUM += col

    def get_cell_possition(self):
        tiles = self.cells[self.state]
        moved_tile = []
        for possition in tiles:
            possition = Possition(possition.row + self.rowNUM, possition.col + self.colNUM)
            moved_tile.append(possition)
        return moved_tile

    def rotate(self):
        self.state += 1
        if self.state == len(self.cells):
            self.state = 0

    def un_rotate(self):
        self.state -= 1
        if self.state < 0:
            self.state = len(self.cells) - 1

    def check_collision(self, grid):
        for pos in self.get_cell_possition():
            if not grid.inside(pos.row, pos.col) or not grid.empty(pos.row, pos.col):
                return True
        return False
