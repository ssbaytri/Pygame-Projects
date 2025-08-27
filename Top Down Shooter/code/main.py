import pygame
from sys import exit
import math
import random
from settings import *
import csv

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top Down Shooter")
clock = pygame.time.Clock()

# background = pygame.image.load("../background/background.png").convert_alpha()
new_bg = pygame.image.load("../background/ground.png").convert_alpha()

all_sprites = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

wall_rects = []

def load_wall_layer(path):
    with open(path, newline='') as f:
        reader = csv.reader(f)
        return [[int(cell) for cell in row] for row in reader]

def find_valid_spawn_position():
    wall_data = load_wall_layer("../data/csvfiles/Map_Walls.csv")
    max_attempts = 100
    
    for _ in range(max_attempts):
        x = random.randint(10, len(wall_data[0]) - 10)  # Stay away from edges
        y = random.randint(10, len(wall_data) - 10)
        
        if wall_data[y][x] == -1:
            pixel_x = x * TILE_SIZE + TILE_SIZE // 2
            pixel_y = y * TILE_SIZE + TILE_SIZE // 2
            return (pixel_x, pixel_y)
    
    return (1000, 1000)

for y, row in enumerate(load_wall_layer("../data/csvfiles/Map_Walls.csv")):
    for x, tile_id in enumerate(row):
        if tile_id != -1:
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            wall_rects.append(rect)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.vel_y = None
		self.vel_x = None
		self.image = pygame.transform.rotozoom(pygame.image.load("../player/0.png").convert_alpha(), 0, PLAYER_SIZE)
		self.base_img = self.image
		self.pos = pygame.math.Vector2(PLAYER_START_X, PLAYER_START_Y)
		self.hitbox_rect = self.base_img.get_rect(center=self.pos)
		self.rect = self.hitbox_rect.copy()
		self.speed = PLAYER_SPEED
		self.shooting = False
		self.shoot_cooldown = 0
		self.gun_barrel_offset = pygame.math.Vector2(GUN_OFFSET_X, GUN_OFFSET_Y)

	def player_rotation(self):
		mouse_x, mouse_y = pygame.mouse.get_pos()
		dx = mouse_x - (WIDTH // 2)
		dy = mouse_y - (HEIGHT // 2)
		self.angle = math.degrees(math.atan2(dy, dx))
		self.image = pygame.transform.rotate(self.base_img, -self.angle)
		self.rect = self.image.get_rect(center=self.hitbox_rect.center)

	def user_input(self):
		direction = pygame.math.Vector2(0, 0)
		keys = pygame.key.get_pressed()

		if keys[pygame.K_w]:
			direction.y = -1
		if keys[pygame.K_s]:
			direction.y = 1
		if keys[pygame.K_a]:
			direction.x = -1
		if keys[pygame.K_d]:
			direction.x = 1

		if direction.length() != 0:
			direction = direction.normalize() * self.speed

		self.vel_x = direction.x
		self.vel_y = direction.y

		if pygame.mouse.get_pressed()[0] or keys[pygame.K_SPACE]:
			self.shooting = True
			self.is_shooting()
		else:
			self.shooting = False

	def is_shooting(self):
		if self.shoot_cooldown == 0:
			self.shoot_cooldown = SHOOT_COOLDOWN
			bullet_pos = self.pos + self.gun_barrel_offset.rotate(self.angle)
			self.bullet = Bullet(bullet_pos[0], bullet_pos[1], self.angle)
			bullet_group.add(self.bullet)
			all_sprites.add(self.bullet)

	def move(self):
		new_pos = self.pos + pygame.math.Vector2(self.vel_x, self.vel_y)
		new_rect = self.hitbox_rect.copy()
		new_rect.center = new_pos

		for wall in wall_rects:
			if new_rect.colliderect(wall):
				return

		self.pos = new_pos
		self.hitbox_rect.center = self.pos
		self.rect.center = self.hitbox_rect.center

	def update(self):
		self.user_input()
		self.move()
		self.player_rotation()

		if self.shoot_cooldown > 0:
			self.shoot_cooldown -= 1


class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y, angle):
		super().__init__()
		self.base_image = pygame.image.load("../bullet/1.png").convert_alpha()
		self.image = pygame.transform.rotozoom(self.base_image, 0, BULLET_SCALE)
		self.rect = self.image.get_rect(center=(x, y))
		self.x = x
		self.y = y
		self.angle = angle
		self.speed = BULLET_SPEED
		self.x_vel = math.cos(math.radians(self.angle)) * self.speed
		self.y_vel = math.sin(math.radians(self.angle)) * self.speed
		self.bullet_lifetime = BULLET_LIFETIME
		self.spawn_time = pygame.time.get_ticks()

	def move(self):
		self.x += self.x_vel
		self.y += self.y_vel
		self.rect.center = (int(self.x), int(self.y))

		if pygame.time.get_ticks() - self.spawn_time > self.bullet_lifetime:
			self.kill()

	def update(self):
		self.move()


class Camera(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.offset = pygame.math.Vector2()
		self.floor_rect = new_bg.get_rect(topleft=(0, 0))

	def custom_draw(self):
		self.offset.x = player.rect.centerx - WIDTH // 2
		self.offset.y = player.rect.centery - HEIGHT // 2

		floor_offset = self.floor_rect.topleft - self.offset
		screen.blit(new_bg, floor_offset)

		for sprite in all_sprites:
			offset_pos = sprite.rect.topleft - self.offset
			screen.blit(sprite.image, offset_pos)


class Enemy(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__(enemy_group, all_sprites)
		self.image = pygame.image.load("../necromancer/hunt/0.png").convert_alpha()
		self.image = pygame.transform.rotozoom(self.image, 0, 2)
		self.rect = self.image.get_rect(center=pos)

		self.direction = pygame.math.Vector2()
		self.vel = pygame.math.Vector2()
		self.speed = ENEMY_SPEED
		self.position = pygame.math.Vector2(pos)

	def hunt_player(self):
		player_vec = pygame.math.Vector2(player.hitbox_rect.center)
		enemy_vec = pygame.math.Vector2(self.rect.center)
		dist = self.get_distance(player_vec, enemy_vec)

		if dist > 0:
			self.direction = (player_vec - enemy_vec).normalize()
		else:
			self.direction = pygame.math.Vector2()
		self.vel = self.direction * self.speed
		self.position += self.vel

		self.rect.center = self.position

	def get_distance(self, vec1, vec2):
		return (vec1 - vec2).magnitude()

	def update(self):
		self.hunt_player()


camera = Camera()
player = Player()
enemy = Enemy(find_valid_spawn_position())

all_sprites.add(player)

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			running = False

	screen.fill("black")
	# all_sprites.draw(screen)
	camera.custom_draw()
	all_sprites.update()
	clock.tick(FPS)
	pygame.display.flip()

pygame.quit()
exit()
