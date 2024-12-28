import pygame

pygame.init()

WIN_WIDTH = 900
WIN_HEIGHT = 950

pygame.display.set_caption("Pacman")
display = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
timer = pygame.time.Clock()
FPS = 60
# font = pygame.font.Font("freesansbold.tff", 20)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
    
    timer.tick(FPS)
    display.fill("black")
    pygame.display.flip()

pygame.quit()