import pygame
from .niveau import *
from .tile import *

screen = pygame.display.set_mode((window_width, window_heigth)) # crée l'écran
def draw_world(): #affiche le monde 
    background = pygame.transform.scale(pygame.image.load(os.path.join("Assets","background_grille.png")),(window_width, window_heigth)) # background
    screen.blit(background,(0,0))
    for elem in WORLD_OBJECTS:
        if elem.type != '.':
            screen.blit(elem.sprite,(elem.hitbox.x,elem.hitbox.y)) #affiche l'élément de premier plan du niveau à la case donnée 
            rect_Surface = pygame.Surface((50,50)) #debuggage hitbox
            rect_Surface.fill((255,0,0))
            screen.blit(rect_Surface,elem.hitbox)
def draw_character(character): # affiche le personnage
    screen.blit(character.sprite, (character.hitbox.x, character.hitbox.y))  # elements après
    
