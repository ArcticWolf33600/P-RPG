from EnemyManager import * 

ENEMIES_S = [Skeleton(50,50),Skeleton(100,100)]
ENEMIES_SE = [Skeleton(360,60),Gobelin(300,300),Gobelin(350,350)]
ENEMIES_NE = [Boss(100,100)]
def enemies_management(WORLD):
    """gère les ennemis selon le niveau chargé"""
    ENEMIES = []
    if WORLD == "S":
        ENEMIES = ENEMIES_S
    if WORLD == "SE":
        ENEMIES = ENEMIES_SE
    if WORLD == "NE":
        ENEMIES = ENEMIES_NE
    return ENEMIES