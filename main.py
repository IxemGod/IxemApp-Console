# -*- coding: utf8 -*

import socket
from os import system, name, path
import time
from couleur import *
from traducteur import *
from luna import Luna
from convertisseur_temps import *
from verlant import *
from art import *
from puissance4 import *
from calculatrice import *
from geometry import *
from allumettes import *
from shifumi import *
from crypt_file import *
from more_or_less import *
from generator_mdp import *
from code_cesare import *
from morse import *
from weather import *
from ip_info import *
from jeux import *


#✅ ❌ ↗️ ↘️

"""

Truc à réglé :

	Vérifié tout les calcules du convvertisseur de temps

"""


def chargement():
    #Affichage de l'annimation de chargement. Il n'y à pas vraiment de temps de chargements mais c'est plus cool avec ^^ !
    for i in range(2):
        clear()
        print(Color.white_bold+ "Chargement du programme.....[/]")
        time.sleep(0.3)
        clear()
        print("Chargement du programme.....[-]")
        time.sleep(0.3)
        clear()
        print("Chargement du programme.....[\\]")
        time.sleep(0.3)
        clear()
        print("Chargement du programme.....[|]")
        time.sleep(0.3)



def banner():
    system('clear')
    print(Color.yellow_bold)
    tprint("IxemApp")




def menu():

    #Affichage de l'introduction à IxemApp.
    print("    "+Color.green_bold+"Salut à toi jeune entrepreneur ! Bienvenu(e) dans IxemApp !\n")

    #Affichage des choix de programme.
    print(Color.red_bold+"            [1] "+Color.white_bold+"Traducteur 1M+"+Color.red_bold+"           [2] "+Color.white_bold+"Luna")
    print(Color.red_bold+"            [3] "+Color.white_bold+"Convertisseur de Temps"+Color.red_bold+"   [4] "+Color.white_bold+"Traducteur Verlent")
    print(Color.red_bold+"            [5] "+Color.white_bold+"Allumêtte"+Color.red_bold+"                [6] "+Color.white_bold+"Plus ou Moins")
    print(Color.red_bold+"            [7] "+Color.white_bold+"Shifumi"+Color.red_bold+"                  [8] "+Color.white_bold+"Générateur de Mot de Passe")
    print(Color.red_bold+"            [9] "+Color.white_bold+"Puissance IV"+Color.red_bold+"             [10] "+Color.white_bold+"Code Césare")
    print(Color.red_bold+"            [11] "+Color.white_bold+"Cypteur de Fichier"+Color.red_bold+"      [12] "+Color.white_bold+"Exercice Géométrie")
    print(Color.red_bold+"            [13] "+Color.white_bold+"Calculatrice"+Color.red_bold+"            [14] "+Color.white_bold+"Code Morse")
    print(Color.red_bold+"            [15] "+Color.white_bold+"Weather"+Color.red_bold+"                 [16] "+Color.white_bold+"Info ip")
    print(Color.red_bold+"            [17] "+Color.white_bold+"Pong"+Color.red_bold+"                    [18] "+Color.white_bold+"Flappy")
    print(Color.red_bold+"            [19] "+Color.white_bold+"Paint"+Color.red_bold+"                   [20] "+Color.white_bold+"Snake")
    
    choix = input(Color.cyan_bold+"\n   [?]"+Color.white_bold+" Tape le numéro de ton choix. "+ Color.blue_bold)
    if choix == 1 or choix == "1":
        traducteur_1M()
    elif choix == 2 or choix == "2":
        Luna()
    elif choix == 3 or choix == "3":
        ConvertisseurTemps()
    elif choix== 4 or choix == "4":

        Verlant()
    elif choix== 5 or choix == "5":
        Allumette()
    elif choix== 6 or choix == "6":
        PlusOuMoins()
    elif choix== 7 or choix == "7":
        Shifumi()
    elif choix== 8 or choix == "8":
        Password_Generator()
    elif choix== 9 or choix == "9":
        Puissance4()
    elif choix== 10 or choix == "10":
        Cesare()
    elif choix== 11 or choix == "11":
        Crypt_File()
    elif choix== 12 or choix == "12":
        Geometrie()
    elif choix== 13 or choix == "13":
        Calculatrice()
    elif choix== 14 or choix == "14":
        Morse()
    elif choix== 15 or choix == "15":
        Weather()
    elif choix==16 or choix == "16":
    	InfoIp()
    elif choix==17 or choix == "17":
        Jeux_Pong()
    elif choix==18 or choix == "18":
        Jeux_Flappy()
    elif choix==19 or choix == "19":
        Jeux_Paint()
    elif choix==20 or choix == "20":
        Jeux_Snake()


while True:
    banner()
    menu()