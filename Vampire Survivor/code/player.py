from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(join("../images", "player", "down", "0.png")).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        
        # movement
        self.pos = pygame.Vector2(self.rect.center)
        self.direction = pygame.Vector2()
        self.speed = 500
        self.collision_sprites = collision_sprites

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.x = round(self.pos.x)
        self.collision("horizontal")
        self.rect.y = round(self.pos.y)
        self.collision("vertical")
        
    def collision(self, direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if direction == "horizontal":
                    if self.direction.x > 0 : self.rect.right = sprite.rect.left
                    if self.direction.x < 0 : self.rect.left = sprite.rect.right
                    self.pos.x = self.rect.x
                else:
                    if self.direction.y < 0 : self.rect.top = sprite.rect.bottom
                    if self.direction.y > 0 : self.rect.bottom = sprite.rect.top
                    self.pos.y = self.rect.y

    def update(self, dt):
        self.input()
        self.move(dt)
