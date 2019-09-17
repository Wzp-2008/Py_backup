from pygame import *
import pygame
import sys
from tools import *
from random import *
pygame.init()
sc = pygame.display.set_mode((800,600))
done=False
while not done:
    for i in pygame.event.get():
        event_type = i.type
        if i.type == QUIT:
            done=True
    r = randrange(0,256)
    g = randrange(0,256)
    b = randrange(0,256)
    x = randrange(0,800,40)
    y = randrange(0,600,30)
    draw_rect(40,30,x,y,r,g,b,sc)
    pygame.display.update()
pygame.quit()

