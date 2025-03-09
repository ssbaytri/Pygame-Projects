import pygame
from pygame.locals import *

window_width, window_height = 300, 300
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tic Tac Toe")

line_width = 6
markers = []

for i in range(3):
    row = [0] * 3
    markers.append(row)


def draw_grid():
    bg_color = (25, 25, 35)
    grid_color = (70, 70, 100)
    window.fill(bg_color)
    for x in range(1, 3):
        pygame.draw.line(window, grid_color, (0, x * 100), (window_width, x * 100), line_width)
        pygame.draw.line(window, grid_color, (x * 100, 0), (x * 100, window_height), line_width)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    draw_grid()

    pygame.display.update()

pygame.quit()
