from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.load_images()
        self.state, self.frame_idx = "down", 0
        self.image = pygame.image.load(join("../images", "player", "down", "0.png")).convert_alpha()
        self.rect = self.image.get_rect(topright=pos)
        self.hitbox_rect = self.rect.inflate(-60, -90)
        
        # movement
        self.pos = pygame.Vector2(self.rect.center)
        self.direction = pygame.Vector2()
        self.speed = 500
        self.collision_sprites = collision_sprites
        
    def load_images(self):
        self.frames = {"left": [], "right": [], "up": [], "down": []}
        
        for state in self.frames.keys():
            for folder_path, sub_folders, file_names in walk(join("../images", "player", state)):
                if file_names:
                    for file_name in sorted(file_names, key= lambda name: int(name.split('.')[0])):
                        full_path = join(folder_path, file_name)
                        surf = pygame.image.load(full_path)
                        self.frames[state].append(surf)

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
    def animate(self, dt):
        # get state
        if self.direction.x != 0:
            self.state = "right" if self.direction.x > 0 else "left"
        if self.direction.y != 0:
            self.state = "down" if self.direction.y > 0 else "up"
        
        # animate
        self.frame_idx = self.frame_idx + 5 * dt if self.direction else 0
        self.image = self.frames[self.state][int(self.frame_idx) % len(self.frames[self.state])]

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)
