from art import *
import pyperclip as pc
from couleur import *
import os

def Morse():

	def banner():
		system("clear")
		print(Color.yellow_bold)
		tprint("Code Morse")


	def coder():
		phrase = input(Color.cyan_bold+"	[?]"+Color.white_bold+" Tapez votre phrase. "+Color.blue_bold)
		phrase = phrase.upper()
		result = ""
		DicoMorse = {"A" : ".-", "B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","k":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-", "U":"..-", "V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","0":"-----"}	
		for lettre in phrase:
			if lettre in DicoMorse:
				result = result+" "+DicoMorse[lettre]
			elif lettre == " ":
				result = result+" / "
			else:
				result = result+"?"
		return result



	def decoder():
		phrase = input(Color.cyan_bold+"	[?]"+Color.white_bold+" Tapez votre phrase. "+Color.blue_bold)
		phrase = phrase.split(" ")
		result = ""
		DicoMorse = {".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E","..-.":"F","--.":"G","....":"H","..":"I",".---":"J","-.-":"k",".-..":"L","--":"M","-.":"N","---":"O",".--.":"P","--.-":"Q",".-.":"R","...":"S","-":"T","..-":"U","...-":"V",".--":"W","-..-":"X","-.--":"Y","--..":"Z",".----":"1","..---":"2","...--":"3","....-":"4",".....":"5","-....":"6","--...":"7","---..":"8","----.":"9","-----":"0"}
		for mot in phrase:
			if mot in DicoMorse:
				result = result+DicoMorse[mot]
			elif mot == "/":
				result = result+" "
		return result


	def menu():
		banner()
		print(Color.green_bold+ "Que voulez vous faire ?\n\n")
		print(Color.red_bold+"		[1]"+Color.white_bold+" Coder 	"+Color.red_bold+"[2]"+Color.white_bold+" Décoder\n\n")
		choix = input(Color.cyan_bold+"[?]"+Color.white_bold+" Choisissez un chiffre. "+Color.blue_bold)

		if choix == 1 or choix == "1":
			result = coder()
			print(Color.yellow_bold+"Voici le résultat : "+Color.red_bold+result+Color.grey_bold+"(Résultat copié dans le presse-papier)")
			pc.copy(result)
			fin = input("")
		elif choix == 2 or choix == "2":
			result = decoder()
			print(Color.yellow_bold+"Voici le résultat : "+Color.red_bold+result+Color.grey_bold+"(Résultat copié dans le presse-papier)")
			pc.copy(result)
			fin = input("")
		else:
			return



	menu()