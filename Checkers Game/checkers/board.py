from checkers.settings import *


class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0

    def draw_cubes(self, win):
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, "white", (row * TILE_SIZE, col * TILE_SIZE, TILE_SIZE, TILE_SIZE))
