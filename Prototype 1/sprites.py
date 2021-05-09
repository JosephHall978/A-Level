#imports and starting variables
import pygame#pygame
import sys #to close window when game stops
from os import path #to use file directory paths to get images
import math#calculate how much to rotate a sprite
import random #random number module
img_dir = path.join(path.dirname(__file__), 'img')#open img directory
black = (0,0,0)
width = 400
height = 400
#sprites
#player
class Player(pygame.sprite.Sprite):#creates player class
    def __init__(self, player_img):#set parameters to be passed in the player and it's image
        pygame.sprite.Sprite.__init__(self)#intiliase pygame sprites
        self.image = player_img
        self.image.set_colorkey(black)#set area behind sprite to black
        self.rect = self.image.get_rect()#get rect for image
        self.radius = 12#set a collison radius of 12 pixels from the centre
        self.rect.center = (width/2, height/2)#centre sprite
        self.speedx = 0#set starting x speed to zero
        self.speedy = 0#set starting y speed to zero
        self.lives = 3#set number of player lives
    def update(self):
        self.speedx = 0#reset x speed
        self.speedy = 0#reset y speed
        keystate = pygame.key.get_pressed() #get any keys pressed during frame
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a] :#if [A] or the left arrow key is down x speed is set -8
            self.speedx = -8
        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d] :#if [D] or the right arrow key is down x speed is set 8
            self.speedx = 8
        if keystate[pygame.K_UP] or keystate[pygame.K_w]:#if [W] or the up arrow key is down y speed is set -8
            self.speedy = -8
        if keystate[pygame.K_DOWN] or keystate[pygame.K_s]:#if [S] or the left arrow key is down y speed is set 8
            self.speedy = 8
        self.rect.x += self.speedx*1.41#increase x coordinate by the x speed
        self.rect.y += self.speed*1.41#increasee y coordinate by the y speed
        if self.rect.right > width:#stops player leaving the right side
            self.rect.right = width
        if self.rect.left < 0:#stops player leaving left side of the screen
            self.rect.left = 0
#dart
class Dart(pygame.sprite.Sprite):#create dart calss
    def __init__(self, dart_img):#set parameter that need to be passed in dart image and which dart
        pygame.sprite.Sprite.__init__(self)#intialise pygame sprite
        self.image = dart_img#scale dart image that is passed in to 30x30 pixels
        self.image.set_colorkey(black)#set the area behind image to black
        self.rect = self.image.get_rect()#define image rectangle for collision
        self.radius = 15
        self.spawn_zone = random.randrange(1,5)#set spawn zone for dart
        if self.spawn_zone == 1:#spawn zone 1 is along the top of the screen
            self.rect.center = ((random.randrange(0,width-20)), -20)#varies where dart spawns along the width
            self.speedx = random.randrange(0,10)#varies x speed
            self.speedy = random.randrange(0,10)#varies y speed
        if self.spawn_zone == 2:#spawn zone 2 is along the left side of the screen
            self.rect.center = (-20,(random.randrange(0, height-20)))#varies where the dart spawns along the height
            self.speedx = random.randrange(1,10)
            self.speedy = random.randrange(1,10)
        if self.spawn_zone == 3:#spawn zone 3 is along the bottom of the screen
            self.rect.center = (height + 20,(random.randrange(0, height-20)))
            self.speedx = random.randrange(-10,-1)
            self.speedy = random.randrange(-10,-1)
        if self.spawn_zone == 4:#spawn zone 4 is along the right of the screen
            self.rect.center = ((random.randrange(0,width-20)),width+20)
            self.speedx = random.randrange(-10,-1)
            self.speedy = random.randrange(-10,-1)
        if self.speedx == 0: #corrects zero speed along x-axis to prevent zero error
            self.speedx = 1
        if self.speedy == 0:#corrects zero speed along y-axis to prevent zero error
            self.speedy = 1
        #rotate so that tip is going in direction of travel
        orig_center = self.rect.center
        if(self.spawn_zone == 1) or (self.spawn_zone == 2): #rotates spawn zone 1 and 2 sprites so they point in the correct direction
            self.rot = math.degrees(math.atan(self.speedx/self.speedy))+180#calculates the bearing the dart is going
            self.image = pygame.transform.rotate(self.image, self.rot)#rotates dart image to match the bearing
            self.rect = self.image.get_rect()#corrects image rect
            self.rect.center =orig_center#corrects the image centre
        if (self.spawn_zone == 3) or (self.spawn_zone == 4):#rotates spawn zone 3 and 4 sprites so they point in the correct direction 
            self.rot = math.degrees(math.atan(self.speedx/self.speedy))#calculates bearing the dart is going
            self.image = pygame.transform.rotate(self.image, self.rot)#rotates dart image to match the bearing
            self.rect = self.image.get_rect()#corrects image rect
            self.rect.center =orig_center#corrects the image centre
    def update(self):#updates sprite postion of the display window
        self.rect.x += self.speedx #increase x coordinate by sprites speed
        self.rect.y += self.speedy#increases y coordinate by sprites speed
        if self.spawn_zone == 1 or self.spawn_zone == 2:#check for defective sprites that originate from spawn zone 1 and 2
            if (self.speedx < 5) and (self.speedy < 5):#if both speeds are below 5 units per frame then the sprite is destoried
                self.kill()#kills sprite
            if self.rect.x > width+20:#checks sprite is within screen width
                self.kill()
            if self.rect.y > height+20:#check sprite is within screen height
                self.kill()
        if (self.spawn_zone == 3) or (self.spawn_zone == 4):#checks for defective sprites that originate from zone 3 and 4
            if (self.speedx > -5) and (self.speedy > -5):#if both speeds are below 5 units per frame then the sprite is destoried
                self.kill()#kills sprite
            if self.rect.x < -20:#check sprite is within screen width
                self.kill()
            if self.rect.y < -20:#check sprite is within screen height
                self.kill()
#asteriod
#explosive debris
#JSH
