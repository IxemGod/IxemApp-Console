import os
from turtle import *
from art import *
from couleur import *
import sys
import platform

class Jeux():
    System_Os = False


def system_exploitation():
    if platform.system() == "Linux":
        Jeux.System_Os = "python3" 
    elif platform.system() == "Windows":
        Jeux.System_Os = "python"

system_exploitation()

def Jeux_Pong():
    os.system(Jeux.System_Os+" -m freegames.pong")


def Jeux_Paint():
    os.system(Jeux.System_Os+" -m freegames.paint")

def Jeux_Ant():
    os.system(Jeux.System_Os+" -m freegames.ant")

def Jeux_Flappy():
    os.system(Jeux.System_Os+" -m freegames.flappy")

def Jeux_Snake():
    os.system(Jeux.System_Os+" -m freegames.snake")


class Morpion():
    Joueur_en_cours = 1
    ListePosi = [(-71,70),(28,70),(127,70),
                 (-71,-30),(28,-30),(127,-30),
                 (-71,-130),(28,-130),(127,-130)]

    ListePion = [0,0,0,
                 0,0,0,
                 0,0,0]

    def Jeux_Morpion():
        
        sc = getscreen()
        sc.setup(800,800)
        ht()

        def initJeu():
            # On crée la liste sur laquel le jeu se lance
            
            sc.reset()
            quadrillage()
            desinnePion()
            speed("fastest")

        def desinnePion():
            for i in range(0,9):
                case = Morpion.ListePion[i]
                if case == 1:
                    Coo = Morpion.ListePosi[i]
                    pionJoueur1(Coo[0], Coo[1])
                elif case == 2:
                    Coo = Morpion.ListePosi[i]
                    pionJoueur2(Coo[0], Coo[1])



        def testGagnant():
            for jouer in range(1,3):

                # On test les lignes
                if Morpion.ListePion[0] == jouer and Morpion.ListePion[1] == jouer and Morpion.ListePion[2] == jouer:
                    afficheText(f"Le joueur {jouer} à gagné(e) !",True)
                elif Morpion.ListePion[3] == jouer and Morpion.ListePion[4] == jouer and Morpion.ListePion[5] == jouer:
                    afficheText(f"Le joueur {jouer} à gagné(e) !",True)
                elif Morpion.ListePion[6] == jouer and Morpion.ListePion[7] == jouer and Morpion.ListePion[8] == jouer:
                    afficheText(f"Le joueur {jouer} à gagné(e) !",True)

                # On test les colonnes
                elif Morpion.ListePion[0] == jouer and Morpion.ListePion[3] == jouer and Morpion.ListePion[6] == jouer:
                    afficheText(f"Le joueur {jouer} à gagné(e) !",True)
                elif Morpion.ListePion[1] == jouer and Morpion.ListePion[4] == jouer and Morpion.ListePion[7] == jouer:
                    afficheText(f"Le joueur {jouer} à gagné(e) !",True)
                elif Morpion.ListePion[2] == jouer and Morpion.ListePion[5] == jouer and Morpion.ListePion[8] == jouer:
                    afficheText(f"Le joueur {jouer} à gagné(e) !",True)


                # On test les diagonales
                elif Morpion.ListePion[3] == jouer and Morpion.ListePion[5] == jouer and Morpion.ListePion[7] == jouer:
                    afficheText(f"Le joueur {jouer} à gagné(e) !",True)
                elif Morpion.ListePion[0] == jouer and Morpion.ListePion[5] == jouer and Morpion.ListePion[8] == jouer:
                    afficheText(f"Le joueur {jouer} à gagné(e) !",True)




        def quadrillage():
            bgcolor('white')
            tracer(False)
            for i in range(0, 4):
                up()
                pencolor("black")
                goto(-124, - 149 + 100 * i)
                down()
                forward(300)

            left(90)
            for i in range(0, 4):
                up()
                goto(-124 + 100 * i, -149)
                down()
                forward(300)


            update()


        def main():
            initJeu()

        def afficheText(text,gagnant):
            
            initJeu()
            up()
            goto(-93,258)
            write(text)
            sc.onclick(play)

        def play(x,y):

            #Ligne 1
            if x > -123.0 and x < -25.0 and y >53.0 and y < 150.0:
                # Case 1
                if Morpion.ListePion[0] == 0:
                    if Morpion.Joueur_en_cours == 1:
                        Morpion.ListePion[0] = 1
                        pionJoueur1(-71,70)
                    else:
                        Morpion.ListePion[0] = 2
                        pionJoueur2(-71,70)
                else:
                    afficheText("Case déjà prise !",False)
            elif x > -20.0 and x < 79.0 and y >53.0 and y < 150.0:
                # Case 2
                if Morpion.ListePion[1] == 0:
                    if Morpion.Joueur_en_cours == 1:
                        Morpion.ListePion[1] = 1
                        pionJoueur1(28,70)
                    else:
                        Morpion.ListePion[1] = 2
                        pionJoueur2(28,70)
                else:
                    afficheText("Case déjà prise !",False)
            elif x > 77.0 and x < 177.0 and y >53.0 and y < 150.0:
                # Case 3
                if Morpion.ListePion[2] == 0:
                    if Morpion.Joueur_en_cours == 1:
                        Morpion.ListePion[2] = 1
                        pionJoueur1(127,70)
                    else:
                        Morpion.ListePion[2] = 2
                        pionJoueur2(127,70)
                else:
                    afficheText("Case déjà prise !",False)
            # Ligne 2
            if x > -123.0 and x < -25.0 and y >-47.0 and y < 51.0:
                # Case 4
                if Morpion.ListePion[3] == 0:
                    if Morpion.Joueur_en_cours == 1:
                        Morpion.ListePion[3] = 1
                        pionJoueur1(-71,-30)
                    else:
                        Morpion.ListePion[3] = 2
                        pionJoueur2(-71,-30)
                else:
                    afficheText("Case déjà prise !",False)
            elif x > -20.0 and x < 79.0 and y >-47.0 and y < 51.0:
                # Case 5
                if Morpion.ListePion[4] == 0:
                    if Morpion.Joueur_en_cours == 1:
                        Morpion.ListePion[4] = 1
                        pionJoueur1(28,-30)
                    else:
                        Morpion.ListePion[4] = 2
                        pionJoueur2(28,-30)
                else:
                    afficheText("Case déjà prise !",False)
            elif x > 77.0 and x < 177.0 and y >-47.0 and y < 51.0:
                # Case 6")
                if Morpion.ListePion[5] == 0:
                    if Morpion.Joueur_en_cours == 1:
                        Morpion.ListePion[5] = 1
                        pionJoueur1(127,-30)
                    else:
                        Morpion.ListePion[5] = 2
                        pionJoueur2(127,-30)
                else:
                    afficheText("Case déjà prise !",False)

            # Ligne 3
            if x > -123.0 and x < -25.0 and y >-147.0 and y < -50.0:
                # Case 7
                if Morpion.ListePion[6] == 0:
                    if Morpion.Joueur_en_cours == 1:
                        Morpion.ListePion[6] = 1
                        pionJoueur1(-71,-130)
                    else:
                        Morpion.ListePion[6] = 2
                        pionJoueur2(-71,-130)
                else:
                    afficheText("Case déjà prise !",False)
            elif x > -20.0 and x < 79.0 and y >-147.0 and y < -50.0:
                # Case 8")
                if Morpion.ListePion[7] == 0:
                    if Morpion.Joueur_en_cours == 1:
                        Morpion.ListePion[7] = 1
                        pionJoueur1(28,-130)
                    else:
                        Morpion.ListePion[7] = 2
                        pionJoueur2(28,-130)
                else:
                    afficheText("Case déjà prise !",False)
            elif x > 77.0 and x < 177.0 and y >-147.0 and y < -50.0:
                # Case 9
                if Morpion.ListePion[8] == 0:
                    if Morpion.Joueur_en_cours == 1:
                        Morpion.ListePion[8] = 1
                        pionJoueur1(127,-130)
                    else:
                        Morpion.ListePion[8] = 2
                        pionJoueur2(127,-130)
                else:
                    afficheText("Case déjà prise !",False)

            testGagnant()
            
        def pionJoueur1(i, j):
            # crée les pions
            Morpion.Joueur_en_cours = 2
            couleur_pion1 = "red"
            up()
            home()
            goto( i, j)
            begin_fill()
            color(couleur_pion1)
            circle(30)
            end_fill()

        def pionJoueur2(i, j):
            Morpion.Joueur_en_cours = 1
            couleur_pion2 = "green"
            up()
            home()
            goto(i,j)
            begin_fill()
            color(couleur_pion2)
            circle(30, None, 4)
            end_fill()


        main()
        sc.onclick(play)
        mainloop()