from settings import * 
from sprites import *
from groups import AllSprites
from support import *
from random import randint


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Platformer')
        self.clock = pygame.time.Clock()
        self.running = True

        # groups 
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        
        # setup
        self.load_assets()
        self.setup()

        # timers
        self.bee_timer = Timer(500, func=self.create_bee, autostart=True, repeat=True)

    def create_bee(self):
        Bee(
            frames=self.bee_frames,
            pos=(self.level_width + WINDOW_WIDTH, randint(0, self.level_height)),
            groups=self.all_sprites,
            speed=randint(300, 500)
        )
        
    def create_bullet(self, pos, direction):
        x = pos[0] + direction * 34 if direction == 1 else pos[0] + direction * 34 - self.bullet_surf.get_width()
        Bullet((x, pos[1]), self.bullet_surf, direction, (self.all_sprites, self.bullet_sprites))
        Fire(pos, self.fire_surf, self.all_sprites, self.player)
        
    def load_assets(self):
        # graphics
        self.player_frames = import_folder("../images", "player")
        self.bullet_surf = import_image("../images", "gun", "bullet")
        self.fire_surf = import_image("../images", "gun", "fire")
        self.bee_frames = import_folder("../images", "enemies", "bee")
        self.worm_frames = import_folder("../images", "enemies", "worm")
        
        # sounds
        self.audio = audio_importer("../audio")

    def setup(self):
        tmx_map = load_pygame(join("../data", "maps", "world.tmx"))
        self.level_width = tmx_map.width * TILE_SIZE
        self.level_height = tmx_map.height * TILE_SIZE
        
        for x, y, image in tmx_map.get_layer_by_name("Main").tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), image, (self.all_sprites, self.collision_sprites))
            
        for x, y, image in tmx_map.get_layer_by_name("Decoration").tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)
            
        for obj in tmx_map.get_layer_by_name("Entities"):
            if obj.name == "Player":
                self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprites, self.player_frames, self.create_bullet)

    def run(self):
        while self.running:
            dt = self.clock.tick(FRAMERATE) / 1000 

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False 
            
            # update
            self.bee_timer.update()
            self.all_sprites.update(dt)

            # draw 
            self.display_surface.fill(BG_COLOR)
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()
        
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run() 