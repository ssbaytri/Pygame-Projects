from settings import *
from sys import exit
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    exit()
                    
            self.display.fill(GRAY)
            pygame.display.update()
            self.clock.tick(60)
        
if __name__ == "__main__":
    game = Game()
    game.run()
