#!/usr/bin/python
# -*- coding: utf8 -*-

import sys
import math
import pygame
from pygame.locals import *

RAQUETTE = "../src/img/raquette1.jpeg"
BALLE = "../src/img/balle2.png"
BRIQUE = "../src/img/brique.jpeg"
GAMEOVER = "../src/img/gameover.png"


pygame.init()
fenetre = pygame.display.set_mode((480, 640))

dx = 0
dy = 5
dz = 0

#affiche le fond
fond = pygame.image.load("../src/img/fondecranbleu.jpg").convert()
fenetre.blit(fond, (0,0))

#affiche le raquette 
raquette = pygame.image.load(RAQUETTE).convert_alpha()
pos_raquette = raquette.get_rect()
pos_raquette = fenetre.blit(raquette, (180,600))

ball = pygame.image.load(BALLE).convert_alpha()
pos_ball = ball.get_rect()
pos_ball = fenetre.blit(ball, (220,300+dy))

pos_briques = [(200, 150), (200,100), (200,50)]

briques = list()
for pos in pos_briques :
    brik = pygame.image.load(BRIQUE).convert_alpha()
    briques.append(brik)
    fenetre.blit(brik, pos)


#flip font pour rafraichir
pygame.display.flip()

pygame.key.set_repeat(1, 1)
continuer = 1
while continuer:
    for event in pygame.event.get():#on parcourt la liste des évènements pygame 
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_LEFT and pos_raquette.x > 000 : #si fleche gauche
                dz = -5
            if event.key == K_RIGHT and pos_raquette.x < 380 : #si la fleche droite
                dz = 5
            pos_raquette = pos_raquette.move(dz,0)
   

    if pos_ball.y == pos_raquette.y and pos_ball.x >= pos_raquette.x+40 and pos_ball.x <= pos_raquette.x+60 :
        dy = -1*dy
        dx = 0
    if pos_ball.y == pos_raquette.y and pos_ball.x >= pos_raquette.x+20 and pos_ball.x < pos_raquette.x+40 :
        dy = -1*dy
        dx = -1
    if pos_ball.y == pos_raquette.y and pos_ball.x >= pos_raquette.x and pos_ball.x < pos_raquette.x+20 :
        dy = -1*dy
        dx = -3
    if pos_ball.y == pos_raquette.y and pos_ball.x > pos_raquette.x+60 and pos_ball.x <= pos_raquette.x+80 :
        dy = -1*dy
        dx = 1
    if pos_ball.y == pos_raquette.y and pos_ball.x > pos_raquette.x+80 and pos_ball.x <= pos_raquette.x+100 :
        dy = -1*dy
        dx = 3

    if pos_ball.x <=0 or pos_ball.x >= 470 :
        dx = -1*dx
        dy = dy

    if pos_ball.y == 620 :
        dx = 0
        dy = 0
        gameover = pygame.image.load(GAMEOVER).convert_alpha()
        pos_gameover = gameover.get_rect()
        pos_gameover = fenetre.blit(gameover, (130,215))      
        fenetre.blit(gameover, pos_gameover)

    if pos_ball.y == 0 :
        dy = -1*dy 

    pos_ball = pos_ball.move(dx,dy)    
   # pos_raquette = pos_raquette.move(dx,0)

    for brik in briques :
        pos = pos_briques[briques.index(brik)]
        if pos_ball.y == pos[1]+40 :
            dy = -1*dy
            # je supprime la brique de la liste
            pos_briques.remove(pos)
            briques.remove(brik)

   
    #Re- collage
    fenetre.blit(fond, (0,0))
    for brik in briques :
        pos = pos_briques[briques.index(brik)]
        fenetre.blit(brik, pos)

    fenetre.blit(raquette, pos_raquette)
    fenetre.blit(ball, pos_ball)
    #rafraichissement
    pygame.display.flip()

