from ursina import *

class Cube(Entity):
	def __init__(self):
		super().__init__(
			model='cube',
			color=color.white,
			texture='white_cube',
			rotation=Vec3(45, 45, 45),
			position=(4, 3)
		)

class Button(Button):
	def __init__(self):
		super().__init__(
			parent=scene,
			model='cube',
			texture='brick',
			color=color.red,
			highlight_color=color.blue,
			pressed_color=color.green
		)

	def input(self, key):
		if self.hovered:
			if key == "left mouse down":
				print("james say what")

def input(key):
	if key == 'escape':
		quit()

app = Ursina()

test_cube = Cube()
test_btn = Button()
app.run()