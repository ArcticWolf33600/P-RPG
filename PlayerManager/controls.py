import pygame
from GameManager import *
window_heigth = 600
window_width = 1000



def player_movements(character):
    keys_pressed = pygame.key.get_pressed()
    player_sprites = {
        "droite" : pygame.transform.scale(pygame.image.load(os.path.join("Assets","Characters", "chevalier.png")), (character.width, character.heigth)),
        "gauche" : pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join("Assets","Characters", "chevalier.png")), (character.width, character.heigth)),True,False)
    }

#    tile = WORLD_OBJECTS[character.hitbox.x][character.hitbox.y]

    if keys_pressed[pygame.K_z] and character.hitbox.y > 0 and not collide(character):  # haut
        character.hitbox.y -= character.speed
    if keys_pressed[pygame.K_q] and character.hitbox.x > 0:  # gauche
        character.hitbox.x -= character.speed
        character.sprite = player_sprites["gauche"]
    if (keys_pressed[pygame.K_s] and character.hitbox.y < window_heigth - character.heigth):  # bas
        character.hitbox.y += character.speed
    if (keys_pressed[pygame.K_d] and character.hitbox.x < window_width - character.width):  # droite
        character.hitbox.x += character.speed
        character.sprite = player_sprites["droite"]

def collide(character):
    for row in WORLD_OBJECTS:
        for elem in row:
            if character.hitbox.colliderect(elem.hitbox):
                return True
    return False
        