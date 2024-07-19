import pygame
from pygame.locals import *

import enemy
import tower

class gioco:
    def __init__(self, punti_iniziali, soldi_iniz, vite, mappa, lista_punti, screen):
        self.punteggio = punti_iniziali
        self.punti_finali = 0
        self.soldi = soldi_iniz
        self.soldi_iniz = soldi_iniz
        self.vita = vite
        self.vite_iniz = vite
        self.mappa = mappa
        self.screen = screen

        self.list_en = []
        self.lista_punti = lista_punti

        self.towers = tower.towers()

        self.fase_gioco = 0
        self.time_spawn = 0
        self.num_en     = 0

        self.mappa = pygame.image.load(mappa).convert()
        self.gameover = pygame.image.load("./TowerDefence/game_over.jpg").convert()
        self.gameover = pygame.transform.scale(self.gameover, (826, 532))

        self.font = pygame.font.SysFont("Times new Roman", 30)
        
        self.livello = 1

    def play(self, events):

        # Fase di posizionamento delle tower
        if self.fase_gioco == 0:
            self.screen.blit(self.mappa, (0,0))
            self.towers.stampa()

            self.scritte()

            str_spiegazione = "Posiziona le torri e premi k"
            str_spiegazione = self.font.render(str_spiegazione, True, "black")
            self.screen.blit(str_spiegazione, (20, 500))

            for ev in events:
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_k:
                        self.fase_gioco = 1
                elif ev.type == pygame.MOUSEBUTTONDOWN:
                    cost_tower = 200
                    if self.soldi - cost_tower >= 0:
                        t = (ev.pos[0] - 20, ev.pos[1] - 20)
                        self.towers.add_tower(tower.tower_AoE(200, "./Sprites/Animals/duck.png", "./Sprites/SpaceArt/laserRed.png", self.screen, t))
                        self.soldi = self.soldi - cost_tower

            

        if self.fase_gioco == 1:
            list_img = ["./Sprites/Animals/cow.png", "./Sprites/Animals/chicken.png", "./Sprites/Animals/dog.png", "./Sprites/Animals/gorilla.png"]
            self.screen.blit(self.mappa, (0, 0))

            livello_en = self.livello * 2
            if len(list_img) < livello_en:
                livello_en = len(list_img)

            self.spawn_enemies(self.livello * 20, livello_en, list_img)
            self.print_enemies()

            self.scritte()

            self.towers.stampa()
            b_pos = []
            for en in self.list_en:
                b_pos.append((en.sprite.x, en.sprite.y))
            self.towers.attack(b_pos)

            self.check_collision()

            if len(self.list_en) == 0:
                self.reset()
                self.fase_gioco = 0
                self.livello = self.livello + 1
            

        # Fase di game over
        if self.fase_gioco == 2:
            self.screen.blit(self.gameover, (0, 0))

            str_gameover = "Hai fatto " + str(self.punti_finali) + ", premi spazio per ricomciare"
            str_gameover = self.font.render(str_gameover, True, "white")
            self.screen.blit(str_gameover, (200, 450))

            for ev in events:
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_SPACE:
                        self.fase_gioco = 0
            
            self.reset()
            self.towers.reset()
            self.punteggio = 0
            self.soldi = self.soldi_iniz
            self.vita = self.vite_iniz
            self.livello = 1

    def scritte(self):
        str_vita = "Vita:" + str(self.vita)
        str_vita = self.font.render(str_vita, True, "black")
        self.screen.blit(str_vita, (500, 10))

        str_soldi = "Soldi:" + str(self.soldi)
        str_soldi = self.font.render(str_soldi, True, "black")
        self.screen.blit(str_soldi, (500, 40))

        str_punti = "Punti:" + str(self.punteggio)
        str_punti = self.font.render(str_punti, True, "black")
        self.screen.blit(str_punti, (500, 70))

    def spawn_enemies(self, num_en, vita_en, img_en):
        act_time = pygame.time.get_ticks()

        # È passato tempo sufficiente
        if act_time - self.time_spawn > 1000:
            # Generare un nemico
            if self.num_en < num_en:
                # Creo il nemico
                    self.list_en.append(enemy.enemy(vita_en, img_en, vita_en * 10, self.screen))
                    self.list_en[len(self.list_en) - 1].punti_movimento(self.lista_punti)
                    self.num_en = self.num_en + 1
            # Resettare il timer
            self.time_spawn = act_time

    def print_enemies(self):
        for e in self.list_en:
            vita_persa = e.muoviti()
            e.stampa()

            if vita_persa == True:
                self.vita = self.vita - 1
                self.list_en.remove(e)

                if self.vita == 0:
                    # print("Game over")
                    self.fase_gioco = 2
                    self.punti_finali = self.punteggio

    def check_collision(self):
        for t in self.towers.list_tower:
            for l in t.img_laser:
                for en in self.list_en:
                    if l.rect.colliderect(en.sprite.rect):
                        gold, morto = en.colpito()
                        t.img_laser.remove(l)

                        self.soldi = self.soldi + gold
                        self.punteggio = self.punteggio + 10

                        if morto == True:
                            print(self.soldi)
                            print(self.punteggio)
                            self.list_en.remove(en)

                        break

    def reset(self):
        self.num_en = 0
        self.list_en = []