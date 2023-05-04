from PIL import Image
from random import randint,choice

class Tuile:
    """Classe permettant de simuler une tuile d'un quadrillage
    attribut :
        - direction : les directions du chemins passant par la tuile en suivant cet ordre : haut (0), droite (1), bas (2), gauche (3)
        - visitee : permet de savoir si la tuile a déjà été visitée ou non
        - fonction : permet de savoir quel est le type de chemin passant par la tuile, 0 = chemin normal, 1 = entrée, 2 = sortie, 3 = joueur"""
    def __init__(self):
        self.direction = [0,0,0,0]
        self.visitee = False
        self.fonction = 0

def voisin_non_visite(tableau,x,y):
    """Permet de renvoyer les voisins non visité d'une tuile dans un tableau
    Entrée :
        tableau : une liste de liste de tuiles
        x,y : int, les coordonnées de la tuile
    Sortie:
        une liste de nombre correspondant aux directions des voisins non visités"""
    tab = []
    if x> 0 and not tableau[y][x-1].visitee:
        tab.append(3)
    if x< len(tableau)-1 and not tableau[y][x+1].visitee:
        tab.append(1)
    if y>0 and not tableau[y-1][x].visitee:
        tab.append(0)
    if y<len(tableau)-1 and not tableau[y+1][x].visitee:
        tab.append(2)
    return tab

def tab_cul_de_sac(tableau):
    """Permet de connaitre où se trouve les cul de sac dans un tableau de tuiles
    Entrée :
        tableau : une liste de liste de tuiles
    Sortie :
        une liste de tuples contenant les coordonnées (x,y) des tuiles"""
    tab = []
    for y in range(len(tableau)):
        for x in range(len(tableau)):
            if sum(tableau[y][x].direction) == 1 and tableau[y][x].fonction != 1:
                tab.append((x,y))
    return tab

def labyrinthe(dimension):
    """Permet de créer une liste de liste de tuiles permettant de représenter un labyrinthe carré d'une dimension donnée
    Entrée :
        dimension : int, le nombre de tuile par côté
    Sortie:
        une liste de liste de tuile"""
    tableau = [[Tuile() for i in range(dimension)] for j in range(dimension)]
    x,y = randint(0, dimension-1), randint(0, dimension-1)
    tableau[y][x].visitee = True
    tableau[y][x].fonction = 1
    stack = [(x,y)]
    while len(stack) != 0:
        x,y = stack.pop()
        voisin = voisin_non_visite(tableau, x, y)
        if voisin:
            stack.append((x,y))
            prochain = choice(voisin)
            tableau[y][x].direction[prochain] = 1
            x = x+1 if prochain == 1 else x-1 if prochain==3 else x
            y = y+1 if prochain == 2 else y-1 if prochain==0 else y
            tableau[y][x].direction[(prochain+2)%4] =1
            tableau[y][x].visitee = True
            stack.append((x,y))
    x,y = choice(tab_cul_de_sac(tableau))
    tableau[y][x].fonction = 2
    return tableau