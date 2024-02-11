import pygame
from PlayerManager import *
from GameManager import *
from EnemyManager import *


# pygame setup
pygame.init()
pygame.display.set_caption("P-RPG")

fps = 60

player = Chevalier()  # crée l'objet chevalier affiché à l'écran
skeleton = Skeleton(50,50)
gobelin = Gobelin(200,200)
ENEMIES = [skeleton,gobelin]

def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(fps)  # limite le nombre de fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        draw_world() # affiche le monde
        draw_character(player) # affiche le personnage chevalier
        player_movements(player)  # contrôles du joueur
        
        # for enemy in ENEMIES: # gestion des ennemis (affichage + déplacements)
        #     draw_character(enemy)
        #     enemy_move_to_player(enemy,player)
        
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
