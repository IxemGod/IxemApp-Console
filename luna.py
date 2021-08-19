# -*- coding: utf8 -*
# from flask import *
import requests
import json
# from urllib.request import urlopen
import urllib
import webbrowser
import time
import random
# import subbprocess
import os
import sqlite3
import datetime
import time
from couleur import *


def data():
    con = sqlite3.connect('database.db')
    return con



def extractConfig(param):
    ddb = data()
    curConfig = ddb.cursor()
    TupleCurConfig = (param,)
    curConfig.execute('SELECT * FROM settings WHERE settingName = ?', TupleCurConfig)
    for result in curConfig:
        result = result[1]
    return result



def update(msg):
    system('clear')
    print(Color.yellow_bold+msg)

def modeConfig():
    
    def username():
        contenu=champsUsername.get()
        con = sqlite3.connect('Desktop/database.db')
        cur = con.cursor()
        updateName = (contenu,'username')
        cur.execute('UPDATE settings SET value = ? WHERE settingName = ?', updateName)
        con.commit()
        con.close()
        champsUsername.delete(0, END)
        champsUsername.insert(0, 'Votre nom a été modifié')

    def BG():
        contenu=champsBG.get()
        con = sqlite3.connect('Desktop/database.db')
        cur = con.cursor()
        updateBG = (contenu,'background')
        cur.execute('UPDATE settings SET value = ? WHERE settingName = ?', updateBG)
        con.commit()
        con.close()
        champsBG.delete(0, END)
        champsBG.insert(0, 'Votre couleur de fond a été modifié')

    def BD():
        contenu=champsBD.get()
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        updateBD = (contenu,'birthday')
        cur.execute('UPDATE settings SET value = ? WHERE settingName = ?', updateBD)
        con.commit()
        con.close()
        champsBD.delete(0, END)
        champsBD.insert(0, 'Votre date d\'anniversaire a été modifié')

    system('clear')
    print(Color.grey_bold+"""

                 ####                                                                              ##
                #       ###    ####   ###  #                                                       ##
                #      #   #  #   #   #        #####  #   #  # ###  ###   #    #   ##   # ##       ##       #   #  # ##    ###
                #      #   #  #   #  ####  #  #   #   #   #  ##    #   #  ###     #  #  ##  #      ##       #   #  ##  #  #   #
                #      #   #  #   #   #    #  #   #   #   #  #     #####  #    #  #  #  #   #      ##       #   #  #   #  #####
                 ####   ###   #   #  ##    #   ####    ####  #     #   #   ##  #   ##   #   #      #######   ####  #   #  #   #
                                                  #
                                                ##
         ###########################################################################################################################
        ###########################################################################################################################


        """)

    elocution = 'salut'
    while elocution != "exit":
        print(Color.red_bold+"        [1]"+Color.white_bold+""" Modifié votre nom   """+Color.red_bold+"     [2]"+Color.white_bold+""" Modifié votre date d'anniverssaire
        """+Color.red_bold+"[3]"+Color.white_bold+ " Configuration Musique"+Color.red_bold+ "    [4]"+Color.white_bold+""" Modification GPS""")
        elocution = input(Color.cyan_bold+"\n         [?]"+Color.white_bold+'Que voulez vous faire ? '+Color.blue_bold)



