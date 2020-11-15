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


'''
Objects
'''


class Player:
    """
    Spawn a player
    """

    def __init__(self, controls, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.controls = controls
        self.moving = False
        self.isJump = False
        self.jumpCount = 10
        self.x = x
        self.y = y
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.jumpH = 12
        self.images = []
        img = pygame.image.load(os.path.join('images', 'jan_stand.png'))
        self.images.append(img)
        self.image = self.images[0]
        
        for i in range(1,4):
            img = pygame.image.load(os.path.join('images', 'jan_run' + str(i) + '.png'))
            self.images.append(img)


    def control(self, x):
        """
        control player movement
        """
        self.movex += x

    def update(self):
        """
        Update sprite position
        """

        self.x = self.x + self.movex
        #self.y = self.y + self.movey
        
        if self.moving:
            # moving left
            if self.movex < 0:
                self.frame += 1
                if self.frame > 3:
                    self.frame = 1
                self.image = pygame.transform.flip(self.images[self.frame], True, False)

            # moving right
            if self.movex > 0:
                self.frame += 1
                if self.frame > 3:
                    self.frame = 1
                self.image = self.images[self.frame]
        else:
            self.image = self.images[0]


    def jump(self):
        self.isJump = True
            if not (player.isJump):
                if player.jumpCount >= -10:
                    neg = 1
                    if player.jumpCount < 0:
                        neg = -1
                    player.y -= (player.jumpCount ** 2) * 0.5 * neg
                    player.jumpCount -= 1
            else:
                player.isJump = False
                player.jumpCount = 10

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        

class Platform:
    def __init__(self, screen, xi, yi, distx, disty):
        self.xi = xi
        self.yi = yi
        self.distx = distx
        self.disty = disty
        self.color = (90, 70, 50)
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.xi, self.yi, self.distx, self.disty))
    
        

def main():
    '''
    Setup
    '''
    backdrop = pygame.image.load("images/bg.png")
    clock = pygame.time.Clock()
    pygame.init()
    #backdropbox = world.get_rect()
    main = True

    steps_x = 10
    steps_y = 5
    player_list = []
    
    player1 = Player(['w', 'a', 'd'], 0, 500)  # spawn player
    player_list.append(player1)
    

    player2 = Player([pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT], 500, 500)  # spawn player
    player_list.append(player2)
    
    plat = Platform(world, 450, 500, 100, 100)

    
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
                    
            for player in player_list:
                if isinstance(player.controls[0], str):
                    if event.type == pygame.KEYDOWN:

                        player.moving = True
                        if event.key == ord(player.controls[1]):
                            player.control(-steps_x)
                        if event.key == ord(player.controls[2]):
                            player.control(steps_x)
                        if event.key == ord(player.controls[0]):
                            player.jump()

                    if event.type == pygame.KEYUP:

                        player.moving = False
                        if event.key == ord(player.controls[1]):
                            player.control(steps_x)
                        if event.key == ord(player.controls[2]):
                            player.control(-steps_x)
                        if event.key == ord(player.controls[0]):
                            player.jump()
                else:
                    if event.type == pygame.KEYDOWN:
                        
                        player.moving = True
                        if event.key == player.controls[1]:
                            player.control(-steps_x)
                        if event.key == player.controls[2]:
                            player.control(steps_x)
                        if event.key == player.controls[0]:
                            print("wtf")
                            

                    if event.type == pygame.KEYUP:
                        
                        player.moving = False
                        if event.key == player.controls[1]:
                            player.control(steps_x)
                        if event.key == player.controls[2]:
                            player.control(-steps_x)
                        if event.key == player.controls[0]:
                            print("wtf")
                        

        world.fill((0,0,0))
        world.blit(backdrop, (0,0))
        
        plat.draw()

        for player in player_list:
            player.update()
            player.draw(world)

        pygame.display.flip()
        clock.tick(fps)
        

main()
