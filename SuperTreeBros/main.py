from typing import Tuple

import pygame
import sys
import os

'''
Variables
'''

worldx = 900
worldy = 700
fps = 40
ani = 4
world = pygame.display.set_mode([worldx, worldy])

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)

'''
Objects
'''


class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        for i in range(1,3):
            img = pygame.image.load(os.path.join('images', 'hero' + str(i) + '.png')).convert()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(ALPHA)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def control(self, x, y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y

    def update(self):
        """
        Update sprite position
        """

        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 1:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame], True, False)

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 1:
                self.frame = 0
            self.image = self.images[self.frame]


def main():

    '''
    Setup
    '''

    backdrop = pygame.image.load("images/stage.png")
    clock = pygame.time.Clock()
    pygame.init()
    backdropbox = world.get_rect()
    main = True

    player = Player()  # spawn player
    player.rect.x = 0  # go to x
    player.rect.y = 500  # go to y
    player_list = pygame.sprite.Group()
    player_list.add(player)
    steps_x = 10
    steps_y = 5
 
    '''
    Main Loop
    '''

    while main:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False

            if event.type == pygame.KEYDOWN:
                if event.key == ord('q'):
                    pygame.quit()
                    try:
                        sys.exit()
                    finally:
                        main = False
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    player.control(-steps_x, 0)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    player.control(steps_x, 0)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    player.control(0, -steps_y)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    player.control(steps_x, 0)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    player.control(-steps_x, 0)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    player.control(0, steps_y)

        world.blit(backdrop, backdropbox)
        player.update()
        player_list.draw(world)
        pygame.display.flip()
        clock.tick(fps)
        

main()
