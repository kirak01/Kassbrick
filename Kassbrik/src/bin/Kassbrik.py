#!/usr/bin/python
# -*- coding: utf8 -*-

import sys
import math
import pygame
from pygame.locals import * 

RAQUETTE = "../img/raquette1.jpeg"
BALLE = "../img/balle2.png"
BRIQUE = "../img/brique.jpeg"
GAMEOVER = "../img/gameover.png"
RESOLUTION = (480, 640)
GAGNER = "../img/youwin.png"
pygame.init()
fenetre = pygame.display.set_mode(RESOLUTION)

dx_balle = 0 #deplacement de la balle en x
dy_balle = 5 #deplacement de la balle en y
dx_raquette = 0 #deplacement de la raquette en x



#affiche le fond
fond = pygame.image.load("../img/fondecranbleu.jpg").convert()
fenetre.blit(fond, (0,0))

#affiche le raquette 
raquette = pygame.image.load(RAQUETTE).convert_alpha()
pos_raquette = raquette.get_rect()
pos_raquette = fenetre.blit(raquette, (180,600))

#affiche la balle
balle = pygame.image.load(BALLE).convert_alpha()
pos_balle = balle.get_rect()
pos_balle = fenetre.blit(balle, (220,560+dy_balle))

#affiche les briques
pos_briques = [(0,50),(70,50),(140,50),(210,50),(280,50),(350,50),(420,50)]
               # (35,100),(105,100),(175,100),(245,100),(315,100),(385,100), 
                #(0,150),(70,150),(140,150),(210,150),(280,150),(350,150),(420,150), 
                #(35,200),(105,200),(175,200),(245,200),(315,200),(385,200)]

briques = list()
for pos in pos_briques :
    brique = pygame.image.load(BRIQUE).convert_alpha()
    briques.append(brique)
    fenetre.blit(brique, pos)


#rafraichissement de l'image
pygame.display.flip()
#nombre de frappe sur le clavier par ms
pygame.key.set_repeat(1, 1)

continuer = 1 

#affichage du GAME OVER lorsque la balle n'est pas rattrapée par la raquette
def game_over():
    global continuer
    while continuer == 1 :
        gameover = pygame.image.load(GAMEOVER).convert_alpha()
        pos_gameover = gameover.get_rect()
        pos_gameover = fenetre.blit(gameover, (0,0))
        fenetre.blit(gameover, pos_gameover)
        pygame.display.flip()
        
        rejouer = False
        for event in pygame.event.get():
            if event.type == QUIT:
                    continuer = 0
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    rejouer = True
                    break
        if rejouer :
            break

continuer = 1

def gagner():
    global continuer
    while continuer == 1 :   
        img_gagner = pygame.image.load(GAGNER).convert_alpha()
        pos_gagner = img_gagner.get_rect()
        pos_gagner = fenetre.blit(img_gagner, (0,0)) 
        fenetre.blit(img_gagner, pos_gagner)  
        pygame.display.flip()

        rejouer = False
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    rejouer = True
                    break
        if rejouer :
                break



        
