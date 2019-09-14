import pygame
from pygame import *
class main:
    def __init__(self):
        pygame.init()
    def window(self,backgrund,w_w,w_h):
        windows = pygame.display.set_mode((w_w,w_h))
        bc = pygame.image.load(backgrund)
        windows.blit(bc,(0,0))
    def sound(self,sound):
        pygame.mixer.init()
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()
    def image(self,image,x,y):
        images = pygame.image.load(image)
        self.windows.blit(images,(x,y))
