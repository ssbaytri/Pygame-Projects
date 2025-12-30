from settings import *
from math import atan2, degrees


class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.ground = True


class CollisionSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        

class Gun(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        self.player = player
        self.dist = 180
        self.player_dir = pygame.Vector2()
        
        super().__init__(groups)
        self.gun_surf = pygame.image.load(join("../images", "gun", "gun.png")).convert_alpha()
        self.image = self.gun_surf
        self.rect = self.image.get_rect(center = self.player.rect.center + self.player_dir * self.dist)
        
    def get_dir(self):
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        player_pos = pygame.Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        self.player_dir = (mouse_pos - player_pos).normalize()
        
    def rotate_gun(self):
        angle = degrees(atan2(self.player_dir.x, self.player_dir.y)) - 90
        if self.player_dir.x > 0:
            self.image = pygame.transform.rotozoom(self.gun_surf, angle, 1)
        else:
            self.image = pygame.transform.rotozoom(self.gun_surf, angle, 1)
            self.image = pygame.transform.flip(self.image, False, True)
        
    def update(self, _):
        self.get_dir()
        self.rotate_gun()
        self.rect.center = self.player.rect.center + self.player_dir * self.dist
    