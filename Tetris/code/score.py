from settings import *

class Score:
    def __init__(self):
        self.surf = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * SCORE_HEIGHT_FRACTION - PADDING))
        self.rect = self.surf.get_rect(bottomright=(WINDOW_WIDTH - PADDING, WINDOW_HEIGHT - PADDING))
        self.display_surf = pygame.display.get_surface()
        
    def run(self):
        self.display_surf.blit(self.surf, self.rect)