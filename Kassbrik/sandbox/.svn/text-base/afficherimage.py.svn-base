#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
pygame.init()

RESOLUTION = (480,640)
BACKGROUND = "../src/img/backgroundearth1.jpg"
RAQUETTE = "../src/img/raquette1.jpeg"
BALLE = "../src/img/balle.png"

#Ouverture de la fenêtre Pygame 640x480p
fenetre = pygame.display.set_mode(RESOLUTION) #affichage et dimension de la fenêtre

fond = pygame.image.load(BACKGROUND).convert() #insertion du fond et convertion
fenetre.blit(fond, (107,186)) #position de la fenêtre

perso = pygame.image.load(RAQUETTE).convert() #insertion raquette et conversion
fenetre.blit(perso, (190,600)) #position raquette1

balle = pygame.image.load(BALLE).convert_alpha()
fenetre.blit(balle, (185,540))

pygame.display.flip() #rafraichissement de l'écran

#boucle infinie pour que l'image reste ?
continuer = 1
while continuer:
    continuer = int(input())

