from settings import *

def import_image(*path, format="png"):
    full_path = join(*path) + f".{format}"
    return pygame.image.load(full_path).convert_alpha()

def import_folder(*path):
    frames = []
    for folder_path, sub_folders, file_names in walk(join(*path)):
        for file_name in sorted(file_names, key= lambda name: int(name.split(".")[0])):
            full_path = join(folder_path, file_name)
            surf = pygame.image.load(full_path).convert_alpha()
            frames.append(surf)
    return frames
