import pygame
from setting import *
from ray import Ray


class RayCaster:
    def __int__(self, player):
        self.rays = []
        self.player = player

    def cast_rays(self):
        pass

    def render(self, screen):
        for ray in self.rays:
            ray.render(screen)