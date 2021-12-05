import random
import os
from couleur import *
from art import *

# 🍃 🤛 ✂️

class Jeux():
    continues = True

def Shifumi():

    Jeux.continues = True

    def banner():
        system("clear")
        print(Color.green_bold)
        tprint("Shifumi")


    def Test_Gagnant(user):
        
        #On teste la validité de la réponse
        try:
            user = int(user)
        except:
            return False
        
        if user < 1 or user > 3:
            return False
        """
            1 : Pièrre
            2 : Feuilles
            3 : Ciseaux
        """
        egal = True

        # On recomence le test avec un nombre diférent en cas d'égalité.
        while egal:
            bot = random.randint(1,3)
            #On teste toute les possibilités ✅❌

            #Pièrres
            if user == 1 and bot == 2:
                return Color.red_bold+"   [❌] La Pièrre n'a aucune chance face à la Feuille"
            elif user == 1 and bot == 3:
                return Color.green_bold+"     [✅] La Pièrre bat les Ciseaux !"

            #Feuilles
            elif user == 2 and bot == 1:
                return Color.green_bold+"     [✅] La Feuille bat la Pièrre !"
            elif user == 2 and bot == 3:
                return Color.red_bold+"   [❌] La Feuille n'a aucune chance face aux Ciseaux"

            #Ciseaux
            elif user == 3 and bot == 1:
                return Color.red_bold+"   [❌] Les Ciseaux n'ont aucune chance face à la Pièrre"
            elif user == 3 and bot == 2:
                return Color.green_bold+"     [✅] Les Ciseaux bat la Feuille !"

    def play():
        banner()
        print(Color.yellow_bold+"  1,2,3 Pièrre🤛, Feuilles🍃, Ciseaux ✂️ !\n")
        print(Color.red_bold+"        [1] "+Color.white_bold+"Pièrres"+Color.red_bold+"       [2] "+Color.white_bold+"Feuilles"+Color.red_bold+"       [3] "+Color.white_bold+"Ciseaux")

        choix = input(Color.cyan_bold+"\n     [?]"+Color.white_bold+"Choissiez une chiffre "+Color.blue_bold)
        result = Test_Gagnant(choix)
        if result == False:
            Jeux.continues = False
        else:
            print(result)
            fin = input("")


    while Jeux.continues:
        play()