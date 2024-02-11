import pygame
import os

class Tile(object): # objet tuile : prend la forme du sprite selon son type saisi 
    def __init__(self,posX,posY,tile_type):
        self.x = posX
        self.y = posY
        self.type = tile_type
        
        match tile_type:
            case 'X':
                sprite_import = pygame.image.load(os.path.join("Assets","Environment","rocher.png"))
                self.sprite = pygame.transform.scale(sprite_import,(50, 50)) 
                self.hitbox = pygame.Rect(self.y*50,self.x*50,50,50)
            case 'a':
                sprite_import = pygame.image.load(os.path.join("Assets","Environment","arbre.png"))
                self.sprite = pygame.transform.scale(sprite_import,(200, 200)) 
                self.hitbox = pygame.Rect(self.y*50,self.x*50,200,200)
            case 'rp':
                sprite_import = pygame.image.load(os.path.join("Assets","Environment","rocher_pointu.png"))
                self.sprite = pygame.transform.scale(sprite_import,(50, 150)) 
                self.hitbox = pygame.Rect(self.y*50,self.x*50,50,150)
            case 'fo':
                sprite_import = pygame.image.load(os.path.join("Assets","Environment","fleur_orange.png"))
                self.sprite = pygame.transform.scale(sprite_import,(50, 50)) 
                self.hitbox = pygame.Rect(self.y*50,self.x*50,0,0)
            case 'fb':
                sprite_import = pygame.image.load(os.path.join("Assets","Environment","fleurs_blanches.png"))
                self.sprite = pygame.transform.scale(sprite_import,(50, 50)) 
                self.hitbox = pygame.Rect(self.y*50,self.x*50,0,0)
            case _:
                sprite_import = pygame.image.load(os.path.join("Assets","Environment","herbe.png"))
                self.sprite = pygame.transform.scale(sprite_import,(0, 0)) # . = rien
                self.hitbox = pygame.Rect(0,0,0,0)

            