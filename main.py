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
    WORLD = "WORLD_INIT"
    MENU = True

    while running:
        clock.tick(fps)  # limite le nombre de fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if MENU == True: #Menu de sélection du personnage à jouer
            menu_principal()
            
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_q]:
                choix = Chevalier()
            
            elif keys_pressed[pygame.K_d]:
                choix = Mage()
                
            elif keys_pressed[pygame.K_SPACE]:
                player = choix
                MENU = False
            
        if MENU == False: #Lancement du jeu
            
            WORLD = draw_world(player,WORLD) # affiche le monde
            
            draw_character(player) # affiche le personnage chevalier
            player_movements(player)  # contrôles du joueur
            
            # for enemy in ENEMIES: # gestion des ennemis (affichage + déplacements)
            #     draw_character(enemy)
            #     enemy_move_to_player(enemy,player)
        

            
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
