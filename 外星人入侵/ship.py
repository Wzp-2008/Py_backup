import settings
import pygame
from pygame import *
setting = settings.settings()
def main(x,y):
    setting.window.blit(pygame.image.load(r"images\plane.png"),(x,y))
