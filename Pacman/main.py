import pygame
from board import boards
import math

pygame.init()

WIN_WIDTH = 900
WIN_HEIGHT = 950

pygame.display.set_caption("Pacman")
display = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
timer = pygame.time.Clock()
FPS = 60
# font = pygame.font.Font("freesansbold.tff", 20)
level = boards
color = "blue"
PI = math.pi

player_images = []
for i in range(1, 5):
    player_img = pygame.image.load(f"assets/player_images/{i}.png")
    scaled_img = pygame.transform.scale(player_img, (45, 45))   
    player_images.append(scaled_img)
    
player_x = 450
player_y = 663
direction = 0
counter = 0
flicker = False

#                 R      L      U      D
allowed_dirs = [False, False, False, False]

def draw_boards():
    num1 = ((WIN_HEIGHT - 50) // 32)
    num2 = (WIN_WIDTH // 30)
        
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.circle(display, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
            if level[i][j] == 2 and not flicker:
                pygame.draw.circle(display, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)
            if level[i][j] == 3:
                pygame.draw.line(display, color, (j * num2 + (0.5 * num2), i * num1),
                                 (j * num2 + (0.5 * num2), i * num1 + num1), 3)
            if level[i][j] == 4:
                pygame.draw.line(display, color, (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
            if level[i][j] == 5:
                pygame.draw.arc(display, color, [(j * num2 - (num2 * 0.4)) - 2, (i * num1 + (0.5 * num1)), num2, num1],
                                0, PI / 2, 3)
            if level[i][j] == 6:
                pygame.draw.arc(display, color,
                                [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], PI / 2, PI, 3)
            if level[i][j] == 7:    
                pygame.draw.arc(display, color, [(j * num2 + (num2 * 0.5)), (i * num1 - (0.4 * num1)), num2, num1], PI,
                                3 * PI / 2, 3)
            if level[i][j] == 8:
                pygame.draw.arc(display, color,
                                [(j * num2 - (num2 * 0.4)) - 2, (i * num1 - (0.4 * num1)), num2, num1], 3 * PI / 2,
                                2 * PI, 3)
            if level[i][j] == 9:
                pygame.draw.line(display, 'white', (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
                
def draw_player():
    # 0 -> right, 1 -> left, 2 -> up, 3 -> down
    if direction == 0:
        display.blit(player_images[counter // 5], (player_x, player_y))
    elif direction == 1:
        display.blit(pygame.transform.flip(player_images[counter // 5], True, False), (player_x, player_y))
    elif direction == 2:
        display.blit(pygame.transform.rotate(player_images[counter // 5], 90), (player_x, player_y))
    elif direction == 3:
        display.blit(pygame.transform.rotate(player_images[counter // 5], 270), (player_x, player_y))
        
def check_collision(cent_x, cent_y):
    turns = [False, False, False, False]
    num1 = (WIN_HEIGHT - 50) // 32
    num2 = (WIN_WIDTH // 30)
    num3 = 15
    
    if cent_x // 30 < 29:
        if direction == 0:
            if level[cent_y // num1][(cent_x - num3) // num2] < 3:
                turns[0] = True
        if direction == 1:
            if level[cent_y // num1][(cent_x + num3) // num2] < 3:
                turns[1] = True
        if direction == 2:
            if level[(cent_y + num3) // num1][cent_x // num2] < 3:
                turns[3] = True
        if direction == 3:
            if level[(cent_y - num3) // num1][cent_x// num2] < 3:
                turns[2] = True
                
        if direction == 2 or direction == 3:
            if 12 <= cent_x % num2 <= 18:
                if level[(center_y + num3) // num1][center_x // num2] < 3:
                    turns[3] = True
                if level[(center_y - num3) // num1][center_x // num2] < 3:
                    turns[2] = True
            
            if 12 <= center_y % num1 <= 18:
                if level[center_y // num1][(center_x - num2) // num2] < 3:
                    turns[1] = True
                if level[center_y // num1][(center_x + num2) // num2] < 3:
                    turns[0] = True
                    
        if direction == 0 or direction == 1:
            if 12 <= cent_x % num2 <= 18:
                if level[(center_y + num3) // num1][center_x // num2] < 3:
                    turns[3] = True
                if level[(center_y - num3) // num1][center_x // num2] < 3:
                    turns[2] = True
            
            if 12 <= center_y % num1 <= 18:
                if level[center_y // num1][(center_x - num2) // num2] < 3:
                    turns[1] = True
                if level[center_y // num1][(center_x + num2) // num2] < 3:
                    turns[0] = True
    else:
        turns[0] = True
        turns[1] = True
    
    return turns

running = True
while running:
    if counter < 19:
        counter += 1
        if counter > 3:
            flicker = False
    else:
        flicker = True
        counter = 0

    center_x = player_x + 23
    center_y = player_y + 24

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = 0
            if event.key == pygame.K_LEFT:
                direction = 1
            if event.key == pygame.K_UP:
                direction = 2
            if event.key == pygame.K_DOWN:
                direction = 3
    
    timer.tick(FPS)
    display.fill("black")
    draw_boards()
    draw_player()
    check_collision(center_x, center_y)
    pygame.display.flip()

pygame.quit()