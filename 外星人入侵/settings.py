import pygame
from pygame import *
import os
class settings:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((768,760))
        os.system("cd images")
    def Backgroud(self):
        bg = pygame.image.load(r"images\bg_image.png")
        self.window.blit(bg,(0,0))
