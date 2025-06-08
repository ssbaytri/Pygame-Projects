import pygame
from settings import *
from map import Map
from player import Player
from raycaster import RayCaster

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
game_map = Map()
player = Player()
ray_caster = RayCaster(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()

    screen.fill("black")

    player.update()
    game_map.render(screen)
    player.render(screen)
    ray_caster.cast_rays()
    ray_caster.render(screen)

    clock.tick(FPS)
    pygame.display.update()
