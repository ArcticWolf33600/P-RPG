import os
import pygame

class Character(object):
    """classe parente de tous les types de personnages"""
    def __init__(self):
        self.width = 50
        self.heigth = 50
        self.speed = 10
        self.hitbox = pygame.Rect(350, 350, self.width, self.heigth)
        self.attack_type = "normal"
        self.health = 10
        self.attack = False

class Knight(Character):
    def __init__(self):
        super().__init__()
        self.strength = 10
        self.range = 0
        self.sprite_import = pygame.image.load(os.path.join("Assets","Characters", "knight.png")).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite_import, (self.width, self.heigth))
        self.classe = "Knight"

class Wizard(Character):
    def __init__(self):
        super().__init__()
        self.strength = 5
        self.range = 40
        self.sprite_import = pygame.image.load(os.path.join("Assets","Characters", "wizard.png")).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite_import, (self.width, self.heigth))
        self.classe = "Wizard"  

