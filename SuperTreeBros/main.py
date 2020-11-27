
import pygame
import sys, os, random

selectedPlayers = [-1, -1]
podium = [None, None, None, None]

'''
Variables
'''

worldx = 900
worldy = 700
fps = 40
world = pygame.display.set_mode([worldx, worldy])


'''
Objects
'''


class Player(object):
    """
    Spawn a player
    """

    def __init__(self, controls, x, y, character):
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
        self.powerEnable = False
        self.images = []
        self.titleFont = pygame.font.Font("freesansbold.ttf", 18)
        self.vida = 3
        self.VIDA = self.titleFont.render(str(self.vida), True, (0, 0, 0))
        self.xi = x
        self.yi = y
        

        if character == 0:
            self.character = "firzen"
            self.height = 77
            self.steps_x = 11
            self.maxJump = 13
            self.power = 10
            self.maxPower = 10
        elif character == 1:
            self.height = 71
            self.character = "jack"
            self.steps_x = 8
            self.maxJump = 20
            self.power = 11
            self.maxPower = 11
        elif character == 2:
            self.height = 80
            self.character = "jan"
            self.steps_x = 17
            self.maxJump = 14
            self.power = 8
            self.maxPower = 8
        elif character == 3:
            self.character = "justin"
            self.height = 71
            self.steps_x = 6
            self.maxJump = 13
            self.power = 18
            self.maxPower = 18
        elif character == 4:
            self.character = "louisEX"
            self.height = 74
            self.steps_x = 15
            self.maxJump = 13
            self.power = 10
            self.maxPower = 10

        img = pygame.image.load(os.path.join('images/Sprites/'+self.character, self.character+'_stand.png'))
        self.images.append(img)
        self.image = self.images[0]
        
        for i in range(1,4):
            img = pygame.image.load(os.path.join('images/Sprites/'+self.character, self.character+'_run' + str(i) + '.png'))
            self.images.append(img)
        img = pygame.image.load(os.path.join('images/Sprites/'+self.character, self.character+'_jump.png'))
        self.images.append(img)
        img = pygame.image.load(os.path.join('images/Sprites/'+self.character, self.character+'_land.png'))
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
            self.jumpCount = self.maxJump
        elif self.extraJumps > 0:
            self.image = self.images[4]
            self.isJump = True
            self.jumpCount = 26
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

    def draw(self, surface, current):
        surface.blit(self.image, (self.x, self.y))
        self.VIDA = self.titleFont.render(str(self.vida), True, (0, 0, 0))
        if current:
            surface.blit(self.VIDA, (75, 676))
        else:
            surface.blit(self.VIDA, (810, 676))
            
        
        

class Powerups:
    def __init__(self, screen, stype, xi, yi, image):
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
        self.image = image

    def fall(self, grv):
        self.movey += grv

    def update(self):
        if self.falling:
            self.y = self.y + self.movey
    
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))


class Platform:
    def __init__(self, screen, xi, yi, distx, disty, image):
        self.xi = xi
        self.yi = yi
        self.distx = distx
        self.disty = disty
        self.screen = screen
        self.ticks = 0
        self.image = image

    def draw(self):
        self.screen.blit(self.image, (self.xi, self.yi))

class Frames:
    def __init__(self):
        self.frame1 = None
        self.frame2 = None
        self.x1 = 0
        self.y1 = 474
        self.x2 = 742
        self.y2 = 474
        self.player0 = pygame.image.load('images/PlayerFrames/firzen_frame.png')
        self.player1 = pygame.image.load('images/PlayerFrames/jack_frame.png')
        self.player2 = pygame.image.load('images/PlayerFrames/jan_frame.png')
        self.player3 = pygame.image.load('images/PlayerFrames/justin_frame.png')
        self.player4 = pygame.image.load('images/PlayerFrames/louisEX_frame.png')
        self.listaFrames = [self.player0, self.player1, self.player2, self.player3, self.player4]
        self.titleFont = pygame.font.Font("freesansbold.ttf", 20)
        self.PLAYER1 = self.titleFont.render("PLAYER 1", True, (0, 0, 0))
        self.PLAYER2 = self.titleFont.render("PLAYER 2", True, (0, 0, 0))
        

    def drawFrames(self, world):
        for i in range(len(self.listaFrames)):
            if i == selectedPlayers[0]:
                self.frame1 = self.listaFrames[i]
                break

        for i in range(len(self.listaFrames)):
            if i == selectedPlayers[1]:
                self.frame2 = self.listaFrames[i]
                break

        world.blit(self.frame1, (self.x1, self.y1))
        world.blit(self.frame2, (self.x2, self.y2))

        world.blit(self.PLAYER1, (self.x1 + 30, self.y1))
        world.blit(self.PLAYER2, (self.x2 + 30, self.y2))
               

