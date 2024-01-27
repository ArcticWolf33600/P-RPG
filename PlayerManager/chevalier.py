import os
import pygame


class Chevalier:
    def __init__(self):
        self.width = 50
        self.heigth = 50
        self.sprite_import = pygame.image.load(os.path.join("Assets", "chevalier.png"))
        self.sprite = pygame.transform.scale(
            self.sprite_import, (self.width, self.heigth)
        )
        self.hitbox = pygame.Rect(50, 550, self.width, self.heigth)
        self.speed = 5
