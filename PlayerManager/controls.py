import pygame
from GameManager import *

def player_movements(character): # gère les déplacements du personnage
    keys_pressed = pygame.key.get_pressed()
    player_sprites = {
        "droite" : pygame.transform.scale(pygame.image.load(os.path.join("Assets","Characters", "chevalier.png")), (character.width, character.heigth)),
        "gauche" : pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join("Assets","Characters", "chevalier.png")), (character.width, character.heigth)),True,False)
    }

    if keys_pressed[pygame.K_z] and not collide_player(character):  # haut
        character.hitbox.y -= character.speed
    elif (keys_pressed[pygame.K_z] and collide_player(character)):
        character.hitbox.y += 10
        
    if keys_pressed[pygame.K_q] and not collide_player(character):  # gauche
        character.hitbox.x -= character.speed
        character.sprite = player_sprites["gauche"]
    elif (keys_pressed[pygame.K_q] and collide_player(character)):
        character.hitbox.x +=10

    if (keys_pressed[pygame.K_s] and not collide_player(character)):  # bas
        character.hitbox.y += character.speed
    elif (keys_pressed[pygame.K_s] and collide_player(character)):
        character.hitbox.y -=10

    if (keys_pressed[pygame.K_d] and not collide_player(character)):  # droite
        character.hitbox.x += character.speed
        character.sprite = player_sprites["droite"]
    elif (keys_pressed[pygame.K_d] and collide_player(character)):
        character.hitbox.x -=10

def collide_player(character): # détermine si le personnage rentre en collision avec un objet
    for elem in WORLD_OBJECTS:
        if character.hitbox.colliderect(elem.hitbox):
            return True
    return False
        