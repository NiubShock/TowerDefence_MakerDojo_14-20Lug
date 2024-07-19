import pygame
from pygame.locals import *

import enemy      
import gioco

lista_punti = [(390, 200), (390, 70), (250, 70), 
               (250, 410), (115, 410), (115, 285), 
               (500, 285), (500, 155), (600, 155),
               (600, 360), (353, 360), (353, 535)]

list_img = ["./Sprites/Animals/cow.png",
            "./Sprites/Animals/chicken.png"]


pygame.init()
screen = pygame.display.set_mode((826, 532))

bkgrd = pygame.image.load("./TowerDefence/map.jpg").convert()
bkgrd = pygame.transform.scale(bkgrd, (800, 600))

enemy1 = enemy.enemy(2, list_img, 100, screen)
enemy1.punti_movimento(lista_punti)

g = gioco.gioco(0, 450, 5, "./TowerDefence/map.jpg", lista_punti, screen)

en_list = [enemy1]

pygame.display.flip()


run = True
clock = pygame.time.Clock()
while run:
    
    clock.tick(90)
    # screen.blit(bkgrd, (0, 0))
    event_list = pygame.event.get()
    g.play(event_list)

    pygame.display.flip()

    for ev in event_list:
        if ev.type == pygame.QUIT:
            run = False

pygame.quit

