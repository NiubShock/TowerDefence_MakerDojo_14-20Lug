import pygame
from pygame.locals import *

class sprite_rend:
    def __init__(self, stringa_pos, cord_scale, cord_iniz, form, print_now):
        #self.sp = pygame.image.load(stringa_pos).convert_alpha()
        self.rect = 0
        self.carica_immagine(stringa_pos, cord_scale)

        #self.sp = pygame.transform.scale(self.sp , cord_scale)

        self.x, self.y = cord_iniz
        self.form = form

        self.list_points = []
        self.point_pos = 0

        if print_now == True:
            self.stampa()

    def carica_immagine(self, img, cord_scale):
        self.sp = pygame.image.load(img).convert_alpha()
        self.sp = pygame.transform.scale(self.sp, cord_scale)
        self.rect = self.sp.get_rect()


    def cord_increase(self, cord_x, cord_y):
        self.x = self.x + cord_x
        self.y = self.y + cord_y

    def stampa(self):
        self.form.blit(self.sp, (self.x, self.y))
        self.rect.topleft = (self.x, self.y)

    def muoviti_al_punto(self, cord_x, cord_y):
        inc_x = cord_x - self.x
        inc_y = cord_y - self.y

        if inc_x != 0 or inc_y != 0:
            if inc_x > 0:
                inc_x = 1
            elif inc_x < 0:
                inc_x = -1

            if inc_y > 0:
                inc_y = 1
            elif inc_y < 0:
                inc_y = -1

            self.cord_increase(inc_x, inc_y)
            return False

        return True
    
    def aggiungi_punto(self, cord):
        self.list_points.append(cord)

    def insieme_punti(self, l):
        for pos in l:
            self.aggiungi_punto(pos)

    def muoviti(self):
        pos_x, pos_y = self.list_points[self.point_pos]
        punto_ragg = self.muoviti_al_punto(pos_x, pos_y)

        if punto_ragg == True:
            self.point_pos = self.point_pos + 1

            if self.point_pos >= len(self.list_points):
                self.point_pos = self.point_pos - 1

                # Aggiungere perdita di vita
                return True
        
        return False