import pygame
from pygame.locals import *

import sprite_render

class enemy:
    def __init__(self, vita, lista_str, coins, form):
        self.vita = vita

        self.lista_str_immagine = lista_str
        self.immagine_load = len(lista_str) - vita - 1

        self.coins = coins
        self.form = form

        self.sprite = sprite_render.sprite_rend(self.lista_str_immagine[self.immagine_load], (40, 40), (0, 200), form, True)

    def stampa(self):
        self.sprite.stampa()

    def punti_movimento(self, l):
        self.sprite.insieme_punti(l)
    
    def muoviti(self):
        return self.sprite.muoviti()

    def colpito(self):
        self.vita = self.vita - 1

        if self.vita <= 0:
            return (self.coins, True)
        else:
            self.immagine_load = self.immagine_load + 1
            self.sprite.carica_immagine(self.lista_str_immagine[self.immagine_load], (40, 40))
            return (0, False)
 