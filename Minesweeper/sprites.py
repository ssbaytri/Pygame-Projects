import pygame
from settings import *
import random

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
        
        self.mine = False
        self.number = 0
        self.revealed = False
        self.flagged = False
        self.exploded = False
        
    def draw(self, screen):
        if self.revealed:
            if self.mine:
                if self.exploded:
                    screen.blit(tile_exploded, self.rect.topleft)
                else:
                    screen.blit(tile_mine, self.rect.topleft)
            elif self.number == 0:
                screen.blit(tile_empty, self.rect.topleft)
            else:
                screen.blit(tile_numbers[self.number - 1], self.rect.topleft)
        else:
            if self.flagged:
                screen.blit(tile_flag, self.rect.topleft)
            else:
                screen.blit(tile_unknown, self.rect.topleft)
                

class Board:
    def __init__(self):
        self.grid = [[Tile(x, y) for y in range(ROWS)] for x in range(COLS)]
        self.mines_placed = False
        self.game_over = False
        self.won = False
        
    def get_neighbors(self, x, y):
        neighbors = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < COLS and 0 <= ny < ROWS:
                    neighbors.append(self.grid[nx][ny])
        return neighbors
        
    def place_mines(self, first_click_x, first_click_y):
        if self.mines_placed:
            return
        
        positions = [(x, y) for x in range(COLS) for y in range(ROWS)]
        positions.remove((first_click_x, first_click_y))
        
        mine_positions = random.sample(positions, AMOUNT_MINES)
        
        for mx, my in mine_positions:
            self.grid[mx][my].mine = True
    
    def calculate_numbers(self):
        for x in range(COLS):
            for y in range(ROWS):
                tile = self.grid[x][y]
    
    def reveal(self, x, y):
        pass
    
    def flag(self, x, y):
        tile = self.grid[x][y]
        if not tile.revealed:
            tile.flagged = not tile.flagged
            
    def check_win(self):
        pass
    
    def draw(self, screen):
        for row in self.grid:
            for tile in row:
                tile.draw(screen)
