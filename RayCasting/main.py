import pygame
from settings import *
from map import Map

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
game_map = Map()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()

    screen.fill("black")
    game_map.render(screen)

    pygame.display.update()
