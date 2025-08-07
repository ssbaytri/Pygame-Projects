import pygame

pygame.init()

WIDTH, HEIGHT = 500, 700
FPS = 60

COLS = 5
ROWS = 6
MARGIN = 12
LEVEL_BOX_MARGIN = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wordle")
clock = pygame.time.Clock()

level = 0
board = [['' for _ in range(COLS)] for _ in range(ROWS)]
letter_idx = 0
input_active = True

font = pygame.font.Font("freesansbold.ttf", 56)
secret_word = "power"
game_over = False


def draw_board():
    for col in range(COLS):
        for row in range(ROWS):
            pygame.draw.rect(screen, "white", (col * 100 + MARGIN, row * 100 + MARGIN, 75, 75), 3, 5)
            text = font.render(board[row][col], True, "white")
            screen.blit(text, (col * 100 + 30, row * 100 + 25))
    pygame.draw.rect(screen, "green", (LEVEL_BOX_MARGIN, level * 100 + LEVEL_BOX_MARGIN, WIDTH - 10, 90), 3, 5)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE and letter_idx > 0:
            board[level][letter_idx - 1] = ''
            letter_idx -= 1
        if event.type == pygame.TEXTINPUT and not game_over and input_active:
            entry = event.text
            board[level][letter_idx] = entry
            letter_idx += 1
    
    if letter_idx == 5:
        input_active = False
    if letter_idx < 5:
        input_active = True
    
    clock.tick(FPS)
    screen.fill("black")
    draw_board()
    pygame.display.flip()

pygame.quit()
