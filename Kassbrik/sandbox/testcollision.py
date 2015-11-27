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
fenetre= pygame.display.set_mode((480, 640))


dx = 6
dy = 6
Dx = 0

#affiche le fond
fond = pygame.image.load("../src/img/fondecranbleu.jpg").convert()
fenetre.blit(fond, (0,0))

#affiche les briques

pos_briques = [(200, 150), (200,100), (200,50)]

briques = list()
for pos in pos_briques :
    brik = pygame.image.load(BRIQUE).convert_alpha()
    briques.append(brik)
    fenetre.blit(brik, pos)


#affiche le raquette 
raquette = pygame.image.load(RAQUETTE).convert_alpha()
pos_raquette = raquette.get_rect()
pos_raquette = fenetre.blit(raquette, (180,600))


#affiche la balle
ball = pygame.image.load(BALLE).convert_alpha()
pos_ball = ball.get_rect()
pos_ball = fenetre.blit(ball, (220,300+dy))



#flip font pour rafraichir
pygame.display.flip()


pygame.key.set_repeat(1, 1)

continuer = 1
while continuer == 1 :
    for event in pygame.event.get():#on parcourt la liste des évènements pygame 
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_LEFT and pos_raquette.x > 000 : #si fleche gauche
                Dx = -5 
                pos_raquette = pos_raquette.move(Dx,0)
            if event.key == K_RIGHT and pos_raquette.x < 380 : #si la fleche droite
                Dx = 5
                pos_raquette = pos_raquette.move(Dx,0)
   

 #les lignes suivantes modifie l'angle de la trajectoire de la balle selon l'endroit ou elle tape la raquette 
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

#si touche en haut de l'ecran
    if pos_ball.y == 0 :
        dy = -1*dy
        dx = 1*dx

#si touche a droite ou a gauche de l'ecran
    if pos_ball.x <= 0 or pos_ball.x >= 470:
        dy = 1*dy
        dx = -1*dx

#si touche en bas
    if pos_ball.y == 620 :
        dx = 0
        dy = 0
        continuer == 2

    for brik in briques :
        pos = pos_briques[briques.index(brik)]
        if pos_ball.y == pos[1]+40 :
            dy = -1*dy
            # je supprime la brique de la liste
            pos_briques.remove(pos)
            briques.remove(brik)


    pos_ball = pos_ball.move(dx,dy)
   # pos_raquette = pos_raquette.move(dx,0)

    #Re- collage
    fenetre.blit(fond, (0,0))
    for brik in briques :
        pos = pos_briques[briques.index(brik)]
        fenetre.blit(brik, pos)
        fenetre.blit(raquette, pos_raquette)
        fenetre.blit(ball, pos_ball)
   
while continuer == 2:
    gameover = pygame.image.load(GAMEOVER).convert_alpha()
    pos_gameover = gameover.get_rect()
    pos_gameover = fenetre.blit(gameover, (0,0))
    fenetre.blit(gameover, pos_gameover)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
                continuer = 0


    #rafraichissement
    pygame.display.flip()

