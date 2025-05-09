import pygame
import math
from settings import *


class Player:
    def __init__(self):
        self.x = WINDOW_WIDTH / 2
        self.y = WINDOW_HEIGHT / 2
        self.radius = 6

    def render(self, screen):
        pygame.draw.circle(screen, "red", (self.x, self.y), self.radius)
