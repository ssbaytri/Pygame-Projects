from settings import *
from support import *
from timers import Timer
from monster import Monster, Opponent
from random import choice
from ui import UI


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Monster Battle')
        self.clock = pygame.time.Clock()
        self.running = True
        self.import_assets()

        # groups 
        self.all_sprites = pygame.sprite.Group()

        # data
        monster_name = choice(list(MONSTER_DATA.keys()))
        self.monster = Monster(monster_name, self.back_surfs[monster_name])
        self.all_sprites.add(self.monster)
        opp_name = choice(list(MONSTER_DATA.keys()))
        self.opp = Opponent(opp_name, self.front_surfs[opp_name], self.all_sprites)

        # ui
        self.ui = UI(self.monster)

    def import_assets(self):
        self.back_surfs = folder_importer("../images", "back")
        self.bg_surfs = folder_importer("../images", "other")
        self.front_surfs = folder_importer("../images", "front")
        
    def draw_monster_floor(self):
        for sprite in self.all_sprites:
            floor_rect = self.bg_surfs["floor"].get_rect(center=sprite.rect.midbottom + pygame.Vector2(0, -10))
            self.display_surface.blit(self.bg_surfs["floor"], floor_rect)

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False
                self.ui.input(event)
           
            # update
            self.all_sprites.update(dt)
            self.ui.update()

            # draw
            self.display_surface.blit(self.bg_surfs["bg"], (0, 0))
            self.draw_monster_floor()
            self.all_sprites.draw(self.display_surface)
            self.ui.draw()
            pygame.display.update()
        
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
