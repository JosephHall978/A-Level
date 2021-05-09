import sys
import pygame
from sprites import * #imports all classes from sprites module
from mechanics import * #imports all functions from mechanics

f = open("high score.txt","a")
width = 550#sets width
height = 500#sets height
fps = 30#sets starting fps to 30
score = 0
gameStatus = "Menu"#sets Game Status "Play"

pygame.init()
pygame.mixer.init()#initialise sound mixer
screen = pygame.display.set_mode((width,height))#creates game window
pygame.display.set_caption("Lone Survivor")#game window caption
player_img = pygame.image.load("player-60x60.png").convert_alpha()#gets base player image
dart_img = pygame.image.load("dart-30x30.png").convert_alpha()#gets base dart image
background = pygame.image.load("background-1000x1000.png").convert_alpha()#gets background image
background_rect = background.get_rect()#gets area of background image
clock = pygame.time.Clock()#starts pygame clock

all_sprites = pygame.sprite.Group()#sets all_sprites as a pygame sprite group
mobs = pygame.sprite.Group()#sets mobs as a pygame spirte group
player = Player(player_img)#creates player from class Player
all_sprites.add(player)#adds player to sprite group all_sprites

def new_dart(dart_img):#function for creating dart sprite
    d = Dart(dart_img)#creates dart from class Dart
    all_sprites.add(d)#adds sprite to all_sprites group
    mobs.add(d)#adds sprite to mobs group

for i in range (8):#loop to create starting sprites
    new_dart(dart_img)#calls newDart function

run = True#sets game loop to true
surface = pygame.Surface((500,500))#bgr

while run:#starts gameplay loop
    keystate = pygame.key.get_pressed()
    game_events = pygame.event.get()
    clock.tick(int(fps))#checks clock speed
    screen.fill(blue)#fills background with blue
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
        for event in game_events:
            if event.type == pygame.MOUSEBUTTONUP:
                if  (mouse[0] > (width - 125))  and (mouse[1] > (height - 200) and mouse[1] < (height - 175)):#button range
                    gameStatus = "Play"#changes gameStatus to "Play"
                elif  (mouse[0] > (width - 170))  and (mouse[1] > (height - 160) and mouse[1] < (height - 135)):#button range
                    gameStatus = "High Score"#changes gameStatus to "High Score"
                elif  (mouse[0] > (width - 165))  and (mouse[1] > (height - 120) and mouse[1] < (height - 95)):#button range
                    gameStatus = "Instructions"#changes gameStatus to "Instructions"

    if gameStatus == "Instructions":
        instructions(screen,width,height)

    if gameStatus == "High Score":
        high_score(screen,gameStatus,width,height)

    if gameStatus == "Play":#if game status is "Play" the game plays through
        while len(mobs) < 6:#checks there is 6 mobs alive
            new_dart(dart_img)#spawns new dart if there isn't 6 mobs
            score += 0.5#increases score by 0.5

        all_sprites.update()#updates all sprite displayed
        fps += 0.01#increases fps 0.01 per frame

        hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)# detects if player collides with a mob
        for hit in hits:
          new_dart(dart_img)#spawns new dart by calling function
          hit.kill()#kills dart that collide with the player
          player.lives -= 1#reduces player lives by 1
        screen.blit(background, background_rect)
        all_sprites.draw(screen)#draws all sprite

        draw_text_mid(screen, str(int(score)), 18, width // 2, 10,white)#displays score top middle
        draw_text_mid(screen, str(player.lives), 18, 10, 10,white)#displays lives top left

        if player.lives < 0:
            gameStatus = "Game Over"#sets gameStatus to "Game Over"
            f = open("high score.txt","a")
            f.writelines((str(int(score)),"\n"))
            f.close()
    if gameStatus == "Game Over":#when gameStatus equals "Game Over" the play stage stop running
        all_sprites.clear(screen,surface)
        screen.fill(blue)
        game_over(screen, int(score), height, width)#displays message appropriate to player performance and score
        high_score(screen, gameStatus, width, height)#takes in the display, width of display, height of the display
    pygame.display.flip()
#JSH
