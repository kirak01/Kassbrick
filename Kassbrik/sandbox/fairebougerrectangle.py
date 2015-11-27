#!/usr/bin/python
# -*- coding: utf8 -*-

import pygame
from pygame.locals import *

#initialise l'affichage 
pygame.display.init() 


#cree la resolution et affiche l'affichage
RESOLUTION = (640 , 480)
screen = pygame.display.set_mode(RESOLUTION)

#definit la couleur et l'affiche
couleur = 0, 0, 0
screen.fill(couleur)

rectangle=pygame.Surface((60,10)) #definit la surface du rectangle
rectangle.fill ( (255,0,0) ) #definit la couleur du rectangle
screen.blit(rectangle, (260,485)) #definit la position du rectangle(plaque l'objet sur la surface d'affichage)

pygame.key.set_repeat(40, 30)

position_rectangle=rectangle.get_rect()

#boucle qui permet le mouvement de l'image
continuer = 1
while continuer:
    for event in pygame.event.get(): #permet le parcours la liste des event de la boucle 
        if event.type == QUIT: #boucle infinie pour que la fenetre ne se ferme pas toute seule mais grace à la croix
            continuer = 0

        if event.type == KEYDOWN:
            if event.key == K_LEFT: #si fleche gauche
                position_rectangle = position_rectangle.move(-3,0) #permet de deplacer l'objet vers la gauche
            if event.key == K_RIGHT: #si la fleche droite
                position_rectangle = position_rectangle.move(3,0) #permet de deplacer l'objet vers la droite
    
    #FIXME trouver comment effacer le rectangle avant de le reafficher 
    # plus loin

    #actualise l'affichage
    pygame.display.flip()
    

