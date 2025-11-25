import pygame
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def draw_grid(positions):
	for pos in positions:
		col, row = pos
		top_left = (col * TILE_SIZE, row * TILE_SIZE)
		pygame.draw.rect(window, "yellow", (*top_left, TILE_SIZE, TILE_SIZE))

	for row in range(GRID_HEIGHT):
		pygame.draw.line(window, "black", (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))
        
	for col in range(GRID_WIDTH):
		pygame.draw.line(window, "black", (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT))


def gen(num):
    return {
        (random.randrange(0, GRID_WIDTH),
         random.randrange(0, GRID_HEIGHT))
        for _ in range(num)
    }


def adjust_grid(positions):
    all_neighbors = set()
    new_positions = set()
    
    for pos in positions:
        neighbors = get_neighbors(pos)
        all_neighbors.update(neighbors)
        
        neighbors = list(filter(lambda x: x in positions, neighbors))
        
        if len(neighbors) in [2, 3]:
            new_positions.add(pos)
            
    for pos in all_neighbors:
        neighbors = get_neighbors(pos)
        neighbors = list(filter(lambda x: x in positions, neighbors))
        
        if len(neighbors) == 3:
            new_positions.add(pos)

    return new_positions


def get_neighbors(pos):
    x, y = pos
    neighbors = []
    for idx in [-1, 0, 1]:
        if x + idx < 0 or x + idx > GRID_WIDTH:
            continue
        for idy in [-1, 0, 1]:
            if y + idy < 0 or y + idy > GRID_HEIGHT:
                continue
            if idx == 0 and idy == 0:
                continue
            
            neighbors.append((x + idx, y + idy))
    
    return neighbors


def main():
    running = True
    playing = False
    count = 0
    update_freq = 120
    
    positions = set()
    while running:
        clock.tick(FPS)
        
        if playing:
            count += 1
            
        if count >= update_freq:
            count = 0
            positions = adjust_grid(positions)
            
        pygame.display.set_caption("Playing" if playing else "Paused")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // TILE_SIZE
                row = y // TILE_SIZE
                pos = (col, row)
                
                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing
                    
                if event.key == pygame.K_c:
                    positions = set()
                    playing = False
                    count = 0
                    
                if event.key == pygame.K_g:
                    positions = gen(random.randrange(4, 10) * GRID_WIDTH)
                
        window.fill("grey")
        draw_grid(positions)
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
	main()
