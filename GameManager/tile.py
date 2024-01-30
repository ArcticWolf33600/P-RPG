import pygame
import os

class Tile(object): # objet tuile : prend la forme du sprite selon son type saisi 
    def __init__(self,posX,posY,tile_type):
        self.x = posX
        self.y = posY
        self.type = tile_type
        
        if tile_type=='X':
            self.sprite = pygame.transform.scale(pygame.image.load(os.path.join("Assets","Environment","rocher.png")),(50, 50)) #X = rocher
            self.hitbox = pygame.Rect(self.x*50,self.y*50,50,50)
        elif tile_type =='.':
            self.sprite = pygame.transform.scale(pygame.image.load(os.path.join("Assets","Environment","herbe.png")),(0, 0)) #. = rien
            self.hitbox = pygame.Rect(0,0,0,0)
        elif tile_type == 'a':
            self.sprite = pygame.transform.scale(pygame.image.load(os.path.join("Assets","Environment","arbre.png")),(200, 200)) #. = herbe
            self.hitbox = pygame.Rect(self.x*50,self.y*50,200,200)
