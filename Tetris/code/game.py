from settings import *
from timers import Timer
from random import choice

class Game:
    def __init__(self, get_next_shape, update_score):
        self.surf = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surf = pygame.display.get_surface()
        self.rect = self.surf.get_rect(topleft=(PADDING, PADDING))
        self.sprites = pygame.sprite.Group()
        
        self.get_next_shape = get_next_shape
        self.update_score = update_score
        
        self.line_surf = self.surf.copy()
        self.line_surf.fill((0, 255, 0))
        self.line_surf.set_colorkey((0, 255, 0))
        self.line_surf.set_alpha(120)
        
        self.field_data = [[0 for _ in range(COLUMNS)]for _ in range(ROWS)]
        self.tetromino = Tetromino(self.get_next_shape(), self.sprites, self.create_new_tetromino, self.field_data)
        
        self.down_speed = UPDATE_START_SPEED
        self.down_speed_faster = self.down_speed * 0.3
        self.down_pressed = False
        self.timers = {
            "vertical_move": Timer(self.down_speed, True, self.move_down),
            "horizontal_move": Timer(MOVE_WAIT_TIME),
            "rotate": Timer(ROTATE_WAIT_TIME)
        }
        self.timers["vertical_move"].activate()
        
        self.curr_level = 1
        self.curr_score = 0
        self.curr_lines = 0
        
    def calc_score(self, lines_num):
        self.curr_lines += lines_num
        self.curr_score += SCORE_DATA[lines_num] * self.curr_level
        
        if self.curr_lines / 10 > self.curr_level:
            self.curr_level += 1
            self.down_speed *= 0.75
            self.down_speed_faster = self.down_speed * 0.3
            self.timers['vertical_move'].duration = self.down_speed
        self.update_score(self.curr_lines, self.curr_score, self.curr_level)
        
    def create_new_tetromino(self):
        self.check_finished_lines()
        self.tetromino = Tetromino(self.get_next_shape(), self.sprites, self.create_new_tetromino, self.field_data)
        
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
                
        if not self.timers["rotate"].active:
            if keys[pygame.K_UP]:
                self.tetromino.rotate()
                self.timers["rotate"].activate()
                
        if not self.down_pressed and keys[pygame.K_DOWN]:
            self.down_pressed = True
            self.timers['vertical_move'].duration = self.down_speed_faster
        
        if self.down_pressed and not keys[pygame.K_DOWN]:
            self.down_pressed = False
            self.timers['vertical_move'].duration = self.down_speed
                
    def check_finished_lines(self):
        delete_rows = []
        for i, row in enumerate(self.field_data):
            if all(row):
                delete_rows.append(i)
        if delete_rows:
            for delete_row in delete_rows:
                for block in self.field_data[delete_row]:
                    block.kill()
                
                for row in self.field_data:
                    for block in row:
                        if block and block.pos.y < delete_row:
                            block.pos.y += 1
            self.field_data = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]
            for block in self.sprites:
                self.field_data[int(block.pos.y)][int(block.pos.x)] = block
                
            self.calc_score(len(delete_rows))
        
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
        self.shape = shape
        
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
                self.field_data[int(block.pos.y)][int(block.pos.x)] = block
            self.create_new_tetromino()
            
    def move_horizontally(self, direction):
        if not self.next_move_horizontal_collide(direction):
            for block in self.blocks:
                block.pos.x += direction
                
    def rotate(self):
        if self.shape != 'O':
            pivot_pos = self.blocks[0].pos
            
            new_block_pos = [block.rotate(pivot_pos) for block in self.blocks]
            
            for pos in new_block_pos:
                if pos.x < 0 or pos.x >= COLUMNS:
                    return
                if self.field_data[int(pos.y)][int(pos.x)]:
                    return
                if pos.y >= ROWS:
                    return
            
            for i, block in enumerate(self.blocks):
                block.pos = new_block_pos[i]


class Block(pygame.sprite.Sprite):
    def __init__(self, group, pos, color):
        super().__init__(group)
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(color)
        self.pos = pygame.Vector2(pos) + BLOCK_OFFSET
        self.rect = self.image.get_rect(topleft=(self.pos * CELL_SIZE))
        
    def rotate(self, pivot_pos):
        return pivot_pos + (self.pos - pivot_pos).rotate(90)
        
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
        
