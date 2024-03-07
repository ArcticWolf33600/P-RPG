import pygame
from .levels import *
from .tile import *

screen = pygame.display.set_mode((window_width, window_heigth)) # crée l'écran

def draw_world(player,WORLD): #affiche le monde 
    background = pygame.transform.scale(pygame.image.load(os.path.join("Assets","Environment","background_grid.png")),(window_width, window_heigth)) # background
    screen.blit(background,(0,0))
    
    if player.hitbox.y < 0 and WORLD == "MIDDLE": #milieu vers le nord
        WORLD = "N"    
        choose_world(WORLD_N)
        player.hitbox.x = window_width/2
        player.hitbox.y = window_heigth-60    
    
    elif player.hitbox.y > window_heigth and WORLD == "N": #nord vers le milieu
        WORLD = "MIDDLE"
        choose_world(WORLD_MIDDLE)
        player.hitbox.x = window_width/2
        player.hitbox.y = 0
    
    elif player.hitbox.y > window_heigth and WORLD == "MIDDLE": #milieu vers le sud
        WORLD = "S"
        choose_world(WORLD_S)
        player.hitbox.x = window_width/2
        player.hitbox.y = 0
    
    elif player.hitbox.y < 0 and WORLD == "S": #sud vers milieu
        WORLD = "MIDDLE"
        choose_world(WORLD_MIDDLE)
        player.hitbox.x = window_width/2
        player.hitbox.y = window_heigth-60  
        
        
        
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
    
def HUD(character):
    heart = pygame.image.load(os.path.join("Assets","Characters", "heart.png")).convert_alpha()
    heart = pygame.transform.scale(heart, (30, 30))
    for k in range(character.health):
        screen.blit(heart,(10 + k*30,20))