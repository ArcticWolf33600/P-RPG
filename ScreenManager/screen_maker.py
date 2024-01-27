import pygame
import os

window_heigth = 600
window_width = 1000
screen = pygame.display.set_mode((window_width, window_heigth))
background_import = pygame.image.load(os.path.join("Assets", "background.png"))
background = pygame.transform.scale(background_import, (window_width, window_heigth))


def draw_window(hitbox_chevalier, chevalier):
    screen.blit(background, (0, 0))  # background toujours en premier
    screen.blit(chevalier, (hitbox_chevalier.x, hitbox_chevalier.y))  # elements après
    pygame.display.update()
