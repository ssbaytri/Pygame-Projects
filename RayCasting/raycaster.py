import pygame
from settings import *
from ray import Ray


class RayCaster:
    def __init__(self, player):
        self.rays = []
        self.player = player

    def cast_rays(self):
        self.rays = []
        ray_angle = (self.player.rot_angle - FOV / 2)
        for i in range(NUMS_RAYS):
            ray = Ray(ray_angle, self.player)
            ray.cast()
            self.rays.append(ray)
            ray_angle += FOV / NUMS_RAYS

    def render(self, screen):
        for ray in self.rays:
            ray.render(screen)
