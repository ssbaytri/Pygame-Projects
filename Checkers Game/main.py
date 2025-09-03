from checkers.settings import *
from checkers.game import Game

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
    game = Game(screen)

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_pos_from_mouse(pos)
                if game.turn == P1_COLOR:
                    game.select(row, col)

        game.update()

    pygame.quit()


if __name__ == "__main__":
    main()
