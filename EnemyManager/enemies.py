import pygame
import os

class Enemy(object): 
    """classe parente de tous les types d'ennemis"""
    def __init__(self,posx,posy):
        self.width = 50
        self.heigth = 50

        self.hitbox = pygame.Rect(posx, posy, self.width, self.heigth)

class Skeleton(Enemy):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.sprite_import = pygame.image.load(os.path.join("Assets","Enemies", "Skeleton.png")).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite_import, (self.width, self.heigth))
        self.speed = 2
        self.health = 3
        
class Gobelin(Enemy):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.sprite_import = pygame.image.load(os.path.join("Assets","Enemies", "Gobelin.png")).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite_import, (self.width, self.heigth))
        self.speed = 3
        self.health = 6

class Boss(object): 
    """classe du boss"""
    def __init__(self,posx,posy):
        self.width = 200
        self.heigth = 200
        self.hitbox = pygame.Rect(posx, posy, self.width, self.heigth)
        self.sprite_import = pygame.image.load(os.path.join("Assets","Enemies", "Boss.png")).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite_import, (self.width, self.heigth))
        self.speed = 2
        self.health = 25
        

