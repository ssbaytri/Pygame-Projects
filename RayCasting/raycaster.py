import pygame
from settings import *
from ray import Ray


class RayCaster:
    def __init__(self, player, map):
        self.rays = []
        self.player = player
        self.map = map

    def cast_rays(self):
        self.rays = []
        ray_angle = (self.player.rot_angle - FOV / 2)
        for i in range(NUMS_RAYS):
            ray = Ray(ray_angle, self.player, self.map)
            ray.cast()
            self.rays.append(ray)
            ray_angle += FOV / NUMS_RAYS

    def render(self, screen):
        i = 0
        for ray in self.rays:
            # ray.render(screen)
            line_height = (64 / ray.distance) * (WINDOW_WIDTH / 2 * math.tan(FOV/2))
            draw_begin = (WINDOW_HEIGHT / 2) - (line_height / 2)
            pygame.draw.rect(screen, (ray.color, ray.color, ray.color), (i * RES, draw_begin, RES, line_height))
            i += 1
