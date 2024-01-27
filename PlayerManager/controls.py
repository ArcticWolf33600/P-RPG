import pygame

window_heigth = 600
window_width = 1000


def player_movement(hitbox_chevalier, vitesse_deplacement, chevalier_heigth, chevalier_width):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_z] and hitbox_chevalier.y > 0:  # haut
        hitbox_chevalier.y -= vitesse_deplacement
    if keys_pressed[pygame.K_q] and hitbox_chevalier.x > 0:  # gauche
        hitbox_chevalier.x -= vitesse_deplacement

    if (
        keys_pressed[pygame.K_s]
        and hitbox_chevalier.y < window_heigth - chevalier_heigth
    ):  # bas
        hitbox_chevalier.y += vitesse_deplacement
    if (
        keys_pressed[pygame.K_d] and hitbox_chevalier.x < window_width - chevalier_width
    ):  # droite
        hitbox_chevalier.x += vitesse_deplacement
