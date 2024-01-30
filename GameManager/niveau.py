import pygame
import os
from .tile import * 

sprites = {
    'X':pygame.transform.scale(pygame.image.load(os.path.join("Assets","Environment","rocher.png")),(50, 50)) #X = rocher
}

WORLD = [ #configuration du niveau
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','X','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X']
]

WORLD_OBJECTS = [ #contient les tuiles sous forme d'objets Tile
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]
    
for row in range(len(WORLD)):
    for col in range(len(WORLD[row])):
        tuile_type = WORLD[row][col]
        tuile_objet = Tile(row,col,tuile_type)
        WORLD_OBJECTS[row].append(tuile_objet)

window_heigth = 600
window_width = 1000