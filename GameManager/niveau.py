import pygame
import os
from .tile import * 


window_heigth = 600
window_width = 1000

WORLD1 = [ #configuration du niveau
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','a','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','X','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X']
]


WORLD_OBJECTS = []

def choose_world(world):
    for row in range(len(world)):
        for col in range(len(world[row])):
            tuile_type = world[row][col]
            tuile_objet = Tile(row,col,tuile_type)
            WORLD_OBJECTS.append(tuile_objet)


choose_world(WORLD1)
