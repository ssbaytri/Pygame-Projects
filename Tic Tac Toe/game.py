import pygame
from pygame.locals import *

window_width, window_height = 300, 300
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tic Tac Toe")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

pygame.quit()
