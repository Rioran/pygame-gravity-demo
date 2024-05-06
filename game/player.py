from pathlib import Path
from random import randint
import pygame

#  print(f'{__file__ = }, {Path().absolute() } =')
CURRENT_FOLDER = Path(__file__).parent

print(f'{Path(__file__).parent = }  ')


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

        self.x_speed = 0

    def update(self):
        self.y_speed += 1
        self.rect.y += self.y_speed
        if self.rect.bottom > self.scene.bottom or self.rect.top < self. scene.top:
            # print('Bye, player!')
            # self.kill()
            self.y_speed *= -1
            self.rect.y += self.y_speed
        if self.rect.left < self.scene.left or self.rect.right > self.scene.right:
            self.x_speed *= -1
            self.rect.x += self.x_speed
        if self.y_speed < 0:
            self.y_speed += 0.2
        # print(f'Player y = {self.rect.y}')
        self.rect.x += self.x_speed

    def boost(self):
        self.x_speed = randint(-40, 40)
        self.y_speed = randint(0, 40)
