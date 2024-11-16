import pygame
from nltk.corpus import words

# Game Setup
pygame.init()

wordlist = words.words()
len_indexes = []
length = 1

wordlist.sort(key=len)
for i in range(len(wordlist)):
    if len(wordlist[i] > length):
        length += 1
        len_indexes.append(i)
len_indexes.append(len(wordlist))
print(len_indexes)

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Racer")
surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
timer = pygame.time.Clock()
FPS = 60

# Game vars
level = 0
active_str = "test string"
score = 0
high_score = 1
lives = 5
paused = False
submit = ""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word_objects = []
new_level = True

# Assets loading
header_font = pygame.font.Font("assets/fonts/Square.ttf", 50)
pause_font = pygame.font.Font("assets/fonts/1up.ttf", 38)
banner_font = pygame.font.Font("assets/fonts/1up.ttf", 28)
font = pygame.font.Font("assets/fonts/AldotheApache.ttf", 48)


class Button:
    def __init__(self, x, y, text, clicked, surf):
        self.x = x
        self.y = y
        self.text = text
        self.clicked = clicked
        self.surf = surf

    def draw(self):
        cir = pygame.draw.circle(self.surf, (45, 89, 135), (self.x, self.y), 35)
        if cir.collidepoint(pygame.mouse.get_pos()):
            btn = pygame.mouse.get_pressed()
            if btn[0]:
                pygame.draw.circle(self.surf, (190, 35, 35), (self.x, self.y), 35)
                self.clicked = True
            else:
                pygame.draw.circle(self.surf, (190, 89, 135), (self.x, self.y), 35)
        pygame.draw.circle(self.surf, "white", (self.x, self.y), 35, 3)
        self.surf.blit(pause_font.render(self.text, True, "white"), (self.x - 15, self.y - 25))


def draw_screen():
    # draw lines for background and titlebar
    pygame.draw.rect(screen, (32, 42, 68), [0, HEIGHT - 100, WIDTH, 100])
    pygame.draw.rect(screen, "white", [0, 0, WIDTH, HEIGHT], 5)
    pygame.draw.line(screen, "white", (250, HEIGHT - 100), (250, HEIGHT), 2)
    pygame.draw.line(screen, "white", (700, HEIGHT - 100), (700, HEIGHT), 2)
    pygame.draw.line(screen, "white", (0, HEIGHT - 100), (WIDTH, HEIGHT - 100), 2)
    pygame.draw.rect(screen, "black", [0, 0, WIDTH, HEIGHT], 2)

    # drawing texts
    screen.blit(header_font.render(f"Level: {level}", True, "white"), (10, HEIGHT - 75))
    screen.blit(header_font.render(f'"{active_str}"', True, "white"), (270, HEIGHT - 75))
    pause_btn = Button(748, HEIGHT - 52, "II", False, screen)
    pause_btn.draw()
    screen.blit(banner_font.render(f"Score: {score}", True, "black"), (250, 10))
    screen.blit(banner_font.render(f"Best: {high_score}", True, "black"), (550, 10))
    screen.blit(banner_font.render(f"Lives: {lives}", True, "black"), (10, 10))
    return pause_btn.clicked


def draw_pause():
    pass


def generate_level():
    word_objs = []
    return word_objs


running = True
while running:
    if paused:
        draw_pause()
    elif new_level:
        word_objects = generate_level()
        new_level = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

        if event.type == pygame.KEYDOWN:
            if not paused:
                if event.unicode.lower() in letters:
                    active_str += event.unicode.lower()
                if event.key == pygame.K_BACKSPACE and len(active_str) > 0:
                    active_str = active_str[:-1]
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    submit = active_str
                    active_str = ""

    screen.fill("gray")
    timer.tick(FPS)
    pause_button = draw_screen()

    pygame.display.flip()
pygame.quit()
