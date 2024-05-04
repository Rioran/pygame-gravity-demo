import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.surface.Surface((30, 30))
        # self.image.fill("red")
        self.image = pygame.image.load('logo.png')  # .convert()
        self.rect = self.image.get_rect()
        self.y_speed = 0

        self.scene = pygame.display.get_surface().get_rect()
        print(f'area bottom = {self.scene.bottom}')
        self.rect.x = self.scene.centerx
        self.rect.y = 100

    def update(self):
        self.y_speed += 1
        self.rect.y += self.y_speed
        if self.rect.bottom > self.scene.bottom:
            # print('Bye, player!')
            # self.kill()
            self.y_speed *= -1
            self.rect.y += self.y_speed
        print(f'Player y = {self.rect.y}')

    def boost(self):
        self.y_speed -= 10
