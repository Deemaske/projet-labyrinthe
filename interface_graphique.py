from creation_labyrinthe import labyrinthe,Tuile
from PIL import Image
import pygame

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