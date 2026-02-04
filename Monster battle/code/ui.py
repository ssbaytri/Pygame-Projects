from settings import *


class UI:
    def __init__(self, monster):
        self.display_surf = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 30)
        self.left = WINDOW_WIDTH / 2 - 100
        self.top = WINDOW_HEIGHT / 2 + 50
        self.monster = monster

        self.general_options = ["attack", "heal", "switch", "escape"]
        self.general_index = {"col": 0, "row": 0}
        self.state = "general"

    def input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.general_index["row"] = min(self.general_index["row"] + 1, 1)
            elif event.key == pygame.K_UP:
                self.general_index["row"] = max(self.general_index["row"] - 1, 0)
            elif event.key == pygame.K_RIGHT:
                self.general_index["col"] = min(self.general_index["col"] + 1, 1)
            elif event.key == pygame.K_LEFT:
                self.general_index["col"] = max(self.general_index["col"] - 1, 0)
            elif event.key == pygame.K_SPACE:
                self.state = self.general_options[self.general_index["col"] + self.general_index["row"] * 2]

    def quad_select(self):
        # bg
        rect = pygame.Rect(self.left + 40, self.top + 60, 400, 200)
        pygame.draw.rect(self.display_surf, COLORS["white"], rect, 0, 4)
        pygame.draw.rect(self.display_surf, COLORS["gray"], rect, 4, 4)

        # menu
        cols, rows = 2, 2
        for col in range(cols):
            for row in range(rows):
                x = rect.left + rect.width / 4 + (rect.width / 2) * col
                y = rect.top + rect.height / 4 + (rect.height / 2) * row

                i = col + 2 * row
                color = COLORS["gray"] if col == self.general_index["col"] and row == self.general_index["row"] else COLORS["black"]
                text_surf = self.font.render(self.general_options[i], True, color)
                text_rect = text_surf.get_rect(center=(x, y))
                self.display_surf.blit(text_surf, text_rect)

    def update(self):
        pass

    def draw(self):
        match self.state:
            case "general" : self.quad_select()
