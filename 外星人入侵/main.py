import settings
from alien import *
from Bullet_f import *
import ship
import pygame
from pygame import *
from pygame.sprite import Group
import tools
b = settings.settings()
done=False
s_x = 289
s_y = 668
B_x = s_x/2-43
B_y = s_y + 105
aliens = Group()
Bullets = Group()
for i in range(5):
    alien = Alien()
    #每个外星人最初都在屏幕左上角附近
    alien.rect.x = alien.rect.width * i + 40
    aliens.add(alien)
for i in range(5):
    alien = Alien()
    #每个外星人最初都在屏幕左上角附近
    alien.rect.x = alien.rect.width * i + 40
    alien.rect.y = alien.rect.height 
    aliens.add(alien)


for i in range(5):
    alien = Alien()
    #每个外星人最初都在屏幕左上角附近
    alien.rect.x = alien.rect.width * i + 40
    alien.rect.y = alien.rect.height*2
    aliens.add(alien)
for i in range(5):
    alien = Alien()
    #每个外星人最初都在屏幕左上角附近
    alien.rect.x = alien.rect.width * i + 40
    alien.rect.y = alien.rect.height*3 
    aliens.add(alien)

for i in range(5):
    alien = Alien()
    #每个外星人最初都在屏幕左上角附近
    alien.rect.x = alien.rect.width * i + 40
    alien.rect.y = alien.rect.height*4
    aliens.add(alien)
for i in range(5):
    alien = Alien()
    #每个外星人最初都在屏幕左上角附近
    alien.rect.x = alien.rect.width * i + 40
    alien.rect.y = alien.rect.height*5
    aliens.add(alien)

for i in range(5):
    alien = Alien()
    #每个外星人最初都在屏幕左上角附近
    alien.rect.x = alien.rect.width * i + 40
    alien.rect.y = alien.rect.height*6
    aliens.add(alien)
while not done:
    B_y += 1
    for i in pygame.event.get():
        event_type = i.type
        if i.type == pygame.QUIT:
            done=True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        s_x -= 10
    if keys[pygame.K_d]:
        s_x += 10
    b.Backgroud()
    aliens.draw(b.window)
    ship.main(s_x,s_y)
    
    pygame.display.update()
pygame.quit()
