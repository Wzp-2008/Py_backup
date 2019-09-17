from pygame import *
import pygame
import sys
from tools import *
from random import *
pygame.init()
pygame.mixer.quit()
movie = pygame.movie.Movie('Test.AVI') 
movie.set_display(pygame.display.set_mode((854,480))) 
movie.set_volume(1.0)
movie.play() 
done=False
while not done:
    for i in pygame.event.get():
        event_type = i.type
        if i.type == QUIT:
            done=True
    pygame.display.update()
pygame.quit()
