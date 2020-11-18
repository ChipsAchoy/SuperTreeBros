
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


class Player(object):
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
        self.powerUp = ""
        self.x = x
        self.y = y
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.extraJumps = 0
        self.shield = False
        self.power = 10
        self.images = []
        img = pygame.image.load(os.path.join('images', 'jan_stand.png'))
        self.images.append(img)
        self.image = self.images[0]
        
        for i in range(1,4):
            img = pygame.image.load(os.path.join('images', 'jan_run' + str(i) + '.png'))
            self.images.append(img)
        img = pygame.image.load(os.path.join('images', 'jan_jump.png'))
        self.images.append(img)
        img = pygame.image.load(os.path.join('images', 'jan_land.png'))
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
                if not self.isJump:
                    self.image = pygame.transform.flip(self.images[self.frame], True, False)
                else:
                    self.image = pygame.transform.flip(self.images[4], True, False)
            # moving right
            if self.movex > 0:
                self.frame += 1
                if self.frame > 3:
                    self.frame = 1
                if not self.isJump:
                    self.image = self.images[self.frame]
                else:
                    self.image = self.images[4]
        else:
            if self.movex > 0:
                self.image = pygame.transform.flip(self.images[0], True, False)
            else:
                self.image = self.images[0]


    def jump(self, grv):
        
        if not self.falling : #or (self.extraJumps > 0):
            self.image = self.images[4]
            self.isJump = True
            self.jumpCount = 14
        elif self.extraJumps > 0:
            self.image = self.images[4]
            self.isJump = True
            self.jumpCount = 35
            self.extraJumps = 0

    def performPower(self):
        if self.powerUp != "":
            if self.powerUp == "forcepush":
                self.power = 50
            elif self.powerUp == "extrajump":
                self.extraJumps = 1
            elif self.powerUp == "shield":
                self.shield = True
       
    def pushed(self, pushed):
        self.x += pushed

    def down(self):
        self.image = self.images[5]

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))



class Powerups:
    def __init__(self):
        print("")

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
    
    player1 = Player(['w', 'a', 'd', 's','g'], 100, 100)  # spawn player
    player_list.append(player1)

    player2 = Player([pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_RSHIFT], 750, 100)  # spawn player
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
                        elif event.key == ord(player.controls[3]):
                            player.down()
                        elif event.key == ord(player.controls[0]):
                            player.jump(gravity)
                        elif event.key == ord(player.controls[4]):
                            player.powerUp = "forcepush"
                            player.performPower()


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
                        elif event.key == player.controls[2]:
                            player.control(steps_x)
                        elif event.key == player.controls[3]:
                            player.down()
                        elif event.key == player.controls[0]:
                            player.jump(gravity)
                        elif event.key == player.controls[4]:
                            player.performPower()
                            

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
                if player != current and not player.shield:
                    if (current.x + 10 <= player.x and current.x + 50 >= player.x) and (current.y >= player.y - 10 and current.y <= player.y +90):
                        player.pushed(current.power)
                    elif (current.x-10 >= player.x and current.x-50 <= player.x) and (current.y >= player.y - 10 and current.y <= player.y +90):
                        player.pushed(-current.power)
                
            player.update()
            player.draw(world)

        pygame.display.flip()
        clock.tick(fps)
        

#main()

