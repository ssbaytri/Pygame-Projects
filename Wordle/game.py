import pygame

pygame.init()

WIDTH, HEIGHT = 500, 700
FPS = 60

COLS = 5
ROWS = 6
MARGIN = 12
LEVEL_BOX_MARGIN = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wordle")
clock = pygame.time.Clock()

level = 0
board = [['' for _ in range(COLS)] for _ in range(ROWS)]

def draw_board():
    for col in range(COLS):
        for row in range(ROWS):
            pygame.draw.rect(screen, "white", (col * 100 + MARGIN, row * 100 + MARGIN, 75, 75), 3, 5)
    pygame.draw.rect(screen, "green", (LEVEL_BOX_MARGIN, level * 100 + LEVEL_BOX_MARGIN, WIDTH - 10, 90), 3, 5)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
    
    clock.tick(FPS)
    screen.fill("black")
    draw_board()
    pygame.display.flip()

pygame.quit()
