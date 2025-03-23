import pygame, os

IMG_PATH = "../data/images/"


def load_image(path):
    img = pygame.image.load(IMG_PATH + path).convert_alpha()
    return img


def load_images(path):
    images = []
    for img_name in os.listdir(IMG_PATH + path):
        images.append(load_image(path + "/" + img_name))
    return images
