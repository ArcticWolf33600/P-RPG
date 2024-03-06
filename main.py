import pygame
from PlayerManager import *
from GameManager import *
from EnemyManager import *


# pygame setup
pygame.init()
pygame.display.set_caption("P-RPG")

fps = 60

def main():
    main_music = os.path.join("Assets","SFX","main_music.mp3")
    main_music = pygame.mixer.Sound(main_music)
    pygame.mixer.Channel(0).play(main_music,loops=-1)
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
            main_menu()
            
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_q]:
                choix = Knight()
            
            elif keys_pressed[pygame.K_d]:
                choix = Wizard()
                
            elif keys_pressed[pygame.K_SPACE]:
                player = choix
                MENU = False
            
        if MENU == False: #Lancement du jeu
            
            WORLD = draw_world(player,WORLD) # affiche le monde
            
            draw_character(player) # affiche le personnage chevalier
            player_movements(player)  # contrôles du joueur
            player_attack_sound()
            attack = player_attack(player)
            HUD(player)
            for enemy in ENEMIES: # gestion des ennemis (affichage + déplacements)
                draw_character(enemy)
                enemy_moves_to_player(enemy,player,attack)
                check_attack_ennemy_to_player(enemy,player)
                if enemy.health<0:
                    ENEMIES.pop(ENEMIES.index(enemy))
            
                    
        
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()