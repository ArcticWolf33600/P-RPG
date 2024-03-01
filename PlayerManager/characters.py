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
        self.force = 10
        self.portee = 1
        self.sprite_import = pygame.image.load(os.path.join("Assets","Characters", "chevalier.png")).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite_import, (self.width, self.heigth))
        self.classe = "Chevalier"

class Mage(Character):
    def __init__(self):
        super().__init__()
        self.force = 5
        self.portee = 5
        self.sprite_import = pygame.image.load(os.path.join("Assets","Characters", "mage.png")).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite_import, (self.width, self.heigth))
        self.classe = "Mage"

