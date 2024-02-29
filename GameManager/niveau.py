from .tile import * 

window_heigth = 600
window_width = 1000

WORLD1 = [ #configuration du niveau
    ['X','X','X','X','X','X','X','X','X','.','.','X','X','X','X','X','X','X','X','X'],
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

WORLD_JARDIN = [ 
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','fb','fb','fb','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','fb','.','rp','.','fb','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','fb','.','.','.','fb','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','fb','.','.','.','fb','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','fb','fb','fb','.','.','.','.','.','.','.','.','a','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','fo','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','X','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']
]

# squelette_de_niveau = [ 
#     ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
#     ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
#     ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
#     ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
#     ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
#     ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
#     ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
#     ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
#     ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
#     ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
#     ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
#     ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']
# ]


WORLD_OBJECTS = [] # récupération des objets tiles ==> sont les assets

def choose_world(world): # permet de run un monde
    WORLD_OBJECTS.clear()
    for row in range(len(world)):
        for col in range(len(world[row])):
            tuile_type = world[row][col]
            tuile_objet = Tile(row,col,tuile_type)
            WORLD_OBJECTS.append(tuile_objet)

choose_world(WORLD1) # run le monde 1