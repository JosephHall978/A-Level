import sys
import pygame
import pathlib
from sprites import * #imports all classes from sprites module
from mechanics import * #imports all functions from mechanics

f = open("high score.txt","a")
width = 550#sets width
height = 500#sets height
fps = 30#sets starting fps to 30
score = 0
gameStatus = "Menu"#sets Game Status "Play"
option = 0

pygame.init()
pygame.mixer.init()#initialise sound mixer
screen = pygame.display.set_mode((width,height))#creates game window
pygame.display.set_caption("Lone Survivor")#game window caption
player_img = pygame.image.load(str(pathlib.Path.cwd().joinpath('img','player-60x60.png'))).convert_alpha()#gets base player image
dart_img = pygame.image.load(str(pathlib.Path.cwd().joinpath('img','dart-30x30.png'))).convert_alpha()#gets base dart image
asteroid_img = pygame.image.load(str(pathlib.Path.cwd().joinpath('img','asteroid-50x42.png'))).convert_alpha()#gets base asteroid image
bomber_img = pygame.image.load(str(pathlib.Path.cwd().joinpath('img','bomber.png'))).convert_alpha()
background = pygame.image.load(str(pathlib.Path.cwd().joinpath('img','background-1000x1000.png'))).convert_alpha()#gets background image
background_rect = background.get_rect()#gets area of background image
menu_background = pygame.image.load(str(pathlib.Path.cwd().joinpath('img','menu-550x500.png'))).convert_alpha()
menu_background_rect = menu_background.get_rect()
clock = pygame.time.Clock()#starts pygame clock

all_sprites = pygame.sprite.Group()#sets all_sprites as a pygame sprite group
mobs = pygame.sprite.Group()#sets mobs as a pygame spirte group
player = Player(player_img)#creates player from class Player
all_sprites.add(player)#adds player to sprite group all_sprites

def new_dart(dart_img):#function for creating dart sprite
    d = Dart(dart_img)#creates dart from class Dart
    all_sprites.add(d)#adds sprite to all_sprites group
    mobs.add(d)#adds sprite to mobs group
def new_asteroid(asteroid_img):#function for creating asteroid sprite
    a = Asteroid(asteroid_img)#insantatiate asteroid
    all_sprites.add(a)#adds asteroid to all_sprites group
    mobs.add(a)#adds asteroid to mobs group
def new_bomber(bomber_img,fps):#function for creating bomber
    b = Bomber(bomber_img,fps)#instatiates bomber after basing image and frame rate
    all_sprites.add(b)#adds bomber sprite to all_sprites group
    mobs.add(b)#adds bomber sprite to mobs group
def new_enemy():#class for creating random enemy
    select = random.randrange(0,3)#random selection value
    if select == 0:
        new_dart(dart_img)#uses new_dart function
    if select == 1:
        new_asteroid(asteroid_img)#uses new_asteroid function
    if select == 2:
        new_bomber(bomber_img,fps)#uses new_bomber function
    
for i in range (6):#loop to create starting sprites
    new_enemy()
run = True#sets game loop to true
surface = pygame.Surface((550,500))#bgr

while run:#starts gameplay loop
    keystate = pygame.key.get_pressed()
    game_events = pygame.event.get()
    clock.tick(int(fps))#checks clock speed
    screen.blit(menu_background, menu_background_rect)
    #screen.fill(blue)#fills background with blue
    if keystate[pygame.K_ESCAPE]:
        if gameStatus == "Game Over":
            player.lives = 3
            score = 0
            fps = 30
        gameStatus = "Menu"

    for event in game_events:#checks pygame events
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    if gameStatus == "Menu":
        mouse = pygame.mouse.get_pos()#store mouse position in mouse 
        menu(screen, height, width)#menu module takes in parameters screen, height and width
        menu_selector(screen,option,height,width)
        keystate = pygame.key.get_pressed()
        if (keystate[pygame.K_RETURN]):
            if option == 0:
                gameStatus = "Play"
            if option == 1:
                gameStatus = "High Score"
            if option == 2:
                gameStatus = "Instructions"
        for event in game_events:
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP or event.key == ord('w')) and (option > 0):
                    option -= 1
                if (event.key == pygame.K_DOWN or event.key == ord('s')) and (option < 2):
                    option += 1                
            if event.type == pygame.MOUSEBUTTONUP:
                if  (mouse[0] > (width//2 - 40))  and (mouse[1] < (height - 175) and mouse[1] > (height - 205)):#button range
                    gameStatus = "Play"#changes gameStatus to "Play"
                elif  (mouse[0] > (width//2 - 115))  and (mouse[1] < (height - 120) and mouse[1] > (height - 150)):#button range
                    gameStatus = "High Score"#changes gameStatus to "High Score"
                elif  (mouse[0] > (width//2 - 110))  and (mouse[1] < (height - 75) and mouse[1] > (height - 105)):#button range
                    gameStatus = "Instructions"#changes gameStatus to "Instructions"
                elif (mouse[0]> 10) and (mouse[0] < (310)) and (mouse[1]> 10) and (mouse[1]<35):
                    gameStatus = "Menu"

    if gameStatus == "Instructions":
        instructions(screen,width,height)
        mouse = pygame.mouse.get_pos()#store mouse position in mouse
        for event in game_events:
            if event.type == pygame.MOUSEBUTTONUP:
                if (mouse[0]> 10) and (mouse[0] < (135)) and (mouse[1]> 10) and (mouse[1]<35):
                    gameStatus = "Menu"
    if gameStatus == "High Score":
        mouse = pygame.mouse.get_pos()#store mouse position in mouse
        for event in game_events:
            if event.type == pygame.MOUSEBUTTONUP:
                if (mouse[0]> 10) and (mouse[0] < (135)) and (mouse[1]> 10) and (mouse[1]<35):
                    gameStatus = "Menu"
        high_score(screen,gameStatus,width,height)

    if gameStatus == "Play":#if game status is "Play" the game plays through
        while len(mobs) < 6:#checks there is 6 mobs alive
            new_enemy()
            score += 0.5#increases score by 0.5

        all_sprites.update()#updates all sprite displayed
        fps += 0.01#increases fps 0.01 per frame

        hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)# detects if player collides with a mob
        for hit in hits:
          new_enemy()
          hit.kill()#kills dart that collide with the player
          player.lives -= 1#reduces player lives by 1
        screen.blit(background, background_rect)
        hearts(screen,player.lives,height,width)
        all_sprites.draw(screen)#draws all sprite

        draw_text_mid(screen, str(int(score)), 20, width // 2, 10,white)#displays score top middle

        if player.lives < 0:
            gameStatus = "Game Over"#sets gameStatus to "Game Over"
            f = open("high score.txt","a")
            f.writelines((str(int(score)),"\n"))
            f.close()
    if gameStatus == "Game Over":#when gameStatus equals "Game Over" the play stage stop running
        all_sprites.clear(screen,surface)
        screen.blit(menu_background, menu_background_rect)
        game_over(screen, int(score), height, width)#displays message appropriate to player performance and score
        high_score(screen, gameStatus, width, height)#takes in the display, width of display, height of the display
        mouse = pygame.mouse.get_pos()#store mouse position in mouse
        for event in game_events:
            if event.type == pygame.MOUSEBUTTONUP:
                if ((mouse[0]> 10) and (mouse[0] < (135))) and ((mouse[1]> 10) and (mouse[1]<35)):
                    player.lives = 3
                    fps = 30
                    score = 0
                    gameStatus = "Menu"
    pygame.display.flip()
#JSH
