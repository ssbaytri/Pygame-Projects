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
        
        self.field_data = [[0 for _ in range(COLUMNS)]for _ in range(ROWS)]
        self.tetromino = Tetromino(choice(list(TETROMINOS.keys())), self.sprites, self.create_new_tetromino, self.field_data)
        
        self.timers = {
            "vertical_move": Timer(UPDATE_START_SPEED, True, self.move_down),
            "horizontal_move": Timer(MOVE_WAIT_TIME)
        }
        self.timers["vertical_move"].activate()
        
    def create_new_tetromino(self):
        self.tetromino = Tetromino(choice(list(TETROMINOS.keys())), self.sprites, self.create_new_tetromino, self.field_data)
        
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
        
    def input(self):
        keys = pygame.key.get_pressed()
        
        if not self.timers["horizontal_move"].active:
            if keys[pygame.K_LEFT]:
                self.tetromino.move_horizontally(-1)
                self.timers["horizontal_move"].activate()
            if keys[pygame.K_RIGHT]:
                self.tetromino.move_horizontally(1)
                self.timers["horizontal_move"].activate()
        
    def run(self):
        self.timer_update()
        self.sprites.update()
        self.input()
        self.surf.fill(GRAY)
        self.sprites.draw(self.surf)
        self.draw_grid()
        self.display_surf.blit(self.surf, (PADDING, PADDING))
        pygame.draw.rect(self.display_surf, LINE_COLOR, self.rect, 2, 2)
        
        

class Tetromino:
    def __init__(self, shape, group, create_new, field_data):
        self.block_pos = TETROMINOS[shape]["shape"]
        self.color = TETROMINOS[shape]["color"]
        self.create_new_tetromino = create_new
        self.field_data = field_data
        
        self.blocks = [Block(group, pos, self.color) for pos in  self.block_pos]
        
    def next_move_horizontal_collide(self, direction):
        collision_list = [block.horizontal_collide(int(block.pos.x + direction), self.field_data) for block in self.blocks]
        return any(collision_list)
    
    def next_move_vertical_collide(self):
        collision_list = [block.vertical_collide(int(block.pos.y + 1), self.field_data) for block in self.blocks]
        return any(collision_list)
        
    def move_down(self):
        if not self.next_move_vertical_collide():
            for block in self.blocks:
                block.pos.y += 1
        else:
            for block in self.blocks:
                self.field_data[int(block.pos.y)][int(block.pos.x)] = 1
            self.create_new_tetromino()
            
    def move_horizontally(self, direction):
        if not self.next_move_horizontal_collide(direction):
            for block in self.blocks:
                block.pos.x += direction


class Block(pygame.sprite.Sprite):
    def __init__(self, group, pos, color):
        super().__init__(group)
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(color)
        self.pos = pygame.Vector2(pos) + BLOCK_OFFSET
        self.rect = self.image.get_rect(topleft=(self.pos * CELL_SIZE))
        
    def horizontal_collide(self, x, field_data):
        if not 0 <= x < COLUMNS:
            return True
        if field_data[int(self.pos.y)][x]:
            return True
        
    def vertical_collide(self, y, field_data):
        if y >= ROWS:
            return True
        if y >= 0 and field_data[y][int(self.pos.x)]:
            return True
    
    def update(self):
        self.rect.topleft = self.pos * CELL_SIZE
        
