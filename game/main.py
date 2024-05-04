import asyncio
import sys

import pygame

from player import Player


FPS = 30
SCREEN_SIZE = (1200, 800)


async def main():
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()

    background = pygame.Surface(screen.get_size()).convert()
    background.fill('black')

    screen.fill('aquamarine')  # https://www.pygame.org/docs/ref/color_list.html

    player = Player()
    all_sprites = pygame.sprite.RenderPlain((player, ))

    while True:
        for event in pygame.event.get():
            if not event.type == pygame.KEYUP:
                continue

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_SPACE:
                player.boost()

        all_sprites.update()

        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(FPS)
        await asyncio.sleep(0)


if __name__ == '__main__':
    asyncio.run(main())
