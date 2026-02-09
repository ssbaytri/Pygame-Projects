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
        self.attack_index = {"col": 0, "row": 0}
        self.state = "general"
        self.cols, self.rows = 2, 2

    def input(self, event):
        if event.type == pygame.KEYDOWN:
            current_index = self.general_index if self.state == "general" else self.attack_index

            if event.key == pygame.K_DOWN:
                current_index["row"] = min(current_index["row"] + 1, self.rows - 1)
            elif event.key == pygame.K_UP:
                current_index["row"] = max(current_index["row"] - 1, 0)
            elif event.key == pygame.K_RIGHT:
                current_index["col"] = min(current_index["col"] + 1, self.cols - 1)
            elif event.key == pygame.K_LEFT:
                current_index["col"] = max(current_index["col"] - 1, 0)
            elif event.key == pygame.K_SPACE:
                self._handle_selection()

    def _handle_selection(self):
        selected_index = self.general_index["col"] + self.general_index["row"] * self.cols

        if self.state == "general":
            self.state = self.general_options[selected_index]
        elif self.state == "attack":
            print(self.monster.abilities[selected_index])

    def quad_select(self, index, options):
        # bg
        rect = pygame.Rect(self.left + 40, self.top + 60, 400, 200)
        pygame.draw.rect(self.display_surf, COLORS["white"], rect, 0, 4)
        pygame.draw.rect(self.display_surf, COLORS["gray"], rect, 4, 4)

        # menu
        for col in range(self.cols):
            for row in range(self.rows):
                x = rect.left + rect.width / (self.cols * 2) + (rect.width / self.cols) * col
                y = rect.top + rect.height / (self.rows * 2) + (rect.height / self.rows) * row

                i = col + 2 * row
                color = COLORS["gray"] if col == index["col"] and row == index["row"] else COLORS["black"]
                text_surf = self.font.render(options[i], True, color)
                text_rect = text_surf.get_rect(center=(x, y))
                self.display_surf.blit(text_surf, text_rect)

    def update(self):
        pass

    def draw(self):
        match self.state:
            case "general": self.quad_select(self.general_index, self.general_options)
            case "attack": self.quad_select(self.attack_index, self.monster.abilities)
