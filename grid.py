import pygame
from color import Colors
class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.size = 30
        self.grid = [[0 for i in range(self.num_cols)] for j in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()

    def draw(self,screen):

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                val = self.grid[row][col]
                rect = pygame.Rect(col* self.size+1,row*self.size+1,self.size-1,self.size-1)
                pygame.draw.rect(surface=screen , color= self.colors[val], rect= rect)
    def inside(self,row,col):
        if row >= 0 and row < self.num_rows and col >= 0 and col < self.num_cols:
            return True
        return False
    def empty(self,row,col):
        if self.grid[row][col] == 0:
            return True
        return False
    def full(self,row):
        for col in range(self.num_cols):
            if self.grid[row][col] == 0:
                return False
        return True
    def remove(self,row):
        for col in range(self.num_cols):
            self.grid[row][col] = 0
    def move_row(self,row,num_rows):
        for col in range(self.num_cols):
            self.grid[row+num_rows][col] = self.grid[row][col]
            self.grid[row][col] = 0
    def clear(self):
        full = 0
        for row in range(self.num_rows-1,0,-1):
            if self.full(row):
                self.remove(row)
                full +=1
            elif full>0:
                self.move_row(row,full)
        return full
    def reset(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.grid[row][col] = 0