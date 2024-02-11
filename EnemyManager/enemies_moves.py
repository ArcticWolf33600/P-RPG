from GameManager import *

def enemy_move_to_player(enemy,player):
    if enemy.hitbox.x > player.hitbox.x and not collide_enemy(enemy): enemy.hitbox.x -= enemy.speed
    elif(collide_enemy(enemy)): enemy.hitbox.x += 5
    if enemy.hitbox.x < player.hitbox.x and not collide_enemy(enemy): enemy.hitbox.x += enemy.speed
    elif(collide_enemy(enemy)): enemy.hitbox.x += 5
    if enemy.hitbox.y > player.hitbox.y and not collide_enemy(enemy): enemy.hitbox.y -= enemy.speed
    elif(collide_enemy(enemy)): enemy.hitbox.x += 5
    if enemy.hitbox.y < player.hitbox.y and not collide_enemy(enemy): enemy.hitbox.y += enemy.speed
    elif(collide_enemy(enemy)): enemy.hitbox.x += 5
    
def collide_enemy(character): # détermine si le personnage rentre en collision avec un objet
    for elem in WORLD_OBJECTS:
        if character.hitbox.colliderect(elem.hitbox):
            return True
    return False