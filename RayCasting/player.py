import pygame
import math
from settings import *


class Player:
    def __init__(self):
        self.x = WINDOW_WIDTH / 2
        self.y = WINDOW_HEIGHT / 2
        self.radius = 3
        self.rot_angle = math.pi / 4

    def render(self, screen):
        pygame.draw.circle(screen, "red", (self.x, self.y), self.radius)

        pygame.draw.line(screen, "red", (self.x, self.y),
                         (self.x + math.cos(self.rot_angle) * 50, self.y + math.sin(self.rot_angle) * 50))
