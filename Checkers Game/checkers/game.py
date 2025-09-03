import pygame.display

from checkers.settings import *
from checkers.board import Board


class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.win.fill(DARK_TILES)
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = P1_COLOR
        self.valid_moves = {}

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        return True
    
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, "blue", (col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2), 15)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == P1_COLOR:
            self.turn = P2_COLOR
        else:
            self.turn = P1_COLOR

    def winner(self):
        return self.board.winner()

    def display_winner(self, win):
        font = pygame.font.SysFont("comicsans", 60)
        winner_text = f"The winner is {self.winner()}"
        text = font.render(winner_text, True, "white")

        text_width, text_height = text.get_size()
        rect_x = (WIDTH // 2) - (text_width // 2) - 10
        rect_y = (HEIGHT // 2) - (text_height // 2) - 10
        rect_width = text_width + 20
        rect_height = text_height + 20

        pygame.draw.rect(win, "black", (rect_x, rect_y, rect_width, rect_height))

        win.blit(text, (WIDTH // 2 - text_width // 2, HEIGHT // 2 - text_height // 2))
        pygame.display.update()
        pygame.time.delay(3000)
