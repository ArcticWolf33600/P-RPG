import pygame
from PlayerManager import *
from GameManager import *

# pygame setup
pygame.init()
pygame.display.set_caption("P-RPG")

fps = 60

chevalier = Chevalier()  # crée l'objet chevalier affiché à l'écran


def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(fps)  # limite le nombre de fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        draw_world() # affiche le monde
        draw_character(chevalier) # affiche le personnage chevalier
        player_movements(chevalier)  # contrôles du joueur
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
