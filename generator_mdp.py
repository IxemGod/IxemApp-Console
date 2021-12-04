import random
import string
import os
from art import *
from couleur import *
from tkinter import *
import webbrowser
import pyperclip as pc


def Password_Generator():

	def banner():
		system("clear")
		print(Color.orange_bold)
		tprint("Generateur de\n"+" "*0+"Mot de Passe")
		tail = input(Color.cyan_bold+"		[?]"+Color.white_bold+" Entrez la longeur. "+Color.blue_bold)

		try:
			tail = int(tail)
			result = ""
			Alpha = string.ascii_letters + string.digits + string.punctuation
			for i in range(tail):
				result+=random.choice(Alpha)
			print(Color.yellow_bold+"	Résultat : "+Color.red_bold+result+Color.grey_bold+" (Mdp copié dans le presse-papier)")
			pc.copy(result)
		except:
			print(Color.red_bold+"	[/!\\]"+Color.white_bold+" Merci de rentrez un nombre")

	banner()
	fin = input("")