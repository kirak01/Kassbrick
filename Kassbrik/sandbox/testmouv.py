#!/usr/bin/python
# -*- coding: utf8 -*-

import pygame
from pygame.locals import *

RAQUETTE = "../src/img/raquette1.jpeg"
BALLE = "../src/img/balle.png"


pygame.init()
fenetre = pygame.display.set_mode((480, 640))


#affiche le fond
fond = pygame.image.load("../src/img/fondecranbleu.jpg").convert() 
fenetre.blit(fond, (0,0))

#affiche le perso 
raquette = pygame.image.load(RAQUETTE).convert_alpha()
position_raquette = raquette.get_rect()
position_raquette = fenetre.blit(raquette, (180,600))


#flip font pour rafraichir
fenetre.blit(raquette, position_raquette)
pygame.display.flip()

#affiche la balle
ball = pygame.image.load(BALLE).convert_alpha()
position_ball = ball.get_rect()
postion_ball = fenetre.blit(ball, (220,300))



#flip font pour rafraichir
pygame.display.flip()


pygame.key.set_repeat(1, 1)
continuer = 1
while continuer:
    # print dir(position_perso)
   # print position_raquette.x, ',', position_raquette.y
    for event in pygame.event.get():#on parcourt la liste des event de la boucle 
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN: 
            if event.key == K_LEFT and position_raquette.x > 000: #si fleche gauche et bloquage de la raquette sur la gauche au bord de la fenetre 
                position_perso = position_raquette.move(-5,0)
        if event.type == KEYDOWN:
            if event.key == K_RIGHT and position_raquette.x < 380: #si la fleche droite et bloquage raquette  sur la droite au bord de la fenetre
                position_perso = position_raquette.move(5,0)

#deplacement balle
    position_ball = position_ball.move(0,5)


    #Re- collage
    fenetre.blit(fond,(0,0))
    fenetre.blit(raquette, position_raquette)
    fenetre.blit(ball, position_ball)

    #rafraichissement
    pygame.display.flip()
