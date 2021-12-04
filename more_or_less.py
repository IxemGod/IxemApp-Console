import random
import os
from art import *
from couleur import *

def PlusOuMoins():

    def banner():
        system("clear")
        print(Color.pink_bold)
        tprint("Plus ou Moins")

    def play():
        Nbr_a_trouver = random.randint(1,100)
        vie = 10

        while True:
            if vie <= 0:
                return Color.red_bold+f"\n    [❌] Perdu ! La réponse était : {Color.yellow_bold}{Nbr_a_trouver}{Color.red_bold}."
            vie -= 1

            Nbr_user = input(Color.cyan_bold+"  [?]"+Color.white_bold+" Entrez un nombre. "+Color.blue_bold)

            try:
                Nbr_user = int(Nbr_user)

                if Nbr_user < Nbr_a_trouver:
                    print(Color.yellow_bold+f"\n   C'est plus ↗️ ! Vie restante : {Color.red_bold}{vie}{Color.yellow_bold}.\n")
                elif Nbr_user > Nbr_a_trouver:
                    print(Color.yellow_bold+f"\n   C'est moins ↘️ ! Vie restante : {Color.red_bold}{vie}{Color.yellow_bold}.\n")
                elif Nbr_user == Nbr_a_trouver:
                    return Color.green_bold+f"\n    [✅] Gagné ! La réponse était : {Color.yellow_bold}{Nbr_a_trouver}{Color.green_bold}."
            except:
                print(Color.red_bold+f"    [❌] Saisi Incorect.")





    banner()
    print(play())
    fin = input("")
