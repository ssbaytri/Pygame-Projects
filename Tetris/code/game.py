from settings import *
from timers import Timer
from random import choice

class Game:
    def __init__(self):
        self.surf = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surf = pygame.display.get_surface()
        self.rect = self.surf.get_rect(topleft=(PADDING, PADDING))
        self.sprites = pygame.sprite.Group()
        
        self.line_surf = self.surf.copy()
        self.line_surf.fill((0, 255, 0))
        self.line_surf.set_colorkey((0, 255, 0))
        self.line_surf.set_alpha(120)
        
        self.tetromino = Tetromino(choice(list(TETROMINOS.keys())), self.sprites)
        
        self.timers = {
            "vertical_move": Timer(UPDATE_START_SPEED, True, self.move_down)
        }
        self.timers["vertical_move"].activate()
        
    def timer_update(self):
        for timer in self.timers.values():
            timer.update()
        
    def move_down(self):
        self.tetromino.move_down()
        
    def draw_grid(self):
        for col in range(1, COLUMNS):
            pygame.draw.line(self.line_surf, LINE_COLOR, (col * CELL_SIZE, 0), (col * CELL_SIZE, GAME_HEIGHT))
        for row in range(1, ROWS):
            pygame.draw.line(self.line_surf, LINE_COLOR, (0, row * CELL_SIZE), (GAME_WIDTH, row * CELL_SIZE))
            
        self.surf.blit(self.line_surf, (0, 0))
        
    def run(self):
        self.timer_update()
        self.sprites.update()
        self.surf.fill(GRAY)
        self.sprites.draw(self.surf)
        self.draw_grid()
        self.display_surf.blit(self.surf, (PADDING, PADDING))
        pygame.draw.rect(self.display_surf, LINE_COLOR, self.rect, 2, 2)
        
        

class Tetromino:
    def __init__(self, shape, group):
        self.block_pos = TETROMINOS[shape]["shape"]
        self.color = TETROMINOS[shape]["color"]
        
        self.blocks = [Block(group, pos, self.color) for pos in  self.block_pos]
        
    def move_down(self):
        for block in self.blocks:
            block.pos.y += 1


class Block(pygame.sprite.Sprite):
    def __init__(self, group, pos, color):
        super().__init__(group)
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(color)
        self.pos = pygame.Vector2(pos) + BLOCK_OFFSET
        self.rect = self.image.get_rect(topleft=(self.pos * CELL_SIZE))
        
    def update(self):
        self.rect.topleft = self.pos * CELL_SIZE
        
