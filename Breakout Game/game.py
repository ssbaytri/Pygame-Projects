import pygame
from pygame.locals import *

pygame.init()

window_width, window_height = 600, 600

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Breakout")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

pygame.quit()