#boucle infinie permettant de faire tourner le jeu en continu
while continuer == 1:
    for event in pygame.event.get(): 
        #si on clique sur la croix, le jeu se ferme
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_RIGHT:
                if  event.key == K_LEFT and pos_raquette.x > 000 : 
                    dx_raquette = -5
                    pos_raquette = pos_raquette.move(dx_raquette,0)
                if event.key == K_RIGHT and pos_raquette.x < 380 :
                    dx_raquette = 5
                    pos_raquette = pos_raquette.move(dx_raquette,0)
   
    #changement de l'angle du deplacement de la balle selon sa position atteinte sur la raquette
    if pos_balle.y+10 == pos_raquette.y and pos_raquette.x+60 > pos_balle.x >= pos_raquette.x+40 :
        dy_balle = -1*dy_balle
        dx_balle = 0
    if pos_balle.y+10 == pos_raquette.y and pos_raquette.x+40 > pos_balle.x >= pos_raquette.x+20 :
        dy_balle = -1*dy_balle
        dx_balle = -1
    if pos_balle.y+10 == pos_raquette.y and pos_raquette.x+20 > pos_balle.x >= pos_raquette.x :
        dy_balle = -1*dy_balle
        dx_balle = -3
    if pos_balle.y+10 == pos_raquette.y and pos_raquette.x+80 >= pos_balle.x >= pos_raquette.x+60 :
        dy_balle = -1*dy_balle
        dx_balle = 1
    if pos_balle.y+10 == pos_raquette.y and pos_raquette.x+100 >= pos_balle.x > pos_raquette.x+80 :
        dy_balle = -1*dy_balle
        dx_balle = 3

    #changement de l'angle du deplacement de la balle selon sa position atteinte sur les bords de l'écran
    if pos_balle.x <=0 or pos_balle.x >= 470 :
        dx_balle = -1*dx_balle
        dy_balle = dy_balle

    #quand la balle atteint le bas de l'écran, affiche GAME OVER et réinitialise les paramètres de départ
    if pos_balle.y == 620 :
        game_over()
        pos_balle = balle.get_rect()
        pos_balle = fenetre.blit(balle, (220,560+dy_balle))
        dx_balle = 0
        dy_balle = 5
        #deplacement de la balle resultant de l'addition des composantes de dx_balle et de dy_balle
        pos_balle = pos_balle.move(dx_balle,dy_balle)
        
        pos_briques = [ (0,50),(70,50),(140,50),(210,50),(280,50),(350,50),(420,50),
                        (35,100),(105,100),(175,100),(245,100),(315,100),(385,100),
                        (0,150),(70,150),(140,150),(210,150),(280,150),(350,150),(420,150),
                        (35,200),(105,200),(175,200),(245,200),(315,200),(385,200) ]
        briques = list()
        for pos in pos_briques :
            brique = pygame.image.load(BRIQUE).convert_alpha()
            briques.append(brique)
            fenetre.blit(brique, pos)

        pos_raquette = raquette.get_rect()
        pos_raquette = fenetre.blit(raquette, (180,600))



    #rebond de la balle lorsqu'elle atteint le haut de l'ecran
    if pos_balle.y == 0 :
        dy_balle = -1*dy_balle 
    #mouvement de la balle
    pos_balle = pos_balle.move(dx_balle,dy_balle)

    #rebond de la balle sur la brique et disparition de celle-ci
    for brique in briques :
        pos = pos_briques[briques.index(brique)]
        if pos[1]+39 <= pos_balle.y <= pos[1]+41 and pos[0]+0 <= pos_balle.x <= pos[0]+60 :
            dy_balle = -1*dy_balle
            if pos in pos_briques :
            #suppression la brique de la liste
                pos_briques.remove(pos)
                briques.remove(brique)
     
        if pos[1]-11 <= pos_balle.y <= pos[1]-9 and pos[0]+0 <= pos_balle.x <= pos[0]+60 :
            dy_balle = -1*dy_balle
            if pos in pos_briques :
                pos_briques.remove(pos)
                briques.remove(brique)
        
        if pos[0]-11 <= pos_balle.x <= pos[0]-9 and pos[1]+0 <= pos_balle.y <= pos[1]+40 :
            if pos in pos_briques :
                pos_briques.remove(pos)
                briques.remove(brique)
                dx_balle = -1*dx_balle

        if pos[0]+59 <= pos_balle.x <= pos[0]+61 and pos[1]+0 <= pos_balle.y <= pos[1]+40 :
            if pos in pos_briques :
                pos_briques.remove(pos)
                briques.remove(brique)   
                dx_balle = -1*dx_balle
  
    if len(pos_briques) == 0 :
        gagner()
        pos_balle = balle.get_rect()
        pos_balle = fenetre.blit(balle, (220,560+dy_balle))
        dx_balle = 0
        dy_balle = 5
        #deplacement de la balle resultant de l'addition des composantes de dx_balle et de dy_balle
        pos_balle = pos_balle.move(dx_balle,dy_balle)

        pos_briques = [(70,50),(70,110),(70,170),(70,230),(70,290),(70,350),
                       (140,200),(210,170),(210,230),(280,110),(280,290),(350,50),(350,350)]
        briques = list()
        for pos in pos_briques :
            brique = pygame.image.load(BRIQUE).convert_alpha()
            briques.append(brique)
            fenetre.blit(brique, pos)

        pos_raquette = raquette.get_rect()
        pos_raquette = fenetre.blit(raquette, (180,600))
        
    #re-collage
    fenetre.blit(fond, (0,0))
    for brique in briques :
        pos = pos_briques[briques.index(brique)]
        fenetre.blit(brique, pos)

    fenetre.blit(raquette, pos_raquette)
    fenetre.blit(balle, pos_balle)
    #rafraichissement
    pygame.display.flip()

