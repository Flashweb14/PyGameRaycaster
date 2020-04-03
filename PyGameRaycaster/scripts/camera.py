import pygame
from math import sin, cos, radians
from PyGameRaycaster.scripts.utilities import load_image

pygame.init()


class Camera(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game.all_sprites)
        self.game = game
        self.speed = 80
        self.view_angle = 120
        self.angle = 50
        self.ray_length = 100

        self.image = load_image('../resources/white_circle.png')
        self.rect = self.image.get_rect()

        self.x = 250
        self.y = 250
        self.rect.x = 250
        self.rect.y = 250

        self.rotate = []

        self.move = None

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.rotate.append(self.speed)
            if event.key == pygame.K_a:
                self.rotate.append(-self.speed)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.rotate.remove(self.speed)
            if event.key == pygame.K_a:
                self.rotate.remove(-self.speed)

    def ray_cast(self):
        for angle in range(int(self.angle), int(self.angle) + self.view_angle):
            pygame.draw.line(self.game.screen, pygame.Color('red'), (self.x + 10, self.y + 10),
                             (int(cos(radians(angle)) * 100 + self.x + 10),
                              int(sin(radians(angle)) * 100 + self.y + 10)), 4)

    def update(self):
        for angle in self.rotate:
            self.angle += angle / self.game.FPS
        self.ray_cast()
