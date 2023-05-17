from creation_labyrinthe import labyrinthe,Tuile
from PIL import Image
import pygame
import time

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

img = dessiner(labyrinthe(10))
img = img.resize((600,600),Image.Resampling.BOX)
img.save("bg.png", format="png")

pygame.init()
fond = pygame.image.load("bg.png")
texte = pygame.font.Font(None,60)
debut = time.time()
dimension = fond.get_size()[0], fond.get_size()[1] + texte.render("0", False, (0,0,0)).get_size()[1]
screen = pygame.display.set_mode(dimension)
fond = fond.convert()
screen.blit(fond,(0,0))

continuer = True
mouvement = False
while continuer:
    pygame.display.flip()
    screen.fill((0,0,0))
    screen.blit(fond,(0,0))
    screen.blit(texte.render(f"{int(time.time()-debut)//60 % 60:02}:{int(time.time()-debut)%60:02}", False, (255,255,255)), (240,fond.get_size()[1]))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == 771:
            continuer = False
        if not mouvement:
            pygame.mouse.set_pos((20,20))
            mouvement = True
        if fond.get_at(pygame.mouse.get_pos()) == (0,0,0,255):
            mouvement = False
        elif fond.get_at(pygame.mouse.get_pos()) == (255,0,0,255):
            continuer = False
            gagner = True

screen.fill((0,0,0))
screen.blit(texte.render(f"Vous avez gagné en {int(time.time()-debut)//60 % 60:02}:{int(time.time()-debut)%60:02}",False,(255,255,255)),(50,300))

continuer = True
while continuer:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == 771:
            continuer = False

pygame.quit()