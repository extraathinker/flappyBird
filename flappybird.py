import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800,500))
pygame.display.set_caption('Flappy Bird')

image = pygame.image.load('001-play.png')
imgX = 50
imgY = 250
imgChange = 0


pilXchange = 0.3
pill1 = {}
pill2 = {}
dis = 0
x1 = 750
pillNumber = 999
for i in range(pillNumber):
    y2 = random.randint(0,340)
    pill1[i] = [x1 + dis,0,50,y2]
    pill2[i] = [x1 + dis,y2+160,50,500-y2-160]
    dis += 300



running = True
while running:

    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                imgChange = -0.5
            if event.key == pygame.K_DOWN:
                imgChange = 0.5
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                imgChange = 0.2
            if event.key == pygame.K_DOWN:
                imgChange = 0.2
        
    for j in range(pillNumber):
        box1 = pygame.Rect(pill1[j][0],pill1[j][1],pill1[j][2],pill1[j][3])
        box2 = pygame.Rect(pill2[j][0],pill2[j][1],pill2[j][2],pill2[j][3])
        if box1.collidepoint(imgX+ 30,imgY) or box2.collidepoint(imgX + 30,imgY):
            exit()
    
    imgY += imgChange
    screen.blit(image,(imgX, imgY))
    
    for i in range(pillNumber):
        pygame.draw.rect(screen,(255,255,255),pygame.Rect(pill1[i][0],pill1[i][1],pill1[i][2],pill1[i][3]))
        pygame.draw.rect(screen,(255,255,255),pygame.Rect(pill2[i][0],pill2[i][1],pill2[i][2],pill2[i][3]))
    for abc in range(pillNumber):
        pill1[abc][0] -= pilXchange
        pill2[abc][0] -= pilXchange
    pygame.display.update()