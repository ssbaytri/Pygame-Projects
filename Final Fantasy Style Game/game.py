import pygame

pygame.init()

# game window
window_width = 800
window_height = 400

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Final Fantasy Style Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        
pygame.quit()
