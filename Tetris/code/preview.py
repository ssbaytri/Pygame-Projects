from settings import *

class Preview:
    def __init__(self):
        self.surf = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * PREVIEW_HEIGHT_FRACTION))
        self.rect = self.surf.get_rect(topright=(WINDOW_WIDTH - PADDING, PADDING))
        self.display_surf = pygame.display.get_surface()
        
    def run(self):
        self.display_surf.blit(self.surf, self.rect)
