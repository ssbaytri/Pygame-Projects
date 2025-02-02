import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

# game window
bottom_panel = 150
window_width = 800
window_height = 400 + bottom_panel

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Final Fantasy Style Game")

# load images
bg_img = pygame.image.load("img/Background/background.png").convert_alpha()
panel_img = pygame.image.load("img/Icons/panel.png").convert_alpha()

class Fighter():
    def __init__(self, x, y, name, hp, strenght, potions):
        self.name = name
        self.max_hp = hp
        self.health = hp
        self.strength = strenght
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
        tmp_list = []
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
            self.frame_index = 0


knight = Fighter(200, 260, "Knight", 30, 10, 3)
bandit1 = Fighter(550, 270, "Bandit", 20, 6, 1)
bandit2 = Fighter(700, 270, "Bandit", 20, 6, 1)

bandits = [bandit1, bandit2]

def drwa_bg():
    window.blit(bg_img, (0, 0))
    
def draw_panel():
    window.blit(panel_img, (0, window_height - bottom_panel))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
            
    clock.tick(FPS)
    drwa_bg()
    draw_panel()
    
    knight.draw()
    knight.update()
    for bandit in bandits:
        bandit.draw()
        bandit.update()

    pygame.display.update()
        
pygame.quit()
