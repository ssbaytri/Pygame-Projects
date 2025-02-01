import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

# game window
bottom_panel = 150
window_width = 800
window_height = 400 + bottom_panel

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Final Fantasy Style Game")

# load images
bg_img = pygame.image.load("img/Background/background.png").convert_alpha()
panel_img = pygame.image.load("img/Icons/panel.png").convert_alpha()

def drwa_bg():
    window.blit(bg_img, (0, 0))
    
def draw_panel():
    window.blit(panel_img, (0, window_height - bottom_panel))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
            
    clock.tick(FPS)
    drwa_bg()
    draw_panel()
    pygame.display.update()
        
pygame.quit()