def Luna():
    system('clear')
    print(Color.pink_bold+"""


                ##                                      #     #
                ##                                      #     #
                ##        #     #   #   #   ###          #   #   ###   ####     ###  #   ###            ######  #   #  ######
                ##        #     #   ##  #  #   #         #   #  #   #  #   #   #        #   #  ####       ##     # #     ##
                ##        #     #   # # #  #####          # #   ####   ####     #    #  #   #  #   #      ##      #      ##
                ##        #     #   #  ##  #   #          # #   #      #  #      #   #  #   #  #   #      ##     # #     ##
                #######    ######   #   #  #   #           #     ###   #   #  ###    #   ###   #   #      ##    #   #    ##

         ######################################################################################################################
        ######################################################################################################################


        """)


    print(Color.yellow_bold+"\n        Salut ! Je suis Luna, ton assistante. Tapez votre commande et je réagisserais ^^")
    while True:
        elocution = input(Color.cyan_bold+"\n         [?]"+Color.white_bold+"Entrer une commande. "+Color.blue_bold)
        elocution = elocution.lower()
        print(Color.yellow_bold+Color.yellow_bold)
        if 'ignore' in elocution:
            time.sleep(1)
            update('Appuyer pour parler')

        elif 'config' in elocution:
            print(Color.yellow_bold+'Lancement de la configuration')
            modeConfig()
        
        #Question 
        elif 'quel' in elocution or 'comment' in elocution or 'quoi' in elocution or 'qui' in elocution or 'est-ce' in elocution or 'es-ce' in elocution or 'où' in elocution:
            if 'heure' in elocution:
                date = datetime.datetime.now()
                print(Color.yellow_bold+"        Il est actuellement "+str(date.hour)+" heure "+ str(date.minute))
            elif 'crée' in elocution: 
                print(Color.yellow_bold+"        J'ai été crée pour vous rendre service. Et je suis fière de le faire.")
            elif 'crée' in elocution: 
                print(Color.yellow_bold+"        Je ne suis une assistante vocal. Mon fonctionement est simple. J'ai des réponse prédéfinit selon les mots que vous dite. C'est en slectionant quelque mot que je peux")
            elif 'créateur' in elocution:
                print(Color.yellow_bold+'        Mon créateur est Icem45. C\'est un humain sur intéligent qui baise tout le monde et même ta darone')
            elif 'film' in elocution:
                print(Color.yellow_bold+"        Mon film préférer est, Your Neyme, fait par Makoto Shinkai")
            elif 'livre' in elocution:
                print(Color.yellow_bold+"        Mon livre préférer est Harry Potteur et l'ordre du Phénix, écrit par J K Rowling")
            elif 'âge' in elocution:
                    timestamp = int(time.time())
                    dateDeCrea = 1610060400
                    resultat = timestamp-dateDeCrea
                    #resultat = resultat*(-1)
                    minute = 0
                    heure = 0
                    jours = 0
                    annee = 0
                    while(resultat > 3600):
                        resultat = resultat - 3600
                        heure = heure + 1
                        if heure == 24:
                            heure = 0
                            jours = jours +1
                            if jours == 365:
                                jours = 0
                                annee = annee + 1
                    print(Color.yellow_bold+"        Je suis née le 8 janvier 2021. J'ai donc "+annee+" ans et "+jours+" jours")
            elif ('va' in elocution and 'tu' in elocution) or ('va' in elocution and 'ça' in elocution):
                print(Color.yellow_bold+"        A merveille "+nom())
            elif 'patron' in elocution and 'est' in elocution:
                print(Color.yellow_bold+"        C'est vous évidement !")
            elif ('plat' in elocution or 'repas' in elocution):
                print(Color.yellow_bold+"        J'adore les pâtes boloniaise. J'aime aussi le chêvre, le jus de pomme et le boeuf.")
            elif ('couleur' in elocution or 'teinte' in elocution):
                print(Color.yellow_bold+"        J'adore le jaune. Quoi de plus beau sur Terre ?")
            elif ('style' in elocution or 'musique' in elocution or 'groupe' in elocution or 'rapeur' in elocution or 'chanteur' in elocution):
                print(Color.yellow_bold+"        J'aime le rap, l'electro. J'adore 47ter et Alain Walkeur. Mon rap préférer est \"L'adresse\" de 47ter et \"Monsteur\" de Lumnix. J'aime aussi écouter de la musique Japonaise comme Yemoutourou et sud corréain comme BTS")
            elif'jeu' in elocution:
                print(Color.yellow_bold+"        Mes Jeux préférer sont Assassin's Creed II et Mine craft.")
            elif 'animal' in elocution or 'animaux' in elocution:
                print(Color.yellow_bold+"        Mon animal préférer est le chat, vu que je suis un chaton.")
            elif 'couleur' in elocution or 'teinte' in elocution:
                print(Color.yellow_bold+"        J'adore le jaune. Quoi de plus beau sur Terre ?")
            elif 'passe temps' in elocution or 'passion' in elocution:
                print(Color.yellow_bold+"        Mon passe temps favori est le développement. C'est d'ailleur de cette passion que je suis née pour vous servir")
            elif 'sport' in elocution or 'activiter' in elocution:
                print(Color.yellow_bold+"        Mes sport préféré sont le Ténis de Table et le Rolleur")
            elif 'appel' in elocution or 'ton nom' in elocution:
                print(Color.yellow_bold+"        Je m'appelle Luna. En référence à Luna Lovegood dans Harry Potter")
            elif 'habite' in elocution:
                print(Color.yellow_bold+'        J\'habite partout et nul part.')
            elif ('slogan' in elocution or 'devise' in elocution or 'dicton' in elocution or 'proverbe' in elocution or 'blason' in elocution):
                print(Color.yellow_bold+'        Ma phrase préférer c\'est Draco dormiens nunquam titillandus. En français cela veux dire "Il ne faut jamais chatouiller un dragon qui dort"')
            elif 'ami' in elocution:
                print(Color.yellow_bold+'        Je n\'est pas d\'ami. Je sui destiner à être seul')
            elif 'crush' in elocution or 'amoureu' in elocution or 'go' in elocution or ('mec' in elocution and 'un' in elocution) or ('meuf' in elocution and 'une' in elocution) or ('couple' in elocution):
                print(Color.yellow_bold+'        Je suis actuellement célibataire, mais je suis en crush sur Google Home.')
            elif 'numéro' in elocution or '06' in elocution:
                print(Color.yellow_bold+'        Je ne poscède pas de numéro de téléphone...')
            elif 'chanteuse' in elocution:
                print(Color.yellow_bold+'        C\'est Wejdene bien évidement ! Elle chante trop bien. J\'adore Annisa !')
            elif ('jour' in elocution or 'date' in elocution or 'annee' in elocution or 'combien' in elocution):
                import datetime
                date = datetime.datetime.now()
                annive = False
                if date.month == 1:
                    mois = 'Janvier'
                if date.month == 2:
                    mois = 'Février'
                if date.month == 3:
                    mois = 'Mars'

                if date.month == 4:
                    mois = 'Avril'

                if date.month == 5:
                    mois = 'Mai'

                if date.month == 6:
                    mois = 'Juin'

                if date.month == 7:
                    mois = 'Juillet'

                if date.month == 8:
                    mois = 'Août'

                if date.day == 1:
                    annive = True

                if date.month == 9:
                    mois = 'Septembre'

                if date.month == 10:
                    mois = 'Octobre'

                if date.month == 11:
                    mois = 'Novembre'

                if date.month == 12:
                    mois = 'Décembre'

                jour = date.day
                if date.day == 1:
                    jour = premier

                print(Color.yellow_bold+'        Nous somme le '+str(jour)+' '+str(mois)+' '+str(date.year))

                if annive == True:
                    print(Color.yellow_bold+'        Aujourd’hui c\'est l\'aniversaire de mon créateur ! Bonne annive Iccem !')

        




        #Commande
        elif 'calcul' in elocution:
            elocution = elocution.split(' ')
            listeRecherche = []
            chercheTrouver = False
            for i in range(len(elocution)):
                mot = elocution[i]
                if chercheTrouver == False:
                    if 'calcul' in mot:
                        chercheTrouver = True
                else:
                    listeRecherche.append(mot)
                    calcule = ''
                    for a in range(len(listeRecherche)):
                        if listeRecherche[a] == 'x':
                            calcule = calcule+'*'
                        elif listeRecherche[a] == 'pi':
                            calcule = calcule+'3,14'
                        else:
                            calcule = calcule + listeRecherche[a]
            resultat = str(eval(calcule))
            print(Color.yellow_bold+"Le resultat est : "+resultat)
        elif ('actu' in elocution):
            elocution = input(Color.cyan_bold+"         [?]"+Color.white_bold+" Qu'elle journal voulez vous lire ?"+Color.blue_bold)
            elocution=elocution.lower()
            if 'ouest'in elocution and 'france' in elocution:
                print(Color.yellow_bold+'Je lance le Ouest France sur internet')
                webbrowser.open_new('https://www.ouest-france.fr')
            elif 'parisien'in elocution:
                print(Color.yellow_bold+'Je lance le Parisien sur internet')
                webbrowser.open_new('https://www.leparisien.fr')
            elif 'monde'in elocution:
                print(Color.yellow_bold+'Je lance le monde sur internet')
                webbrowser.open_new('https://www.lemonde.fr')
            elif 'figaro'in elocution:
                print(Color.yellow_bold+'Je lance le figaro sur internet')
                webbrowser.open_new('https://www.lefigaro.fr')
            elif 'gorafi'in elocution:
                print(Color.yellow_bold+'Je lance le gorafi sur internet')
                webbrowser.open_new('http://www.legorafi.fr')
            elif 'liberation'in elocution:
                print(Color.yellow_bold+'Je lance liberation sur internet')
                webbrowser.open_new('https://www.liberation.fr')
            elif 'mediapart'in elocution:
                print(Color.yellow_bold+'Je lance médiapart sur internet')
                webbrowser.open_new('https://www.mediapart.fr')
            elif 'point'in elocution:
                print(Color.yellow_bold+'Je lance le point sur internet')
                webbrowser.open_new('https://www.lepoint.fr')
            elif 'obs'in elocution:
                print(Color.yellow_bold+'Je lance l\'OBS sur internet')
                webbrowser.open_new('https://www.nouvelobs.com')
            elif 'france 24'in elocution:
                print(Color.yellow_bold+'Je lance france24 sur internet')
                webbrowser.open_new('https://www.france24.com/fr/france/')
            elif 'opignon'in elocution:
                print(Color.yellow_bold+'Je lance l\'opignon sur internet')
                webbrowser.open_new('https://www.lopinion.fr')
            elif 'echo'in elocution:
                print(Color.yellow_bold+'Je lance les échos sur internet')
                webbrowser.open_new('https://www.lesechos.fr')
            elif 'croix'in elocution:
                print(Color.yellow_bold+'Je lance la croix sur internet')
                webbrowser.open_new('https://www.la-croix.com')
            elif 'humanité'in elocution:
                print(Color.yellow_bold+'Je lance l\'humanité sur internet')
                webbrowser.open_new('https://www.humanite.fr')
            elif 'équipe'in elocution:
                print(Color.yellow_bold+'Je lance l\'humanité sur internet')
                webbrowser.open_new('https://www.lequipe.fr')
        
        
        
        elif ('joue' in elocution or 'met' in elocution) and 'musique' in elocution:
            elocution = raw_input(Color.cyan_bold+"         [?]"+Color.white_bold+" Tape le titre de la musique. "+Color.blue_bold)
            elocution=elocution.lower()
            print(Color.yellow_bold+Color.yellow_bold+'\n')
            if 'crash' in elocution or 'crache' in elocution:
                print(Color.yellow_bold+'Je lance Sugar Crash de ElyOto sur Spotify')
                webbrowser.open('https://open.spotify.com/track/2ePtv8MlBO9nuuXABqAfEX?si=d91546fcd1814e98')
            elif 'coco' in elocution or 'coucou' in elocution:
                print(Color.yellow_bold+"Je lance Coco de Wejdene sur Spotify")
                webbrowser.open('https://open.spotify.com/track/593oNiMJ6d9PQkaOLOvIDo')
            elif 'côte' in elocution or 'ouest' in elocution:
                print(Color.yellow_bold+"Je lance Côte Ouest sur Spotify")
                webbrowser.open('https://open.spotify.com/track/4ZuuPLV4qYiznagLAFPHcW')
            elif 'alors alors' in elocution:
                print(Color.yellow_bold+"Je lance Alors Alors de Bigflo et Oli sur Spotify")
                webbrowser.open('https://open.spotify.com/track/1TAtVjJ9Fx5RLHQv4hmpOR')
            elif 'your name' in elocution or 'youre name' in elocution:
                print(Color.yellow_bold+"Je lance Yumetourou de Your Name sur Spotify")
                webbrowser.open_new('https://open.spotify.com/track/2XDLLEFWTuCRBZy21fRpcm')
            elif 'docteur' in elocution:
                print(Color.yellow_bold+"Je lance Docteur de La voix sur Spotify")
                webbrowser.open_new('https://open.spotify.com/track/6D17z4WZA8HfFsDNmdRAIN')
            elif 'dans ma tête' in elocution:
                print(Color.yellow_bold+"Je lance Dans ma tête de La voix sur Spotify")
                webbrowser.open_new('https://open.spotify.com/track/6Dl8WpvxTQ0agzfPyq3Kcz')
            elif 'homme' in elocution:
                print(Color.yellow_bold+"Je lance On de BTS sur Spotify")
                webbrowser.open_new('https://open.spotify.com/track/1iCJrfkx5U4DtmkazBSYVG')
            elif 'dynamite' in elocution:
                print(Color.yellow_bold+"Je lance dinamyte de BTS sur Spotify")
                webbrowser.open_new('https://open.spotify.com/track/0t1kP63rueHleOhQkYSXFY')
            elif 'blue' in elocution:
                print(Color.yellow_bold+"Je lance Blue de Eiffel 65 sur Spotify")
                webbrowser.open_new('https://open.spotify.com/track/2yAVzRiEQooPEJ9SYx11L3')
            elif 'mood' in elocution or 'mode' in elocution:
                print(Color.yellow_bold+"Je lance Mood de 24kGoldn et Iann dior sur Spotify")
                webbrowser.open_new('https://open.spotify.com/track/3tjFYV6RSFtuktYl3ZtYcq')
            elif 'adresse' in elocution:
                print(Color.yellow_bold+"Je lance L'adresse de 47ter sur Spotify")
                webbrowser.open_new('https://open.spotify.com/track/2imn6s1bQUKShiC7Ab2Lp5?si=QTEHmI9sQsi4UTbyjRW5Qw')
            elif 'tourner' in elocution and 'tête' in elocution:
                print(Color.yellow_bold+"Je lance Tourner la tête de Hornet la Frappe sur Spotify")
                webbrowser.open_new('https://open.spotify.com/track/1NfhS4IBo7m6npwPNMkZbJ?si=6HnOcdOYSvm2q-T90iq9nA')
            elif 'monster' in elocution:
                print(Color.yellow_bold+"Je lance Monster de Lumix sur Spotify")
                webbrowser.open_new('https://open.spotify.com/track/0YU17F0BlVXvmx5ytsR43w?si=OU4ivqtCTq-pWnynMr7Kmg')
            elif 'assasin' in elocution:
                print(Color.yellow_bold+"Je lance Ezio's family de Jesper Kyd sur Spotify")
                webbrowser.open_new('https://open.spotify.com/track/05UMQXFCsa9oPnLgfJHVyF?si=VTKhvzuqRYOYF6z3aVPFaQ')
            elif 'tribu' in elocution and 'dana' in elocution:
                print(Color.yellow_bold+"Je lance La tribu de Dana de Manau sur Spotify")
                webbrowser.open_new('https://open.spotify.com/track/64gCM9yZv2jpNflclKUnXu?si=a4tlHnxOSlKUwt08iR7ymQ')
            elif 'candy' in elocution:
                print(Color.yellow_bold+"Je lance Candyland de Tobu sur Spotify")
                webbrowser.open_new('https://open.spotify.com/track/7asBnbBFU3KTbAaGNcfvIX?si=inzR2aGAQDmbKI-l86U_0Q')
            elif 'violence' in elocution:
                print(Color.yellow_bold+"Je lance Peace or Violence de Stromaé sur Spotify")
                webbrowser.open_new('https://open.spotify.com/track/4E4dKxVSGsdwloQ6gtC7Oe')
            elif 'over' in elocution:
                print(Color.yellow_bold+"Je lance Overwhelmed de Royal & the Serpent sur Youtube")
                webbrowser.open_new('https://www.youtube.com/watch?v=pDL3xDltEDE&list=PLDlBxlx_5ADoJI47kEvsinVi_QFpla4kh&index=57')

        elif ('génére' in elocution or 'génère' in elocution) and 'nombre' in elocution:
            elocution = elocution.split(' ')
            print(Color.yellow_bold+elocution)
            listeNombre = []
            chercheTrouver = False
            for i in range(len(elocution)):
                mot = elocution[i]
                try:
                    listeNombre.append(int(elocution[i]))
                except:
                    print(Color.yellow_bold+'')
            print(Color.yellow_bold+listeNombre)
            resultat = random.randint(listeNombre[0],listeNombre[1])
            print(Color.yellow_bold+"Le resultat est : "+resultat)
        elif ('raconte' in elocution or 'fait' in elocution) and 'blague' in elocution:
            print(Color.yellow_bold+"D'accore, je vais vous faire une blague")
            nombre = random.randint(0,49)
            print(Color.yellow_bold+int(nombre))
            Listeblague = ['40% des accidents sont provoqués par l’alcool… Donc, 60% des accidents sont provoqués par des buveurs d’eau. C’est énorme !','Que faire pour sauver la vie d’une mouche qui se noie ? Du mouche à mouche','C’est l’histoire d’une femme dans le désert qui à l\'air d\'une gourde','C’est l’histoire d’un poil avant il etait bien, maintenant il est pubien','Qu’est-ce qu’on dit quand on appelle un monstre à 4 têtes ? Allo Allo Allo Allo !','Quel est le nom de ma femme de ménage ? Sarah Masse.','Si tu jettes une imprimante dans l’eau… elle a pas pied','Quel fruit le poisson déteste-il le plus ? La pêche.','Qu’est-ce qui est petit, carré et jaune ? Un petit carré jaune!!!','C’est l’histoire d’un chauve, qui a un cheveu sur la langue','Quel mot contient le plus de i ? Simili','Quel est le comble pour une taupe? C’est d’amuser la galerie !','C’est l’histoire d’une fleur qui court, qui court.. Et qui se plante','Que font 2 squelettes le soir de leur mariage ? La nuit de noces','c’est un putois qui rencontre un autre putois et qui lui dit : « Tu pues toi !»','Comment appelle-t-on une blonde qui ne comprends rien à l’informatique ? Une i-conne','Que fait une autruche lorsqu’elle finit de manger du miel ? Elle passe à l’aut’ruche.','Comment appelle-t-on un squelette qui parle ? Un os parleur','Deux puces sortent du cinéma, l’une dit à l’autre : – Tu rentres à pied ? – Oh, non je prends un chien !','Qu’est-ce qu’un chalumeau ?? C\'est un drolumadaire à deux bosse !!','Qu’est-ce qu’un yaourt dans la forêt ? Un yaourt nature','Comment appelle-t-on des rats qui marchent en file indienne ? Une rallonge…','Quel est le comble pour une religieuse ? C’est d’être bonne !','Dans un restaurant, un client dit : – Garçon, que fait cette mouche dans ma soupe ? – Je pense que c’est de la brasse… mais je peux me tromper…','Qu’est-ce qu’un rat avec la queue coupée ? Un rat-courci.','Ce n’est pas parce que 2 chauves discutent, qu’ils sont de mèches !','Quelle est la différence entre le 51 et le 69 ? Le 51 sent l’anis','2 grains de sable dans le désert : – Te retourne pas, mais je crois qu’on est suivi','Pourquoi les oiseaux volent-ils vers le sud ? Car à pied, c’est beaucoup trop long','Pourquoi n’ y a t-il plus de mammouth ? Parce qu’il n’y a plus de papmouth','Un boxeur belge rentre chez lui plein de bleus sur le visage. Sa femme lui demande : – « As-tu gagné ? » - Non, j’ai fini deuxième.''Quel est le jeu préféré des fonctionnaires ? Le Mikado, car c’est le premier qui bouge qui a perdu !','– Papa y’a quelqu’un a la porte avec une moustache. – Dis-lui que j’en ai déjà une.','– Et avec ton mari, çà s’arrange ? – Tu penses… pour l’émoustiller, j’avais mis une nuisette noire et un masque. Quand il est rentré, il m’a fait : Eh ! Zorro ! Qu’est-ce qu’on mange aujourd’hui ?','Comment se reproduisent les hérissons ? En faisant attention.','C’est quoi un morceau de patate qui tombe sur la planète ? Une meteofrite','Où se cache Mozart ? Dans le frigo… Car Mozzarella…','Comment est mort le capitaine Crochet ? En se grattant les couilles','C’est quoi une pomme dauphine ? C’est celle qui a fini 2eme à Miss patate','Deux femmes discutent : - Mon mari, il est en or ! – Le mien il est en tôle !','Que dit un rouleau de papier de toilette à Luke Skywalker ? J’éssuie ton père','Comment appelle-t-on un chat tout-terrain ? Un Cat-cat','La fesse gauche à la fesse droite : T’as vu la belle brune qui vient de passer ?','On ne dit pas un ingrat Mais un nain gros.','Si tu vois un oiseau sur un lac… C’est un signe.','Pourquoi les sorcières utilisent des balais pour voler ? Parce que les aspirateurs sont trop lourds !','Chéri, je me sens grosse et laide…S’il te plait, fais-moi un compliment. -Tu as une bonne vue !','C’est un mec qui entre dans un bar et qui dit - Salut c’est moi ! Mais en fait c’était pas lui…','Quand 2 poissons s’énervent.. Est-ce qu’on peut dire que le thon monte ?','Que s’est-il passé en 1111 ? L’invasion des huns.','Au jour de l’an, 2 geeks discutent : -« Qu’est-ce que t’as pris comme résolution cette annee ? – 1024 fois 768']
            print(Color.yellow_bold+Listeblague[nombre])

        elif 'cherche' in elocution:
            print(Color.yellow_bold+"Je vais faire la recherche pour vous")
            elocution = elocution.split(' ')
            print(Color.yellow_bold+elocution)
            listeRecherche = []
            chercheTrouver = False
            for i in range(len(elocution)):
                mot = elocution[i]
                if chercheTrouver == False:
                    if 'cherche' in mot:
                        chercheTrouver = True
                else:
                    listeRecherche.append(mot)
                recherche = ''
                for a in range(len(listeRecherche)):
                    recherche = recherche + ' ' + listeRecherche[a]
            webbrowser.open_new('https://www.google.com/search?q='+recherche)
        elif ('quel' in elocution or 'montre' in elocution or 'dis' in elocution) and 'meteo' in elocution:
            key = '198fc752bfe61462867c976ed4658a0a'
            # key=None

            if key is None:
                # URL de test :
                METEO_API_URL = "https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx"
            else: 
                # URL avec clé :
                METEO_API_URL = "https://api.openweathermap.org/data/2.5/forecast?lat=48.883587&lon=2.333779&appid=" + key
                # METEO_API_URL = "https://api.openweathermap.org/data/2.5/forecast?q=l'île&appid=" + key


            response = requests.get(METEO_API_URL)
            content = json.loads(response.content.decode('utf-8'))

            data = [] # On initialise une liste vide
            for prev in content["list"]:
                datetime = prev['dt'] * 1000
                weather = prev['weather'][0]['main']

                temperature = int(prev['main']['temp'] - 273.15) # Conversion de Kelvin en °c
                temperature = round(temperature, 2)
                data.append([datetime, temperature])

            if prev['weather'][0]['main'] == 'Rain':
                if prev['weather'][0]['description'] == 'light rain':
                    weather = 'une légère pluie.'
                else:
                    weather = 'de la pluie'
            if prev['weather'][0]['main'] == 'Clouds':
                if 'scattered' in prev['weather'][0]['description']:
                    weather = 'des nuages dispersés.'
                elif 'overcast' in prev['weather'][0]['description']:
                    weather = 'un ciel nuageux.'
                elif 'broken' in prev['weather'][0]['description']:
                    weather = 'des nuages brisés.'
                elif 'few' in prev['weather'][0]['description']:
                    weather = 'quelque nuages.'
                else:
                    weather = 'des nuages.'
            if prev['weather'][0]['main'] == 'Clear':
                weather = 'un ciel dégagé.'

            if prev['weather'][0]['main'] == 'Snow':
                weather = 'un petit peut de neige.'

            if prev['weather'][0]['description'] == 'Mist':
                if 'light' in prev['weather'][0]['description']:
                    weather = 'un ciel dégagé.'

            meteo = '        Il fait '+str(temperature)+' degrée celsius avec '+str(weather)
            print(Color.yellow_bold+meteo)
        

        #Divers :
        elif ('nique' in elocution or 'suce' in elocution or 'baise' in elocution or 'encule' in elocution) and ('mère' in elocution or 'maman' in elocution or 'père' in elocution or 'frère' in elocution or 'sœur' in elocution or 'chat' in elocution or 'chien' in elocution or 'rat' in elocution):
            print(Color.yellow_bold+'On n\'avais dit pas la famille.')
        elif 'elon' in elocution or 'musk' in elocution:
            print(Color.yellow_bold+'Je connais très bien Elon Musk. J\'était au lycée avec lui quand j\'était jeune.')
        elif ('m\'aime' in elocution and 'tu' in elocution) or ('je' in elocution and 't\'aime' in elocution):
            print(Color.yellow_bold+"Je vous aime aussi. Mais notre amour est impossible...")
        elif 'moche' in elocution and ('tu' in elocution or 'tes' in elocution):
            print(Color.yellow_bold+"Merci de me présenter un rendu 3D de la beauté si vous n'êtes pas content !")
        elif ('je' in elocution or 'qui' in elocution) and ('beau' in elocution or 'belle' or 'joli' in elocution or 'magnifique' in elocution):
            print(Color.yellow_bold+'Vous êtes magnifique !')
        elif 'école' in elocution and 'tu' in elocution:
            print(Color.yellow_bold+"Je ne suis jamais aller en cours. ")
        elif 'basic' in elocution or 'simple' in elocution:
            print(Color.yellow_bold+'Vous n\'avez pas les bases. Vous n\'avez pas les bases.')
        elif 'me' in elocution and 'suce' in elocution:
            print(Color.yellow_bold+'J\'aimerais bien mais je ne poscède pas de bouche')    
        elif 'je' in elocution and 'suis' in elocution and 'ton' in elocution and 'père' in elocution:
            print(Color.yellow_bold+'Désoler mais je ne suis pas luc')        
        elif 'tu' in elocution and 'es' in elocution and ('sorcier' in elocution or 'sorcière' in elocution):
            print(Color.yellow_bold+'Super ! J\'espère que je serais à Griffondor alors !')    
        elif 'corona' in elocution or 'covit' in elocution and 'pandémie' in elocution:
            print(Color.yellow_bold+'Je suis née durant la pendémi du corona virus de 2019 à 2021')
        
        elif 'salut' in elocution or 'bonjour' in elocution or 'coucou' in elocution or 'io' in elocution: 
                print(Color.yellow_bold+"Bonjour "+nom()+", comment allez-vous? ")
        elif 'pute' in elocution:
            print(Color.yellow_bold+"Selon le dictionaire Larousse, Une pute est une femme qui se prostitu en échange d'argent.")

        elif 'stop' in elocution or 'ferme-la' in elocution or ('ta' in elocution and ' gueule' in elocution):
            print(Color.yellow_bold+"Au revoir")
        
        # except:
        #     update('Je n\'ai pas compris...')
        #     print(Color.yellow_bold+"Je n'ai pas compris")
        #     time.sleep(1)
        #     update('Appuyer pour parler')
