import pygame
from .niveau import *
from .tile import *

screen = pygame.display.set_mode((window_width, window_heigth)) # crée l'écran

def draw_world(player,WORLD): #affiche le monde 
    background = pygame.transform.scale(pygame.image.load(os.path.join("Assets","background_grille.png")),(window_width, window_heigth)) # background
    screen.blit(background,(0,0))
    
    if player.hitbox.y < 0 and WORLD == "WORLD_INIT":
        WORLD = "JARDIN"    
        choose_world(WORLD_JARDIN)
        player.hitbox.x = window_width/2
        player.hitbox.y = window_heigth-60    
    
    elif player.hitbox.y > window_heigth and WORLD == "JARDIN":
        WORLD = "WORLD_INIT"
        choose_world(WORLD1)
        player.hitbox.x = window_width/2
        player.hitbox.y = 0
        
    for elem in WORLD_OBJECTS:
        if elem.type != '.':
            screen.blit(elem.sprite,(elem.hitbox.x,elem.hitbox.y)) #affiche l'élément de premier plan du niveau à la case donnée 
            # ======= debuggage hitbox =======
            # rect_Surface = pygame.Surface((50,50)) 
            # rect_Surface.fill((255,0,0))
            # screen.blit(rect_Surface,elem.hitbox)
            # ================================

    return WORLD

def draw_character(character): # affiche le personnage
    screen.blit(character.sprite, (character.hitbox.x, character.hitbox.y))  # elements après
    
