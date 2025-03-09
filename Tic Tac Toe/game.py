import pygame
from pygame.locals import *

window_width, window_height = 300, 300
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tic Tac Toe")

line_width = 6
markers = []
clicked = False
pos = []
player = 1

green = (0, 255, 0)
red = (255, 0, 0)

for i in range(3):
    row = [0] * 3
    markers.append(row)


def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(window, green, (x_pos * 100 + 15, y_pos * 100 + 15))


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
        if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked:
            clicked = False
            pos = pygame.mouse.get_pos()
            cell_x, cell_y = pos[0], pos[1]
            if markers[cell_x // 100][cell_y // 100] == 0:
                markers[cell_x // 100][cell_y // 100] = player
                player *= -1

    draw_grid()

    pygame.display.update()

pygame.quit()
