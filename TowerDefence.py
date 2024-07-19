import pygame
from pygame.locals import *

import baloon

class BaloonS:
    def __init__(self):
        self.baloons_list = []
    
    def add_element(self):
        self.baloons_list.append(baloon.baloon(3, baloon_red, pygame.sprite.Sprite(all_sprites), (50,350)))
 
    def update_sprites(self):
        for e in self.baloons_list:
            must_kill = e.follow_path(1) 

            if must_kill == True:
                self.baloons_list.remove(e)
                e.baloon_sprite.kill()


# imposto la risoluzione
res_x = 1200
res_y = 900

# Setto gli FPS
fps = 60

# Inizializzazione di pygame
pygame.init()

# Preparo i font
font = pygame.font.SysFont("Times New Roman", 50)

# Imposto le caratteristiche della finestra
form = pygame.display.set_mode((res_x, res_y))
pygame.display.set_caption("Tower Defence")

# Carico il background
bkgrd = pygame.image.load("./TowerDefence/map.jpg").convert()
bkgrd = pygame.transform.scale(bkgrd, (res_x, res_y))

# Prendo il tipo degli oggetti
all_sprites = pygame.sprite.Group()

# Preparazione degli sprite
baloon_red = pygame.image.load("./Sprites/Animals/bear.png").convert_alpha()    # Carico l'immagine
baloon_red = pygame.transform.scale(baloon_red, (20, 20))
baloons_list = []                                                               # Preparo il vettore 

# ===========================
# Codice eseguito di continuo
# ===========================
run = True
tot_baloons = 0
start_cycle = pygame.time.get_ticks()
baloons = BaloonS()

while run:
    pygame.time.Clock().tick(fps)
    run_time = pygame.time.get_ticks()

    # Ogni secondo aggiungo un palloncino finche non sono 10
    if run_time - start_cycle > 1000:
        if tot_baloons < 10:
            print("Aggiungo un palloncino")
            # baloons_list.append(baloon(3, baloon_red, pygame.sprite.Sprite(all_sprites), (50,50)))
            tot_baloons = tot_baloons + 1
            baloons.add_element()
            start_cycle = run_time
        
    baloons.update_sprites() 

    for ev in pygame.event.get():
        if ev.type == QUIT:
            run = False
        
        if ev.type == MOUSEBUTTONDOWN:
            click = ev.pos
            b = baloon.baloon(3, baloon_red, pygame.sprite.Sprite(all_sprites), click)

    form.blit(bkgrd, (0,0))
    all_sprites.draw(form)

    money_string = "Money 100g"
    money_rend = font.render(money_string, True, "yellow")
    form.blit(money_rend, (20, 20))


    pygame.display.flip()

pygame.quit()