def main():
    '''
    Setup
    '''
    global selectedPlayers
    backdrop = pygame.image.load("images/background/bg.png")
    platImage1 = pygame.image.load("images/Platforms/small_platform.png")
    platImage2 = pygame.image.load("images/Platforms/big_platform.png")

    force_image = pygame.image.load("images/powericons/forcepush.png")
    shield_image = pygame.image.load("images/powericons/shield.png")
    jump_image = pygame.image.load("images/powericons/jump.png")

    
    clock = pygame.time.Clock()
    pygame.init()
    #backdropbox = world.get_rect()
    main = True
    
    gravity = 1
    #steps_x = 10
    player_list = []
    powerup_list = []
    powerup_types = ["forcepush","shield","extrajump"]
    powerup_images = [force_image, shield_image, jump_image]
    
    crono = 0
    flag = True
    flag2 = True
    
    player1 = Player(['w', 'a', 'd', 's','g'], 100, 100,selectedPlayers[0])  # spawn player
    player_list.append(player1)

    player2 = Player([pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_RSHIFT], 750, 100,selectedPlayers[1])  # spawn player
    player_list.append(player2)
    
    plat1 = Platform(world, 250, 450, 400, 30, platImage2)
    plat2 = Platform(world, 50, 300, 150, 30, platImage1)
    plat3 = Platform(world, 700, 300, 150, 30, platImage1)

    plat_list = [plat1, plat2, plat3]
    print(plat_list)

    global podium

    fs = Frames()

    '''
    Main Loop
    '''

    ref_crono = (pygame.time.get_ticks()) // 1000
    
    while main:
        
        crono = ((pygame.time.get_ticks()) // 1000) - ref_crono
        

        if crono%30 == 0 and crono != 0 and flag:
            positionx = random.randint(50, 850)
            p_type = random.randint(0,2)
            powerup_list.append(Powerups(world, powerup_types[p_type], positionx, 0, powerup_images[p_type]))
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
                        player.power = player.maxPower
            
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
                            player.control(-player.steps_x)
                        elif event.key == ord(player.controls[2]):
                            player.pressed[1] = True
                            player.control(player.steps_x)
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
                            player.control(player.steps_x)
                        elif event.key == ord(player.controls[2]):
                            player.pressed[1] = False
                            player.control(-player.steps_x)
                        if not player.pressed[0] and not player.pressed[1]:
                            player.moving = False
  
                            
                else:
                    if event.type == pygame.KEYDOWN:
                        
                        player.moving = True
                        if event.key == player.controls[1]:
                            player.pressed[0] = True
                            player.control(-player.steps_x)
                        elif event.key == player.controls[2]:
                            player.pressed[1] = True
                            player.control(player.steps_x)
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
                            player.control(player.steps_x)
                            player.pressed[0] = False
                        elif event.key == player.controls[2]:
                            player.control(-player.steps_x)
                            player.pressed[1] = False
                        if not player.pressed[0] and not player.pressed[1]:
                            player.moving = False

                        
        world.fill((0,0,0))
        world.blit(backdrop, (0,0))
        fs.drawFrames(world)

        for plat in plat_list:
            plat.draw()

        for player in player_list:
            cord = True
            if player == player_list[0]:
                cord = True
            elif player == player_list[1]:
                cord = False
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
                    if (player.x-10 >= plat.xi and player.x+45 <= plat.xi + plat.distx) and (player.y + player.height >= plat.yi and player.y + player.height <= plat.yi+30):
                        player.y = plat.yi - player.height
                        player.movey = 0
                        player.falling = False
                if player.y >= 700:
                    player.vida -= 1
                    player.x = player.xi
                    player.y = player.yi
                if player.vida == 0:
                    if player == player_list[0]:
                        podium = [player2, player1, "PLAYER2", "PLAYER1"]
                        main = False
                        ganador_perdedor(podium)
                    else:
                        podium = [player1, player2, "PLAYER1", "PLAYER2"]
                        main = False
                        ganador_perdedor(podium)

                        
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
            player.draw(world, cord)


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

def escoger_jugador():
    #Base de la ventana
    pygame.init()
    running = True
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 700
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("ESCOGER EL JUGADOR")

    #Colores
    GRIS = (100, 100, 100)
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    AZUL = (0, 26, 51)

    #Textos y fonts
    titleFont = pygame.font.Font("freesansbold.ttf", 40)
    subtitleFONT = pygame.font.Font("freesansbold.ttf", 20)
    player1 = titleFont.render("PLAYER 1", True, BLANCO)
    player2 = titleFont.render("PLAYER 2", True, BLANCO)
    FIJAR = titleFont.render("FIJAR", True, NEGRO)

    FIRZEN = subtitleFONT.render("Jugador seleccionado: FIRZEN", True, BLANCO)
    JACK = subtitleFONT.render("Jugador seleccionado: JACK", True, BLANCO)
    JAN = subtitleFONT.render("Jugador seleccionado: JAN", True, BLANCO)
    JUSTIN = subtitleFONT.render("Jugador seleccionado: JUSTIN", True, BLANCO)
    LOUISEX = subtitleFONT.render("Jugador seleccionado: LOUISEX", True, BLANCO)
    NINGUNO = subtitleFONT.render("Jugador seleccionado: ", True, BLANCO)

    #Imagenes de los jugadores
    firzen = pygame.image.load("images/Sprites/firzen/firzen_splash.png")
    jack = pygame.image.load("images/Sprites/jack/jack_splash.png")
    jan = pygame.image.load("images/Sprites/jan/jan_splash.png")
    justin = pygame.image.load("images/Sprites/justin/justin_splash.png")
    louisex = pygame.image.load("images/Sprites/louisEX/louisEX_splash.png")


    listaFlag = [False, False, False, False, False]
    listaFlag2 = [False, False, False, False, False]
    selected1 = -1
    selected2 = -1
    global selectedPlayers

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        screen.fill(AZUL)
        pygame.draw.line(screen, NEGRO, (450, 0), (450, 900), 5)
        screen.blit(player1, (150, 50))
        screen.blit(player2, (575, 50))

        # Mouse, click y prosiciones de los cuadros
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        personaje0 = 100 + 120 > mouse[0] > 100 and 150 + 120 > mouse[1] > 150 and click[0] == 1
        personaje1 = 250 + 120 > mouse[0] > 250 and 150 + 120 > mouse[1] > 150 and click[0] == 1
        personaje2 = 100 + 120 > mouse[0] > 100 and 300 + 120 > mouse[1] > 300 and click[0] == 1
        personaje3 = 250 + 120 > mouse[0] > 250 and 300 + 120 > mouse[1] > 300 and click[0] == 1
        personaje4 = 175 + 120 > mouse[0] > 175 and 450 + 120 > mouse[1] > 450 and click[0] == 1

        listaPersonajes = [personaje0, personaje1, personaje2, personaje3, personaje4]


        if click[0] == 1:
            for i in range(len(listaPersonajes)):
                if listaPersonajes[i] == True:
                    selected1 = i
                    break

            for i in range(len(listaFlag)):
                if i == selected1:
                    listaFlag[i] = True
                else:
                    listaFlag[i] = False
        else:
            screen.blit(NINGUNO, (100, 100))

        if listaFlag[0] == True:
            screen.blit(FIRZEN, (100, 100))
        if listaFlag[1] == True:
            screen.blit(JACK, (100, 100))
        if listaFlag[2] == True:
            screen.blit(JAN, (100, 100))
        if listaFlag[3] == True:
            screen.blit(JUSTIN, (100, 100))
        if listaFlag[4] == True:
            screen.blit(LOUISEX, (100, 100))

        #Cuadros para seleccionar personajes:

        #SELECCION DEL PEROSNAJE 1
        #Personaje 0
        screen.blit(firzen, (100, 150))
        pygame.draw.rect(screen, NEGRO, (100, 150, 120, 120), 2)

        #Personaje 1
        screen.blit(jack, (250, 150))
        pygame.draw.rect(screen, NEGRO, (250, 150, 120, 120), 2)

        #Personaje 2
        screen.blit(jan, (100, 300))
        pygame.draw.rect(screen, NEGRO, (100, 300, 120, 120), 2)

        #Personaje 3
        screen.blit(justin, (250, 300))
        pygame.draw.rect(screen, NEGRO, (250, 300, 120, 120), 2)

        #Personaje 4
        screen.blit(louisex, (175, 450))
        pygame.draw.rect(screen, NEGRO, (175, 450, 120, 120), 2)

        #Botones de fijar1
        if 125 + 200 > mouse[0] > 125 and 580 + 50 > mouse[1] > 580:
            pygame.draw.rect(screen, GRIS, (125, 580, 200, 50))
            if click[0] == 1:
                selectedPlayers[0] = selected1
                print(selectedPlayers)
        else:
            pygame.draw.rect(screen, BLANCO, (125, 580, 200, 50))
        screen.blit(FIJAR, (160, 585))


        #SELECCION DEL PEROSNAJE 2

        personaje5 = 525 + 120 > mouse[0] > 525 and 150 + 120 > mouse[1] > 150 and click[0] == 1 #(525, 150, 120, 120)
        personaje6 = 675 + 120 > mouse[0] > 675 and 150 + 120 > mouse[1] > 150 and click[0] == 1 #(675, 150, 120, 120)
        personaje7 = 525 + 120 > mouse[0] > 525 and 300 + 120 > mouse[1] > 300 and click[0] == 1 #(525, 300, 120, 120)
        personaje8 = 675 + 120 > mouse[0] > 675 and 300 + 120 > mouse[1] > 300 and click[0] == 1 #(675, 300, 120, 120)
        personaje9 = 600 + 120 > mouse[0] > 600 and 450 + 120 > mouse[1] > 450 and click[0] == 1 #(600, 450, 120, 120)

        listaPersonajes2 = [personaje5, personaje6, personaje7, personaje8, personaje9]

        if click[0] == 1:
            for i in range(len(listaPersonajes2)):
                if listaPersonajes2[i] == True:
                    selected2 = i
                    break

            for i in range(len(listaFlag2)):
                if i == selected2:
                    listaFlag2[i] = True
                else:
                    listaFlag2[i] = False
        else:
            screen.blit(NINGUNO, (500, 100))

        if listaFlag2[0] == True:
            screen.blit(FIRZEN, (500, 100))
        if listaFlag2[1] == True:
            screen.blit(JACK, (500, 100))
        if listaFlag2[2] == True:
            screen.blit(JAN, (500, 100))
        if listaFlag2[3] == True:
            screen.blit(JUSTIN, (500, 100))
        if listaFlag2[4] == True:
            screen.blit(LOUISEX, (500, 100))

        #Personaje 0
        screen.blit(firzen, (525, 150))
        pygame.draw.rect(screen, NEGRO, (525, 150, 120, 120), 2)

        #Personaje 1
        screen.blit(jack, (675, 150))
        pygame.draw.rect(screen, NEGRO, (675, 150, 120, 120), 2)

        #Personaje 2
        screen.blit(jan, (525, 300))
        pygame.draw.rect(screen, NEGRO, (525, 300, 120, 120), 2)

        #Personaje 3
        screen.blit(justin, (675, 300))
        pygame.draw.rect(screen, NEGRO, (675, 300, 120, 120), 2)

        #Personaje 4
        screen.blit(louisex, (600, 450))
        pygame.draw.rect(screen, NEGRO, (600, 450, 120, 120), 2)

        if 550 + 200 > mouse[0] > 550 and 580 + 50 > mouse[1] > 580:
            pygame.draw.rect(screen, GRIS, (550, 580, 200, 50))
            if click[0] == 1:
                selectedPlayers[1] = selected2
                print(selectedPlayers)
        else:
            pygame.draw.rect(screen, BLANCO, (550, 580, 200, 50))
        screen.blit(FIJAR, (590, 585))

        if selectedPlayers[0] != -1 and selectedPlayers[1] != -1:
            main()

        pygame.display.update()


def ventana_controles():
    pygame.init()
    AZUL = (0, 26, 51)
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    GRIS = (111, 111, 111)
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

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

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
        
        #BOTON DE REGRESO
        if 360 + 200 > mouse[0] > 360 and 620 + 50 > mouse[1] > 620:
            pygame.draw.rect(screen, GRIS, (360, 620, 200, 50))
            if click[0] == 1:
                running = False
                main_menu()

        else:
            BR1 = pygame.draw.rect(screen, BLANCO, (360, 620, 200, 50))

        textFont = pygame.font.Font("freesansbold.ttf", 32)
        text1 = textFont.render("REGRESAR", True, NEGRO)  
        screen.blit(text1, (370, 630))

        pygame.display.update()


def ganador_perdedor(podium):
    pygame.init()
    
    SCREEN_WIDTH = 626
    SCREEN_HEIGHT = 626
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("GANADOR Y PERDEDOR")
    
    GRIS = (211, 211, 211)
    NEGRO = (0, 0, 0)
    GOLD = (212, 175, 55)
    screen.fill(GRIS)

    titleFont = pygame.font.Font("freesansbold.ttf", 30)

    backGround = pygame.image.load("images/background/fondoGanador3.png")

    running = True

    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
        screen.blit(backGround, (0, 0))

        ganador = titleFont.render(("GANADOR: " + str(podium[2])), True, GOLD)
        screen.blit(ganador, (155, 250))

        screen.blit(podium[0].images[0], (295, 345))
            
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
                escoger_jugador()

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
