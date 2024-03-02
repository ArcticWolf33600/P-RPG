import pygame
from GameManager import *

def player_movements(character): # gère les déplacements du personnage
    keys_pressed = pygame.key.get_pressed()
    
    if character.classe == "Knight":
        player_sprites = {
            "right" : pygame.transform.scale(pygame.image.load(os.path.join("Assets","Characters", "knight.png")), (character.width, character.heigth)),
            "left" : pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join("Assets","Characters", "knight.png")), (character.width, character.heigth)),True,False)
        }
    else:
        player_sprites = {
            "right" : pygame.transform.scale(pygame.image.load(os.path.join("Assets","Characters", "wizard.png")), (character.width, character.heigth)),
            "left" : pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join("Assets","Characters", "wizard.png")), (character.width, character.heigth)),True,False)
        }

    if keys_pressed[pygame.K_z] and not collide_player(character):  # haut
        character.hitbox.y -= character.speed
    elif (keys_pressed[pygame.K_z] and collide_player(character)):
        character.hitbox.y += 10
        
    if keys_pressed[pygame.K_q] and not collide_player(character):  # gauche
        character.hitbox.x -= character.speed
        character.sprite = player_sprites["left"]
    elif (keys_pressed[pygame.K_q] and collide_player(character)):
        character.hitbox.x +=10

    if (keys_pressed[pygame.K_s] and not collide_player(character)):  # bas
        character.hitbox.y += character.speed
    elif (keys_pressed[pygame.K_s] and collide_player(character)):
        character.hitbox.y -=10

    if (keys_pressed[pygame.K_d] and not collide_player(character)):  # droite
        character.hitbox.x += character.speed
        character.sprite = player_sprites["right"]
    elif (keys_pressed[pygame.K_d] and collide_player(character)):
        character.hitbox.x -=10

def collide_player(character): # détermine si le personnage rentre en collision avec un objet
    for elem in WORLD_OBJECTS:
        if character.hitbox.colliderect(elem.hitbox):
            collide_sfx = os.path.join("Assets","SFX","collision.mp3")
            collide_sfx = pygame.mixer.Sound(collide_sfx)
            pygame.mixer.Channel(1).play(collide_sfx,loops=0)
            return True
    return False
        