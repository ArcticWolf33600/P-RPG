from GameManager import *
from math import *


def enemy_move_to_player(enemy,player):
    if not (abs(enemy.hitbox.x - player.hitbox.x) > 60 and abs(enemy.hitbox.y - player.hitbox.y) > 60 and not collide_enemy(enemy)): # l'ennemi est proche du joueur et se rapproche de lui
        if enemy.hitbox.x > player.hitbox.x and not collide_enemy(enemy): enemy.hitbox.x -= enemy.speed
        if(collide_enemy(enemy)): enemy.hitbox.x += 5
        if enemy.hitbox.x < player.hitbox.x and not collide_enemy(enemy): enemy.hitbox.x += enemy.speed
        if(collide_enemy(enemy)): enemy.hitbox.x -= 5
        if enemy.hitbox.y > player.hitbox.y and not collide_enemy(enemy): enemy.hitbox.y -= enemy.speed
        if(collide_enemy(enemy)): enemy.hitbox.y += 5
        if enemy.hitbox.y < player.hitbox.y and not collide_enemy(enemy): enemy.hitbox.y += enemy.speed
        if(collide_enemy(enemy)): enemy.hitbox.y -= 5
    
def collide_enemy(character): # détermine si le personnage rentre en collision avec un objet
    for elem in WORLD_OBJECTS:
        if character.hitbox.colliderect(elem.hitbox):
            return True
    return False