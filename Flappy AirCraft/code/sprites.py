import pygame
from settings import *


class BG(pygame.sprite.Sprite):
    def __init__(self, scale_factor, *groups):
        super().__init__(*groups)
        bg_image = pygame.image.load("../graphics/environment/background.png").convert_alpha()

        full_width = bg_image.get_width() * scale_factor
        full_height = bg_image.get_height() * scale_factor
        full_sized_image = pygame.transform.scale(bg_image, (full_width, full_height))

        self.image = pygame.Surface((full_width * 2, full_height))
        self.image.blit(full_sized_image, (0, 0))
        self.image.blit(full_sized_image, (full_width, 0))
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.pos = pygame.math.Vector2(self.rect.topleft)

    def update(self, dt):
        self.pos.x -= 300 * dt
        self.rect.x = round(self.pos.x)
        if self.rect.centerx <= 0:
            self.pos.x = 0


class Ground(pygame.sprite.Sprite):
    def __init__(self, scale_factor, *groups):
        super().__init__(*groups)
        ground_surf = pygame.image.load("../graphics/environment/ground.png").convert_alpha()
        self.image = pygame.transform.scale(ground_surf, pygame.math.Vector2(ground_surf.get_size()) * scale_factor)

        self.rect = self.image.get_rect(bottomleft=(0, WINDOW_HEIGHT))
        self.pos = pygame.math.Vector2(self.rect.topleft)

    def update(self, dt):
        self.pos.x -= 360 * dt
        self.rect.x = round(self.pos.x)
        if self.rect.centerx <= 0:
            self.pos.x = 0


class Plane(pygame.sprite.Sprite):
    def __init__(self, scale_factor, *groups):
        super().__init__(*groups)

        self.import_frames(scale_factor)
        self.frame_idx = 0
        self.image = self.frames[self.frame_idx]

        self.rect = self.image.get_rect(midleft=(WINDOW_WIDTH / 20, WINDOW_HEIGHT / 2))
        self.pos = pygame.math.Vector2(self.rect.topleft)

        self.gravity = 250
        self.direction = 0

    def import_frames(self, scale_factor):
        self.frames = []
        for i in range(3):
            surf = pygame.image.load(f"../graphics/plane/red{i}.png").convert_alpha()
            scaled_surf = pygame.transform.scale(surf, pygame.math.Vector2(surf.get_size()) * scale_factor)
            self.frames.append(scaled_surf)

    def gravity_logic(self, dt):
        self.direction += self.gravity * dt
        self.pos.y += self.direction * dt
        self.rect.y = round(self.pos.y)

    def update(self, dt):
        self.gravity_logic(dt)
