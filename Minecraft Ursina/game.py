import random
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()

grass_texture = load_texture("assets/grass_block.png")
stone_texture = load_texture("assets/stone_block.png")
brick_texture = load_texture("assets/brick_block.png")
dirt_texture = load_texture("assets/dirt_block.png")
textures = [grass_texture, stone_texture, brick_texture, dirt_texture]
block_pick = 1


def update():
    global block_pick

    if held_keys['1'] : block_pick = 1
    if held_keys['2'] : block_pick = 2
    if held_keys['3'] : block_pick = 3
    if held_keys['4'] : block_pick = 4


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model="assets/block.obj",
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                voxel = Voxel(position=self.position + mouse.normal, texture=textures[block_pick - 1])
            if key == "right mouse down":
                destroy(self)
        if key == "escape":
            application.quit()


for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x, 0, z))

player = FirstPersonController()

app.run()
