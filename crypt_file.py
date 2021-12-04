import pyAesCrypt
from art import *
import os
from couleur import *

def Crypt_File():

    def banner():
        system("clear")
        print(Color.grey_bold)
        tprint("Crypter \n"+" "*20+"de    Fichier")

    def encrypt(file, password, bufferSize):
        try:
            pyAesCrypt.encryptFile(file, "C"+file, password, bufferSize)
            return Color.green_bold+"   [✅] Votre fichier a bien été Crypté"
        except ValueError as err:
            resultErr = str(err)
            if resultErr == "Unable to read input file.":
                return Color.red_bold+"   [❌] Fichier Inexistant."

    def decrypt(file, password, bufferSize):
        try:
            pyAesCrypt.decryptFile(file, "D"+file, password, bufferSize)
            return Color.green_bold+"   [✅] Votre fichier a bien été Décrypté"
        except ValueError as err:
            resultErr = str(err)
            if resultErr == "Wrong password (or file is corrupted).":
                return Color.red_bold+"   [❌] Le mot de passe est incorrecte."
            elif resultErr == "Unable to read input file.":
                return Color.red_bold+"   [❌] Fichier Inexistant."
                
    banner()
    print(Color.red_bold+"            [1] "+Color.white_bold+"Crypter"+Color.red_bold+"           [2] "+Color.white_bold+"Décrypter\n")
    choice = str(input(Color.cyan_bold+"    [?]"+Color.white_bold+" Choisissez un chiffre "+Color.blue_bold))

    file = str(input(Color.cyan_bold+"    [?]"+Color.white_bold+" Nom du fichier : "+Color.blue_bold))
    password = str(input(Color.cyan_bold+"    [?]"+Color.white_bold+" Mot de passe : "+Color.blue_bold))

    bufferSize = 64 * 1024

    if choice == "1" or choice == 1:
        print(encrypt(file, password, bufferSize))
        fin = input("")
    elif choice == "2" or choice == 2:
        print(decrypt(file, password, bufferSize))
        fin = input("")