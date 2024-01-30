import pygame
from .niveau import *
from .tile import *


screen = pygame.display.set_mode((window_width, window_heigth))

# def draw_world():
#     background = pygame.transform.scale(pygame.image.load(os.path.join("Assets","background_grille.png")),(window_width, window_heigth)) # background
#     screen.blit(background,(0,0))
#     for row in WORLD_OBJECTS:
#         for elem in row:
#             if elem.type != '.':
#                 screen.blit(elem.sprite,(elem.hitbox.y,elem.hitbox.x)) #affiche l'élément de premier plan du niveau à la case donnée 

def draw_world():
    background = pygame.transform.scale(pygame.image.load(os.path.join("Assets","background_grille.png")),(window_width, window_heigth)) # background
    screen.blit(background,(0,0))
    for elem in WORLD_OBJECTS:
        if elem.type != '.':
            screen.blit(elem.sprite,(elem.hitbox.y,elem.hitbox.x)) #affiche l'élément de premier plan du niveau à la case donnée 

def draw_character(character):
    screen.blit(character.sprite, (character.hitbox.x, character.hitbox.y))  # elements après
    
