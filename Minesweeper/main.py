import pygame
from settings import *
from sprites import *


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

    def new(self):
        self.board = Board()
        self.playing = True

    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()

    def draw(self):
        self.screen.fill(BGCOLOUR)
        self.board.draw(self.screen)
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit(0)
                
            if event.type == pygame.MOUSEBUTTONDOWN and not self.board.game_over and not self.board.won:
                x = event.pos[0] // TILESIZE
                y = event.pos[1] // TILESIZE
                
                if 0 <= x < COLS and 0 <= y < ROWS:
                    if event.button == 1:
                        self.board.reveal(x, y)
                    elif event.button == 3:
                        self.board.flag(x, y)


if __name__ == "__main__":
    game = Game()
    while True:
        game.new()
        game.run()
