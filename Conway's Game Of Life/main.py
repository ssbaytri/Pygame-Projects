import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game Of Life")
clock = pygame.time.Clock()

def main():
    running = True
    
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
                
    pygame.quit()
    
if __name__ == "__main__":
	main()
