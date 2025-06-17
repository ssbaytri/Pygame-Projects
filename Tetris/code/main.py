from settings import *
from game import Game, Block
from score import Score
from preview import Preview
from sys import exit
from random import choice

class Main:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        
        self.next_shapes = [choice(list(TETROMINOS.keys())) for _ in range(3)]
        
        self.game = Game(self.get_next_shape)
        self.score = Score()
        self.preview = Preview(self.next_shapes)
        
    def get_next_shape(self):
        next_shape = self.next_shapes.pop(0)
        self.next_shapes.append(choice(list(TETROMINOS.keys())))
        return next_shape
                
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    exit()
                    
            self.display.fill(GRAY)
            
            self.game.run()
            self.score.run()
            self.preview.run(self.next_shapes)
            
            pygame.display.update()
            self.clock.tick(60)
        
if __name__ == "__main__":
    main = Main()
    main.run()
