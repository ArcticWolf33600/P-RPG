import pygame
import os
from .levels import *
from .screen_maker import *
from PlayerManager.characters import *

def main_menu(): #menu affiché au démarrage du jeu
    pygame.font.init() 
    screen.fill((0,0,0))
    PRPG = pygame.image.load(os.path.join("Assets","PRPG.png")).convert_alpha()
    PRPG = pygame.transform.scale(PRPG, (window_width, window_heigth))
    PRPG.set_alpha(1)
    screen.blit(PRPG, (0,0))
    
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render('Quel personnage souhaitez-vous incarner ?', False, (255, 255, 0))
    screen.blit(text_surface, (window_width/5.5,20))
            
    text_surface = my_font.render('Chevalier : appuyez sur "q"', False, (255, 255, 0))
    screen.blit(text_surface, (100,420))
            
    text_surface = my_font.render('Mage : appuyez sur "d"', False, (255, 255, 0))
    screen.blit(text_surface, (600,420))
            
    chevalier = pygame.image.load(os.path.join("Assets","Characters", "knight.png")).convert_alpha()
    chevalier = pygame.transform.scale(chevalier, (200, 200))
    screen.blit(chevalier, (200,120))  
            
    mage = pygame.image.load(os.path.join("Assets","Characters", "wizard.png")).convert_alpha()
    mage = pygame.transform.scale(mage, (200, 200))
    screen.blit(mage, (600,120))
            
    fleche = pygame.image.load(os.path.join("Assets","arrow.png")).convert_alpha()
    fleche = pygame.transform.scale(fleche, (100, 100))
    fleche = pygame.transform.rotate(fleche,90)
            
    text_surface = my_font.render('Pour valider, appuyez sur "Espace"', False, (255, 255, 0))
    screen.blit(text_surface, (250,500))
            
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_q]:
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(650, 320, 100, 100))
        screen.blit(fleche, (250,320))
     
            
    elif keys_pressed[pygame.K_d]:
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(250, 320, 100, 100))
        screen.blit(fleche, (650,320))

def game_over():
    pygame.font.init() 

    screen.fill((0,0,0))

    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render('GAME OVER', False, (255, 255, 0))
    screen.blit(text_surface, (window_width/2 - 100,60))
    
    text_surface = my_font.render('Rejouer : appuyez sur "q"', False, (255, 255, 0))
    screen.blit(text_surface, (100,420))
            
    text_surface = my_font.render('Quitter : appuyez sur "d"', False, (255, 255, 0))
    screen.blit(text_surface, (600,420))
    
    
