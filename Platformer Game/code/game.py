import pygame, sys
from entities import PhysicEntity
from utils import *
from tilemap import Tilemap

WIDTH, HEIGHT = 640, 480
FPS = 60


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.display = pygame.Surface((320, 240))
        pygame.display.set_caption("Platformer Game")
        self.clock = pygame.time.Clock()
        
        self.assets = {
            "decoy": load_images("tiles/decor"),
            "grass": load_images("tiles/grass"),
            "large_decor": load_images("tiles/large_decor"),
            "stone": load_images("tiles/stone"),
            "player": load_image("entities/player.png")
        }
        
        self.movement = [0, 0]
        self.player = PhysicEntity(self, 'player', (50, 50), (8, 15))
        self.tile_map = Tilemap(self)

    def run(self):
        while True:
            self.display.fill((12, 22, 89))
            self.tile_map.render(self.display)
            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)
            
            print(self.tile_map.tiles_arround(self.player.pos))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = 1
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = 0
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = 0

            self.window.blit(pygame.transform.scale(self.display, self.window.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
