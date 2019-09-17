import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self):
        super().__init__()
         #加载外星人图像，并设置其rect属性
        self.image = pygame.image.load("images/alien.png")
        self.rect = self.image.get_rect()
