import math
import random
import time
from tkinter import *

import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Road Travelers")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Background
bkgd = pygame.image.load('tlo3.png').convert()
bkgd_change = 0.08
x = 0

#gracz 1
playerImg = pygame.image.load('player1.png').convert_alpha()
playerImg = pygame.transform.scale(playerImg, (100,100))
playerX = 900
playerY = 600
playerX_change_left = 0
playerX_change_right = 0
playerX_change = playerX_change_left + playerX_change_right

#gracz 2
player2Img = pygame.image.load('player2.png').convert_alpha()
player2Img = pygame.transform.scale(player2Img, (100,100))
player2X = 300
player2Y = 600
player2X_change_left = 0
player2X_change_right = 0
player2X_change = player2X_change_left + player2X_change_right


#wróg 1
enemyImg = pygame.image.load('enemy.png').convert_alpha()
enemyImg = pygame.transform.scale(enemyImg, (100,100))
enemyX = random.randint(140, 1000)
enemyY = random.randint(-700, -500)
enemyY_change = 0.1


#wróg 2
enemyImg2 = pygame.image.load('enemy2.png').convert_alpha()
enemyImg2 = pygame.transform.scale(enemyImg2, (100,100))
enemyX1 = random.randint(140, 1000)
enemyY1 = random.randint(-1250, -600)
enemyY1_change = 0.1


#wróg 3
enemyImg3 = pygame.image.load('enemy3.png').convert_alpha()
enemyImg3 = pygame.transform.scale(enemyImg3, (100,100))
enemyX2 = random.randint(140, 1000)
enemyY2 = random.randint(-1250, -600)
enemyY2_change = 0.1

#wróg 4
enemyX3 = random.randint(140, 1000)
enemyY3 = random.randint(-1250, -600)
enemyY3_change = 0.1


#wróg 5
enemyX4 = random.randint(140, 1000)
enemyY4 = random.randint(-1250, -600)
enemyY4_change = 0.1

#wróg 6
enemyX5 = random.randint(140, 1000)
enemyY5 = random.randint(-1250, -600)
enemyY5_change = 0.1

#karetka
ambulanceImg = pygame.image.load('ambulance.png').convert_alpha()
ambulanceImg = pygame.transform.scale(ambulanceImg, (100,100))
ambulanceX = random.randint(140, 1000)
ambulanceY = -7000
ambulanceY_change = 0.4

#policja
policeImg = pygame.image.load('police.png').convert_alpha()
policeImg = pygame.transform.scale(policeImg, (100,100))
policeX = random.randint(140, 1020)
policeY = -10000
policeY_change = 0.6

#punkty
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

def player(x, y):
    screen.blit(playerImg, (x, y))

def player2(x, y):
    screen.blit(player2Img, (x, y))

