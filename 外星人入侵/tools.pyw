import pygame
def Button(image,x,y,event_type,sc):
    m_x = pygame.mouse.get_pos()[0]
    m_y = pygame.mouse.get_pos()[1]
    i1 = pygame.image.load(image )
    sc.blit(i1,(x,y))
    i1rect = i1.get_rect()[2:4]
    if m_x>=x and m_x<=x+i1rect[0] and m_y>=y and m_y<=m_y+i1rect[1] and event_type ==  pygame.MOUSEBUTTONDOWN:
        return True
    else:
        return False
def draw_rect(w,h,x,y,r,g,b,sc):
    colour = pygame.color.Color(r,g,b)
    pygame.draw.rect(sc,colour,(x,y,w,h))
    pygame.display.flip()
def draw_circle(b_r,x,y,r,g,b,sc):
    colour = pygame.color.Color(r,g,b)
    pygame.draw.circle(sc,colour,(x,y),b_r)
    pygame.display.flip()
