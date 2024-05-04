from pathlib import Path

import pygame
import random

#print(f'{__file__ = }, {Path().absolute() = }')
CURRENT_FOLDER = Path(__file__).parent


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.surface.Surface((30, 30))
        # self.image.fill("red")
        self.image = pygame.image.load(CURRENT_FOLDER / 'logo.png')  # .convert()
        self.rect = self.image.get_rect()
        self.y_speed = 0

        self.scene = pygame.display.get_surface().get_rect()
        print(f'area bottom = {self.scene.bottom}')
        # self.rect.x = self.scene.centerx
        self.rect.centerx = self.scene.centerx
        self.rect.y = 100

    def update(self):
        self.y_speed += 1
        self.rect.y += self.y_speed
        if self.rect.bottom > self.scene.bottom:
            # print('Bye, player!')
            # self.kill()
            self.y_speed *= -1
            self.rect.y += self.y_speed
        if self.y_speed < 0:
            self.y_speed += 0.2
        # print(f'Player y = {self.rect.y}')

    def boost(self):
        self.y_speed -= 10

class Brick(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((20, 20))
        self.image.fill("red")
        self.rect = self.image.get_rect()

        self.scene = pygame.display.get_surface().get_rect()

        # Рандомно выбираем сторону, по которой будет располагаться кирпич
        side = random.choice(["top", "bottom", "left", "right"])
        if side == "top":
            self.rect.top = 0
            self.rect.left = random.randint(0, self.scene.width - 20)
        elif side == "bottom":
            self.rect.bottom = self.scene.height
            self.rect.left = random.randint(0, self.scene.width - 20)
        elif side == "left":
            self.rect.left = 0
            self.rect.top = random.randint(0, self.scene.height - 20)
        elif side == "right":
            self.rect.right = self.scene.width
            self.rect.top = random.randint(0, self.scene.height - 20)