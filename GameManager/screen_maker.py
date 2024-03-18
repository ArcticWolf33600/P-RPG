import pygame
from .levels import *
from .tile import *
# from EnemyManager import *

screen = pygame.display.set_mode((window_width, window_heigth)) # crée l'écran

def draw_world(player,WORLD,ENEMIES_S,ENEMIES_SE): 
    """affiche le monde""" 
    background = pygame.transform.scale(pygame.image.load(os.path.join("Assets","Environment","background_grid.png")),(window_width, window_heigth)) # background
    screen.blit(background,(0,0))
    if player.attack:
        WORLD_SW = WORLD_SW_OPEN
    else:
        WORLD_SW = [ 
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','.','.','.','.','.','.','.','.','cua','.','.','.','.','.','.','.','.','.','.'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X']
]
    if len(ENEMIES_S) == 0 and len(ENEMIES_SE)==0:
        WORLD_E = WORLD_E_DEFEATED
    else:
        WORLD_E = [ 
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','ch','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X']
]
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

def draw_character(character):
    """affiche le personnage"""
    screen.blit(character.sprite, (character.hitbox.x, character.hitbox.y))  # elements après
    
def HUD(character,world):
    """affiche le hud"""
    heart = pygame.image.load(os.path.join("Assets","Characters", "heart.png")).convert_alpha()
    heart = pygame.transform.scale(heart, (30, 30))
    for k in range(character.health):
        screen.blit(heart,(10 + k*30,20))
    
    if world == "SW":
        
        pygame.font.init()
        my_font = pygame.font.SysFont('Comic Sans MS', 20)
        text_surface = my_font.render('Déplacements : Z,Q,S,D', False, (0, 0, 0))
        screen.blit(text_surface, (60,100))
        text_surface = my_font.render('Attaquer : flèches', False, (0, 0, 0))
        screen.blit(text_surface, (800,100))
        text_surface = my_font.render('Utiliser : Espace', False, (0, 0, 0))
        screen.blit(text_surface, (400,360))

    if character.attack == True:    
        pygame.draw.rect(screen, (124,124,124), pygame.Rect(880, 450, 100, 100))
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(890, 460, 80, 80))
        attack_type_string = character.attack_type + "_slash.png"
        attack = pygame.transform.scale(pygame.image.load(os.path.join("Assets","Characters", attack_type_string)),(80,80))
        screen.blit(attack, (890, 460))