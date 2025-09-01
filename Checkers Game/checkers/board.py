from checkers.settings import *
from checkers.piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    def draw_cubes(self, win):
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, LIGHT_TILES, (row * TILE_SIZE, col * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, P2_COLOR))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, P1_COLOR))
                    else:
                        self.board[row].append(0)

    def draw(self, win):
        self.draw_cubes(win)
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
