import os
import pygame

class Character(object): # classe parente de tous les types de personnages
    def __init__(self):
        self.width = 50
        self.heigth = 50
        self.speed = 5
        self.hitbox = pygame.Rect(350, 350, self.width, self.heigth)

class Chevalier(Character):
    def __init__(self):
        super().__init__()
        self.sprite_import = pygame.image.load(os.path.join("Assets","Characters", "chevalier.png"))
        self.sprite = pygame.transform.scale(self.sprite_import, (self.width, self.heigth))

class Magicien(Character):
    def __init__(self):
        super().__init__()
        pass
        
