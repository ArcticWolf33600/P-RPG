from GameManager import *
from math import *
from PlayerManager import *

def enemy_moves_to_player(enemy,player,attack):
    if not (abs(enemy.hitbox.x - player.hitbox.x) > 60 and abs(enemy.hitbox.y - player.hitbox.y) > 60 and not collide_enemy(enemy)): # l'ennemi est proche du joueur et se rapproche de lui
        if enemy.hitbox.x > player.hitbox.x and not collide_enemy(enemy): enemy.hitbox.x -= enemy.speed
        if(collide_enemy(enemy)): enemy.hitbox.x += 5
        if enemy.hitbox.x < player.hitbox.x and not collide_enemy(enemy): enemy.hitbox.x += enemy.speed
        if(collide_enemy(enemy)): enemy.hitbox.x -= 5
        if enemy.hitbox.y > player.hitbox.y and not collide_enemy(enemy): enemy.hitbox.y -= enemy.speed
        if(collide_enemy(enemy)): enemy.hitbox.y += 5
        if enemy.hitbox.y < player.hitbox.y and not collide_enemy(enemy): enemy.hitbox.y += enemy.speed
        if(collide_enemy(enemy)): enemy.hitbox.y -= 5
        
        if collide_attack(enemy,attack):
            enemy.hitbox.x -= 20
            enemy.health -= 0.5
            enemy_hurt_sound = os.path.join("Assets","SFX","enemy_hurt.mp3")
            enemy_hurt_sound = pygame.mixer.Sound(enemy_hurt_sound)
            pygame.mixer.Channel(3).play(enemy_hurt_sound,loops=0)

            
def collide_attack(character,attack):
    if character.hitbox.colliderect(attack):
        return True
    return False
def collide_enemy(character): # détermine si le personnage rentre en collision avec un objet
    for elem in WORLD_OBJECTS:
        if character.hitbox.colliderect(elem.hitbox):
            return True
    return False

def enemy_management(ENEMIES, player,attack):
    for enemy in ENEMIES: # gestion des ennemis (affichage + déplacements)
        draw_character(enemy)
        enemy_moves_to_player(enemy,player,attack)
        check_attack_ennemy_to_player(enemy,player)
        if enemy.health<0:
            ENEMIES.pop(ENEMIES.index(enemy))