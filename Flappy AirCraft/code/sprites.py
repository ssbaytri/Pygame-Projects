import pygame
from settings import *


class BG(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        bg_image = pygame.image.load("../graphics/environment/background.png").convert_alpha()
        self.image = pygame.transform.scale(bg_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.rect = self.image.get_rect(topleft=(0, 0))
