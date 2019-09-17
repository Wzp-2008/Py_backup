from pygame import *
import pygame
import sys
from tools import *
from random import *
pygame.init()
sc = pygame.display.set_mode((600,496))
dog1 = image.load("dog1.png")
dog2 = image.load("dog2.png")
done=False
white = pygame.color.Color("white")
while not done:
    sc.blit(dog1,(0,0))
    for i in pygame.event.get():
        event_type = i.type
        if i.type == QUIT:
            done=True
        if i.type == MOUSEBUTTONDOWN:
            sc.fill(white)
            sc.blit(dog2,(0,0))
    pygame.display.update()
pygame.quit()
