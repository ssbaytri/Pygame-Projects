from settings import *
from os import path

class Preview:
    def __init__(self, next_shapes):
        self.surf = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * PREVIEW_HEIGHT_FRACTION))
        self.rect = self.surf.get_rect(topright=(WINDOW_WIDTH - PADDING, PADDING))
        self.display_surf = pygame.display.get_surface()
        
        self.next_shapes = next_shapes
        self.shapes_surf = {shape: pygame.image.load(path.join('..', 'graphics', f'{shape}.png')).convert_alpha() for shape in TETROMINOS.keys()}
        self.fragment_height = self.surf.get_height() / 3
        
    def display_pieces(self, shapes):
        for i, shape in enumerate(shapes):
            shape_surf = self.shapes_surf[shape]
            x = self.surf.get_width() / 2
            y = self.fragment_height / 2 + (i * self.fragment_height)
            rect = shape_surf.get_rect(center=(x, y))
            self.surf.blit(shape_surf, rect)
        
    def run(self, next_shapes):
        self.surf.fill(GRAY)
        self.display_pieces(next_shapes)
        self.display_surf.blit(self.surf, self.rect)
        pygame.draw.rect(self.display_surf, LINE_COLOR, self.rect, 2, 2)
