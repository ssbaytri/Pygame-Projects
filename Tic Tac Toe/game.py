import pygame
from pygame.locals import *

pygame.init()
window_width, window_height = 300, 300
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tic Tac Toe")

line_width = 6
markers = []
clicked = False
pos = []
player = 1
winner = 0
game_over = False

green = (0, 255, 0)
red = (255, 0, 0)
font_bg_color = (45, 55, 90)

font = pygame.font.SysFont(None, 40)
font_color = (220, 230, 255)

restart_rect = pygame.Rect(window_width // 2 - 90, window_height // 2, 180, 50)

for i in range(3):
    row = [0] * 3
    markers.append(row)


def check_winner():
    global winner
    global game_over
    y_pos = 0
    for x in markers:
        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = 2
            game_over = True

        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 1
            game_over = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            winner = 2
            game_over = True
        y_pos += 1

    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
        winner = 1
        game_over = True
    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
        winner = 2
        game_over = True


def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(window, green, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
                pygame.draw.line(window, green, (x_pos * 100 + 15, y_pos * 100 + 85), (x_pos * 100 + 85, y_pos * 100 + 15), line_width)
            if y == -1:
                pygame.draw.circle(window, red, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
            y_pos += 1
        x_pos += 1


def draw_grid():
    bg_color = (25, 25, 35)
    grid_color = (70, 70, 100)
    window.fill(bg_color)
    for x in range(1, 3):
        pygame.draw.line(window, grid_color, (0, x * 100), (window_width, x * 100), line_width)
        pygame.draw.line(window, grid_color, (x * 100, 0), (x * 100, window_height), line_width)


def draw_winner(winner):
    win_text = "Player " + str(winner) + " Won!"
    win_img = font.render(win_text, True, font_color)
    pygame.draw.rect(window, font_bg_color, (window_width // 2 - 100, window_height // 2 - 60, 200, 50))
    window.blit(win_img, (window_width // 2 - 90, window_height // 2 - 50))

    restart_txt = "Play Again?"
    restart_img = font.render(restart_txt, True, font_color)
    pygame.draw.rect(window, font_bg_color, restart_rect)
    window.blit(restart_img, (window_width // 2 - 80, window_height // 2 + 10))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        if not game_over:
            if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x, cell_y = pos[0], pos[1]
                if markers[cell_x // 100][cell_y // 100] == 0:
                    markers[cell_x // 100][cell_y // 100] = player
                    player *= -1
                    check_winner()

    draw_grid()
    draw_markers()

    if game_over:
        draw_winner(winner)
        if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked:
            clicked = False
            pos = pygame.mouse.get_pos()
            if restart_rect.collidepoint(pos):
                markers = []
                pos = []
                player = 1
                winner = 0
                game_over = False
                for i in range(3):
                    row = [0] * 3
                    markers.append(row)

    pygame.display.update()

pygame.quit()

#-------------------  END OF THE GAME  -------------------
