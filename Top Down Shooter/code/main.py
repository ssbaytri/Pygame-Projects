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

player = Player()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			running = False

	screen.fill("black")
	screen.blit(new_bg, (0, 0))
	screen.blit(player.new_image, player.pos)
	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()
exit()
