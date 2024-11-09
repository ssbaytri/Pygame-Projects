import pygame

# Game Setup
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Racer")
surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
timer = pygame.time.Clock()
FPS = 60

# Assets loading


def draw_screen():
    pygame.draw.rect(screen, (32, 42, 68), [0, HEIGHT - 100, WIDTH, 100])
    pygame.draw.rect(screen, "white", [0, 0, WIDTH, HEIGHT], 5)
    pygame.draw.line(screen, "white", (250, HEIGHT - 100), (250, HEIGHT), 2)
    pygame.draw.line(screen, "white", (700, HEIGHT - 100), (700, HEIGHT), 2)
    pygame.draw.line(screen, "white", (0, HEIGHT - 100), (WIDTH, HEIGHT - 100), 2)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    screen.fill("gray")
    timer.tick(FPS)
    draw_screen()

    pygame.display.flip()
pygame.quit()
