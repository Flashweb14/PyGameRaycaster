import pygame

pygame.init()


def load_image(filename):
    image = pygame.image.load(filename).convert_alpha()
    return image
