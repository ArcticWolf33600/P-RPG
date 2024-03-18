from .tile import * 

window_heigth = 600
window_width = 1000

WORLD_SW = [ 
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','fb','.','.','.','.'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','.','.','fo','.','.','.','.','.','cua','.','.','.','.','.','.','.','.','.','.'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','.','.','.','.','.','.','.','fb','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X']
]
WORLD_SW_OPEN = [ 
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','fb','.','.','.','.'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','.','.','fo','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','.','.','.','.','.','.','.','fb','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X']
]
WORLD_S = [ 
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','fo','.','.','.','.','.','.','.','rp','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','a','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','fo','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X']
]

WORLD_SE = [ 
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['.','.','.','.','.','.','.','.','.','fb','.','.','.','.','.','.','.','.','.','X'],
    ['.','.','.','.','.','.','.','.','fb','.','fb','.','.','.','.','.','.','.','.','X'],
    ['.','.','.','.','.','.','.','fb','.','.','.','fb','.','.','.','.','.','.','.','X'],
    ['.','.','.','.','.','.','.','fb','.','.','.','fb','.','.','.','.','.','.','.','X'],
    ['.','.','.','.','.','.','.','.','fb','.','fb','.','.','.','.','.','.','.','.','X'],
    ['.','.','.','.','.','.','.','.','.','fb','.','.','.','.','.','.','.','.','.','X'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X']
]

WORLD_E = [ 
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','a','.','.','.','.','ch','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X']
]
WORLD_E_DEFEATED = [ 
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','cna','.','.','.','a','.','.','.','.','ch','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X']
]

WORLD_NE = [ 
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','X'] 
]
# empty_level = [ 
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

def choose_world(world):
    """permet de run un monde"""
    WORLD_OBJECTS.clear()
    for row in range(len(world)):
        for col in range(len(world[row])):
            tuile_type = world[row][col]
            tuile_objet = Tile(row,col,tuile_type)
            WORLD_OBJECTS.append(tuile_objet)

choose_world(WORLD_SW) # run le monde 1