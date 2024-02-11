from GameManager import *
from math import *
import random



def enemy_move_to_player(enemy,player):
    if abs(enemy.hitbox.x - player.hitbox.x) > 40 and abs(enemy.hitbox.y - player.hitbox.y) > 40 and not collide_enemy(enemy): # si le joueur est trop éloigné, on se balade aléatoirement
        enemy.hitbox.x += enemy.speed * random.choice([-1,1]) #gauche ou droite aléatoirement
        enemy.hitbox.y += enemy.speed * random.choice([-1,1]) #bas ou haut aléatoirement
        
    else: #l'ennemi est proche du joueur et se rapproche de lui
        if enemy.hitbox.x > player.hitbox.x and not collide_enemy(enemy): enemy.hitbox.x -= enemy.speed
        elif(collide_enemy(enemy)): enemy.hitbox.x += 5
        if enemy.hitbox.x < player.hitbox.x and not collide_enemy(enemy): enemy.hitbox.x += enemy.speed
        elif(collide_enemy(enemy)): enemy.hitbox.x -= 5
        if enemy.hitbox.y > player.hitbox.y and not collide_enemy(enemy): enemy.hitbox.y -= enemy.speed
        elif(collide_enemy(enemy)): enemy.hitbox.y += 5
        if enemy.hitbox.y < player.hitbox.y and not collide_enemy(enemy): enemy.hitbox.y += enemy.speed
        elif(collide_enemy(enemy)): enemy.hitbox.y -= 5
    
def collide_enemy(character): # détermine si le personnage rentre en collision avec un objet
    for elem in WORLD_OBJECTS:
        if character.hitbox.colliderect(elem.hitbox):
            return True
    return False