import pygame
import random
from button import Button
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
potion_img = pygame.image.load("img/Icons/potion.png").convert_alpha()

# game variables
current_fighter = 1
total_fighters = 3
action_cooldown = 0
action_wait_time = 90
potion_effect = 15
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
        self.potions = potions
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0  # 0:idle, 1:attack, 2:hurt, 3:dead
        self.update_timer = pygame.time.get_ticks()
        # idle sprites
        tmp_list = []
        for i in range(8):
            img = pygame.image.load(f"img/{self.name}/Idle/{i}.png").convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            tmp_list.append(img)
        self.animation_list.append(tmp_list)
        # attack sprites
        tmp_list = []
        for i in range(8):
            img = pygame.image.load(f"img/{self.name}/Attack/{i}.png").convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            tmp_list.append(img)
        self.animation_list.append(tmp_list)
        # hurt sprites
        tmp_list = []
        for i in range(3):
            img = pygame.image.load(f"img/{self.name}/Hurt/{i}.png").convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            tmp_list.append(img)
        self.animation_list.append(tmp_list)
        # dead sprites
        tmp_list = []
        for i in range(10):
            img = pygame.image.load(f"img/{self.name}/Death/{i}.png").convert_alpha()
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
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.idle()
            
    def idle(self):
        self.action = 0
        self.frame_index = 0
        self.update_timer = pygame.time.get_ticks()
            
    def attack(self, target):
        randd = random.randint(-5, 5)
        dmg = self.strength + randd
        target.health -= dmg
        target.hurt()
        
        if target.health < 0:
            target.health = 0
            target.alive = False
            target.death()

        damage_text = DamageText(target.rect.centerx, target.rect.y, str(dmg), "red")
        dmg_text_group.add(damage_text)
        self.action = 1
        self.frame_index = 0
        self.update_timer = pygame.time.get_ticks()
    
    def hurt(self):
        self.action = 2
        self.frame_index = 0
        self.update_timer = pygame.time.get_ticks()
        
    def death(self):
        self.action = 3
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


class DamageText(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(damage, True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0

    def update(self):
        self.rect.y -= 1
        self.counter += 1
        if self.counter > 30:
            self.kill()


dmg_text_group = pygame.sprite.Group()

knight = Fighter(200, 260, "Knight", 30, 10, 3)
bandit1 = Fighter(550, 270, "Bandit", 20, 6, 1)
bandit2 = Fighter(700, 270, "Bandit", 20, 6, 1)

bandits = [bandit1, bandit2]

knight_hp = HealthBar(100, window_height - bottom_panel + 40, knight.health, knight.max_hp)
bandit1_hp = HealthBar(550, window_height - bottom_panel + 40, bandit1.health, bandit1.max_hp)
bandit2_hp = HealthBar(550, window_height - bottom_panel + 100, bandit2.health, bandit2.max_hp)

potion_btn = Button(window, 100, window_height - bottom_panel + 70, potion_img, 64, 64)


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

    dmg_text_group.update()
    dmg_text_group.draw(window)
    attack = False
    potion = False
    target = None
    pygame.mouse.set_visible(True)
    pos = pygame.mouse.get_pos()
    for index, bandit in enumerate(bandits):
        if bandit.rect.collidepoint(pos):
            pygame.mouse.set_visible(False)
            window.blit(sword_img, pos)
            if clicked and bandit.alive:
                attack = True
                target = bandits[index]

    if potion_btn.draw():
        potion = True
    draw_text(str(knight.potions), font, "red", 150, window_height - bottom_panel + 70)

    if knight.alive:
        if current_fighter == 1:
            action_cooldown += 1
            if action_cooldown >= action_wait_time:
                if attack and target is not None:
                    knight.attack(target)
                    current_fighter += 1
                    action_cooldown = 0
                if potion:
                    if knight.potions > 0:
                        if knight.max_hp - knight.health > potion_effect:
                            heal_amount = potion_effect
                        else:
                            heal_amount = knight.max_hp - knight.health
                        knight.health += heal_amount
                        heal_text = DamageText(knight.rect.centerx, knight.rect.y, str(heal_amount), "green")
                        dmg_text_group.add(heal_text)
                        knight.potions -= 1
                        current_fighter += 1
                        action_cooldown = 0

    for idx, bandit in enumerate(bandits):
        if current_fighter == idx + 2:
            if bandit.alive:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    if (bandit.health / bandit.max_hp) < 0.5 and bandit.potions > 0:
                        if bandit.max_hp - bandit.health > potion_effect:
                            heal_amount = potion_effect
                        else:
                            heal_amount = bandit.max_hp - bandit.health
                        bandit.health += heal_amount
                        heal_text = DamageText(bandit.rect.centerx, bandit.rect.y, str(heal_amount), "green")
                        dmg_text_group.add(heal_text)
                        bandit.potions -= 1
                        current_fighter += 1
                        action_cooldown = 0
                    else:
                        bandit.attack(knight)
                        current_fighter += 1
                        action_cooldown = 0
            else:
                current_fighter += 1
                
    if current_fighter > total_fighters:
        current_fighter = 1

    pygame.display.update()

pygame.quit()
