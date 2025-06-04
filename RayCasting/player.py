import pygame
import math
from settings import *


class Player:
    def __init__(self):
        self.x = WINDOW_WIDTH / 2
        self.y = WINDOW_HEIGHT / 2
        self.radius = 3
        self.turn_dir = 0
        self.walk_dir = 0
        self.rot_angle = math.pi / 4
        self.mov_speed = 1
        self.rot_speed = 1.5 * (math.pi / 180)

    def update(self):
        keys = pygame.key.get_pressed()

        self.turn_dir = 0
        self.walk_dir = 0

        if keys[pygame.K_RIGHT]:
            self.turn_dir = 1
        if keys[pygame.K_LEFT]:
            self.turn_dir = -1
        if keys[pygame.K_UP]:
            self.walk_dir = 1
        if keys[pygame.K_DOWN]:
            self.walk_dir = -1

        move_step = self.walk_dir * self.mov_speed
        self.rot_angle += self.turn_dir * self.rot_speed
        self.x += math.cos(self.rot_angle) * move_step
        self.y += math.sin(self.rot_angle) * move_step

    def render(self, screen):
        pygame.draw.circle(screen, "red", (self.x, self.y), self.radius)

        pygame.draw.line(screen, "red", (self.x, self.y),
                         (self.x + math.cos(self.rot_angle) * 50, self.y + math.sin(self.rot_angle) * 50))
