from settings import *


class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)


class Player(Sprite):
    def __init__(self, pos, groups, collision_sprites):
        surf = pygame.Surface((40, 80))
        super().__init__(pos, surf, groups)
        
        # movement & collisions
        self.direction = pygame.Vector2()
        self.collision_sprites = collision_sprites
        self.speed = 400
        
    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        
    def collision(self, direction):
        pass
        
    def move(self, dt):
        self.rect.x += self.direction.x * self.speed * dt
        self.rect.y += self.direction.y * self.speed * dt
        
    def update(self, dt):
        self.input()
        self.move(dt)
