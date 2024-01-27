import pygame
import os

# pygame setup
pygame.init()
window_heigth = 600
window_width = 1000
screen = pygame.display.set_mode((window_width, window_heigth))
pygame.display.set_caption("P-RPG")

white = (255, 255, 255)
fps = 60
vitesse_deplacement = 5
chevalier_import = pygame.image.load(os.path.join("Assets", "chevalier.png"))
chevalier_width = 50
chevalier_heigth = 50
chevalier = pygame.transform.scale(
    chevalier_import, (chevalier_width, chevalier_heigth)
)
# Tourner l'image de 90° :
# chevalier = pygame.transform.rotate(pygame.transform.scale(chevalier_import,(50,50)),90)

# Symétrie axiale de l'image (X=True, y = False):
# chevalier = pygame.transform.flip(chevalier,True,False)

background_import = pygame.image.load(os.path.join("Assets", "background.png"))
background = pygame.transform.scale(background_import, (window_width, window_heigth))


def draw_window(hitbox_chevalier):
    screen.blit(background, (0, 0))  # background toujours en premier
    screen.blit(chevalier, (hitbox_chevalier.x, hitbox_chevalier.y))  # elements après
    pygame.display.update()

def player_movement(keys_pressed,hitbox_chevalier):
    direction = "est"

    if keys_pressed[pygame.K_z] and hitbox_chevalier.y > 0:  # haut
        hitbox_chevalier.y -= vitesse_deplacement
    if keys_pressed[pygame.K_q] and hitbox_chevalier.x > 0:  # gauche
        hitbox_chevalier.x -= vitesse_deplacement
            
    if keys_pressed[pygame.K_s] and hitbox_chevalier.y < window_heigth-chevalier_heigth:  # bas
        hitbox_chevalier.y += vitesse_deplacement
    if keys_pressed[pygame.K_d] and hitbox_chevalier.x < window_width-chevalier_width:  # droite
        hitbox_chevalier.x += vitesse_deplacement
        
def main():
    hitbox_chevalier = pygame.Rect(50, 550, chevalier_width, chevalier_heigth)

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(fps)  # limite le nombre de fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys_pressed = pygame.key.get_pressed()
        player_movement(keys_pressed,hitbox_chevalier)

        draw_window(hitbox_chevalier)

    pygame.quit()


if __name__ == "__main__":
    main()
