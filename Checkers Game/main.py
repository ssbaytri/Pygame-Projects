from checkers.settings import *
from checkers.board import Board

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")


def get_pos_from_mouse(pos):
    x, y = pos
    row = y // TILE_SIZE
    col = x // TILE_SIZE
    return row, col


def main():
    running = True
    clock = pygame.time.Clock()
    board = Board()

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_pos_from_mouse(pos)
                piece = board.get_piece(row, col)
                print(row, col)

        screen.fill(DARK_TILES)
        board.draw(screen)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
