import pygame
from pygame.locals import *

import math

import sprite_render

class towers:
    def __init__(self):
        self.list_tower = []

    def add_tower(self, t):
        self.list_tower.append(t)

    def stampa(self):
        for t in self.list_tower:
            t.stampa()

    def euc_distance(self, p1, p2):
        delta_x = p1[0] - p2[0]
        delta_y = p1[1] - p2[1]

        d = math.sqrt(delta_x * delta_x + delta_y * delta_y)

        return d

    def attack(self, baloons_position):
            for t in self.list_tower:
                atk_time = pygame.time.get_ticks()
                if t.atk_ongoing == False and atk_time - t.atk_start > 2500:
                    t.reset_atk()
                    for b_pos in baloons_position:
                        if self.euc_distance((t.img.x, t.img.y), (b_pos[0], b_pos[1])) < 100:
                            self.atk_ongoing = True
                            t.attack()
                            t.atk_start = pygame.time.get_ticks()

    def reset(self):
        self.list_tower = []



class tower_AoE:
    def __init__(self, price, img_path, img_atk, screen, pos):
        self.price = price
        self.screen = screen
        self.img_atk = img_atk
        self.pos = pos

        self.img_laser = [] 
        self.add_atk_sprite()
        self.img = sprite_render.sprite_rend(img_path, (40, 40), pos, screen, True)
        
        self.atk_ongoing = False
        self.atk_start = 0

    def add_atk_sprite(self):
        t = (self.pos[0] + 20, self.pos[1] + 20)
        self.img_laser.append(sprite_render.sprite_rend(self.img_atk, (10, 10), t, self.screen, False))
        self.img_laser.append(sprite_render.sprite_rend(self.img_atk, (10, 10), t, self.screen, False))
        self.img_laser.append(sprite_render.sprite_rend(self.img_atk, (10, 10), t, self.screen, False))
        self.img_laser.append(sprite_render.sprite_rend(self.img_atk, (10, 10), t, self.screen, False))
        self.img_laser.append(sprite_render.sprite_rend(self.img_atk, (10, 10), t, self.screen, False))
        self.img_laser.append(sprite_render.sprite_rend(self.img_atk, (10, 10), t, self.screen, False))
        self.img_laser.append(sprite_render.sprite_rend(self.img_atk, (10, 10), t, self.screen, False))
        self.img_laser.append(sprite_render.sprite_rend(self.img_atk, (10, 10), t, self.screen, False))

        for l in self.img_laser:
            l.rect.topleft = self.pos
 
    def stampa(self):
        self.img.stampa()

        if self.atk_ongoing == True:
            self.print_atk()

    def print_atk(self):
        done = True

        for l in self.img_laser:
            done = l.muoviti()
            l.stampa()
            if done == True:
                self.img_laser.remove(l)

        if len(self.img_laser) == 0:
            self.atk_ongoing = False
            
        return done
    
    def reset_atk(self):
        self.img_laser = []
        self.add_atk_sprite()
    
    def attack(self):
        self.atk_ongoing = True

        angle = 0
        for l in self.img_laser:
            x, y = self.calc_xy((self.img.x + 20, self.img.y + 20), math.radians(angle), 100) 
            x = int(x)
            y = int(y)
            l.aggiungi_punto((x, y))
            angle = angle + 45

    def calc_xy(self, xy, angle, r):
        x = xy[0] + r * math.cos(angle)
        y = xy[1] + r * math.sin(angle)

        return (x, y)
    
    def get_laser(self):
        return self.img_laser

