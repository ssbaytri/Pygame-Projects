import pygame, sys
from entities import PhysicEntity
from utils import load_image

WIDTH, HEIGHT = 640, 480
FPS = 60

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Platformer Game")
        self.clock = pygame.time.Clock()
        
        self.assets = {
            "player": load_image("entities/player.png")
        }
        
        self.movement = [0, 0]
        self.player = PhysicEntity(self, 'player', (50, 50), (8, 15))

    def run(self):
        while True:
            self.window.fill((0, 0, 0))
            
            self.player.update((0, self.movement[1] - self.movement[0]))
            self.player.render(self.window)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = 1
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = 0
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = 0

            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()
