import pygame
from settings import *
from map import Map
from player import Player

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
game_map = Map()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()

    screen.fill("black")

    player.update()
    game_map.render(screen)
    player.render(screen)

    clock.tick(FPS)
    pygame.display.update()
