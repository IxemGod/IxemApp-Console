from tkinter import *
from turtle import *
import math
from random import *
import sys
from couleur import *
from art import *
import os

class Geo():
    Response = 0

def Geometrie():
    
    def volumes():
 

        def volumes_rep(response):
            résultat_geo = response
            Otest = résultat_geo.isdigit()
            if Otest == True:
                résultat_geo = int(résultat_geo)
                if résultat_geo == Geo.Response:
                    phrase = "Bravo tu as trouvé la bonne réponse !"
                else:
                    phrase = "Tu n'as pas trouvé"
            elif Otest == False:
                phrase = "Ce n'est pas un chiffre."

            return phrase  
        
        def ChoixExercice():
            Forme = randint(0, 6)
            if Forme == 0:
                # Cube
                Omesure = randint(1, 12)
                Ovolume = Omesure * Omesure * Omesure
                Ovolume = round(Ovolume)
                Geo.Response = Ovolume
                return f"Donne moi le volume du cube d'arrête de {Omesure} cm, arrondi à l'entier. "
            elif Forme == 1:
                # Pavé Droit
                Olongeur = randint(1, 12)
                Olargeur = randint(1, 12)
                Ohauteur = randint(1, 12)
                Ovolume = Olongeur * Olargeur * Ohauteur
                Ovolume = round(Ovolume)
                Geo.Response = Ovolume
                return f"Donne moi le volume de ce pavé droit de longeur  {Olongeur} cm, de largeur {Olargeur} cm, et de hauteur {Ohauteur} cm,  arrondi à l'entier."
            elif Forme == 2:
                #Sphère
                Orayon = randint(1, 12)
                Ovolume = 4 * math.pi * Orayon * Orayon * Orayon
                Ovolume = Ovolume / 3
                Ovolume = round(Ovolume)
                Geo.Response = Ovolume
                return f"Donne moi le volume de cette sphère de rayon {Orayon} cm, arrondi à l'entier. "
            elif Forme == 3:
                #Cône
                Orayon = randint(1, 12)
                Ohauteur = randint(1, 12)
                Ovolume = math.pi * Orayon * Orayon * Ohauteur
                Ovolume = Ovolume / 3
                Ovolume = round(Ovolume)
                Geo.Response = Ovolume
                return f"Donne moi le volume de ce cône de rayon {Orayon} cm, et de hauteur {Ohauteur} cm, arrondi à l'entier."
            elif Forme == 4:
                #Cylindre
                Orayon = randint(1, 12)
                Ohauteur = randint(1, 12)
                Ovolume = math.pi * Orayon * Orayon * Ohauteur
                Ovolume = round(Ovolume)
                Geo.Response = Ovolume
                return f"Donne moi le volume de ce cylindre de rayon {Orayon} cm, et de hauteur {Ohauteur} cm, arrondi à l'entier. "
            elif Forme == 5:
                #Pyramide de base Triangle Rectangle
                Olongeur = randint(1, 12)
                Olargeur = randint(1, 12)
                Ohauteur = randint(1, 12)
                Ovolume = (Olongeur * Olargeur) / 2
                Ovolume = Ovolume * Ohauteur
                Ovolume = Ovolume / 3
                Ovolume = round(Ovolume)
                Geo.Response = Ovolume
                return f"Donne moi le volume de cette pyramide à base triangle rectangle de largeur {Olargeur} cm, de longeur {Olongeur} cm et de hauteur {Ohauteur} cm, arrondi à l'entier."
            elif Forme == 6:
                # pyramide de base carré
                Ocoter = randint(1, 12)
                Ohauteur = randint(1, 12)
                Ovolume = Ocoter * Ocoter * Ohauteur
                Ovolume = Ovolume / 3
                Ovolume = round(Ovolume)
                Geo.Response = Ovolume
                return f"Donne moi le volume de cette pyramide de base caré de coté {Ocoter} cm, et de hauteur {Ohauteur} cm,  arrondi à l'entier."

    
        banner()
        print(Color.yellow_bold+"   "+ChoixExercice())
        rep = input(Color.cyan_bold+"    [?]"+Color.white_bold+" Tapez votre réponse "+Color.blue_bold)
        print("     "+volumes_rep(rep))
        fin = input('')
        Menu()

    def aires():

        def air_rep(response):
            résultat_geo = response
            Otest = résultat_geo.isdigit()
            if Otest == True:
                résultat_geo = int(résultat_geo)
                if résultat_geo == Geo.Response:
                    phrase = "Bravo tu as trouvé la bonne réponse !"
                else:
                    phrase = "Tu n'as pas trouvé"
            elif Otest == False:
                phrase = "Ce n'est pas un chiffre."

            return phrase 


        def ChoixExercice():
            Oran = randint(0, 5)
            if Oran == 0:
                # carré
                Omesure = randint(1, 12)
                Oaire = Omesure*Omesure
                Oaire = round(Oaire)
                Geo.Response = Oaire
                return f"Donne moi l'aire du carré de côté {Omesure} cm, arrondi à l'entier. "
            elif Oran == 1:
                # rectangle
                Olongeur = randint(1, 12)
                Olargeur = randint(1, 12)
                Oaire = Olongeur * Olargeur
                Oaire = round(Oaire)
                Geo.Response = Oaire
                return f"Donne moi l'aire de ce rectangle de longeur {Olongeur}cm, de largeur {Olargeur} cm, arrondi à l'entier. "
            elif Oran == 2:
                # triangle rectangle
                Ocoter = randint(1, 12)
                Ohauteur = randint(1, 12)
                Oaire = Ocoter * Ohauteur
                Oaire = Oaire / 2
                Oaire = round(Oaire)
                Geo.Response = Oaire
                return f"Donne moi l'aire de ce triangle recrantgle de longueur {Ocoter}cm, de largeur {Ohauteur} cm, arrondi à l'entier. "
            elif Oran == 3:
                # Cercle
                Orayon = randint(1, 12)
                Oaire = Orayon * Orayon * math.pi
                Oaire = round(Oaire)
                Geo.Response = Oaire
                return f"Donne moi l'aire de ce cercle de rayon {Orayon}cm, arrondi à l'entier. "
            elif Oran == 4:
                # aire latérale du cilyndre
                Orayon = randint(1, 12)
                Ohauteur = randint(1, 12)
                Oaire = math.pi * Orayon * Ohauteur * 2
                Oaire = round(Oaire)
                Geo.Response = Oaire                
                return f"Donne moi le l'aire latérale de ce cylindre de rayon {Orayon}cm, et de hauteur {Ohauteur} cm, arrondi à l'entier. "

            elif Oran == 5:
                # triangle quelconque
                Obase = randint(1, 12)
                Ohauteur = randint(1, 12)
                Oaire = Obase * Ohauteur
                Oaire = Oaire / 2
                Oaire = round(Oaire)
                Geo.Response = Oaire
                return f"Donne moi l'aire de ce triangle quelconque de base {Obase}cm, et de hauteur {Ohauteur} cm, arrondi à l'entier. "

        
        
        banner()
        print(Color.yellow_bold+"   "+ChoixExercice())
        rep = input(Color.cyan_bold+"    [?]"+Color.white_bold+" Tapez votre réponse "+Color.blue_bold)
        print("     "+air_rep(rep))
        fin = input('')
        Menu()

    def  périmêtre():
        
        def ChoixExercice():
            Oran = randint(0, 4)
            if Oran == 0:
                # carré
                Omesure = randint(1, 12)
                Operi = Omesure * 4
                Operi = round(Operi)
                Geo.Response = Operi
                return f"Donne moi le périmêtre du carré de côté {Omesure} cm, arrondi à l'entier. "
            elif Oran == 1:
                # rectangle
                Olongeur = randint(1, 12)
                Olargeur = randint(1, 12)
                Operi = (Olongeur + Olargeur) * 2
                Operi = round(Operi)
                Geo.Response = Operi
                return f"Donne moi le périmêtre de ce rectangle de longeur {Olongeur} cm, et de largeur {Olargeur} cm, arrondi à l'entier. "
            elif Oran == 2:
                # triangle rectangle
                Ocoter = randint(1, 12)
                Ohauteur = randint(1, 12)
                Ohypo = randint(1, 12)
                Operi = Ocoter + Ohauteur + Ohypo
                Operi = round(Operi)
                Geo.Response = Operi
                return f"Donne moi le périmêtre de ce triangle rectangle de longueur {Ocoter} cm, et de largeur {Ohauteur} cm, de l'hypothénuse {Ohypo} arrondi à l'entier."
            elif Oran == 3:
                # cercle
                Orayon = randint(1, 12)
                Operi = Orayon * 2 * math.pi
                Operi = round(Operi)
                Geo.Response = Operi
                return f"Donne moi le périmêtre de ce cercle de rayon {Orayon} cm, arrondi à l'entier."
            elif Oran == 4:
                # triangle quelconque
                Obase = randint(1, 12)
                Olargeur = randint(1, 12)
                Olongeur = randint(1, 12)
                Operi = Obase + Olongeur + Olargeur
                Operi = round(Operi)
                Geo.Response = Operi
                return f"Donne moi le périmêtre de ce triangle quelconque de longueur {Olongeur} cm, de largeur {Olargeur} cm, de base {Obase} cm, arrondi à l'entier. "


        def peri_rep(response):
            résultat_geo = response
            Otest = résultat_geo.isdigit()
            if Otest == True:
                résultat_geo = int(résultat_geo)
                if résultat_geo == Geo.Response:
                    phrase = "Bravo tu as trouvé la bonne réponse !"
                else:
                    phrase = "Tu n'as pas trouvé"
            elif Otest == False:
                phrase = "Ce n'est pas un chiffre."

            return phrase 

        banner()
        print(Color.yellow_bold+"   "+ChoixExercice())
        rep = input(Color.cyan_bold+"    [?]"+Color.white_bold+" Tapez votre réponse "+Color.blue_bold)
        print("     "+peri_rep(rep))
        fin = input('')
        Menu()

    def leçon():
        import turtle
        def volumes_leçon():
            wn = turtle.Screen()
            try:
                turtle.up()
            except:
                print('')
            turtle.up()
            turtle.speed(20)
            turtle.goto(-300, 250)
            turtle.down()
            turtle.color("red")
            turtle.write("LE COURS :", font=("Arial", 30, "normal"))
            turtle.up()
            turtle.setup(1050, 600, 200, 200)
            turtle.goto(-500, 250)
            turtle.down()
            for i in range(2):
                turtle.bgcolor("yellow")
                turtle.width(10)
                turtle.color("black")
                turtle.forward(1000)
                turtle.right(90)
                turtle.forward(300)
                turtle.right(90)
            turtle.up()
            turtle.goto(-480, 160)
            turtle.color("purple")
            turtle.down()
            turtle.write("Les volumes :", font=("Arial", 25, "normal"))
            turtle.up()
            turtle.goto(-480, 120)
            turtle.down()
            turtle.write("Pour calculer le volume d'un cube on utilise la formule : V=C * C * C", font=("Arial", 15, "normal"))
            turtle.up()
            turtle.goto(-480, 80)
            turtle.down()
            turtle.write("Pour calculer le volume d'un pavé on utilise la formule : V=L * l * h", font=("Arial", 15, "normal"))
            turtle.up()
            turtle.goto(-480, 60)
            turtle.down()
            turtle.write("Pour calculer le volume d'une sphère on utilise la formule : V=π * 4/3 * R * R * R ",font=("Arial", 15, "normal"))
            turtle.up()
            turtle.goto(-480, 40)
            turtle.down()
            turtle.write("Pour calculer le volume d'une pyramide de base carré on utilise la formule : V=(C * C * H)/3",font=("Arial", 15, "normal"))
            turtle.up()
            turtle.goto(-480, 20)
            turtle.down()
            turtle.write("Pour calculer le volume d'un cone on utilise la formule : V=(π * R * R * H)/3",font=("Arial", 15, "normal"))
            turtle.up()
            turtle.goto(-480, 0)
            turtle.down()
            turtle.write("Pour calculer le volume d'un cylindre, on utilise la fromule : V=π * R * R * H",font=("Arial", 15, "normal"))
            turtle.up()
            turtle.goto(-480, -20)
            turtle.down()
            turtle.write("Pour calculer le volume d'une pyramide de base triangle rectangle on utilise la formule : V=(Airbase * H)/3",font=("Arial", 15, "normal"))
            turtle.up()
        def aires_leçon():
            wn = turtle.Screen()
            try:
                turtle.up()
            except:
                print('')
            turtle.up()
            turtle.speed(20)
            turtle.goto(-300, 250)
            turtle.down()
            turtle.color("red")
            turtle.write("LE COURS :", font=("Arial", 30, "normal"))
            turtle.up()
            turtle.setup(1050, 600, 200, 200)
            turtle.goto(-500, 250)
            turtle.down()
            for i in range(2):
                turtle.bgcolor("yellow")
                turtle.width(10)
                turtle.color("black")
                turtle.forward(1000)
                turtle.right(90)
                turtle.forward(300)
                turtle.right(90)
            turtle.up()
            turtle.goto(-480, 160)
            turtle.down()
            turtle.color("purple")
            turtle.write("Les airs :", font=("Arial", 25, "normal"))
            turtle.up()
            turtle.goto(-480, 120)
            turtle.down()
            turtle.write("Pour calculer l'air d'un carré on utilise la formule : A=C * C", font=("Arial", 15, "normal"))
            turtle.up()
            turtle.goto(-480, 100)
            turtle.down()
            turtle.write("Pour calculer l'air d'un rectangle on utilise la formule : A=L * 2 + l * 2",font=("Arial", 15, "normal"))
            turtle.up()
            turtle.goto(-480, 80)
            turtle.down()
            turtle.write("Pour calculer l'air d'un triangle rectangle on utilise la formule : A=(L * 2 + l * 2)/2",font=("Arial", 15, "normal"))
            turtle.up()
            turtle.goto(-480, 60)
            turtle.down()
            turtle.write("Pour calculer l'air d'un cercle on utilise la formule : A=π * R * R", font=("Arial", 15, "normal"))
            turtle.up()
            turtle.goto(-480, 40)
            turtle.down()
            turtle.write("Pour calculer l'air d'un triangle quelconque on utilise la formule : A=(B * H)/2",font=("Arial", 15, "normal"))
            turtle.up()
            turtle.goto(-480, 20)
            turtle.down()
            turtle.write("Pour calculer l'air de la face latérale d'un cylindre on utilise la formule : A=π * R * H * 2",font=("Arial", 15, "normal"))
            turtle.up()
            turtle.goto(-480, 0)
        def périmêtre_leçon():
            wn = turtle.Screen()
            try:
                turtle.up()
            except:
                print('')
            turtle.up()
            turtle.speed(20)
            turtle.goto(-300, 250)
            turtle.down()
            turtle.color("red")
            turtle.write("LE COURS :", font=("Arial", 30, "normal"))
            turtle.up()
            turtle.setup(1050, 600, 200, 200)
            turtle.goto(-500, 250)
            turtle.down()
            for i in range(2):
                turtle.bgcolor("yellow")
                turtle.width(10)
                turtle.color("black")
                turtle.forward(1000)
                turtle.right(90)
                turtle.forward(250)
                turtle.right(90)
            turtle.up()
            turtle.goto(-490, 160)
            turtle.down()
            turtle.color("purple")
            turtle.write("Les périmêtres :", font=("Arial", 25, "normal"))
            turtle.up()
            turtle.goto(-490, 120)
            turtle.down()
            turtle.write("Pour calculer le périmêtre d'un carré on utilise la formule : A= C * C",font=("Arial", 15, "normal"))
            turtle.up()
            turtle.goto(-490, 100)
            turtle.down()
            turtle.write("Pour calculer le périmêtre d'un rectangle on utilise la formule : A= (L + l) * 2",font=("Arial", 15, "normal"))
            turtle.up()
            turtle.goto(-490, 80)
            turtle.down()
            turtle.write("Pour calculer le périmêtre d'un triangle rectangle on utilise la formule : A= C + H + hypothénuse",font=("Arial", 15, "normal"))
            turtle.up()
            turtle.goto(-490, 60)
            turtle.down()
            turtle.write("Pour calculer le périmêtre d'un cercle on utilise la formule : A= R * 2 * π",font=("Arial", 15, "normal"))
            turtle.up()
            turtle.goto(-490, 40)
            turtle.down()
            turtle.write("Pour calculer le périmêtre d'un triangle quelconque on utilise la formule : A= B + l + L",font=("Arial", 15, "normal"))
        
        banner()
        print(Color.yellow_bold+'   Menu de thème : \n\n')
        print(Color.red_bold+'      [1]'+Color.white_bold+" Volume"+Color.red_bold+'        [2]'+Color.white_bold+" Aires")
        print(Color.red_bold+'      [3]'+Color.white_bold+" Périmêtre")
        choix = input(Color.cyan_bold+"\n    [?]"+Color.white_bold+" Choissez un chiffre "+Color.blue_bold)

        if choix == 1 or choix == "1":
            volumes_leçon()
        elif choix == 2 or choix == "2":
            aires_leçon()
        elif choix == 3 or choix == "3":
            périmêtre_leçon()

    
    
    def banner():
        system("clear")
        print(Color.green_bold)
        tprint("Exercice de \ngeometrie")


    
    def Menu():
        banner()
        print(Color.yellow_bold+'   Menu d\'exercice : \n\n')
        print(Color.red_bold+'      [1]'+Color.white_bold+" Volume"+Color.red_bold+'        [2]'+Color.white_bold+" Aires")
        print(Color.red_bold+'      [3]'+Color.white_bold+" Périmêtre"+Color.red_bold+'     [4]'+Color.white_bold+" Leçon")
        choix = input(Color.cyan_bold+"\n\n    [?]"+Color.white_bold+" Choissez un chiffre "+Color.blue_bold)

        if choix == 1 or choix == "1":
            volumes()
        elif choix == 2 or choix == "2":
            aires()
        elif choix == 3 or choix == "3":
            périmêtre()
        elif choix == 4 or choix == "4":
            leçon()

    Menu()