from checkers.settings import *


class Piece:
    def __init__(self, row, col, color):
        self.PADDING = 10
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        if self.color == P1_COLOR:
            self.direction = -1
        else:
            self.direction = 1

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = TILE_SIZE * self.col + TILE_SIZE // 2
        self.y = TILE_SIZE * self.row + TILE_SIZE // 2

    def set_king(self):
        self.king = True

    def draw(self, win):
        radius = TILE_SIZE // 2 - self.PADDING // 2
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)
