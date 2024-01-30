import pygame
from GameManager import *
window_heigth = 600
window_width = 1000


def player_movements(character):
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_z] and character.hitbox.y > 0:  # haut
        character.hitbox.y -= character.speed
    if keys_pressed[pygame.K_q] and character.hitbox.x > 0:  # gauche
        character.hitbox.x -= character.speed
    if (keys_pressed[pygame.K_s] and character.hitbox.y < window_heigth - character.heigth):  # bas
        character.hitbox.y += character.speed
    if (keys_pressed[pygame.K_d] and character.hitbox.x < window_width - character.width):  # droite
        character.hitbox.x += character.speed


        