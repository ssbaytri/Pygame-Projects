from settings import *

class Game:
    def __init__(self):
        self.surf = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surf = pygame.display.get_surface()
        self.rect = self.surf.get_rect(topleft=(PADDING, PADDING))
        
        self.line_surf = self.surf.copy()
        self.line_surf.fill((0, 255, 0))
        self.line_surf.set_colorkey((0, 255, 0))
        self.line_surf.set_alpha(120)
        
    def draw_grid(self):
        for col in range(1, COLUMNS):
            pygame.draw.line(self.line_surf, LINE_COLOR, (col * CELL_SIZE, 0), (col * CELL_SIZE, GAME_HEIGHT))
        for row in range(1, ROWS):
            pygame.draw.line(self.line_surf, LINE_COLOR, (0, row * CELL_SIZE), (GAME_WIDTH, row * CELL_SIZE))
            
        self.surf.blit(self.line_surf, (0, 0))
        
    def run(self):
        self.surf.fill(GRAY)
        self.draw_grid()
        self.display_surf.blit(self.surf, (PADDING, PADDING))
        pygame.draw.rect(self.display_surf, LINE_COLOR, self.rect, 2, 2)
        
