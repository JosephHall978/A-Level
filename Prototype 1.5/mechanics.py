import pygame#import pygame

#setup some basic colours for later use
white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
yellow = (255,255,0)

#draw text module
def draw_text_mid(surf, text, size, x, y, colour):#takes in surface, text to output, size of text, and x and y coordinates
    font_name = pygame.font.match_font("comic sans ms")#sets font to comic sans
    font = pygame.font.Font(font_name, size)#sets font and font size
    text_surface = font.render(text, True, colour)#renders text
    text_rect = text_surface.get_rect()#draws rect for text to be in
    text_rect.midtop = (x, y)#uses x and y coordinates to place the top middle of the box
    surf.blit(text_surface, text_rect)#displays it on the screen

def draw_text_left(surf, text, size, x, y, colour):#takes in surface, text to output, size of text, and x and y coordinates
    font_name = pygame.font.match_font("comic sans ms")#sets font to comic sans
    font = pygame.font.Font(font_name, size)#sets font and font size
    text_surface = font.render(text, True, colour)#renders text
    text_rect = text_surface.get_rect()#draws rect for text to be in
    text_rect = (x, y)#uses x and y coordinates to place the top middle of the box
    surf.blit(text_surface, text_rect)#displays it on the screen

def game_over(screen, score, height, width):#takes in screen, score, heigh of display, width of display
    if score <= 10:#if score taken in less than 10
        draw_text_mid(screen, "Better luck next time",30, (width//2), (10), yellow)#displays message top middle of the screen
    if score > 10 and score <= 25:#if score is between 10 and 25 then a different message is displayed with the score
        draw_text_mid(screen, "Doing alright", 30,(width//2), (10),yellow)
    if score > 25 and score <= 75:#if score is between 25 and 75 then a different message is displayed
        draw_text_mid(screen, "Impressive score", 30,(width//2), (10),yellow)
    if score > 75:#if score is greater than 75 different message is display
        draw_text_mid(screen, "Nice skills", 30,(width//2), (10),yellow)
    draw_text_mid(screen, ("Your score is: "+str(score)), 30,(width//2),(40),yellow)#display the player score

def menu(screen, height, width):#creates menu to display on the screen
    draw_text_mid(screen, "Lone Survivor", 50,(width//2), (20),yellow)
    draw_text_mid(screen, "Play", 25,(width-100), (height - 200),yellow)
    draw_text_mid(screen, "Score Board", 25,(width-100), (height - 160),yellow)
    draw_text_mid(screen, "Instructions", 25,(width-100), (height - 120),yellow)

def high_score(screen, gameStatus, width, height):#creates high score board
    s=[]#creates an array to hold scores
    f=open("high score.txt","r")#gets scores from high score file
    for j in f:
        s.append(j.strip("\n"))#strips [return] and adds score to array
    n = len(s)#finds length of array
    for j in range(n):
        for v in range(n-j-1):
            if int(s[v]) < int(s[v+1]):#if term is less then next term
                temp=s[v]#stores orignal score
                s[v]=s[v+1]#sets next term to current term
                s[v+1] = temp#sets next term as current term
    for v in range(10):#takes first 10 scores
        if gameStatus == "High Score":
            draw_text_mid(screen,"Top 10 Score",30,(width//2),20,yellow)
        temp = 80+v*30#sets temp to term number times 20 then adds 100
        draw_text_mid(screen, str(s[v]), 25,(width//2), (temp),yellow)#displays scores in order

def instructions(screen, width,height):
    draw_text_mid(screen, "INSTRUCTIONS", 25, width/2, 10,yellow)#displays Instructions top middle
    draw_text_left(screen, "Dodge all enemies", 20, width//20, 60,yellow)
    draw_text_left(screen, "Controls:", 20, width//20, 90,yellow)
    draw_text_left(screen, "Use arrow keys or 'W','A','S','D'", 20, width//10, 120,yellow)
    draw_text_left(screen, "Controllers not supported yet", 20, width//10, 150,yellow)
