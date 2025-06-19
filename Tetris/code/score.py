from settings import *
from os import path

class Score:
    def __init__(self):
        self.surf = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * SCORE_HEIGHT_FRACTION - PADDING))
        self.rect = self.surf.get_rect(bottomright=(WINDOW_WIDTH - PADDING, WINDOW_HEIGHT - PADDING))
        self.display_surf = pygame.display.get_surface()
        
        self.font = pygame.font.Font(path.join('..', 'graphics', 'Russo_One.ttf'), 30)
        self.increment_height = self.surf.get_height() / 3
        
    def display_text(self, pos, text):
        text_surf = self.font.render(text, True, 'white')
        text_rect = text_surf.get_rect(center=pos)
        self.surf.blit(text_surf, text_rect)
        
    def run(self):
        self.surf.fill(GRAY)
        for i, text in enumerate(['Score', 'Level', 'Lines']):
            x = self.surf.get_width() / 2
            y = self.increment_height / 2 + (i * self.increment_height)
            self.display_text((x, y), text)
        self.display_surf.blit(self.surf, self.rect)
        pygame.draw.rect(self.display_surf, LINE_COLOR, self.rect, 2, 2)