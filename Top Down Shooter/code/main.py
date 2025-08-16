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

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			running = False

	screen.fill("black")
	screen.blit(new_bg, (0, 0))
	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()
exit()
