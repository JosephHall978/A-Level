import pygame#import pygame
#setup some basic colours for later use
white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
#draw text module
def draw_text(surf, text, size, x, y):#takes in surface, text to output, size of text, and x and y coordinates
    font_name = pygame.font.match_font("comic sans ms")#sets font to comic sans
    font = pygame.font.Font(font_name, size)#sets font and font size
    text_surface = font.render(text, True, white)#renders text
    text_rect = text_surface.get_rect()#draws rect for text to be in
    text_rect.midtop = (x, y)#uses x and y coordinates to place the top middle of the box
    surf.blit(text_surface, text_rect)#displays it on the screen
def game_over(screen, score, height, width):#takes in screen, score, heigh of display, width of display
    if score < 10:#if score taken in less than 10
        draw_text(screen, "Better luck next time",18, (width//2), (20))#displays message top middle of the screen
    if score > 10 and score < 25:#if score is between 10 and 25 then a different message is displayed with the score
        draw_text(screen, "Doing alright", 18,(width//2), (20))
    if score > 25 and score < 75:#if score is between 25 and 75 then a different message is displayed
        draw_text(screen, "Impressive score", 18,(width//2), (20))
    if score > 75:#if score is greater than 75 different message is display
        draw_text(screen, "Nice skills", 18,(width//2), (20))
    draw_text(screen, ("Your score is: "+str(score)), 18,(width//2),(40))#display the player score
def menu(screen, height, width):#creates menu to display on the screen
    draw_text(screen, "Lone Survivor", 50,(width//2), (20))
    draw_text(screen, "Play", 25,(width-100), (height - 180))
    draw_text(screen, "Score Board", 25,(width-100), (height - 120))
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
            draw_text(screen,"Top 10 Score",18,(width//2),20)
        temp = 70+v*20#sets temp to term number times 20 then adds 100
        draw_text(screen, str(s[v]), 18,(width//2), (temp))#displays scores in order