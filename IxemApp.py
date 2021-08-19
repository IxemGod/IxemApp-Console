# -*- coding: utf8 -*

import socket
from os import system, name, path
import time
from couleur import *
from traducteur import *
from luna import Luna

def clear():
    system('clear')

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
    print(Color.yellow_bold+"""
       #####     
       #    #   ##   
       #     #        ###   #   #  #   #   ###  #   #  #    #   #  ###  #      ###  #    #  ####
       ######   ##   #   #  ##  #  #   #  #   # ##  #  #    #  #  #   #  #    #     #    #  #   #
       #    #   ##   ####   # # #   # #   ####  # # #  #    #  #  ####   #     #    #    #  ####
       #     #  ##   #      #  ##   # #   #     #  ##  #    #  #  #      #      #   #    #  #  #
       ######   ##    ###   #   #    #     ###  #   #   #####   #  ###  #    ###     #####  #   #

                                   ######                         ####
                                     ##    #   #  ###   #     #  #    #  ###   ###    ##
                                     ##     # #  #   #  ##   ##  #    #  #  #  #  #   ##
                                     ##      #   ####   # # # #  ######  #  #  #  #   ##
                                     ##     # #  #      #  #  #  #    #  ###   ###    ##
                                   ######  #   #  ###   #     #  #    #  #     #      
                                                                         #     #      ##

       """)




def menu():

    #Affichage de l'introduction à IxemApp.
    print("              "+Color.orange_bold+"Salut à toi jeune entrepreneur !\n")
    print(Color.blue_bold+"    IxemApp est une application qui à été développer par IxemGod et qui était c"+'\u0332'+"e"+'\u0332'+"n"+'\u0332'+"s"+'\u0332'+"é"+'\u0332'+" être conçu pour Windows.")
    print(Color.blue_bold+"    Mais IxemGod à découvert le monde incroyable de Linux ! Il à donc installer Ubuntu et il ne souhaite pour rien au monde revenir à Windows !\n")
    print(Color.cyan_bold+"         [i]"+Color.white_bold+" IxemApp ne verra plus de mise à jours pour Windows. Si ça marche, tant mieux mais sinon tant pis !\n\n")


    print(Color.green_bold+"       Rentrons dans le vive du sujet ! Choisi ce que tu souahite faire !\n")

    #Affichage des choix de programme.
    print(Color.red_bold+"                 [1] "+Color.white_bold+"""Traducteur 1M+"""+Color.red_bold+"           [10] "+Color.white_bold+"""Allumêtte
      """+Color.red_bold+"           [2] "+Color.white_bold+"""Luna"""+Color.red_bold+"                     [11] "+Color.white_bold+"""Shifumi
      """+Color.red_bold+"           [3] "+Color.white_bold+"""Convertisseur de Temps"""+Color.red_bold+"   [12] "+Color.white_bold+"""Plus ou Moins
      """+Color.red_bold+"           [4] "+Color.white_bold+"""Traducteur Verlent"""+Color.red_bold+"       [13] "+Color.white_bold+"""Générateur de Mot de Passe
      """+Color.red_bold+"           [5] "+Color.white_bold+"""Traducteur RL"""+Color.red_bold+"            [14] "+Color.white_bold+"""Liste de Diviseur
      """+Color.red_bold+"           [6] "+Color.white_bold+"""Puissance IV"""+Color.red_bold+"             [15] "+Color.white_bold+"""Générateur de Mot de Passe
      """+Color.red_bold+"           [7] "+Color.white_bold+"""Cypteur de Fichier"""+Color.red_bold+"       [16] "+Color.white_bold+"""Exercice sur les Airs
      """+Color.red_bold+"           [8] "+Color.white_bold+"""Calculatrice"""+Color.red_bold+"             [17] "+Color.white_bold+"""Exercice sur les Volumes
      """+Color.red_bold+"           [9] "+Color.white_bold+"""Exercice Géométrie"""+Color.red_bold+"       [18] "+Color.white_bold+"""Exercice sur les Périmêtres


      """)
    
    choix = input(Color.cyan_bold+"   [?]"+Color.white_bold+" Tape le numéro de ton choix. "+ Color.blue_bold)
    if choix == 1 or choix == "1":
        # chargement()
        traducteur_1M()
        return

    if choix == 2 or choix == "2":
        # chargement()
        Luna()
        return


while 'lol' == 'lol':
    clear()
    banner()
    menu()