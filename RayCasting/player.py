import pygame
import math
from settings import *


class Player:
    def __init__(self):
        self.x = WINDOW_WIDTH / 2
        self.y = WINDOW_HEIGHT / 2
        self.radius = 3
        self.turnDir = 0
        self.walkDir = 0
        self.rot_angle = 90 * (math.pi / 180)
        self.move_speed = 1.5
        self.rot_speed = 2 * (math.pi / 180)

    def update(self):
        keys = pygame.key.get_pressed()

        self.turnDir = 0
        self.walkDir = 0

        if keys[pygame.K_RIGHT]:
            self.turnDir = 1
        if keys[pygame.K_LEFT]:
            self.turnDir = -1
        if keys[pygame.K_UP]:
            self.walkDir = 1
        if keys[pygame.K_DOWN]:
            self.walkDir = -1

        self.rot_angle += self.turnDir * self.rot_speed
        self.rot_angle %= 2 * math.pi

        move_step = self.walkDir * self.move_speed
        self.x += math.cos(self.rot_angle) * move_step
        self.y += math.sin(self.rot_angle) * move_step

    def render(self, screen):
        pygame.draw.circle(screen, "red", (self.x, self.y), self.radius)
        pygame.draw.line(screen, "red", (self.x, self.y),
                         (self.x + math.cos(self.rot_angle) * 50, self.y + math.sin(self.rot_angle) * 50))
