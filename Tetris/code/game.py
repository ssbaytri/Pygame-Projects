from settings import *

class Game:
    def __init__(self):
        self.surf = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surf = pygame.display.get_surface()
        
    def run(self):
        self.display_surf.blit(self.surf, (PADDING, PADDING))
