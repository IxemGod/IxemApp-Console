""" Un menu apparait avec plusieur option :

    Coder avec un décalage
    Décoder avec un décalage

"""
from art import *
from couleur import *
import os
import string
import pyperclip as pc

def Cesare():


    def banner():
        system("clear")
        print(Color.pink_bold)
        tprint("Code Cesare")



    def menu():
        banner()
        print(Color.red_bold+"      [1]"+Color.white_bold+" Coder"+Color.red_bold+"     [2]"+Color.white_bold+" Décoder")
        choix = input(Color.cyan_bold+"\n[?]"+Color.white_bold+"Tapez un chiffre. "+Color.blue_bold)

        if choix == 1 or choix == "1":
            banner()
            sentence = input(Color.cyan_bold+"      [?]"+Color.white_bold+" Tapez votre phrase. "+Color.blue_bold)
            key = int(input(Color.cyan_bold+"      [?]"+Color.white_bold+" Tapez votre décalage. "+Color.blue_bold))
            result = crypt(key,sentence)
            banner()
            print(Color.yellow_bold+"Résultat"+Color.red_bold+result+Color.grey_bold+" (Résultat copié dans le presse-papier)")
            pc.copy(result)
            fin  = input("")
        elif choix == 2 or choix == "2":
            banner()
            sentence = input(Color.cyan_bold+"      [?]"+Color.white_bold+" Tapez votre phrase. "+Color.blue_bold)
            key = int(input(Color.cyan_bold+"      [?]"+Color.white_bold+" Tapez votre décalage. "+Color.blue_bold))
            result = uncrypt(key, sentence)
            print(Color.yellow_bold+"Résultat"+Color.red_bold+result+Color.grey_bold+" (Résultat copié dans le presse-papier)")
            pc.copy(result)
            fin = input("")
        else:
            return

    def crypt(key:int,sentence):
        all_chars = "tYc(zlBo8G4IuH~`Kv'*ajp@Fh{s]qm1OULA}RT-b"+'"EC!g%D+i,&X06k^[NZ>y;ew7$Mx:3PVSn|WfdJ.Q5_2#)<r/?9='
        New_Alpha = {}
        posi = int(key) - 1
        for i in range(len(all_chars)):
            posi = posi +1
            if int(posi) >= 93:
                posi = 0
            New_Alpha[all_chars[i]] = all_chars[posi]

        result = ""
        for letter in sentence:
            if letter == " ":
                result = result + " "
            else:
                result = result + New_Alpha[letter]
        return result


    def uncrypt(key : int, sentence):

        all_chars = "tYc(zlBo8G4IuH~`Kv'*ajp@Fh{s]qm1OULA}RT-b"+'"EC!g%D+i,&X06k^[NZ>y;ew7$Mx:3PVSn|WfdJ.Q5_2#)<r/?9='
        New_Alpha = {}
        posi = int(key) -1
        for i in range(len(all_chars)):
            posi = posi +1
            if int(posi) >= 93:
                posi = 0
            New_Alpha[all_chars[posi]] = all_chars[i]
        
        result = ""
        for letter in sentence:
            if letter == " ":
                result = result + " "
            else:
                result = result + New_Alpha[letter]

        return result


    menu()

