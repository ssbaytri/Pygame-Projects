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
		self.pos = pygame.math.Vector2(PLAYER_START_X, PLAYER_START_Y)
		self.speed = PLAYER_SPEED

	def user_input(self):
		self.vel_x = 0
		self.vel_y = 0

		keys = pygame.key.get_pressed()

		if keys[pygame.K_w]:
			self.vel_y = -self.speed
		if keys[pygame.K_s]:
			self.vel_y = self.speed
		if keys[pygame.K_a]:
			self.vel_x = -self.speed
		if keys[pygame.K_d]:
			self.vel_x = self.speed

	def move(self):
		self.pos += pygame.math.Vector2(self.vel_x, self.vel_y)

	def update(self):
		self.user_input()
		self.move()


player = Player()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			running = False

	screen.fill("black")
	screen.blit(new_bg, (0, 0))
	screen.blit(player.new_image, player.pos)
	player.update()
	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()
exit()
