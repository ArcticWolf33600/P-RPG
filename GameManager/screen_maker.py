import pygame
from .niveau import *
from .tile import *


screen = pygame.display.set_mode((window_width, window_heigth))

def draw_world():
    for row in WORLD_OBJECTS:
        for elem in row:
            screen.blit(Tile(elem.hitbox.y,elem.hitbox.x,'.').sprite,(elem.hitbox.y,elem.hitbox.x)) #Affiche toujours de l'herbe en fond
            screen.blit(elem.sprite,(elem.hitbox.y,elem.hitbox.x)) #affiche l'élément de premier plan du niveau à la case donnée 
         
def draw_character(character):
    screen.blit(character.sprite, (character.hitbox.x, character.hitbox.y))  # elements après
    
