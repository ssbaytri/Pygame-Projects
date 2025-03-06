import pygame
from pygame.locals import *

pygame.init()

window_width, window_height = 600, 600

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()
FPS = 60

cols = 6
rows = 6

BACKGROUND_COLOR = (10, 20, 50)
PADDLE_COLOR = (240, 240, 240)
PADDLE_OUTLINE = (80, 80, 80)

blue = (50, 150, 255)
teal = (50, 255, 150)
red = (255, 50, 50)

BLOCK_OUTLINE = (10, 20, 50)


class wall:
    def __init__(self):
        self.width = window_width // cols
        self.height = 50
        
    def create_walls(self):
        self.blocks = []
        block = []
        for row in range(rows):
            block_row = []
            for col in range(cols):
                block_x = col * self.width
                block_y = row * self.height
                rect = pygame.Rect(block_x, block_y, self.width, self.height)
                if row < 2:
                    strength = 3
                elif row < 4:
                    strength = 2
                elif row < 6:
                    strength = 1
                block = [rect, strength]
                block_row.append(block)
            self.blocks.append(block_row)
            
    def draw_walls(self):
        for row in self.blocks:
            for block in row:
                if block[1] == 3:
                    color = blue
                elif block[1] == 2:
                    color = teal
                elif block[1] == 1:
                    color = red
                pygame.draw.rect(window, color, block[0])
                pygame.draw.rect(window, BLOCK_OUTLINE, block[0], 2)


class paddle:
    def __init__(self):
        self.width = int(window_width / cols)
        self.height = 20
        self.x = int((window_width / 2) - (self.width / 2))
        self.y = window_height - (self.height * 2)
        self.speed = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.direction = 0
        
    def move(self):
        self.direction = 0
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and self.rect.left > 0:
            self.direction = -1
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.right < window_width:
            self.direction = 1
            self.rect.x += self.speed
    
    def draw(self):
        pygame.draw.rect(window, PADDLE_COLOR, self.rect)
        pygame.draw.rect(window, PADDLE_OUTLINE, self.rect, 3)
        
        
class Ball:
    def __init__(self, x, y):
        self.ball_rad = 10
        self.x = x - self.ball_rad
        self.y = y
        self.rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
        self.speed_x = 4
        self.speed_y = -4
        self.max_speed = 5
        self.game_over = 0
        
    def draw(self):
        pygame.draw.circle(window, PADDLE_COLOR, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)
        pygame.draw.circle(window, PADDLE_OUTLINE, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad, 3)
        
    def move(self):
        collision_thresh = 5

        if self.rect.left < 0 or self.rect.right > window_width:
            self.speed_x *= -1
        if self.rect.top < 0:
            self.speed_y *= -1
        if self.rect.bottom > window_height:
            self.game_over = -1
            
        if self.rect.colliderect(player_paddle):
            if abs(self.rect.bottom - player_paddle.rect.top) < collision_thresh and self.speed_y > 0:
                self.speed_y *= -1
                self.speed_x += player_paddle.direction
                if self.speed_x > self.max_speed:
                    self.speed_x = self.max_speed
                elif self.speed_x < -self.max_speed:
                    self.speed_x = -self.max_speed
            else:
                self.speed_x *= -1
                
            
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        return self.game_over


wall = wall()
wall.create_walls()

player_paddle = paddle()

ball = Ball(player_paddle.x + (player_paddle.width // 2), player_paddle.y - player_paddle.height)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
                
    window.fill(BACKGROUND_COLOR)
    
    wall.draw_walls()
    player_paddle.draw()
    player_paddle.move()
    ball.draw()
    ball.move()
    
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
