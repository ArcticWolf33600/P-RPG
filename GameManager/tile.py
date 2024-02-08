import pygame
import os

class Tile(object): # objet tuile : prend la forme du sprite selon son type saisi 
    def __init__(self,posX,posY,tile_type):
        self.x = posX
        self.y = posY
        self.type = tile_type
        
        if tile_type=='X':
            sprite_import = pygame.image.load(os.path.join("Assets","Environment","rocher.png"))
            self.sprite = pygame.transform.scale(sprite_import,(50, 50)) #X = rocher
            self.hitbox = pygame.Rect(self.y*50,self.x*50,50,50)
        elif tile_type =='.':
            sprite_import = pygame.image.load(os.path.join("Assets","Environment","herbe.png"))
            self.sprite = pygame.transform.scale(sprite_import,(0, 0)) #. = rien
            self.hitbox = pygame.Rect(0,0,0,0)
        elif tile_type == 'a':
            sprite_import = pygame.image.load(os.path.join("Assets","Environment","arbre.png"))
            self.sprite = pygame.transform.scale(sprite_import,(200, 200)) #a = arbre
            self.hitbox = pygame.Rect(self.y*50,self.x*50,200,200)
