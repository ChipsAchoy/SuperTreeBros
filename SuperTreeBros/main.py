
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
        self.falling = True
        self.jumpCount = 0
        self.colide = False
        self.x = x
        self.y = y
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.extraJumps = 0
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

    def fall(self, grv):
        self.movey += grv
    
    def update(self):
        """
        Update sprite position
        """

        self.x = self.x + self.movex
        self.y = self.y + self.movey
        
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


    def jump(self, grv):
        
        if (not self.falling): #or (self.extraJumps > 0):
            self.isJump = True
            self.jumpCount = 14
            #if self.extraJumps > 0:
                #self.extraJumps -= 1

            
    def pushed(self, pushed):
        self.x += pushed
    
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
    
    gravity = 1
    steps_x = 10
    player_list = []
    
    player1 = Player(['w', 'a', 'd'], 100, 100)  # spawn player
    player_list.append(player1)
    

    player2 = Player([pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT], 750, 100)  # spawn player
    player_list.append(player2)
    
    plat1 = Platform(world, 250, 450, 400, 30)
    plat2 = Platform(world, 50, 300, 150, 30)
    plat3 = Platform(world, 700, 300, 150, 30)

    plat_list = [plat1, plat2, plat3]
    print(plat_list)
    
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
                        elif event.key == ord(player.controls[2]):
                            player.control(steps_x)
                        elif event.key == ord(player.controls[0]):
                            player.jump(gravity)

                    elif event.type == pygame.KEYUP:
                        player.moving = False
                        if event.key == ord(player.controls[1]):
                            player.control(steps_x)
                        elif event.key == ord(player.controls[2]):
                            player.control(-steps_x)
                        
                            
                else:
                    if event.type == pygame.KEYDOWN:
                        
                        player.moving = True
                        if event.key == player.controls[1]:
                            player.control(-steps_x)
                        if event.key == player.controls[2]:
                            player.control(steps_x)
                        if event.key == player.controls[0]:
                            player.jump(gravity)
                            

                    elif event.type == pygame.KEYUP:
                        player.moving = False
                        if event.key == player.controls[1]:
                            player.control(steps_x)
                        elif event.key == player.controls[2]:
                            player.control(-steps_x)

                        
        world.fill((0,0,0))
        world.blit(backdrop, (0,0))

        for plat in plat_list:
            plat.draw()

        for player in player_list:
            #player.extraJumps = 1
            if player.isJump:
                player.falling = True
                if player.jumpCount > 0:
                    player.fall(-gravity)
                    player.jumpCount -= 1
                else:
                    player.isJump = False
                    
            #Colision de caida
            elif player.falling:
                player.fall(gravity)
                for plat in plat_list:
                    if (player.x-10 >= plat.xi and player.x+45 <= plat.xi + plat.distx) and (player.y + 79 >= plat.yi and player.y + 79 <= plat.yi+30):
                        player.y = plat.yi - 76
                        player.movey = 0
                        player.falling = False
                        
            else:
                checks = 0
                for plat in plat_list:
                    if player.x < plat.xi or player.x+45 > plat.xi + plat.distx:
                        checks += 1
                if checks == 3:
                    player.falling = True

            for current in player_list:
                if player != current:
                    if (current.x + 10 <= player.x and current.x + 50 >= player.x) and (current.y >= player.y - 10 and current.y <= player.y +90):
                        player.pushed(5)
                    elif (current.x-10 >= player.x and current.x-50 <= player.x) and (current.y >= player.y - 10 and current.y <= player.y +90):
                        player.pushed(-5)
                
            player.update()
            player.draw(world)

        pygame.display.flip()
        clock.tick(fps)
        

main()
