import pygame
from GameManager import *

def player_movements(character):
    """gère les déplacements du personnage"""
    
    player_sprites = {
        "Knight" : {
            "right" : pygame.transform.scale(pygame.image.load(os.path.join("Assets","Characters", "knight.png")), (character.width, character.heigth)),
            "left" : pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join("Assets","Characters", "knight.png")), (character.width, character.heigth)),True,False)
        },
        "Wizard": {
            "right" : pygame.transform.scale(pygame.image.load(os.path.join("Assets","Characters", "wizard.png")), (character.width, character.heigth)),
            "left" : pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join("Assets","Characters", "wizard.png")), (character.width, character.heigth)),True,False)
        }
    }
    
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_z] and not collide_player(character):  # haut
        character.hitbox.y -= character.speed
    elif (keys_pressed[pygame.K_z] and collide_player(character)):
        character.hitbox.y += 10
        
    if keys_pressed[pygame.K_q] and not collide_player(character):  # gauche
        character.hitbox.x -= character.speed
        character.sprite = player_sprites[character.classe]["left"]
    elif (keys_pressed[pygame.K_q] and collide_player(character)):
        character.hitbox.x +=10

    if (keys_pressed[pygame.K_s] and not collide_player(character)):  # bas
        character.hitbox.y += character.speed
    elif (keys_pressed[pygame.K_s] and collide_player(character)):
        character.hitbox.y -=10

    if (keys_pressed[pygame.K_d] and not collide_player(character)):  # droite
        character.hitbox.x += character.speed
        character.sprite = player_sprites[character.classe]["right"]
    elif (keys_pressed[pygame.K_d] and collide_player(character)):
        character.hitbox.x -=10
    
    if (keys_pressed[pygame.K_SPACE]):
        openable(character)

def player_attack_sound(player):
    """effectue le son d'attaque"""
    if player.attack == True:
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_DOWN]: 
            attack = os.path.join("Assets","SFX","attack.mp3")
            attack = pygame.mixer.Sound(attack)
            pygame.mixer.Channel(2).play(attack,loops=0)
    
def player_attack(character):
    """crée une zone à l'endroit de l'attaque du joueur et anime l'attaque"""
    ATTACK_HITBOX = pygame.Rect(0, 0, 0, 0)
    if character.attack == True:
        if character.classe == "Knight":
            attack_type_string = character.attack_type + "_slash.png"
            attack_sprites = {
                "right" : pygame.image.load(os.path.join("Assets","Characters", attack_type_string)),
                "left" : pygame.transform.flip(pygame.image.load(os.path.join("Assets","Characters", attack_type_string)),True,False),
                "up" : pygame.transform.rotate(pygame.image.load(os.path.join("Assets","Characters", attack_type_string)),90),
                "down" : pygame.transform.rotate(pygame.image.load(os.path.join("Assets","Characters", attack_type_string)),-90)
            }
        else : 
            attack_type_string = character.attack_type + "_fireball.png"
            attack_sprites = {
                "right" : pygame.image.load(os.path.join("Assets","Characters", attack_type_string)),
                "left" : pygame.transform.flip(pygame.image.load(os.path.join("Assets","Characters", attack_type_string)),True,False),
                "up" : pygame.transform.rotate(pygame.image.load(os.path.join("Assets","Characters", attack_type_string)),90),
                "down" : pygame.transform.rotate(pygame.image.load(os.path.join("Assets","Characters", attack_type_string)),-90)
            }
        
        keys_pressed = pygame.key.get_pressed()
        
        if keys_pressed [pygame.K_RIGHT]:
            attack = attack_sprites["right"]
            ATTACK_HITBOX = pygame.Rect(30+character.hitbox.x+20+character.range, character.hitbox.y, 60, 60)
            screen.blit(attack, (character.hitbox.x+20+character.range, character.hitbox.y))
        if keys_pressed [pygame.K_LEFT]:
            attack = attack_sprites["left"]
            ATTACK_HITBOX = pygame.Rect(character.hitbox.x-60-character.range, character.hitbox.y, 60, 60)
            screen.blit(attack, (character.hitbox.x-60-character.range, character.hitbox.y))
        if keys_pressed [pygame.K_UP]:
            attack = attack_sprites["up"]
            ATTACK_HITBOX = pygame.Rect(character.hitbox.x, character.hitbox.y-60-character.range, 60, 60)
            screen.blit(attack, (character.hitbox.x, character.hitbox.y-60-character.range))        
        if keys_pressed [pygame.K_DOWN]:
            attack = attack_sprites["down"]
            ATTACK_HITBOX = pygame.Rect(character.hitbox.x, character.hitbox.y+20+character.range+30, 60, 60)
            screen.blit(attack, (character.hitbox.x, character.hitbox.y+20+character.range))
    
    return ATTACK_HITBOX
    
def collide_player(character):
    """détermine si le personnage rentre en collision avec un objet"""
    for elem in WORLD_OBJECTS:
        if character.hitbox.colliderect(elem.hitbox):
            collide_sfx = os.path.join("Assets","SFX","collision.mp3")
            collide_sfx = pygame.mixer.Sound(collide_sfx)
            pygame.mixer.Channel(1).play(collide_sfx,loops=0)
            return True
    return False

def check_attack_ennemy_to_player(enemy,player):
    """retire de la vie si le joueur entre en collision avec l'ennemi"""
    if enemy.hitbox.colliderect(player.hitbox):
        player.health -= 1
        player.hitbox.x += 20
        
def openable(character): 
    """détermine si on peut interagir avec l'objet"""
    for elem in WORLD_OBJECTS:
        if character.hitbox.colliderect(elem.hitbox) and elem.interactable == True :
            if elem.loot == "unlock":
                character.attack = True
            elif elem.loot== "buff":
                character.attack_type="strong"
                character.strength += 5
            elif elem.loot == "heal":
                character.health = 10
            WORLD_OBJECTS.pop(WORLD_OBJECTS.index(elem))
            