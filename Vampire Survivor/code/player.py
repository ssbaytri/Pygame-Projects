from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(join("../images", "player", "down", "0.png")).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.hitbox_rect = self.rect.inflate(-60, 0)
        
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
        self.pos.x += self.direction.x * self.speed * dt
        self.hitbox_rect.x = round(self.pos.x)
        self.collision("horizontal")
        
        self.pos.y += self.direction.y * self.speed * dt
        self.hitbox_rect.y = round(self.pos.y)
        self.collision("vertical")
        
        self.rect.center = self.hitbox_rect.center
        
    def collision(self, direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.hitbox_rect):
                if direction == "horizontal":
                    if self.direction.x > 0 : self.hitbox_rect.right = sprite.rect.left
                    if self.direction.x < 0 : self.hitbox_rect.left = sprite.rect.right
                    self.pos.x = self.hitbox_rect.x
                else:
                    if self.direction.y < 0 : self.hitbox_rect.top = sprite.rect.bottom
                    if self.direction.y > 0 : self.hitbox_rect.bottom = sprite.rect.top
                    self.pos.y = self.hitbox_rect.y

    def update(self, dt):
        self.input()
        self.move(dt)
