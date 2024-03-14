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
    WORLD = "SW"
    MENU = "start"

    while running:
        clock.tick(fps)  # limite le nombre de fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if MENU == "start": #Menu de sélection du personnage à jouer
            main_menu()
            
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_q]:
                choix = Knight()
            
            elif keys_pressed[pygame.K_d]:
                choix = Wizard()
                
            elif keys_pressed[pygame.K_SPACE]:
                player = choix
                MENU = "game"
            
        if MENU == "game": #Lancement du jeu
            
            WORLD = draw_world(player,WORLD) # affiche le monde
            
            draw_character(player) # affiche le personnage chevalier
            player_movements(player)  # contrôles du joueur
            player_attack_sound()
            attack = player_attack(player)
            
            HUD(player)

            enemy_management(ENEMIES,player,attack)

            if player.health == 0:
                MENU = "over"
        
        if MENU == "over":
            game_over()

            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_q]:
                choix = "start"
            
            elif keys_pressed[pygame.K_d]:
                choix = "quit"
                
            elif keys_pressed[pygame.K_SPACE]:
                MENU = choix
        
        if MENU == "quit":
            running = False
                

        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()