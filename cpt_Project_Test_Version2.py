import pygame

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (  60, 153,  48)
red      = ( 255,   0,   0)
grey     = ( 216, 216, 208)
light_Blue     = ( 103, 166, 184)
orange         = ( 204, 162,  47)
dark_Grey      = (  86, 103, 105)
yellow         = ( 224, 218,  40)
turquoise      = (  63, 140, 124)
dark_Turquoise = (  24,  61,  54)
light_Yellow   = ( 230, 232, 183)

pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()

# Set the width and height of the screen [width, height]
size = (900, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Running Man Tony")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Fonts
menu_Font = pygame.font.Font("8Bit.TTF", 40)
menu_Font2 = pygame.font.Font("Pixeled.ttf", 30)

controls_Font = pygame.font.Font("VCR_OSD_MONO_1.001.ttf", 70)
instructions_Font = pygame.font.Font("VCR_OSD_MONO_1.001.ttf", 25)

# Text Render
menu_Title = menu_Font.render("RUNNING Man Tony", True, white)

menu_Start = menu_Font2.render("PLAY", True, white)
menu_Start2 = menu_Font2.render("PLAY", True, green)

menu_Controls = menu_Font2.render("CONTROLS", True, white)
menu_Controls2 = menu_Font2.render("CONTROLS", True, green)

menu_Exit = menu_Font2.render("EXIT", True, white)
menu_Exit2 = menu_Font2.render("EXIT", True, green)

controls_Title = controls_Font.render("Instructions", True, white)

controls_Back = menu_Font2.render("BACK", True, white)
controls_Back2 = menu_Font2.render("BACK", True, orange)

controls_Forward = instructions_Font.render("Use the \"W\" key to make Tony move forward.", True, white)
controls_Left = instructions_Font.render("Use the \"A\" key to make Tony move left.", True, white)
controls_Backward = instructions_Font.render("Use the \"S\" key to make Tony move backwards.", True, white)
controls_Right = instructions_Font.render("Use the \"D\" key to make Tony move right.", True, white)
controls_Jump = instructions_Font.render("Use the \"Spacebar\" to make Tony jump.", True, white)

gameintro_Start = instructions_Font.render("Start -->", True, white)
gameintro_Start2 = instructions_Font.render("Start -->", True, green)

gameover_Restart = menu_Font2.render("Restart", True, black)
gameover_Restart2 = menu_Font2.render("Restart", True, white)

gameover_Exit = menu_Font2.render("Exit", True, black)
gameover_Exit2 = menu_Font2.render("Exit", True, white)

# Background images
background_Image_Menu = pygame.image.load("menu_image2.png").convert()
background_Image_Controls = pygame.image.load("controls_image.png").convert()
background_Image_GameOver = pygame.image.load("gameover_image.png").convert()
background_Image_Intro = pygame.image.load("intro_screen1.png").convert()

# Menu Music
pygame.mixer.music.load("menu_music.ogg")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

# Level1 Images
character_Tony = pygame.image.load("Tony.png").convert()
character_Tony.set_colorkey(white)

orange_Car = pygame.image.load("orange_car.png").convert()
orange_Car.set_colorkey(white)

green_Car = pygame.image.load("green_car.png").convert()
green_Car.set_colorkey(black)

police_Car = pygame.image.load("police_car.png").convert()
police_Car.set_colorkey(black)

grey_Car = pygame.image.load("grey_car.png").convert()
grey_Car.set_colorkey(black)

main_Building = pygame.image.load("building.png").convert()

sidewalkTexture = pygame.image.load("sidewalk_texture.png").convert()

grassTexture = pygame.image.load("level1_grass.png").convert()

fenceTexture = pygame.image.load("fence.png").convert()
fenceTexture.set_colorkey(white)

lightpostTexture = pygame.image.load("lightpost2.png").convert()
lightpostTexture.set_colorkey(black)

side_Tree = pygame.image.load("tree.png").convert()
side_Tree.set_colorkey(black)

side_Bushes = pygame.image.load("bushes.png").convert()
side_Bushes.set_colorkey(black)

crosswalk_Sign = pygame.image.load("crosswalk_sign.png").convert()
crosswalk_Sign.set_colorkey(black)

side_Bench = pygame.image.load("bench.png").convert()
side_Bench.set_colorkey(white)

side_Pond = pygame.image.load("pond.png").convert()
side_Pond.set_colorkey(black)

# Main Menu
def drawMenu():
    menu = True
    while menu == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos() # format = [x,y]
        click = pygame.mouse.get_pressed()
#########################################################
        screen.blit(background_Image_Menu, [-3,-3])
##########################################################
        if 42+136 > mouse[0] and 310+50 > mouse[1] > 310: #PLay Button
            screen.blit(menu_Start2, [50,290])
            if click[0] == 1:
                menu = False
        else:
            screen.blit(menu_Start, [50,290])
##########################################################
        if 40+260 > mouse[0] and 370+50 > mouse[1] > 370: #Control Button
            screen.blit(menu_Controls2, [50,350])
            if click[0] == 1:
                menu = False
                drawControls()
        else:
            screen.blit(menu_Controls, [50,350])
##########################################################
        if 40+140 > mouse[0] and 432+50 > mouse[1] > 432: #Exit Button
            screen.blit(menu_Exit2, [50,410])
            if click[0] == 1:
                menu = False
                pygame.mixer.music.fadeout(3000)
                pygame.quit()
                quit()
        else:
            screen.blit(menu_Exit, [50,410])

        pygame.display.flip()
        clock.tick(60)


# Control Screen
def drawControls():
    controls = True
    while controls == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                controls = False
                pygame.quit()
                quit()
##########################################################
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
##########################################################
        screen.fill(grey)

        background = screen.blit(background_Image_Controls, [0,-70])

        instructions_Title = screen.blit(controls_Title, [230,30])

        back_Button = pygame.draw.rect(screen, light_Blue, [670,510,135,55])
        back = screen.blit(controls_Back, [680,490])

        forward = screen.blit(controls_Forward, [10,200])
        left = screen.blit(controls_Left, [10,250])
        backward = screen.blit(controls_Backward, [10,300])
        right = screen.blit(controls_Right, [10,350])
        jump = screen.blit(controls_Jump, [10,400])

        if 670+135 > mouse[0] > 670 and 510+55 > mouse[1] > 510: #back button
            screen.blit(controls_Back2, [680,490])
            if click[0] == 1:
                controls = False
        else:
            screen.blit(controls_Back, [680,490])

        pygame.display.flip()
        clock.tick(60)


    drawMenu() # menu is drawn if controls = False

# Game over screen
def drawGameOver():
    gameOver = False
    while gameOver == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
                pygame.quit()
                quit()
##########################################################
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
##########################################################
        screen.fill(orange)
        screen.blit(background_Image_GameOver, [0,0])
        ###########################################
        screen.blit(gameover_Exit, [415,375])

        # Restart and Exit Buttons
        if 354+223 > mouse[0] > 354 and 280+78 > mouse[1] > 280: # Restart Button
            screen.blit(gameover_Restart2, [365,270])
            if click[0] == 1:
                gameOver = True
                drawLevel1()
        else:
            screen.blit(gameover_Restart, [365,270])

        if 353+223 > mouse[0] > 354 and 388+76 > mouse[1] > 388: # Exit Button
            screen.blit(gameover_Exit2, [415,375])
            if click[0] == 1:
                gameOver = True
                pygame.quit()
                quit()
        else:
            screen.blit(gameover_Exit, [415,375])

        ###########################################
        pygame.display.flip()
        clock.tick(60)

# Introduction screen- introduces player to character Tony and his story
def drawIntro():
    drwIntro = True
    while drwIntro == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                drwIntro = False
                pygame.quit()
                quit()
##########################################################
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
##########################################################
        screen.fill(white)
        screen.blit(background_Image_Intro, [0,0]) # background image

        pygame.draw.rect(screen, black, [670,30,200,60])

        if 671+196 > mouse[0] > 671 and 32+56 > mouse[1] > 32: # Start button hitbox
            screen.blit(gameintro_Start2, [705,45])
            if click[0] == 1:
                drwIntro = False
                pygame.mixer.music.fadeout(3000)
        else:
            screen.blit(gameintro_Start, [705,45])

        pygame.display.flip()
        clock.tick(60)

# Level 1
def drawLevel1():
    level1 = True
##    size  = (900,600)
##    screen = pygame.display.set_mode(size)
    x_Character_Tony_Coordinate = 415
    y_Character_Tony_Coordinate = 500
    x_Character_Tony_Speed = 0
    y_Character_Tony_Speed = 0

    x_Orange_Car_Coordinate = -200 # top lane
    x_Orange_Car_Speed = 20


    x_Green_Car_Coordinate = 400 # bottom lane
    x_Green_Car_Speed = -20

    x_Police_Car_Coordinate = 1050 #top lane
    x_Police_Car_Speed = -20

    x_Grey_Car_Coordinate = -500 #bottom lane
    x_Grey_Car_Speed = 20
# ----------------  Level 1 Loop ---------------- #
    while level1 == True:
        # ----- Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level1 = False
                pygame.quit()
                quit()

            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    y_Character_Tony_Speed = -5
##                elif event.key==pygame.K_a:
##                    x_Character_Tony_Speed = -5
                elif event.key==pygame.K_s:
                    y_Character_Tony_Speed = 5
##                elif event.key==pygame.K_d:
##                    x_Character_Tony_Speed = 5

            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_w or event.key==pygame.K_s:
                    y_Character_Tony_Speed = 0
                elif event.key==pygame.K_a or event.key==pygame.K_d:
                    x_Character_Tony_Speed = 0


        # ------ Level 1 Game Logic
##        mouse = pygame.mouse.get_pos()
##        print mouse[0]

##        print x_Orange_Car_Coordinate

##        print x_Grey_Car_Coordinate

        x_Character_Tony_Coordinate += x_Character_Tony_Speed
        y_Character_Tony_Coordinate += y_Character_Tony_Speed
#####################################################################
        if x_Character_Tony_Coordinate > 840: # right side boundry
            x_Character_Tony_Coordinate = 840

        if x_Character_Tony_Coordinate < 0: # left side boundry
            x_Character_Tony_Coordinate = 0

        if y_Character_Tony_Coordinate > 520: # bottom screen boundry
            y_Character_Tony_Coordinate = 520
#####################################################################
        x_Orange_Car_Coordinate += x_Orange_Car_Speed
        if x_Orange_Car_Coordinate >= 950:
            x_Orange_Car_Coordinate = -100

        x_Green_Car_Coordinate += x_Green_Car_Speed
        if x_Green_Car_Coordinate <= -1050:
            x_Green_Car_Coordinate = 1450

        x_Police_Car_Coordinate += x_Police_Car_Speed
        if x_Police_Car_Coordinate <= -300:
            x_Police_Car_Coordinate = 1000

        x_Grey_Car_Coordinate += x_Grey_Car_Speed
        if x_Grey_Car_Coordinate >= 1200:
            x_Grey_Car_Coordinate = -2000

        if y_Character_Tony_Coordinate < 430 + 50 and y_Character_Tony_Coordinate + 82 > 430: # grey car hitbox
            if x_Grey_Car_Coordinate+100 > x_Character_Tony_Coordinate and 430+50 > y_Character_Tony_Coordinate > x_Grey_Car_Coordinate:
                level1 = False
                drawGameOver()

        if y_Character_Tony_Coordinate < 220 + 50 and y_Character_Tony_Coordinate + 82 > 220: # orange car hitbox
            if x_Orange_Car_Coordinate < x_Character_Tony_Coordinate and x_Orange_Car_Coordinate+100 > x_Character_Tony_Coordinate:
                level1 = False
                drawGameOver()

        if y_Character_Tony_Coordinate < 330 + 50 and y_Character_Tony_Coordinate + 82 > 330: # green car hitbox
            if x_Green_Car_Coordinate+100 < x_Character_Tony_Coordinate and 330+50 > y_Character_Tony_Coordinate < 330:
                level1 = False
                drawGameOver()

        if y_Character_Tony_Coordinate < 120 + 50 and y_Character_Tony_Coordinate + 82 > 120: # police car hitbox
            if x_Police_Car_Coordinate+100 < x_Character_Tony_Coordinate and 120+50 > y_Character_Tony_Coordinate < x_Police_Car_Coordinate:
                level1 = False
                drawGameOver()

        if 390<x_Character_Tony_Coordinate<490 and 30<y_Character_Tony_Coordinate<50:
            level1 = False #load level 2

        screen.fill(white)
############################################################################
        # ------- Level 1 Drawing Code
        screen.blit(grassTexture, [0,0]) #grass
        screen.blit(grassTexture, [0,30])
        screen.blit(grassTexture, [0,510])
        streetCurve = pygame.draw.rect(screen, grey, [0,50,900,50])
        side_Of_Main_Building = pygame.draw.polygon(screen, dark_Turquoise, [[550,00],[550,100],[570,80],[570,-30]])
        building = screen.blit(main_Building, [340,-50])
        main_Building_Door = pygame.draw.rect(screen, light_Yellow, [440,50,50,50])
        street = pygame.draw.rect(screen, dark_Grey, [0,100,900,400])
        for y_offset in range(0,40,20):
            street_Lines = pygame.draw.line(screen, white, [0,y_offset+280], [900,y_offset+280], 10) # road devider (white)

        for y1 in range(0,150,70): # lower road crosswalk
            crossWalk = pygame.draw.line(screen, white, [350,470-y1], [550,470-y1], 25)

        for y2 in range(0,150,70): # upper road crosswalk
            crossWalk = pygame.draw.line(screen, white, [350,255-y2], [550,255-y2], 25)

        orangeCar = screen.blit(orange_Car, [x_Orange_Car_Coordinate,220]) # orange car
        greenCar = screen.blit(green_Car, [x_Green_Car_Coordinate,330]) # green car
        policeCar = screen.blit(police_Car, [x_Police_Car_Coordinate,120]) # police car
        greyCar = screen.blit(grey_Car, [x_Grey_Car_Coordinate,430]) # grey car

        streetCurve2 = pygame.draw.rect(screen, grey, [0,500,900,10])

        for x in range(0,250,80): # lane devider
            roadDevider1 = pygame.draw.line(screen, orange, [0+x,190], [50+x,190], 10)
            roadDevider2 = pygame.draw.line(screen, orange, [0+x,400], [50+x,400], 10)

        for x in range(630,900,80): # lane devider
            roadDevider3 = pygame.draw.line(screen, orange, [0+x,190], [50+x,190], 10)
            roadDevider4 = pygame.draw.line(screen, orange, [0+x,400], [50+x,400], 10)


        screen.blit(sidewalkTexture, [335,510])
        pygame.draw.line(screen, grey, [335,510], [335,620],15)
        pygame.draw.line(screen, grey, [565,510], [565,620],15)

        for x_offset in range(540,900,150):
                    tree = screen.blit(side_Tree, [x_offset+30,-60])

        screen.blit(fenceTexture,[0,465]) #fences
        screen.blit(fenceTexture,[150,465])
        screen.blit(fenceTexture,[600,465])
        screen.blit(fenceTexture,[750,465])

        screen.blit(fenceTexture,[0,55]) # fences
        screen.blit(fenceTexture,[150,55])
        screen.blit(fenceTexture,[600,55])
        screen.blit(fenceTexture,[750,55])

        screen.blit(lightpostTexture, [50,130]) # lightposts
        screen.blit(lightpostTexture, [640,130])

        bench = screen.blit(side_Bench, [700,520])

        Tony = screen.blit(character_Tony, [x_Character_Tony_Coordinate,y_Character_Tony_Coordinate]) # tony drawn

        for x_offset in range(-80,300,100):
            bushes = screen.blit(side_Bushes, [x_offset+5,540])

        pond = screen.blit(side_Pond, [50,-30])

        pole_Sign = pygame.draw.line(screen, grey, [295,10], [295,95], 4)
        back_Sign = pygame.draw.rect(screen, black, [282,0,20,30])
        crosswalk = screen.blit(crosswalk_Sign, [270,-10])

        pole_Sign = pygame.draw.line(screen, grey, [584,500], [584,585], 4)
        back_Sign = pygame.draw.rect(screen, black, [572,480,20,30])
        crosswalk = screen.blit(crosswalk_Sign, [560,470])
############################################################################

        pygame.display.flip()
        clock.tick(60)

def drawLevel2():
    level2 = True
    while level2 == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level2 = False
                pygame.quit()
                quit()

        screen.fill(grey)
        pygame.draw.rect(screen, black, [0,0,0,0])

        pygame.display.flip()
        clock.tick(60)



# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    # --- Game logic should go here
    # i.e calculations for positions, variable updates
    mouse = pygame.mouse.get_pos()

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(white)


    # --- Drawing code should go here
    drawMenu()
    drawIntro()
    drawLevel1()
    drawLevel2()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()