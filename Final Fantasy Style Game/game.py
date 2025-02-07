import pygame
import random

pygame.init()

clock = pygame.time.Clock()
FPS = 60

# game window
bottom_panel = 150
window_width = 800
window_height = 400 + bottom_panel

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Final Fantasy Style Game")
font = pygame.font.SysFont("Times New Roman", 26)

# load images
bg_img = pygame.image.load("img/Background/background.png").convert_alpha()
panel_img = pygame.image.load("img/Icons/panel.png").convert_alpha()
sword_img = pygame.image.load("img/Icons/sword.png").convert_alpha()

# game variables
current_fighter = 1
total_fighters = 3
action_cooldown = 0
action_wait_time = 90
attack = False
potion = False
clicked = False


class Fighter:
    def __init__(self, x, y, name, hp, strength, potions):
        self.name = name
        self.max_hp = hp
        self.health = hp
        self.strength = strength
        self.start_potion = potions
        self.potion = potions
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0  # 0:idle, 1:attack, 2:hurt, 3:dead
        self.update_timer = pygame.time.get_ticks()
        tmp_list = []
        for i in range(8):
            img = pygame.image.load(f"img/{self.name}/Idle/{i}.png").convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            tmp_list.append(img)
        self.animation_list.append(tmp_list)
        tmp_list = []
        for i in range(8):
            img = pygame.image.load(f"img/{self.name}/Attack/{i}.png").convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            tmp_list.append(img)
        self.animation_list.append(tmp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        window.blit(self.image, self.rect)

    def update(self):
        animation_cooldown = 100
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_timer > animation_cooldown:
            self.update_timer = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            self.idle()
            
    def idle(self):
        self.action = 0
        self.frame_index = 0
        self.update_timer = pygame.time.get_ticks()
            
    def attack(self, target):
        randd = random.randint(-5, 5)
        dmg = self.strength + randd
        target.health -= dmg
        
        if target.health < 0:
            target.health = 0
            target.alive = False
        
        self.action = 1
        self.frame_index = 0
        self.update_timer = pygame.time.get_ticks()


class HealthBar:
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, hp):
        self.hp = hp
        ratio = self.hp / self.max_hp
        pygame.draw.rect(window, "red", (self.x, self.y, 150, 20))
        pygame.draw.rect(window, "green", (self.x, self.y, 150 * ratio, 20))


knight = Fighter(200, 260, "Knight", 30, 10, 3)
bandit1 = Fighter(550, 270, "Bandit", 20, 6, 1)
bandit2 = Fighter(700, 270, "Bandit", 20, 6, 1)

bandits = [bandit1, bandit2]

knight_hp = HealthBar(100, window_height - bottom_panel + 40, knight.health, knight.max_hp)
bandit1_hp = HealthBar(550, window_height - bottom_panel + 40, bandit1.health, bandit1.max_hp)
bandit2_hp = HealthBar(550, window_height - bottom_panel + 100, bandit2.health, bandit2.max_hp)


def draw_text(text, text_font, color, x, y):
    img = text_font.render(text, True, color)
    window.blit(img, (x, y))


def draw_bg():
    window.blit(bg_img, (0, 0))


def draw_panel():
    window.blit(panel_img, (0, window_height - bottom_panel))
    draw_text(f"{knight.name} HP: {knight.health}", font, "red", 100, window_height - bottom_panel + 10)
    for i, bandit in enumerate(bandits):
        draw_text(f"{bandit.name} HP: {bandit.health}", font, "red", 550,
                  (window_height - bottom_panel + 10) + i * 60)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        else:
            clicked = False

    clock.tick(FPS)
    draw_bg()
    draw_panel()
    
    knight_hp.draw(knight.health)
    bandit1_hp.draw(bandit1.health)
    bandit2_hp.draw(bandit2.health)

    knight.draw()
    knight.update()
    for bandit in bandits:
        bandit.draw()
        bandit.update()

    attack = False
    potion = False
    target = None
    pygame.mouse.set_visible(True)
    pos = pygame.mouse.get_pos()
    for index, bandit in enumerate(bandits):
        if bandit.rect.collidepoint(pos):
            pygame.mouse.set_visible(False)
            window.blit(sword_img, pos)
            if clicked:
                attack = True
                target = bandits[index]
        
    if knight.alive:
        if current_fighter == 1:
            action_cooldown += 1
            if action_cooldown >= action_wait_time:
                if attack and target is not None:
                    knight.attack(target)
                    current_fighter += 1
                    action_cooldown = 0

    for idx, bandit in enumerate(bandits):
        if current_fighter == idx + 2:
            if bandit.alive:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    bandit.attack(knight)
                    current_fighter += 1
                    action_cooldown = 0
            else:
                current_fighter += 1
                
    if current_fighter > total_fighters:
        current_fighter = 1

    pygame.display.update()

pygame.quit()
