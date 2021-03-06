import math
from couleur import *
from os import system, name, path
from art import *


def banner():
    system('clear')
    print(Color.green_bold)
    tprint("Convertisseur \n"+" "*15+"de Temps")
    

def ConvertisseurTemps():
    banner()
    print(Color.red_bold+'                 [1]'+Color.white_bold+'Seconde'+Color.red_bold+"           [5] "+Color.white_bold+"Semaine")
    print(Color.red_bold+'                 [2]'+Color.white_bold+'Minute'+Color.red_bold+"            [6] "+Color.white_bold+"Mois")
    print(Color.red_bold+'                 [3]'+Color.white_bold+'Heure'+Color.red_bold+"             [7] "+Color.white_bold+"Année") 
    print(Color.red_bold+'                 [4]'+Color.white_bold+'Jours')
    print('\n\n')

    # Ici on reviens au menu principal D'IxemApp car l'unité n'est pas un chiffre.
    try:
        Choix1 = int(input(Color.cyan_bold+"   [?]"+Color.white_bold+"Choisissez une unité. "+Color.blue_bold))
    except:
        return

    # Si le nombre rentré est inférieur à 1 et Supérieur à 7, alors on reviens au menu principal D'IxemApp
    if Choix1 < 1 or Choix1 > 7:
        return

    print('\n')
    entrer = int(input(Color.cyan_bold+"   [?]"+Color.white_bold+"Tapez un chifre. "+Color.blue_bold))
    print('\n\n')
    print(Color.red_bold+'                 [1]'+Color.white_bold+'Seconde'+Color.red_bold+"           [5] "+Color.white_bold+"Semaine")
    print(Color.red_bold+'                 [2]'+Color.white_bold+'Minute'+Color.red_bold+"            [6] "+Color.white_bold+"Mois")
    print(Color.red_bold+'                 [3]'+Color.white_bold+'Heure'+Color.red_bold+"             [7] "+Color.white_bold+"Année") 
    print(Color.red_bold+'                 [4]'+Color.white_bold+'Jours') 
    print('\n')
    
    # Ici on reviens au menu principal D'IxemApp car l'unité n'est pas un chiffre.
    try:
        Choix2 = int(input(Color.cyan_bold+"   [?]"+Color.white_bold+"Choisissez une unité. "+Color.blue_bold))
    except:
        return

    # Si le nombre rentré est inférieur à 1 et Supérieur à 7, alors on reviens au menu principal D'IxemApp
    if Choix2 < 1 or Choix2 > 7:
        return

    print(Color.orange_bold+'\n\n')
    seconde = 0
    minute = 0
    heure = 0
    jour = 0
    semaine = 0
    mois = 0
    year = 0

    

    #Convertire année en secondes
    if Choix1 == 7 and Choix2 == 1:
        annee = entrer
        result = annee*365 * 24 * 60 *60
        print(f"        "+f'Dans {entrer} années il y à {result} secondes.')

    #Convertire année en minutes
    elif Choix1 == 7 and Choix2 == 2:
        annee = entrer
        result = annee*365 *24 * 60
        print(f"        "+f'Dans {entrer} années il y à {result} minutes.')

    #Convertire année en heures
    elif Choix1 == 7 and Choix2 == 3:
        annee = entrer
        result = annee*365 * 24
        print(f"        "+f'Dans {entrer} années il y à {result} heures.')

    #Convertire année en jours
    elif Choix1 == 7 and Choix2 == 4:
        annee = entrer
        result = annee*365
        print(f"        "+f'Dans {entrer} années il y à {result} jours.')

    #Convertire année en semaine
    elif Choix1 == 7 and Choix2 == 5:
        annee = entrer
        result = annee*52
        print(f"        "+f'Dans {entrer} années il y à {result} semaines.')

    #Convertire année en mois
    elif Choix1 == 7 and Choix2 == 6:
        annee = entrer
        result = annee*12
        print(f"        "+f'Dans {entrer} années il y à {result} mois.')

    #Convertire année en mois
    elif Choix1 == 7 and Choix2 == 7:
        annee = entrer
        result = annee
        print(f"        "+f'Dans {entrer} années il y à {result} années.')



    #Convertire mois en secondes
    elif Choix1 == 6 and Choix2 == 1:
        mois = entrer
        result = mois*30.5 * 24 * 60 *60
        print(f"        "+f'Dans {entrer} mois il y à {result} secondes.')

    #Convertire mois en minutes
    elif Choix1 == 6 and Choix2 == 2:
        mois = entrer
        result = mois*30.5 *24 * 60
        print(f"        "+f'Dans {entrer} mois il y à {result} minutes.')

    #Convertire moisen heures
    elif Choix1 == 6 and Choix2 == 3:
        mois = entrer
        result = mois*30.5 * 24
        print(f"        "+f'Dans {entrer} mois il y à {result} heures.')

    #Convertire mois en jours
    elif Choix1 == 6 and Choix2 == 4:
        mois = entrer
        result = mois*30.5
        print(f"        "+f'Dans {entrer} mois il y à {result} jours.')

    #Convertire mois en semaine
    elif Choix1 == 6 and Choix2 == 5:
        mois = entrer
        result = mois*4
        print(f"        "+f'Dans {entrer} mois il y à {result} semaines.')

    #Convertire mois en mois
    elif Choix1 == 6 and Choix2 == 6:
        mois = entrer
        result = mois
        print(f"        "+f'Dans {entrer} mois il y à {result} mois.')

    #Convertire mois en année
    elif Choix1 == 6 and Choix2 == 7:
        mois = entrer
        result = mois / 12
        print(f"        "+f'Dans {entrer} mois il y à {result} années.')


        #Convertire semaines en secondes
    elif Choix1 == 5 and Choix2 == 1:
        semaines = entrer
        result = semaines*7 * 24 * 60 *60
        print(f"        "+f'Dans {entrer} semaines il y à {result} secondes.')

    #Convertire semaines en minutes
    elif Choix1 == 5 and Choix2 == 2:
        semaines = entrer
        result = semaines*7 *24 * 60
        print(f"        "+f'Dans {entrer} semaines il y à {result} minutes.')

    #Convertire semaines en heures
    elif Choix1 == 5 and Choix2 == 3:
        semaines = entrer
        result = semaines*7 * 24
        print(f"        "+f'Dans {entrer} semaines il y à {result} heures.')

    #Convertire semaines en jours
    elif Choix1 == 5 and Choix2 == 4:
        semaines = entrer
        result = semaines*7
        print(f"        "+f'Dans {entrer} semaines il y à {result} jours.')

    #Convertire semaines en semaine
    elif Choix1 == 5 and Choix2 == 5:
        semaines = entrer
        result = semaines
        print(f"        "+f'Dans {entrer} semaines il y à {result} semaines.')

    #Convertire semaines en mois
    elif Choix1 == 5 and Choix2 == 6:
        semaines = entrer
        result = semaines/4
        print(f"        "+f'Dans {entrer} semaines il y à {result} mois.')

    #Convertire semaines en année
    elif Choix1 == 5 and Choix2 == 7:
        semaines = entrer
        result = semaines / 52
        print(f"        "+f'Dans {entrer} semaines il y à {result} années.')


    #Convertire jours en secondes
    elif Choix1 == 4 and Choix2 == 1:
        jours = entrer
        result = jours * 24 * 60 * 60
        print(f"        "+f'Dans {entrer} jours il y à {result} secondes.')

    #Convertire jours en minutes
    elif Choix1 == 4 and Choix2 == 2:
        jours = entrer
        result = jours*24 * 60
        print(f"        "+f'Dans {entrer} jours il y à {result} minutes.')

    #Convertire jours en heures
    elif Choix1 == 4 and Choix2 == 3:
        jours = entrer
        result = jours*24
        print(f"        "+f'Dans {entrer} jours il y à {result} heures.')

    #Convertire jours en jours
    elif Choix1 == 4 and Choix2 == 4:
        jours = entrer
        result = jours
        print(f"        "+f'Dans {entrer} jours il y à {result} jours.')

    #Convertire jours en semaine
    elif Choix1 == 4 and Choix2 == 5:
        jours = entrer
        result = jours/7
        print(f"        "+f'Dans {entrer} jours il y à {result} semaines.')

    #Convertire jours en mois
    elif Choix1 == 4 and Choix2 == 6:
        jours = entrer
        result = jours/(7*4)
        print(f"        "+f'Dans {entrer} jours il y à {result} mois.')

    #Convertire jours en année
    elif Choix1 == 4 and Choix2 == 7:
        jours = entrer
        result = jours/(7*4*12)
        print(f"        "+f'Dans {entrer} jours il y à {result} années.')



        #Convertire heures en secondes
    elif Choix1 == 3 and Choix2 == 1:
        heures = entrer
        result = heures*60 *60
        print(f"        "+f'Dans {entrer} heures il y à {result} secondes.')

    #Convertire heures en minutes
    elif Choix1 == 3 and Choix2 == 2:
        heures = entrer
        result = heures* 60
        print(f"        "+f'Dans {entrer} heures il y à {result} minutes.')

    #Convertire heures en heures
    elif Choix1 == 3 and Choix2 == 3:
        heures = entrer
        result = heures
        print(f"        "+f'Dans {entrer} heures il y à {result} heures.')

    #Convertire heures en jours
    elif Choix1 == 3 and Choix2 == 4:
        heures = entrer
        result = heures/24
        print(f"        "+f'Dans {entrer} heures il y à {result} jours.')

    #Convertire heures en semaine
    elif Choix1 == 3 and Choix2 == 5:
        heures = entrer
        result = heures/(7*24)
        print(f"        "+f'Dans {entrer} heures il y à {result} semaine.')

    #Convertire heures en mois
    elif Choix1 == 3 and Choix2 == 6:
        heures = entrer
        result = heures/(4*7*24)
        print(f"        "+f'Dans {entrer} heures il y à {result} mois.')

    #Convertire heures en année
    elif Choix1 == 3 and Choix2 == 7:
        heures = entrer
        result = heures /(12*7*4*24)
        print(f"        "+f'Dans {entrer} heures il y à {result} années.')




        #Convertire minutes en secondes
    elif Choix1 == 2 and Choix2 == 1:
        minutes = entrer
        result = minutes*60
        print(f"        "+f'Dans {entrer} minutes il y à {result} secondes.')

    #Convertire minutes en minutes
    elif Choix1 == 2 and Choix2 == 2:
        minutes = entrer
        result = minutes
        print(f"        "+f'Dans {entrer} minutes il y à {result} minutes.')

    #Convertire minutes en heures
    elif Choix1 == 2 and Choix2 == 3:
        minutes = entrer
        result = minutes/60
        print(f"        "+f'Dans {entrer} minutes il y à {result} heures.')

    #Convertire minutes en jours
    elif Choix1 == 2 and Choix2 == 4:
        minutes = entrer
        result = minutes/(24*60)
        print(f"        "+f'Dans {entrer} minutes il y à {result} jours.')

    #Convertire minutes en semaine
    elif Choix1 == 2 and Choix2 == 5:
        minutes = entrer
        result = minutes/(7*24*60)
        print(f"        "+f'Dans {entrer} minutes il y à {result} semaine.')

    #Convertire minutes en mois
    elif Choix1 == 2 and Choix2 == 6:
        minutes = entrer
        result = minutes/(4*7*24*60)
        print(f"        "+f'Dans {entrer} minutes il y à {result} mois.')

    #Convertire minutes en année
    elif Choix1 == 2 and Choix2 == 7:
        minutes = entrer
        result = minutes /(12*7*4*24*60)
        print(f"        "+f'Dans {entrer} minutes il y à {result} années.')


        #Convertire secondes en secondes
    elif Choix1 == 1 and Choix2 == 1:
        secondes = entrer
        result = secondes
        print(f"        "+f'Dans {entrer} secondes il y à {result} secondes.')

    #Convertire secondes en minutes
    elif Choix1 == 1 and Choix2 == 2:
        secondes = entrer
        result = secondes/60
        print(f"        "+f'Dans {entrer} secondes il y à {result} minutes.')

    #Convertire secondes en heures
    elif Choix1 == 1 and Choix2 == 3:
        secondes = entrer
        result = secondes/(60*60)
        print(f"        "+f'Dans {entrer} secondes il y à {result} heures.')

    #Convertire secondes en jours
    elif Choix1 == 1 and Choix2 == 4:
        secondes = entrer
        result = secondes/(24*60*60)
        print(f"        "+f'Dans {entrer} secondes il y à {result} jours.')

    #Convertire secondes en semaine
    elif Choix1 == 1 and Choix2 == 5:
        secondes = entrer
        result = secondes/(7*24*60*60)
        print(f"        "+f'Dans {entrer} secondes il y à {result} semaine.')

    #Convertire secondes en mois
    elif Choix1 == 1 and Choix2 == 6:
        secondes = entrer
        result = secondes/(4*7*24*60*60)
        print(f"        "+f'Dans {entrer} secondes il y à {result} mois.')

    #Convertire secondes en année
    elif Choix1 == 1 and Choix2 == 7:
        secondes = entrer
        result = secondes /(12*7*4*24*60*60)
        print(f"        "+f'Dans {entrer} secondes il y à {result} années.')

    else:
        return
    lol = input('')