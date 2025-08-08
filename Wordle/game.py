import pygame
import random
import words

pygame.init()

# --- Config ---
WIDTH, HEIGHT = 500, 700
FPS = 60
COLS, ROWS = 5, 6
TILE_SIZE = 80
TILE_GAP = 10
OFFSET_X = (WIDTH - (COLS * (TILE_SIZE + TILE_GAP) - TILE_GAP)) // 2
OFFSET_Y = 80

# --- Colors ---
BG_COLOR = "#121213"
TILE_COLOR = "#3a3a3c"
TEXT_COLOR = "white"
CORRECT_COLOR = "#538d4e"
PRESENT_COLOR = "#b59f3b"
ABSENT_COLOR = "#3a3a3c"
BORDER_COLOR = "#565758"

# --- Fonts ---
font = pygame.font.Font("freesansbold.ttf", 48)
reset_font = pygame.font.Font("freesansbold.ttf", 32)
status_font = pygame.font.Font("freesansbold.ttf", 36)

# --- Init ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wordle")
clock = pygame.time.Clock()

# --- Game State ---
board = [['' for _ in range(COLS)] for _ in range(ROWS)]
guessed_rows = [False] * ROWS
level = 0
letter_idx = 0
input_active = True
game_over = False
secret_word = random.choice(words.WORDS)

# --- Functions ---
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            x = OFFSET_X + col * (TILE_SIZE + TILE_GAP)
            y = OFFSET_Y + row * (TILE_SIZE + TILE_GAP)
            letter = board[row][col].upper()

            # Background color logic
            if guessed_rows[row]:
                if secret_word[col] == board[row][col]:
                    color = CORRECT_COLOR
                elif board[row][col] in secret_word:
                    color = PRESENT_COLOR
                else:
                    color = ABSENT_COLOR
            else:
                color = TILE_COLOR

            pygame.draw.rect(screen, color, (x, y, TILE_SIZE, TILE_SIZE), border_radius=6)
            pygame.draw.rect(screen, BORDER_COLOR, (x, y, TILE_SIZE, TILE_SIZE), width=2, border_radius=6)

            if letter:
                text = font.render(letter, True, TEXT_COLOR)
                text_rect = text.get_rect(center=(x + TILE_SIZE // 2, y + TILE_SIZE // 2))
                screen.blit(text, text_rect)

def draw_status_message():
    if game_over:
        if level == ROWS:
            msg = "You Lost!"
        else:
            msg = "You Won!"
        status = status_font.render(msg, True, TEXT_COLOR)
        rect = status.get_rect(center=(WIDTH // 2, HEIGHT - 40))
        screen.blit(status, rect)

        restart = reset_font.render("Press R to Restart", True, TEXT_COLOR)
        restart_rect = restart.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        # Background behind restart message
        padding = 10
        bg_rect = pygame.Rect(
            restart_rect.left - padding,
            restart_rect.top - padding,
            restart_rect.width + 2 * padding,
            restart_rect.height + 2 * padding
        )
        pygame.draw.rect(screen, "dimgray", bg_rect, border_radius=8)
        screen.blit(restart, restart_rect)

def reset_game():
    global board, level, letter_idx, input_active, game_over, guessed_rows, secret_word
    board = [['' for _ in range(COLS)] for _ in range(ROWS)]
    guessed_rows = [False] * ROWS
    level = 0
    letter_idx = 0
    input_active = True
    game_over = False
    secret_word = random.choice(words.WORDS)

# --- Game Loop ---
running = True
while running:
    clock.tick(FPS)
    screen.fill(BG_COLOR)

    draw_board()
    draw_status_message()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                reset_game()

            if not game_over:
                if event.key == pygame.K_BACKSPACE and letter_idx > 0:
                    board[level][letter_idx - 1] = ''
                    letter_idx -= 1

                elif event.key == pygame.K_RETURN:
                    guess = ''.join(board[level])
                    if len(guess) == 5:
                        guessed_rows[level] = True
                        if guess == secret_word:
                            game_over = True
                        else:
                            level += 1
                            letter_idx = 0
                            if level == ROWS:
                                game_over = True

        if event.type == pygame.TEXTINPUT and not game_over and input_active:
            entry = event.text.lower()
            if letter_idx < 5 and entry.isalpha():
                board[level][letter_idx] = entry
                letter_idx += 1

    input_active = letter_idx < 5
    pygame.display.flip()

pygame.quit()
