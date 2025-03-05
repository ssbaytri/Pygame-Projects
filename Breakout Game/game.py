import pygame
from pygame.locals import *

pygame.init()

window_width, window_height = 600, 600

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Breakout")

cols = 6
rows = 6

class wall:
    def __init__(self):
        self.width = window_width // cols
        self.height = 50
        
    def create_walls(self):
        self.blocks = []
        block = []
        for row in range(rows):
            block_row = []
            for col in range(cols):
                block_x = col * self.width
                block_y = row * self.height
                rect = pygame.Rect(block_x, block_y, self.width, self.height)
                if row < 2:
                    strength = 3
                elif row < 4:
                    strength = 2
                elif row < 6:
                    strength = 1
                block = [rect, strength]
                block_row.append(block)
            self.blocks.append(block_row)
            
    def draw_walls(self):
        for row in self.blocks:
            for block in row:
                if block[1] == 3:
                    color = "blue"
                elif block[1] == 2:
                    color = "green"
                elif block[1] == 1:
                    color = "red"
                pygame.draw.rect(window, color, block[0])
                pygame.draw.rect(window, "black", block[0], 2)

wall = wall()
wall.create_walls()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
            
            
    window.fill("black")
    wall.draw_walls()
    pygame.display.update()

pygame.quit()
