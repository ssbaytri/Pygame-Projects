from settings import *

class Score:
    def __init__(self):
        self.surf = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * SCORE_HEIGHT_FRACTION - PADDING))
        self.display_surf = pygame.display.get_surface()
        
    def run(self):
        self.display_surf.blit(self.surf, (0, 0))