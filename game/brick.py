import random

import pygame

class Brick(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((20, 20))
        self.image.fill("red")
        self.rect = self.image.get_rect()

        self.scene = pygame.display.get_surface().get_rect()

        # Рандомно выбираем сторону, по которой будет располагаться кирпич
        side = random.choice(["top", "bottom", "left", "right"])
        self.rect.left = random.randint(0, self.scene.width - 20)
        self.rect.top = random.randint(0, self.scene.height - 20)

        if side == "top":
            self.rect.top = 0
        elif side == "bottom":
            self.rect.bottom = self.scene.height
        elif side == "left":
            self.rect.left = 0
        elif side == "right":
            self.rect.right = self.scene.width

