from checkers.settings import *
from checkers.board import Board


class Game:
    def __init__(self, win):
        self.selected = None
        self.board = Board()
        self.turn = P1_COLOR
        self.valid_moves = {}
        self.win = win

    def update(self):
        self.win.fill(DARK_TILES)
        self.board.draw(self.win)
        pygame.display.update()

    def reset(self):
        self.selected = None
        self.board = Board()
        self.turn = P1_COLOR
        self.valid_moves = {}
