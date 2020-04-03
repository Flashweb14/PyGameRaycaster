import pygame
from PyGameRaycaster.scripts.camera import Camera

pygame.init()


class Game:
    def __init__(self):
        self.size = self.width, self.height = 500, 500
        self.screen = pygame.display.set_mode(self.size)
        self.all_sprites = pygame.sprite.Group()
        self.FPS = 30
        self.clock = pygame.time.Clock()
        self.camera = Camera(self)
