from settings import *
from timers import Timer


class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)


class AnimatedSprites(Sprite):
    def __init__(self, frames, pos, groups):
        self.frames, self.frame_idx, self.anim_speed = frames, 0, 10
        super().__init__(pos, self.frames[self.frame_idx], groups)
        
    def animate(self, dt):
        self.frame_idx += self.anim_speed * dt
        self.image = self.frames[int(self.frame_idx) % len(self.frames)]


class Bee(AnimatedSprites):
    def __init__(self, frames, pos, groups):
        super().__init__(frames, pos, groups)
        
    def update(self, dt):
        self.animate(dt)


class Worm(AnimatedSprites):
    def __init__(self, frames, pos, groups):
        super().__init__(frames, pos, groups)
        
    def update(self, dt):
        self.animate(dt)


class Player(AnimatedSprites):
    def __init__(self, pos, groups, collision_sprites, frames):
        super().__init__(frames, pos, groups)
        self.flip = False
        
        # movement & collisions
        self.direction = pygame.Vector2()
        self.collision_sprites = collision_sprites
        self.speed = 400
        self.gravity = 50
        self.on_floor = False
        
        # timer
        self.shoot_timer = Timer(500)
        
    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        if keys[pygame.K_SPACE] and self.on_floor:
            self.direction.y = -20
            
        if keys[pygame.K_s] and not self.shoot_timer:
            print("shoot bullet")
            self.shoot_timer.activate()
        
    def collision(self, direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if direction == "horizontal":
                    if self.direction.x > 0 : self.rect.right = sprite.rect.left
                    if self.direction.x < 0 : self.rect.left = sprite.rect.right
                if direction == "vertical":
                    if self.direction.y > 0 : self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0 : self.rect.top = sprite.rect.bottom
                    self.direction.y = 0
        
    def check_floor(self):
        bottom_rect = pygame.Rect(self.rect.left, self.rect.bottom, self.rect.width, 2)
        self.on_floor = any(bottom_rect.colliderect(sprite.rect) for sprite in self.collision_sprites)
        
    def move(self, dt):
        # horizontal
        self.rect.x += self.direction.x * self.speed * dt
        self.collision("horizontal")
        
        # vertical
        self.direction.y += self.gravity * dt
        self.rect.y += self.direction.y
        self.collision("vertical")
        
    def animate(self, dt):
        if self.direction.x:
            self.frame_idx += self.anim_speed * dt
            self.flip = self.direction.x < 0
        else:
            self.frame_idx = 0
        
        self.frame_idx = 1 if not self.on_floor else self.frame_idx
        self.image = self.frames[int(self.frame_idx) % len(self.frames)]
        self.image = pygame.transform.flip(self.image, self.flip, False)
        
    def update(self, dt):
        self.shoot_timer.update()
        self.check_floor()
        self.input()
        self.move(dt)
        self.animate(dt)
