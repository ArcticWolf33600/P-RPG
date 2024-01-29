import pygame
from PlayerManager import *
from ScreenManager import *

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

        player_movement(chevalier.hitbox, chevalier.speed, chevalier.heigth, chevalier.width)  # contrôles du joueur
        draw_world()
        draw_characters(chevalier.hitbox, chevalier.sprite)  
        
    pygame.quit()


if __name__ == "__main__":
    main()
