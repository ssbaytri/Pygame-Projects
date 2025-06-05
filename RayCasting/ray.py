import pygame, math


class Ray:
    def __init__(self, angle, player):
        self.ray_angle = angle
        self.player = player

    def cast(self):
        pass

    def render(self, screen):
        pygame.draw.line(screen, "red", (self.player.x, self.player.y),
                         (
                             self.player.x + math.cos(self.ray_angle) * 50,
                             self.player.y + math.sin(self.ray_angle) * 50)
                         )
