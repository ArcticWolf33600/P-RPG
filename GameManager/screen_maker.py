import pygame
from .levels import *
from .tile import *

screen = pygame.display.set_mode((window_width, window_heigth)) # crée l'écran

def draw_world(player,WORLD): #affiche le monde 
    background = pygame.transform.scale(pygame.image.load(os.path.join("Assets","Environment","background_grid.png")),(window_width, window_heigth)) # background
    screen.blit(background,(0,0))
        
    if WORLD == "SW":
        if player.hitbox.x > window_width: #sud-est vers sud
            WORLD = "S"
            choose_world(WORLD_S)
            player.hitbox.x = 60
            player.hitbox.y = window_heigth/2  
    
    elif WORLD == "S":
        if player.hitbox.x < 0: #sud vers sud-ouest
            WORLD = "SW"
            choose_world(WORLD_SW)
            player.hitbox.x = window_width-60
            player.hitbox.y = window_heigth/2
        
        if player.hitbox.x > window_width: #sud vers sud-est
            WORLD = "SE"
            choose_world(WORLD_SE)
            player.hitbox.x = 60
            player.hitbox.y = window_heigth/2
    
    elif WORLD == "SE":
        if player.hitbox.x < 0: # sud-est vers sud
            WORLD = "S"
            choose_world(WORLD_S)
            player.hitbox.x = window_width-60
            player.hitbox.y = window_heigth/2
        
        if player.hitbox.y < 0: #sud-est vers est
            WORLD = "E"
            choose_world(WORLD_E)
            player.hitbox.x = window_width/2
            player.hitbox.y = window_heigth-60
    
    elif WORLD == "E":
        if player.hitbox.y > window_heigth : # est vers sud-est
            WORLD = "SE"
            choose_world(WORLD_SE)
            player.hitbox.x = window_width/2
            player.hitbox.y = 0
                
        if player.hitbox.y < 0 : #est vers nord-est
            WORLD = "NE"
            choose_world(WORLD_NE)
            player.hitbox.x = window_width/2
            player.hitbox.y = window_heigth - 60
    
    elif  WORLD == "NE":
        if player.hitbox.y > window_heigth: #nord-est vers est
            WORLD = "E" 
            choose_world(WORLD_E)
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
    
def HUD(character):
    heart = pygame.image.load(os.path.join("Assets","Characters", "heart.png")).convert_alpha()
    heart = pygame.transform.scale(heart, (30, 30))
    for k in range(character.health):
        screen.blit(heart,(10 + k*30,20))