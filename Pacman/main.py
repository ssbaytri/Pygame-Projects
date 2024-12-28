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

running = True
while running:
    if counter < 19:
        counter += 1
        if counter > 3:
            flicker = False
    else:
        flicker = True
        counter = 0

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
    pygame.display.flip()

pygame.quit()