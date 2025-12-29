from settings import *


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
    def __inti__(self, player, groups):
        self.player = player
        self.dist = 140
        self.player_dir = pygame.Vector2(1, 0)
        
        super().__init__(groups)
        self.gun_surf = pygame.image.load(join("../images", "gun", "gun.png")).convert_alpha()
        self.image = self.gun_surf
    