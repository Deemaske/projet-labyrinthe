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


pygame.init()

#initialisation des variables de départ
texte = pygame.font.Font(None,60)
dimension = 600, 600 + texte.render("0", False, (0,0,0)).get_size()[1]
screen = pygame.display.set_mode(dimension)


#Afficher les bouttons 
easybutton_img = pygame.image.load('easybutton.png').convert_alpha()
mediumbutton_img = pygame.image.load('mediumbutton.png').convert_alpha()
hardbutton_img = pygame.image.load('hardbutton.png').convert_alpha()

class Button():
    def __init__(self, x, y, image, scale):
        largeur = image.get_width()
        hauteur = image.get_height()
        self.image = pygame.transform.scale(image, (int(largeur * scale), int(hauteur * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self):
        action = False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

easy = Button(135, 100, easybutton_img, 0.8)
medium = Button(135, 300, mediumbutton_img, 0.8)
hard = Button(135, 500, hardbutton_img, 0.8)

continuer = True
while continuer:
    for event in pygame.event.get():
        pygame.display.flip()
        screen.fill((0,0,0))

        if easy.draw():
            lvl = 5
            pos_depart =(60,60)
            continuer = False
        if medium.draw():
            lvl = 10
            pos_depart = (30,30)
            continuer = False
        if hard.draw():
            lvl = 15
            pos_depart = (20,20)
            continuer = False
        if event.type == pygame.QUIT:
            pygame.quit()

#initialisation du labyrinthe
img = dessiner(labyrinthe(lvl))
img = img.resize((600,600),Image.Resampling.BOX)
img.save("bg.png", format="png")
fond = pygame.image.load("bg.png")
fond = fond.convert()

debut = time.time()

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
        if not mouvement:
            pygame.mouse.set_pos(pos_depart)
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
        if event.type == pygame.QUIT:
            continuer = False
            pygame.quit()