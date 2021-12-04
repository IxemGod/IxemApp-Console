# -*- coding: utf8 -*
from couleur import *
import socket
from os import system, name, path
import time
import random
from art import *


def banner():
    system('clear')
    print(Color.green_bold)
    tprint("Verlant")

def Verlant():
    banner()
    phrase = input(Color.cyan_bold+"      [?]"+Color.white_bold+'Tapez votre phrase à traduire. '+Color.blue_bold)
    phrase = phrase.split(" ")
    phrase.reverse()
    resultat = " ".join(phrase)
    print(Color.purple_bold+"      [output] "+Color.white_bold+resultat)
    lol = input('')