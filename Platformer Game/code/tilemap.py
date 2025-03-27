NEIGHBORS_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]

class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid = []

        for i in range(10):
            self.tilemap[str(3 + i) + ";10"] = {"type": "grass", "variant": 1, "pos": (3 + i, 10)}
            self.tilemap["10;" + str(i + 5)] = {"type": "stone", "variant": 1, "pos": (10, i + 5)}

    def tiles_arround(self, pos):
        tile_loc = (int(pos[0] // self.tile_size))

    def render(self, surf):
        for tile in self.offgrid:
            surf.blit(self.game.assets[tile["type"]][tile["variant"]], tile["pos"])
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            surf.blit(self.game.assets[tile["type"]][tile["variant"]],
                      (tile["pos"][0] * self.tile_size, tile["pos"][1] * self.tile_size))
