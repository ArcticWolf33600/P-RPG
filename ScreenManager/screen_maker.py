import pygame
import os
from .niveau import *


screen = pygame.display.set_mode((window_width, window_heigth))
background_import = pygame.image.load(os.path.join("Assets", "background.png"))
background = pygame.transform.scale(background_import, (window_width, window_heigth))



def draw_world():
    screen.blit(background, (0, 0))  # background toujours en premier
    for x in range(len(WORLD)):
        for y in range(len(WORLD[0])):
            tuile = WORLD[x][y]
            if tuile == 'X':
                tuile_image = sprites[tuile]
                screen.blit(tuile_image,(y*60,x*60))

                
                

def draw_characters(hitbox_chevalier, chevalier):
    screen.blit(chevalier, (hitbox_chevalier.x, hitbox_chevalier.y))  # elements après
    pygame.display.flip()
