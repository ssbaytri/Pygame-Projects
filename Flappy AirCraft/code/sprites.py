import pygame
from settings import *
from random import choice, randint


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
        self.sprite_type = "ground"
        ground_surf = pygame.image.load("../graphics/environment/ground.png").convert_alpha()
        self.image = pygame.transform.scale(ground_surf, pygame.math.Vector2(ground_surf.get_size()) * scale_factor)

        self.rect = self.image.get_rect(bottomleft=(0, WINDOW_HEIGHT))
        self.pos = pygame.math.Vector2(self.rect.topleft)

        self.mask = pygame.mask.from_surface(self.image)

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

        self.mask = pygame.mask.from_surface(self.image)

        self.gravity = 600
        self.direction = 0

        self.jump_sound = pygame.mixer.Sound("../sounds/jump.wav")
        self.jump_sound.set_volume(0.3)

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

    def jump(self):
        self.jump_sound.play()
        self.direction = -400

    def animate(self, dt):
        self.frame_idx += 10 * dt
        if self.frame_idx >= len(self.frames):
            self.frame_idx = 0
        self.image = self.frames[int(self.frame_idx)]

    def rotate(self, dt):
        rotated_plane = pygame.transform.rotozoom(self.image, -self.direction * 0.06, 1)
        self.image = rotated_plane
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt):
        self.gravity_logic(dt)
        self.animate(dt)
        self.rotate(dt)


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, scale_factor, *groups):
        super().__init__(*groups)
        self.sprite_type = "obstacle"
        obstacle_orientation = choice(["up", "down"])
        surf = pygame.image.load(f"../graphics/obstacles/{choice((0, 1))}.png").convert_alpha()
        self.image = pygame.transform.scale(surf, pygame.math.Vector2(surf.get_size()) * scale_factor)

        x = WINDOW_WIDTH + randint(40, 100)

        if obstacle_orientation == "up":
            y = WINDOW_HEIGHT + randint(10, 50)
            self.rect = self.image.get_rect(midbottom=(x, y))
        else:
            y = randint(-50, -10)
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect = self.image.get_rect(midtop=(x, y))

        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt):
        self.pos.x -= 400 * dt
        self.rect.x = round(self.pos.x)
        if self.rect.right <= -100:
            self.kill()

# END OF THE GAME
