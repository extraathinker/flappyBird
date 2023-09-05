import pygame
import random
from pygame import mixer
import math

pygame.init()
mixer.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption('Flappy Bird Game')
icon = pygame.image.load('001-play.png')
pygame.display.set_icon(icon)

background = pygame.image.load('3.jpg')

bird = pygame.image.load('001-play.png')
birdX = 100
birdY = 300
birdChangeY = 0

pillar11 = []
pillar22 = []
pillar1X = []
pillar1Y = []
pillar2X = []
pillar2Y = []
pillarChangeX = []
newPillar = 0
for i in range(99):
    pillar11.append(pygame.image.load('ppp.png'))
    pillar22.append(pygame.image.load('ppp.png'))
    pillar1X.append(750 + newPillar)
    pillar1Y.append(-(random.randint(150, 550)))
    pillar2X.append(750 + newPillar)
    pillar2Y.append(pillar1Y[i] + 750)
    pillarChangeX.append(-0.08)
    newPillar += 400

def player(x, y):
    screen.blit(bird, (x, y))

def pillar1(x, y,i):
    screen.blit(pillar11[i], (x, y))
    
def pillar2(x, y,i):
    screen.blit(pillar22[i], (x, y))

def collision(playerX,playerY, pillarX, pillarY):
    if playerX in [pillarX,pillarX + 85] and [pillarY, pillarY + 567]:
        return True
    else:
        return False
pillardict = {}
running = True
while running:

    screen.fill((0, 0, 0))

    screen.blit(background, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                going = mixer.Sound('laser.mp3')
                going.play()
                birdChangeY = -0.3
            if event.key == pygame.K_DOWN:
                birdChangeY = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                birdChangeY = 0.1
    
    for j in range(99):
        pillar1X[j] += pillarChangeX[j]
        pillar2X[j] += pillarChangeX[j]
        
        pillar1(pillar1X[j], pillar1Y[j], j)
        pillar2(pillar2X[j], pillar2Y[j], j)
  
    birdY += birdChangeY
    player(birdX, birdY)
    pygame.display.update()