def show_score(x, y):
    score = font.render("Punkty:" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def enemy1(x, y):
    screen.blit(enemyImg, (x, y))

def enemy2(x, y):
    screen.blit(enemyImg2, (x, y))

def enemy3(x, y):
    screen.blit(enemyImg2, (x, y))

def enemy4(x, y):
    screen.blit(enemyImg3, (x, y))

def enemy5(x, y):
    screen.blit(enemyImg3, (x, y))

def ambulance(x, y):
    screen.blit(ambulanceImg, (x, y))

def police(x, y):
    screen.blit(policeImg, (x, y))

class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = 530
        self.y = 300
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

def lose():
    greenButton.draw(screen, (0,0,0))
    show_score(590, 450)


    
greenButton = button((0,255,0), 150, 225, 250, 100, 'Przegrana :(')

running = True
while running:

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
        #Gracz1 sterowanie
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change_left = -0.4
            if event.key == pygame.K_RIGHT:
                playerX_change_right = 0.4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerX_change_left = 0
            if event.key == pygame.K_RIGHT:
                playerX_change_right = 0

        #Gracz2 sterowanie
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player2X_change_left = -0.4
            if event.key == pygame.K_d:
                player2X_change_right = 0.4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player2X_change_left = 0
            if event.key == pygame.K_d:
                player2X_change_right = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            if greenButton.isOver(pos):
                print('clicked the button')
                pygame.quit()
                quit()

        if event.type == pygame.MOUSEMOTION:
            if greenButton.isOver(pos):
                greenButton.color = (0,255,0)
            else:
                greenButton.color = (255,0,0)
                

                


    rel_x = x % bkgd.get_rect().width
    screen.blit(bkgd, (0, rel_x - bkgd.get_rect().width))
    if rel_x < 0:
        screen.blit(bkgd, (0, rel_x))
        bkgd_change + 0.01
    x += bkgd_change


    #zasady gracz1
    playerX_change = playerX_change_right + playerX_change_left
    playerX += playerX_change
    if playerX <= 140:
        playerX = 140
    elif playerX >= 1020:
        playerX = 1020
    player(playerX, playerY)

    #zasady gracz2
    player2X_change = player2X_change_right + player2X_change_left
    player2X += player2X_change
    if player2X <= 140:
        playerX = 140
    elif player2X >= 1020:
        player2X = 1020
    player2(player2X, player2Y)

    

    enemyY += enemyY_change
    enemyY1 += enemyY1_change
    enemyY2 += enemyY2_change
    enemyY3 += enemyY3_change
    enemyY4 += enemyY4_change
    enemyY5 += enemyY5_change
    ambulanceY += ambulanceY_change
    policeY += policeY_change
    enemy(enemyX, enemyY)
    enemy1(enemyX1, enemyY1)
    enemy2(enemyX2, enemyY2)
    enemy3(enemyX3, enemyY3)
    enemy4(enemyX4, enemyY4)
    enemy5(enemyX5, enemyY5)
    ambulance(ambulanceX, ambulanceY)
    police(policeX, policeY)
    show_score(textX, textY)


    #kolizja gracz 1
    if enemyY >= 500 and enemyY <= 710:
        if math.sqrt((math.pow(enemyX-playerX,2)) + (math.pow(enemyY-playerY,2))) < 40:
            playerY= -100

    if enemyY1 >= 500 and enemyY1 <= 710:
        if math.sqrt((math.pow(enemyX1-playerX,2)) + (math.pow(enemyY1-playerY,2))) < 40:
            playerY= -100

    if enemyY2 >= 500 and enemyY2 <= 710:
        if math.sqrt((math.pow(enemyX2-playerX,2)) + (math.pow(enemyY2-playerY,2))) < 40:
            playerY= -100
            
    if enemyY3 >= 500 and enemyY3 <= 710:
        if math.sqrt((math.pow(enemyX3-playerX,2)) + (math.pow(enemyY3-playerY,2))) < 40:
            playerY= -100

    if enemyY4 >= 500 and enemyY4 <= 710:
        if math.sqrt((math.pow(enemyX4-playerX,2)) + (math.pow(enemyY4-playerY,2))) < 40:
            playerY= -100

    if enemyY5 >= 500 and enemyY5 <= 710:
        if math.sqrt((math.pow(enemyX5-playerX,2)) + (math.pow(enemyY5-playerY,2))) < 40:
            playerY= -100

    if ambulanceY >= 500 and ambulanceY <= 710:
        if math.sqrt((math.pow(ambulanceX-playerX,2)) + (math.pow(ambulanceY-playerY,2))) < 40:
            playerY= -100

    if policeY >= 500 and policeY <=710:
        if math.sqrt((math.pow(policeX-playerX,2)) + (math.pow(policeY-playerY,2))) < 40:
            playerY= -100

    if playerY < 100:
        if player2Y < 100:
            lose()
    if player2Y < 100:
        if playerY < 100:
            lose()

    #kolizja gracz 2
    if enemyY >= 500 and enemyY <= 710:
        if math.sqrt((math.pow(enemyX-player2X,2)) + (math.pow(enemyY-player2Y,2))) < 40:
            player2Y= -100

    if enemyY1 >= 500 and enemyY1 <= 710:
        if math.sqrt((math.pow(enemyX1-player2X,2)) + (math.pow(enemyY1-player2Y,2))) < 40:
            player2Y= -100

    if enemyY2 >= 500 and enemyY2 <= 710:
        if math.sqrt((math.pow(enemyX2-player2X,2)) + (math.pow(enemyY2-player2Y,2))) < 40:
            player2Y= -100
            
    if enemyY3 >= 500 and enemyY3 <= 710:
        if math.sqrt((math.pow(enemyX3-player2X,2)) + (math.pow(enemyY3-player2Y,2))) < 40:
            player2Y= -100

    if enemyY4 >= 500 and enemyY4 <= 710:
        if math.sqrt((math.pow(enemyX4-player2X,2)) + (math.pow(enemyY4-player2Y,2))) < 40:
            player2Y= -100

    if enemyY5 >= 500 and enemyY5 <= 710:
        if math.sqrt((math.pow(enemyX5-player2X,2)) + (math.pow(enemyY5-player2Y,2))) < 40:
            player2Y= -100

    if ambulanceY >= 500 and ambulanceY <=710:
        if math.sqrt((math.pow(ambulanceX-player2X,2)) + (math.pow(ambulanceY-player2Y,2))) < 40:
            player2Y= -100

    if policeY >= 500 and policeY <=710:
        if math.sqrt((math.pow(policeX-player2X,2)) + (math.pow(policeX-player2Y,2))) < 40:
            player2Y= -100



#
#Ambulans zasady
#
    if ambulanceY >=0 and ambulanceY <=710:
        if abs(ambulanceX - enemyX) <=20:
            enemyY= -100
    if ambulanceY >=0 and ambulanceY <=710:
        if abs(ambulanceX - enemyX1) <=20:
            enemyY1= -100
    if ambulanceY >=0 and ambulanceY <=710:
        if abs(ambulanceX - enemyX2) <=20:
            enemyY2= -100
    if ambulanceY >=0 and ambulanceY <=710:
        if abs(ambulanceX - enemyX3) <=20:
            enemyY3= -100
    if ambulanceY >=0 and ambulanceY <=710:
        if abs(ambulanceX - enemyX4) <=20:
            enemyY4= -100
    if ambulanceY >=0 and ambulanceY <=710:
        if abs(ambulanceX - enemyX5) <=20:
            enemyY5= -100

#
#policja zasady
#
    if policeY >=0 and policeY <=710:
        if abs(policeX - enemyX) <=20:
            enemyY = -100
        if abs(policeX - enemyX1) <=20:
            enemyY1 = -100
        if abs(policeX - enemyX2) <=20:
            enemyY2 = -100
        if abs(policeX - enemyX3) <=20:
            enemyY3 = -100
        if abs(policeX - enemyX4) <=20:
            enemyY4 = -100
        if abs(policeX - enemyX5) <=20:
            enemyY4 = -100

#
#punkty
#


            
    
    if enemyY >= 800:
        enemyX = random.randint(140, 1020)
        enemyY = random.randint(-1250, -600)
        enemyY_change = enemyY_change + 0.01
        if playerY == 600 or player2Y == 600:
            score_value += 1

        
    if enemyY1 >= 800:
        enemyX1 = random.randint(140, 1020)
        enemyY1 = random.randint(-1250, -600)
        enemyY1_change = enemyY_change + 0.01
        if playerY == 600 or player2Y == 600:
            score_value += 1

        
    if enemyY2 >= 800:
        enemyX2 = random.randint(140, 1020)
        enemyY2 = random.randint(-1250, -600)
        enemyY2_change = enemyY_change + 0.01
        if playerY == 600 or player2Y == 600:
            score_value += 1


    if enemyY3 >= 800:
        enemyX3 = random.randint(140, 1020)
        enemyY3 = random.randint(-1250, -600)
        enemyY3_change = enemyY_change + 0.01
        if playerY == 600 or player2Y == 600:
            score_value += 1
        
    if enemyY4 >= 800:
        enemyX4 = random.randint(140, 1020)
        enemyY4 = random.randint(-1250, -600)
        enemyY4_change = enemyY_change + 0.01
        if playerY == 600 or player2Y == 600:
            score_value += 1
        
    if enemyY5 >= 800:
        enemyX5 = random.randint(140, 1020)
        enemyY5 = random.randint(-1250, -600)
        enemyY5_change = enemyY_change + 0.01
        if playerY == 600 or player2Y == 600:
            score_value += 1

    if ambulanceY >= 800:
        ambulanceX = random.randint(140, 1020)
        ambulanceY = -20000
        ambulanceY_change = ambulanceY_change + 0.01
        if playerY == 600 or player2Y == 600:
            score_value += 1

    if policeY >= 800:
        policeX = random.randint(140, 1020)
        policeY = -30000
        policey_change = policeY_change + 0.01
        if playerY == 600 or player2Y == 600:
            score_value += 1


    pygame.display.update()
    
    
