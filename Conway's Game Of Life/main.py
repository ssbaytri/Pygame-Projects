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

def draw_grid(pos):
    for row in range(GRID_HEIGHT):
        pygame.draw.line(window, "black", (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))
        
    for col in range(GRID_WIDTH):
        pygame.draw.line(window, "black", (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT))

def main():
    running = True
    
    positions = set()
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
                
        window.fill("grey")
        draw_grid(positions)
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
	main()
