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

img = dessiner(labyrinthe(15))
img = img.resize((600,600),Image.Resampling.BOX)
img.save("bg.png", format="png")

pygame.init()
fond = pygame.image.load("bg.png")
screen = pygame.display.set_mode(fond.get_size())
fond = fond.convert()
screen.blit(fond,(0,0))

continuer = True
mouvement = False
while continuer:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == 771:
            continuer = False
        if not mouvement:
            pygame.mouse.set_pos((20,20))
            mouvement = True
        if fond.get_at(pygame.mouse.get_pos()) == (0,0,0,255):
            mouvement = False
        elif fond.get_at(pygame.mouse.get_pos()) == (255,0,0,255):
            continuer = False
            print("Vous avez gagné!")
    pygame.display.flip()

pygame.quit()