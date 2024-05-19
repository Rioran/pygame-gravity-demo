from pathlib import Path

from random import randint


import pygame


CURRENT_FOLDER = Path(__file__).parent
START_X = 600
START_Y = 100


class Player(pygame.sprite.Sprite):
    def __init__(self, x_position=START_X, y_position=START_Y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(CURRENT_FOLDER / 'logo.png')  # .convert()
        self.rect = self.image.get_rect()
        self.y_speed = 0
        self.x_speed = 0

        self.scene = pygame.display.get_surface().get_rect()

        self.rect.x = x_position
        self.rect.y = y_position


    def update(self):
        self.y_speed += 1
        self.rect.y += self.y_speed
        self.rect.x += self.x_speed
        if self.rect.bottom > self.scene.bottom or self.rect.top < self.scene.top:
            self.y_speed *= -1
            self.rect.y += self.y_speed

        if self.rect.left < self.scene.left or self.rect.right > self.scene.right:
            self.x_speed *= -1
            self.rect.x += self.x_speed

        if self.y_speed < 0:
            self.y_speed += 0.2

    def boost(self):
        self.x_speed = randint(-40, 40)
        self.y_speed = randint(-40, 40)
