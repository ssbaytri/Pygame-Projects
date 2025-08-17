import pygame
from sys import exit
import math
from settings import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top Down Shooter")
clock = pygame.time.Clock()

background = pygame.image.load("../background/background.png").convert_alpha()
new_bg = pygame.transform.scale(background, (WIDTH, HEIGHT))


class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("../player/0.png").convert_alpha()
		self.new_image = pygame.transform.rotozoom(self.image, 0, PLAYER_SIZE)
		self.base_img = self.image
		self.pos = pygame.math.Vector2(PLAYER_START_X, PLAYER_START_Y)
		self.hitbox_rect = self.base_img.get_rect(center=self.pos)
		self.rect = self.hitbox_rect.copy()
		self.speed = PLAYER_SPEED

	def player_rotation(self):
		self.mouse_cords = pygame.mouse.get_pos()
		self.x_change = (self.mouse_cords[0] - self.hitbox_rect.centerx)
		self.y_change = (self.mouse_cords[1] - self.hitbox_rect.centery)
		self.angle = math.degrees(math.atan2(self.y_change, self.x_change))
		self.new_image = pygame.transform.rotate(self.base_img, -self.angle)
		self.rect = self.new_image.get_rect(center=self.hitbox_rect.center)

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

	def move(self):
		self.pos += pygame.math.Vector2(self.vel_x, self.vel_y)
		self.hitbox_rect.center = self.pos
		self.rect.center = self.hitbox_rect.center

	def update(self):
		self.user_input()
		self.move()
		self.player_rotation()


player = Player()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			running = False

	screen.fill("black")
	screen.blit(new_bg, (0, 0))
	screen.blit(player.new_image, player.rect)
	pygame.draw.rect(screen, "red", player.hitbox_rect, 2)
	pygame.draw.rect(screen, "yellow", player.rect, 2)
	player.update()
	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()
exit()
