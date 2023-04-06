from PIL import Image
from random import randint,choice

#direction dans une liste : 0 = haut, 1 = droite, 2 = bas, 3 = gauche
#la fonction d'une tuile : 0 = chemin, 1 = entrée, 2 = sortie
class Tuile:
    """Classe permettant de simuler une tuile d'un quadrillage
    attribut :
        - direction : les directions du chemins passant par la tuile en suivant cet ordre : haut (0), droite (1), bas (2), gauche (3)
        - visitee : permet de savoir si la tuile a déjà été visitée ou non
        - fonction : permet de savoir quel est le type de chemin passant par la tuile, 0 = chemin normal, 1 = entrée, 2 = sortie"""
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
            prochain = voisin[randint(0,len(voisin)-1)]
            tableau[y][x].direction[prochain] = 1
            x = x+1 if prochain == 1 else x-1 if prochain==3 else x
            y = y+1 if prochain == 2 else y-1 if prochain==0 else y
            tableau[y][x].direction[(prochain+2)%4] =1
            tableau[y][x].visitee = True
            stack.append((x,y))
    x,y = choice(tab_cul_de_sac(tableau))
    tableau[y][x].fonction = 2
    return tableau

if __name__ == "__main__":
    def dessiner(tableau):
        """Permet de dessiner un labyrinthe à partir d'une liste de liste de tuiles
        Entrée :
            une liste de liste de tuiles
        Sortie : 
            une image"""
        image = Image.new("RGB",(len(tableau)*3,len(tableau)*3))
        for x in range(len(tableau)):
            for y in range(len(tableau)):
                if tableau[y][x].fonction == 0:
                    couleur = (255,255,255)
                elif tableau[y][x].fonction == 1:
                    couleur = (0,255,0)
                else:
                    couleur = (255,0,0)
                image.putpixel((x*3+1,y*3+1),couleur)
                if tableau[y][x].direction[0]:
                    image.putpixel((x*3+1,y*3),couleur)
                if tableau[y][x].direction[1]:
                    image.putpixel((x*3+2,y*3+1),couleur)
                if tableau[y][x].direction[2]:
                    image.putpixel((x*3+1,y*3+2),couleur)
                if tableau[y][x].direction[3]:
                    image.putpixel((x*3,y*3+1),couleur)
        return image

    def agrandir(img,n):
        """Permet de créer une version agrandi d'une image d'un facteur n
        Entrée :
            img : une image
            n : int, le ratio d'aggrandissement de l'image
        Sortie :
            une image"""
        if n<=1:return img
        new_image = Image.new("RGB",(int(img.size[0]*n),int(img.size[1]*n)))
        for x in range(new_image.size[0]):
            for y in range(new_image.size[1]):
                new_image.putpixel((x,y),img.getpixel((x//n,y//n)))
        return new_image
    
    dimension = int(input("dimension : "))
    img = agrandir(dessiner(labyrinthe(dimension)), 100//dimension)
    img.show()