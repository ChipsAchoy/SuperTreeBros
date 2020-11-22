
import pygame
import sys, os, random

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
        self.pressed = [False, False]
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
        self.ticks = 0
        self.power = 10
        self.powerEnable = False
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
            self.jumpCount = 25
            self.extraJumps = 0
            self.powerEnable = False
            self.powerUp = ""

    def performPower(self):
        if self.powerUp != "":
            self.powerEnable = True
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

    def checkTime(self):
        if (self.powerUp == "shield" or "forcepush") and self.powerEnable == True:
            return True
        else:
            return False

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))



class Powerups:
    def __init__(self, screen, stype, xi, yi):
        self.type = stype
        self.x = xi
        self.y = yi
        self.distx = 30
        self.disty = 30
        self.screen = screen
        self.movey = 0
        self.falling = True
        self.catch = False
        self.ticks = 0
        #self.image = image

        if self.type == "extrajump":
            self.color = (180,0,0)
        elif self.type == "forcepush":
            self.color = (0,180,0)
        elif self.type == "shield":
            self.color = (0,0,180)

    def fall(self, grv):
        self.movey += grv

    def update(self):
        if self.falling:
            self.y = self.y + self.movey
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.distx, self.disty))


class Platform:
    def __init__(self, screen, xi, yi, distx, disty):
        self.xi = xi
        self.yi = yi
        self.distx = distx
        self.disty = disty
        self.color = (90, 70, 50)
        self.screen = screen
        self.ticks = 0

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
    powerup_list = []
    powerup_types = ["forcepush","shield","extrajump"]
    
    crono = 0
    flag = True
    flag2 = True
    
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

    ref_crono = (pygame.time.get_ticks()) // 1000
    
    while main:
        
        crono = ((pygame.time.get_ticks()) // 1000) - ref_crono
        

        if crono%30 == 0 and crono != 0 and flag:
            positionx = random.randint(50, 850)
            p_type = random.randint(0,2)
            powerup_list.append(Powerups(world, powerup_types[p_type], positionx, 0))
            flag = False

        elif crono%30 != 0 and crono != 0 and not flag:
            flag = True

        if crono>=30 and crono%2 == 0 and flag2:
            for power in powerup_list:
                power.ticks += 1
                if power.ticks > 7:
                    powerup_list.pop(powerup_list.index(power))

            for player in player_list:
                if player.checkTime():
                    player.ticks += 1
                    if player.ticks > 6:
                        player.ticks = 0
                        player.powerEnable = False
                        print("Finalizado: "+player.powerUp)
                        player.powerUp = ""
                        player.shield = False
                        player.power = 10
            
            flag2 = False

            
        elif crono>=30 and crono%2 != 0 and not flag2:
            flag2 = True
        ###Programar un cronometro para cada objeto#### Esto para que sepa cuando desaparecer
        
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
                            player.pressed[0] = True
                            player.control(-steps_x)
                        elif event.key == ord(player.controls[2]):
                            player.pressed[1] = True
                            player.control(steps_x)
                        elif event.key == ord(player.controls[3]):
                            player.down()
                        elif event.key == ord(player.controls[0]):
                            player.jump(gravity)
                        elif event.key == ord(player.controls[4]):
                            if player.powerUp != "" and not player.powerEnable:
                                print(player.powerUp)
                                player.performPower()


                    elif event.type == pygame.KEYUP:
                        
                        if event.key == ord(player.controls[1]):
                            player.pressed[0] = False
                            player.control(steps_x)
                        elif event.key == ord(player.controls[2]):
                            player.pressed[1] = False
                            player.control(-steps_x)
                        if not player.pressed[0] and not player.pressed[1]:
                            player.moving = False
                        
                            
                else:
                    if event.type == pygame.KEYDOWN:
                        
                        player.moving = True
                        if event.key == player.controls[1]:
                            player.pressed[0] = True
                            player.control(-steps_x)
                        elif event.key == player.controls[2]:
                            player.pressed[1] = True
                            player.control(steps_x)
                        elif event.key == player.controls[3]:
                            player.down()
                        elif event.key == player.controls[0]:
                            player.jump(gravity)
                        elif event.key == player.controls[4]:
                            if player.powerUp != "" and not player.powerEnable:
                                print(player.powerUp)
                                player.performPower()
                            

                    elif event.type == pygame.KEYUP:
                        if event.key == player.controls[1]:
                            player.control(steps_x)
                            player.pressed[0] = False
                        elif event.key == player.controls[2]:
                            player.control(-steps_x)
                            player.pressed[1] = False
                        if not player.pressed[0] and not player.pressed[1]:
                            player.moving = False

                        
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
                

            for power in powerup_list:
                if player.x-10 <= power.x+15 and player.x+100 >= power.x+15 and player.y <= power.y+15 and player.y+90 >= power.y+15:
                    if not player.powerEnable and player.powerUp == "":
                        player.powerUp = power.type
                        print("obtenido: "+power.type)
                        powerup_list.pop(powerup_list.index(power))
                    
            
            player.update()
            player.draw(world)


        for power in powerup_list:
            for plat in plat_list:
                if power.x-10 >= plat.xi and power.x + 30 <= plat.xi + plat.distx and power.y+30 >= plat.yi and power.y+30 <= plat.yi+30:
                    power.y = plat.yi - 30
                    power.falling = False
            if power.y > 700:
                powerup_list.pop(powerup_list.index(power))
                    
            if power.falling:
                power.fall(gravity*0.5)
                    
            power.update()
            power.draw()
            
        
        pygame.display.flip()
        clock.tick(fps)
        


def ventana_controles():
    pygame.init()
    AZUL = (0, 26, 51)
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 700
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(AZUL)
    pygame.display.set_caption("CONTROLES")

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

        power1 = pygame.draw.rect(screen, BLANCO, (570, 190, 70, 70))
        G = letrasFont.render("G", True, NEGRO)
        screen.blit(G, (580, 195))
        power1 = titleFont.render("Power", True, NEGRO)
        screen.blit(power1, (660, 205))

        flecha1 = pygame.draw.rect(screen, BLANCO, (200, 420, 70, 70))
        cordenadas1 = [(235, 430), (250, 470), (220, 470)]
        pygame.draw.polygon(screen, NEGRO, cordenadas1, 0)
        salto2 = titleFont.render("Jump", True, NEGRO)
        screen.blit(salto2, (280, 435))

        flecha2 = pygame.draw.rect(screen, BLANCO, (200, 520, 70, 70))
        cordenadas2 = [(235, 575), (250, 535), (220, 535)]
        pygame.draw.polygon(screen, NEGRO, cordenadas2, 0)
        abajo2 = titleFont.render("Down", True, NEGRO)
        screen.blit(abajo2, (185, 600))

        flecha3 = pygame.draw.rect(screen, BLANCO, (290, 520, 70, 70))
        cordenadas3 = [(305, 540), (305, 570), (350, 555)]
        pygame.draw.polygon(screen, NEGRO, cordenadas3, 0)
        derecha2 = titleFont.render("Right", True, NEGRO)
        screen.blit(derecha2, (370, 535))

        flecha4 = pygame.draw.rect(screen, BLANCO, (110, 520, 70, 70))
        cordenadas4 = [(120, 555), (165, 540), (165, 570)]
        pygame.draw.polygon(screen, NEGRO, cordenadas4, 0)
        izquierda2 = titleFont.render("Left", True, NEGRO)
        screen.blit(izquierda2, (20, 535))

        power2 = pygame.draw.rect(screen, BLANCO, (570, 520, 140, 70))
        SHIFTD = titleFont.render("SHIFTD", True, NEGRO)
        screen.blit(SHIFTD, (565, 535))
        screen.blit(power1, (730, 535))

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