def ventana_controles():
    pygame.init()
    AZUL = (0, 26, 51)
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 700
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(AZUL)
    pygame.display.set_caption("CREDITOS")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        titleFont = pygame.font.Font("freesansbold.ttf", 40)
        letrasFont = pygame.font.Font("freesansbold.ttf", 70)
        player1 = titleFont.render("PLAYER 1 CONTROLS:", True, BLANCO)
        player2 = titleFont.render("PLAYER 2 CONTROLS:", True, BLANCO)
        screen.blit(player1, (20, 20))
        screen.blit(player2, (20, 340))

        cuadrado1 = pygame.draw.rect(screen, BLANCO, (200, 100, 70, 70))
        W = letrasFont.render("W", True, NEGRO)
        screen.blit(W, (200, 105))
        salto = titleFont.render("Jump", True, NEGRO)
        screen.blit(salto, (280, 115))

        cuadrado2 = pygame.draw.rect(screen, BLANCO, (200, 190, 70, 70))
        S = letrasFont.render("S", True, NEGRO)
        screen.blit(S, (210, 195))
        abajo = titleFont.render("Down", True, NEGRO)
        screen.blit(abajo, (185, 270))

        cuadrado3 = pygame.draw.rect(screen, BLANCO, (290, 190, 70, 70))
        D = letrasFont.render("D", True, NEGRO)
        screen.blit(D, (300, 195))
        derecha = titleFont.render("Right", True, NEGRO)
        screen.blit(derecha, (370, 205))

        cuadrado4 = pygame.draw.rect(screen, BLANCO, (110, 190, 70, 70))
        A = letrasFont.render("A", True, NEGRO)
        screen.blit(A, (120, 195))
        izquierda = titleFont.render("Left", True, NEGRO)
        screen.blit(izquierda, (20, 205))

        cuadrado5 = pygame.draw.rect(screen, BLANCO, (570, 190, 70, 70))
        G = letrasFont.render("G", True, NEGRO)
        screen.blit(G, (580, 195))
        power = titleFont.render("Power", True, NEGRO)
        screen.blit(power, (660, 205))

        pygame.display.update()

def main_menu():
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    GRIS = (211, 211, 211)
    pygame.init()
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 700
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Super Tree bros")
    # BackGround = pygame.image.load('')

    running = True
    # screen.blit(BackGround, (0, 0))

    while running:  # iteration for space of the button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 350 + 200 > mouse[0] > 350 and 150 + 50 > mouse[1] > 150:
            pygame.draw.rect(screen, GRIS, (350, 150, 200, 50))
            if click[0] == 1:
                running = False
                main()

        else:
            BR1 = pygame.draw.rect(screen, BLANCO, (350, 150, 200, 50))

        if 350 + 200 > mouse[0] > 350 and 250 + 50 > mouse[1] > 250:
            pygame.draw.rect(screen, GRIS, (350, 250, 200, 50))
            if click[0] == 1:
                running = False
                main()

        else:
            BR2 = pygame.draw.rect(screen, BLANCO, (350, 250, 200, 50))

        if 350 + 200 > mouse[0] > 350 and 350 + 50 > mouse[1] > 350:
            pygame.draw.rect(screen, GRIS, (350, 350, 200, 50))
            if click[0] == 1:
                running = False
                main()

        else:
            BR3 = pygame.draw.rect(screen, BLANCO, (350, 350, 200, 50))

        if 350 + 200 > mouse[0] > 350 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(screen, GRIS, (350, 450, 200, 50))
            if click[0] == 1:
                running = False
                ventana_controles()

        else:
            BR4 = pygame.draw.rect(screen, BLANCO, (350, 450, 200, 50))

        titleFont = pygame.font.Font("freesansbold.ttf", 60)
        gameTitle = titleFont.render("SUPER TREE BROS", True, NEGRO)
        screen.blit(gameTitle, (150, 50))
        textFont = pygame.font.Font("freesansbold.ttf", 28)  # font
        text1 = textFont.render("2 JUGADORES", True, NEGRO)  # new game text
        screen.blit(text1, (350, 165))
        text2 = textFont.render("3 JUGADORES", True, NEGRO)  # load text
        screen.blit(text2, (350, 265))
        text3 = textFont.render("4 JUGADORES", True, NEGRO)  # Instructions text
        screen.blit(text3, (350, 365))
        text4 = textFont.render("CONTROLES", True, NEGRO)  # Credits text
        screen.blit(text4, (350, 465))

        pygame.display.update()

main_menu()
