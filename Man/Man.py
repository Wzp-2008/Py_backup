import pygame
from pygame import *
import os
pygame.init()
sc = pygame.display.set_mode((800,600))
white = pygame.color.Color("white")
sc.fill(white)
done=False
down1 = pygame.image.load(r"image\down1.png")
down2 = pygame.image.load(r"image\down2.png")
side1 = pygame.image.load(r"image\side1.png")
side2 = pygame.image.load(r"image\side2.png")
standing = pygame.image.load(r"image\standing.png")
up1 = pygame.image.load(r"image\up1.png")
up2 = pygame.image.load(r"image\up2.png")
y1 = pygame.image.load(r"image\y1.png")
y2 = pygame.image.load(r"image\y2.png")
x = 10
y = 10
sc.blit(standing,(x,y))
while not done:
    for i in pygame.event.get():
        event_type = i.type
        if i.type == QUIT:
            done=True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= 1
        sc.blit(up1,(x,y))
        sc.fill(white)
        sc.blit(up2,(x,y))
    if keys[pygame.K_s]:
        y += 1
        sc.blit(down1,(x,y))
        sc.fill(white)
        sc.blit(down2,(x,y))
    if keys[pygame.K_a]:
        x -= 1
        sc.blit(side1,(x,y))
        sc.fill(white)
        sc.blit(side2,(x,y))
    if keys[pygame.K_d]:
        x += 1
        sc.blit(y1,(x,y))
        sc.fill(white)
        sc.blit(y2,(x,y))
    pygame.display.update()
pygame.quit()
