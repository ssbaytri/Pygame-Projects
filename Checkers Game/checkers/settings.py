import pygame

ROWS, COLS = 8, 8
TILE_SIZE = 80
WIDTH, HEIGHT = COLS * TILE_SIZE, ROWS * TILE_SIZE
FPS = 60

LIGHT_TILES = "#DDB892"
DARK_TILES = "#6B4226"
P1_COLOR = "#000000"
P2_COLOR = "#FFFFF0"

CROWN = pygame.transform.scale(pygame.image.load("assets/crown.png"), (44, 25))
