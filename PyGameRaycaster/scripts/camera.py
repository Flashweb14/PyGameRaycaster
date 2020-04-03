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
        self.angle = 0
        self.ray_length = 100

        self.image = load_image('../resources/white_circle.png')
        self.rect = self.image.get_rect()

        self.x = 250
        self.y = 250
        self.rect.x = 250
        self.rect.y = 250

        self.rotate = []

        self.direction = None
        self.move_forward = False
        self.move_back = False

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.rotate.append(self.speed)
            if event.key == pygame.K_a:
                self.rotate.append(-self.speed)
            if event.key == pygame.K_w:
                self.move_forward = True
            if event.key == pygame.K_s:
                self.move_back = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.rotate.remove(self.speed)
            if event.key == pygame.K_a:
                self.rotate.remove(-self.speed)
            if event.key == pygame.K_w:
                self.move_forward = False
            if event.key == pygame.K_s:
                self.move_back = False

    def ray_cast(self):
        angles = range(int(self.angle), int(self.angle) + self.view_angle)
        for angle in angles:
            pygame.draw.line(self.game.screen, pygame.Color('red'), (self.x + 10, self.y + 10),
                             (int(cos(radians(angle)) * self.ray_length + self.x + 10),
                              int(sin(radians(angle)) * self.ray_length + self.y + 10)), 4)
            if angles.index(angle) == self.view_angle // 2 + 1:
                self.direction = (cos(radians(angle)) * (self.speed / self.game.FPS)), \
                                 (sin(radians(angle)) * (self.speed / self.game.FPS))

    def move(self):
        if self.move_forward:
            self.x += self.direction[0]
            self.y += self.direction[1]
        if self.move_back:
            self.x -= self.direction[0]
            self.y -= self.direction[1]
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def update(self):
        for angle in self.rotate:
            self.angle += angle / self.game.FPS
        self.ray_cast()
        self.move()
