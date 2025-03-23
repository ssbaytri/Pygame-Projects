import pygame

IMG_PATH = "../data/images/"

def load_image(path):
    img = pygame.image.load(IMG_PATH + path).convert_alpha()
    return img