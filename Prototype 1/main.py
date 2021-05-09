from sprites import * #imports all classes from sprites module
from mechanics import * #imports all functions from mechanics

f = open("high score.txt","a")
width = 400#sets width 400
height = 400#sets height 400
fps = 30#sets starting fps to 30
score = 0
black = (0,0,0)#sets black colour value
white= (255,255,255)#sets white colour value
red = (255,0,0)#sets red colour value
green = (0,255,0)#sets green colour value
blue = (0,0,255)#sets blue colour value
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
surface = pygame.Surface((400,400))#bgr
while run:#starts gameplay loop
    game_events = pygame.event.get()
    clock.tick(int(fps))#checks clock speed
    for event in game_events:#checks pygame events
            if event.type == pygame.QUIT:
                if gameStatus != "High Score":
                    pygame.quit()#quits pygame
                    sys.exit()
                    break
    if gameStatus == "Menu":
        mouse = pygame.mouse.get_pos() 
        menu(screen, height, width)
        for event in game_events:
            if event.type == pygame.MOUSEBUTTONUP:
                if  (mouse[0] > (width - 125))  and (mouse[1] > (height - 180) and mouse[1] < (height - 155)):
                    gameStatus = "Play"
                elif  (mouse[0] > (width - 170))  and (mouse[1] > (height - 155) and mouse[1] < (height - 90)):
                    gameStatus = "High Score"
    if gameStatus == "High Score":
        screen.fill(blue)
        high_score(screen,gameStatus,width,height)
        for event in game_events:#checks pygame events
            if event.type == pygame.QUIT:
                screen.fill(black)
                gameStatus = "Menu"
    if gameStatus == "Play":#if game status is "Play" the game plays through
        while len(mobs) < 6:#checks there is 6 mobs alive
            new_dart(dart_img)#spawns new dart if there isn't 6 mobs

        all_sprites.update()#updates all sprite displayed
        score = int(fps-30) #defines score value relative to frame rate
        fps += 0.01#increases fps 0.01 per frame

        hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)# detects if player collides with a mob
        for hit in hits:
          new_dart(dart_img)#spawns new dart by calling function
          hit.kill()#kills dart that collide with the player
          player.lives -= 1#reduces player lives by 1
        screen.fill(black)#fills in background as black
        screen.blit(background, background_rect)
        all_sprites.draw(screen)#draws all sprite

        draw_text(screen, str(int(score)), 18, width // 2, 10)#displays score top middle
        draw_text(screen, str(player.lives), 18, 10, 10)#displays lives top left

        if player.lives < 0:
            gameStatus = "Game Over"#sets gameStatus to "Game Over"
            f = open("high score.txt","a")
            f.writelines((str(int(score)),"\n"))
            f.close()
    if gameStatus == "Game Over":#when gameStatus equals "Game Over" the play stage stop running
        all_sprites.clear(screen, surface)#clears all sprites
        screen.fill(blue)#fills background with blue
        game_over(screen, int(score), height, width)#displays message appropriate to player performance and score
        high_score(screen, gameStatus, width, height)#takes in the display, width of display, height of the display
    pygame.display.flip()
#JSH