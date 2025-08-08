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
reset_font = pygame.font.Font("freesansbold.ttf", 40)
secret_word = "power"
game_over = False

guessed_rows = [False] * ROWS

def draw_board():
    for col in range(COLS):
        for row in range(ROWS):
            pygame.draw.rect(screen, "white", (col * 100 + MARGIN, row * 100 + MARGIN, 75, 75), 3, 5)
            text = font.render(board[row][col], True, "gray")
            screen.blit(text, (col * 100 + 30, row * 100 + 25))
    pygame.draw.rect(screen, "green", (LEVEL_BOX_MARGIN, level * 100 + LEVEL_BOX_MARGIN, WIDTH - 10, 90), 3, 5)

def check_words():
    for row in range(ROWS):
        if not guessed_rows[row]:
            continue
        for col in range(COLS):
            letter = board[row][col]
            if secret_word[col] == letter:
                pygame.draw.rect(screen, "green", (col * 100 + MARGIN, row * 100 + MARGIN, 75, 75), 0, 5)
            elif letter in secret_word:
                pygame.draw.rect(screen, "yellow", (col * 100 + MARGIN, row * 100 + MARGIN, 75, 75), 0, 5)

def reset_game():
    global board, level, letter_idx, input_active, game_over, guessed_rows
    board = [['' for _ in range(COLS)] for _ in range(ROWS)]
    level = 0
    letter_idx = 0
    input_active = True
    game_over = False
    guessed_rows = [False] * ROWS


running = True
while running:
    
    clock.tick(FPS)
    screen.fill("black")
    check_words()
    draw_board()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and letter_idx > 0:
                board[level][letter_idx - 1] = ''
                letter_idx -= 1
            
            if event.key == pygame.K_SPACE and not game_over:
                guess = ''.join(board[level])
                if len(guess) == 5:
                    guessed_rows[level] = True
                    if guess == secret_word:
                        game_over = True
                    if not game_over:
                        level += 1
                        letter_idx = 0
                        if level == 6:
                            game_over = True
            
            if game_over and event.key == pygame.K_r:
                reset_game()
            
        if event.type == pygame.TEXTINPUT and not game_over and input_active:
            entry = event.text
            board[level][letter_idx] = entry
            letter_idx += 1
    
    if letter_idx == 5:
        input_active = False
    if letter_idx < 5:
        input_active = True
    
    if level == 6:
        game_over = True
        loser_text = font.render("You Lost!", True, "white")
        loser_rect = loser_text.get_rect(center=(WIDTH / 2, 650))
        screen.blit(loser_text, loser_rect)
        
    if game_over and level < 6:
        winner_text = font.render("You Won!", True, "white")
        winner_rect = winner_text.get_rect(center=(WIDTH / 2, 650))
        screen.blit(winner_text, winner_rect)
        
    if game_over:
        restart_msg = reset_font.render("Press R to Restart", True, "white")
        msg_rect = restart_msg.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        padding = 10
        bg_rect = pygame.Rect(
            msg_rect.left - padding,
            msg_rect.top - padding,
            msg_rect.width + 2 * padding,
            msg_rect.height + 2 * padding
        )
        pygame.draw.rect(screen, "dimgray", bg_rect, border_radius=8)
        screen.blit(restart_msg, msg_rect)
        
    pygame.display.flip()
pygame.quit()
