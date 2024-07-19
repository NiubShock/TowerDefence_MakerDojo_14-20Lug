import pygame
from pygame.locals import *

class baloon:
    def __init__(self, vite, img, sprite, coord):
        self.img_red = pygame.image.load("./Sprites/Animals/bear.png").convert_alpha()
        self.img_red = pygame.transform.scale(self.img_red, (70,70))
        self.img_blue = pygame.image.load("./Sprites/Animals/buffalo.png").convert_alpha()
        self.img_blue = pygame.transform.scale(self.img_blue, (70,70))
        self.img_yellow = pygame.image.load("./Sprites/Animals/cow.png").convert_alpha()
        self.img_yellow = pygame.transform.scale(self.img_yellow, (70,70))

        self.vite = vite 

        self.baloon_sprite = sprite
        self.baloon_sprite.image = self.img_red
        self.baloon_sprite.rect = img.get_rect()
        self.baloon_sprite.rect.topleft = coord
        self.x, self.y = coord
        self.path_pos = 0
        self.set_image()

    def set_image(self):
        if self.vite == 1:
            self.baloon_sprite.image = self.img_red
        if self.vite == 2:
            self.baloon_sprite.image = self.img_blue
        if self.vite == 3:
            self.baloon_sprite.image = self.img_yellow

    def set_coord(self, x, y):

        self.x = x
        self.y = y
        self.baloon_sprite.rect.topleft = (x, y)

    def inc_coord(self, x, y):
        self.x = self.x + x
        self.y = self.y + y

        self.set_coord(self.x, self.y)

    def follow_path(self, increment):
        if self.path_pos == 0:
            self.inc_coord(increment, 0)

            if self.x == 570:
                self.path_pos = 1
                self.collinsion_hap()
        
        if self.path_pos == 1:
            self.inc_coord(0, -increment)
            
            if self.y == 150:
                self.path_pos = 2
                self.collinsion_hap()


        if self.path_pos == 2:
            self.inc_coord(-increment, 0)
            
            if self.x == 370:
                self.path_pos = 3
            
        if self.path_pos == 3:
            self.inc_coord(0, increment)

            if self.y == 700:
                self.path_pos = 4

        if self.path_pos == 4:
            self.inc_coord(-increment, 0)

            if self.x == 150:
                self.path_pos = 5

        if self.path_pos == 5:
            self.inc_coord(0, -increment)

            if self.y == 500:
                self.path_pos = 6
        
        if self.path_pos == 6:
            self.inc_coord(increment, 0)

            if self.x == 720:
                self.path_pos = 7

        if self.path_pos == 7:
            self.inc_coord(0, -increment)

            if self.y == 250:
                self.path_pos = 8

        if self.path_pos == 8:
            self.inc_coord(increment, 0)

            if self.x == 870:
                self.path_pos = 9

        if self.path_pos == 9:
            self.inc_coord(0, increment)

            if self.y == 600:
                self.path_pos = 10

        if self.path_pos == 10:
            self.inc_coord(-increment, 0)

            if self.x == 500:
                self.path_pos = 11

        if self.path_pos == 11:
            self.inc_coord(0, increment)

            if self.y == 900:
                return True
        
        return False
    
    def collinsion_hap(self):
        self.vite = self.vite - 1
        self.set_image()