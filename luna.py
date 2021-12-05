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
from datetime import datetime as dt
import time
from art import *
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


def banner():
    system('clear')
    print(Color.pink_bold)
    tprint("Luna")

def modeConfig():

    def username():
        contenu= input(Color.cyan_bold+"\n         [?]"+Color.white_bold+"Entrez votre nom : "+Color.blue_bold)
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        updateName = (contenu,'username')
        cur.execute('UPDATE settings SET value = ? WHERE settingName = ?', updateName)
        con.commit()
        con.close()
        print("\n"+Color.green_bold+"     "+Color.white_bold+"["+Color.green_bold+"✅"+Color.white_bold+"] Votre nom à été modifié.")
        fin = input("")
        banner()

    def GPS():
        contenu= input(Color.cyan_bold+"\n         [?]"+Color.white_bold+"Entrez vos coordonée GPS décimale : "+Color.blue_bold)
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        updateGPS = (contenu,'coordone')
        cur.execute('UPDATE settings SET value = ? WHERE settingName = ?', updateGPS)
        con.commit()
        con.close()
        print("\n"+Color.green_bold+"     "+Color.white_bold+"["+Color.green_bold+"✅"+Color.white_bold+"] Vos coordonées on été modifié.")
        fin = input("")
        banner()

    def BD():
        contenu= input(Color.cyan_bold+"\n         [?]"+Color.white_bold+"Entrez votre date d'anniverssaire (JJ/MM/AAAA) : "+Color.blue_bold)
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        updateBD = (contenu,'birthday')
        cur.execute('UPDATE settings SET value = ? WHERE settingName = ?', updateBD)
        con.commit()
        con.close()
        print("\n"+Color.green_bold+"     "+Color.white_bold+"["+Color.green_bold+"✅"+Color.white_bold+"] Votre date d'anniverssaire à été modifié.")
        fin = input("")
        banner()

    def musique():
        banner()
        print(Color.red_bold+"  Extraction et construction du tableau des musique depuis la base de donnée...\n")
        print(Color.white_bold+"""          Mot-clef"""+" "*5+Color.orange_bold+"|"+Color.white_bold+" Liens   "+Color.orange_bold+"|"+Color.white_bold+""" Titre"""+" "*25+Color.orange_bold+"|"+Color.white_bold+"ID"+Color.yellow_bold+"\n         "+"#"*63)
        

        con = sqlite3.connect('musiqueDb.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM musique")
        
        for item in cur:
            Espace_MotClef = 14 - len(item[0])
            link  = "Autre"

            #Racourciceur d'url
            if "spotify" in item[1]:
                link = "Spotify"
                # link = item[1]+"s"
                # link = link[31:53]
            elif "youtube" in item[1]:
                # link = item[1]+"s"
                # link = link[32:-1]
                link = "Youtube"
            elif "deezer" in item[1]:
                link = "Deezer"

            Espace_link = 7 - len(link)
            Espace_Tittle = 30 - len(item[3])
            Espace_Id = 4 - len(item[3])
            print(Color.blue_bold+f"         {item[0]}"+" "*Espace_MotClef+Color.yellow_bold+"|"+Color.blue_bold+f" {link} "+" "*Espace_link+Color.yellow_bold+"|"+Color.blue_bold+f" {item[3]}"+" "*Espace_Tittle+Color.yellow_bold+"|"+Color.blue_bold+f" {item[4]}"+" "*Espace_Id)
            print("         "+Color.yellow_bold+"-"*63)

        print(Color.red_bold+"                 [1] "+Color.white_bold+"""Ajouter un Titre"""+Color.red_bold+"           [2] "+Color.white_bold+"""Suprimer un Titre
        """)


        choix = input(Color.cyan_bold+"\n         [?]"+Color.white_bold+"Choisisez un nombre. "+Color.blue_bold)

        if choix == 1 or choix == "1":
            motClef = input(Color.cyan_bold+"\n         [?]"+Color.white_bold+"Saisissez des mot-clef. Chaque mot doit être séprarer d'une virgule. "+Color.blue_bold)
            print('')
            url = input(Color.cyan_bold+"\n         [?]"+Color.white_bold+"Saisissez le liens vers le Titre. "+Color.blue_bold)
            print('')
            author = input(Color.cyan_bold+"\n         [?]"+Color.white_bold+"Saisissez l'Auteur. "+Color.blue_bold)
            print('')
            title = input(Color.cyan_bold+"\n         [?]"+Color.white_bold+"Saisissez le titre de la musique. "+Color.blue_bold)
            Id = random.randint(10000,99999)

            cur.execute("INSERT INTO musique values(?,?,?,?,?)",(motClef,url,author,title,Id))
            con.commit()
            con.close()
            print("\n"+Color.purple_bold+"          [output] "+Color.white_bold+'Votre titre à été ajouter !')
            fin = input("")
            banner()
        elif choix == 2 or choix == "2":
            con = sqlite3.connect('musiqueDb.db')
            cur = con.cursor()
            Id = input(Color.cyan_bold+"\n         [?]"+Color.white_bold+" Tapez l'Id du titre que vous souhaitez suprimé. "+Color.blue_bold)
            cur.execute('DELETE FROM musique WHERE id = ?',(Id,))
            con.commit()
            print("\n"+Color.purple_bold+"          [output] "+Color.white_bold+f'La musique portant l\'id {Id} à été correctement effacer')
            fin = input("")
            banner()
        else:
            banner()

    print(Color.grey_bold)
    while True:
        banner()
        print(Color.red_bold+"      [1]"+Color.white_bold+""" Modifié votre nom   """+Color.red_bold+"     [2]"+Color.white_bold+""" Modifié votre date d'anniverssaire
      """+Color.red_bold+"[3]"+Color.white_bold+ " Configuration Musique"+Color.red_bold+ "    [4]"+Color.white_bold+""" Modification GPS""")
        elocution = input(Color.cyan_bold+"\n         [?]"+Color.white_bold+'Que voulez vous faire ? '+Color.blue_bold)
        if elocution == 1 or elocution == "1":
            username()
        elif elocution == 2 or elocution == "2":
            BD()
        elif elocution == 3 or elocution == "3":
            musique()
        elif elocution == 4 or elocution == "4":
            GPS()
        else:
            banner()
            return

def Luna():

    def nom():


        con = sqlite3.connect('database.db')
        curConfig = con.cursor()
        TupleCurConfig = ("username",)
        curConfig.execute('SELECT * FROM settings WHERE settingName = ?', TupleCurConfig)
        for result in curConfig:
            result = result[1]
        return result


    banner()
    print(Color.yellow_bold+"\nSalut ! Je suis Luna, votre assistante. Tapez votre commande et je réagisserais 😄")
    print(Color.purple_bold+"Pour obtenir la liste des commandes, tapez \"help\". Pour retourner au menu principal, tapez \"exit\".")
    while True:
        elocution = input(Color.cyan_bold+"\n         [?]"+Color.white_bold+"Entrez une commande. "+Color.blue_bold)
        elocution = elocution.lower()
        print(Color.yellow_bold+Color.yellow_bold)

        if 'config' in elocution:
            banner()
            print(Color.yellow_bold+'Lancement de la configuration du systême')
            modeConfig()

        elif elocution == "help":
            banner()
            print(Color.yellow_bold+ "Liste des commandes :")


            #Question personnel

            #Chaque ligne ont une couleur
            #Le code couleur est Bleue, Blanc
            print("\n")
            Liste_Commande = ["Heure : Affiche l'heure actuel avec la Timezone de Paris","Développeur / créateur : Affiche les infos du développeur", "config : Donne accès au paramêtre", "calc <calcule> : Effectue le calcule.", "actus/news : affiche la liste des journaux que vous pouvez ouvrir", "random <nombre1>/<nombre2> : génère un nombre aléatoire entre ces deux nombres.", "src <votre phrase> : vas faire la recherche dans votre navigateur.","Raconte moi une blague : affiche un blague random à partir d'une liste de 50 blagues","stop : Retourne au menu principal d'IxemApp","Montre moi la météo : Affiche la météo selon vos coordonée GPS décimale que vous aurrez renseigner au préalable en tapant config."]
            couleur = 1
            for item in Liste_Commande:
                if couleur == 1:
                    print(Color.blue_bold+" "*5+item+"\n")
                    couleur+=1
                elif couleur == 2:
                    print(Color.white_bold+" "*5+item+"\n")
                    couleur=1

        #Question 
        elif 'quel' in elocution or 'comment' in elocution or 'quoi' in elocution or 'qui' in elocution or 'est-ce' in elocution or 'es-ce' in elocution or 'où' in elocution:
            banner()

            if 'heure' in elocution:
                temps = dt.now()
                print(Color.yellow_bold+"        Il est actuellement "+str(temps.hour)+" heure "+ str(temps.minute))
            elif 'développeur' in elocution or 'qui' in elocution and ('créateur' in elocution or 'crée' in elocution):
                print(Color.yellow_bold+'        Mon créateur est IxemGod. C\'est un jeune développeur très compétent.\n Voici ses résaux :\n')
                print(Color.cyan_bold+"[*]"+Color.blue_bold+" Discord :   IxemGod#5206")
                print(Color.cyan_bold+"[*]"+Color.red_bold+" Instagram :  _IxemGod")
                print(Color.cyan_bold+"[*]"+Color.blue_bold+" FaceBook:   IxemGod Jedusors")
                print(Color.cyan_bold+"[*]"+Color.cyan_bold+" Twitter:  IxemGod")
                print(Color.cyan_bold+"[*]"+Color.grey_bold+" Github:  IxemGod")
            elif 'âge' in elocution:
                    timestamp = int(time.time())
                    dateDeCrea = 1610060400
                    resultat = timestamp-dateDeCrea
                    minute, heure, jours, annee = 0,0,0,0
                    while(resultat > 3600):
                        resultat = resultat - 3600
                        heure = heure + 1
                        if heure == 24:
                            heure = 0
                            jours = jours +1
                            if jours == 365:
                                jours = 0
                                annee = annee + 1
                    print(Color.yellow_bold+"        Je suis née le 8 janvier 2021. J'ai donc "+str(annee)+" ans et "+str(jours)+" jours")
           
            elif 'appel' in elocution or 'ton nom' in elocution:
                banner()
                print(Color.yellow_bold+"        Je m'appelle Luna. En référence à Luna Lovegood dans Harry Potter")

            elif ('jour' in elocution or 'date' in elocution or 'annee' in elocution or 'combien' in elocution):
                banner()
                date = dt.now()
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
                    jour = "premier"

                print(Color.yellow_bold+'        Nous somme le '+str(jour)+' '+str(mois)+' '+str(date.year))

                if annive == True:
                    print(Color.yellow_bold+'        Aujourd’hui c\'est l\'aniversaire de mon créateur ! Bonne annive IxemGod !')

        
        #Commande
        elif 'calc' in elocution:
            banner()
            elocution = elocution.split(' ')
            listeRecherche = []
            chercheTrouver = False
            for i in range(len(elocution)):
                mot = elocution[i]
                if chercheTrouver == False:
                    if 'calc' in mot:
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
        elif ('actu' in elocution or "news" in elocution):
            banner()
            Journaux = {"ouest france" : "https://www.ouest-france.fr", "parisien" : "https://www.leparisien.fr",
            "monde": "https://www.lemonde.fr",
            "figaro":"https://www.lefigaro.fr",
            "gorafi":"http://www.legorafi.fr",
            "libération":"https://www.liberation.fr",
            "médiapart" :"https://www.mediapart.fr",
            "point" : "https://www.lepoint.fr",
            "obs" : "https://www.nouvelobs.com",
            "france 24" : "https://www.france24.com/fr/france/",
            "opignon" :"https://www.lopinion.fr",
            "échos" : "https://www.lesechos.fr",
            "croix" :"https://www.la-croix.com",
            "humanité" : "https://www.humanite.fr",
            "équipe" : "https://www.lequipe.fr"}

            #On test si présence d'un argument
            if len(elocution) > 5: 
                elocution= elocution+" "
                nomJournau = elocution[5:-1]
                for name,link in Journaux.items():
                    if nomJournau == name:
                        webbrowser.open_new(link)
                        break
            else:
                print(Color.yellow_bold+"Pour ouvrir un journal, tapez "+Color.red_bold+"\"actu/news <nom du journal>\"")
                print(Color.yellow_bold+"Voici la liste des journaux disponible :\n"+Color.green_bold)
                for name,link in Journaux.items():
                    link = link + " "
                    print(f"{name} : {link[11:-1]}")

        
        
        elif ('joue' in elocution or 'met' in elocution) and 'musique' in elocution:
            banner()
            elocution = input(Color.cyan_bold+"         [?]"+Color.white_bold+" Tapez le titre de la musique. "+Color.blue_bold)
            elocution=elocution.lower()
            print('\n')
            con = sqlite3.connect('musiqueDb.db')
            cur = con.cursor()
            cur.execute("SELECT * FROM musique")
            for item in cur:
                mot_clef = item[0]
                mot_clef = mot_clef.split('/')
                state = 0
                for mot in mot_clef:
                    if mot in elocution and state == 0:
                        webbrowser.open(item[1])
                        print("\n"+Color.purple_bold+"        [output] "+Color.white_bold+'Lancement de la musique...')
                        state = 1





        elif "random" in elocution:
            banner()
            elocution = elocution.split(' ')
            nombre = elocution[1]
            nombre = nombre.split("/")
            resultat = random.randint(int(nombre[0]),int(nombre[1]))
            print(Color.yellow_bold+"Le resultat est : "+str(resultat))


        elif ('raconte' in elocution or 'fais' in elocution) and 'blague' in elocution:
            banner()
            print(Color.yellow_bold+"D'accord, je vais vous faire une blague")
            nombre = random.randint(0,49)
            Listeblague = ['40% des accidents sont provoqués par l’alcool… Donc, 60% des accidents sont provoqués par des buveurs d’eau. C’est énorme !','Que faire pour sauver la vie d’une mouche qui se noie ? Du mouche à mouche','C’est l’histoire d’une femme dans le désert qui à l\'air d\'une gourde','C’est l’histoire d’un poil avant il etait bien, maintenant il est pubien','Qu’est-ce qu’on dit quand on appelle un monstre à 4 têtes ? Allo Allo Allo Allo !','Quel est le nom de ma femme de ménage ? Sarah Masse.','Si tu jettes une imprimante dans l’eau… elle a pas pied','Quel fruit le poisson déteste-il le plus ? La pêche.','Qu’est-ce qui est petit, carré et jaune ? Un petit carré jaune!!!','C’est l’histoire d’un chauve, qui a un cheveu sur la langue','Quel mot contient le plus de i ? Simili','Quel est le comble pour une taupe? C’est d’amuser la galerie !','C’est l’histoire d’une fleur qui court, qui court.. Et qui se plante','Que font 2 squelettes le soir de leur mariage ? La nuit de noces','c’est un putois qui rencontre un autre putois et qui lui dit : « Tu pues toi !»','Comment appelle-t-on une blonde qui ne comprends rien à l’informatique ? Une i-conne','Que fait une autruche lorsqu’elle finit de manger du miel ? Elle passe à l’aut’ruche.','Comment appelle-t-on un squelette qui parle ? Un os parleur','Deux puces sortent du cinéma, l’une dit à l’autre : – Tu rentres à pied ? – Oh, non je prends un chien !','Qu’est-ce qu’un chalumeau ?? C\'est un drolumadaire à deux bosse !!','Qu’est-ce qu’un yaourt dans la forêt ? Un yaourt nature','Comment appelle-t-on des rats qui marchent en file indienne ? Une rallonge…','Quel est le comble pour une religieuse ? C’est d’être bonne !','Dans un restaurant, un client dit : – Garçon, que fait cette mouche dans ma soupe ? – Je pense que c’est de la brasse… mais je peux me tromper…','Qu’est-ce qu’un rat avec la queue coupée ? Un rat-courci.','Ce n’est pas parce que 2 chauves discutent, qu’ils sont de mèches !','Quelle est la différence entre le 51 et le 69 ? Le 51 sent l’anis','2 grains de sable dans le désert : – Te retourne pas, mais je crois qu’on est suivi','Pourquoi les oiseaux volent-ils vers le sud ? Car à pied, c’est beaucoup trop long','Pourquoi n’ y a t-il plus de mammouth ? Parce qu’il n’y a plus de papmouth','Un boxeur belge rentre chez lui plein de bleus sur le visage. Sa femme lui demande : – « As-tu gagné ? » - Non, j’ai fini deuxième.''Quel est le jeu préféré des fonctionnaires ? Le Mikado, car c’est le premier qui bouge qui a perdu !','– Papa y’a quelqu’un a la porte avec une moustache. – Dis-lui que j’en ai déjà une.','– Et avec ton mari, çà s’arrange ? – Tu penses… pour l’émoustiller, j’avais mis une nuisette noire et un masque. Quand il est rentré, il m’a fait : Eh ! Zorro ! Qu’est-ce qu’on mange aujourd’hui ?','Comment se reproduisent les hérissons ? En faisant attention.','C’est quoi un morceau de patate qui tombe sur la planète ? Une meteofrite','Où se cache Mozart ? Dans le frigo… Car Mozzarella…','Comment est mort le capitaine Crochet ? En se grattant les couilles','C’est quoi une pomme dauphine ? C’est celle qui a fini 2eme à Miss patate','Deux femmes discutent : - Mon mari, il est en or ! – Le mien il est en tôle !','Que dit un rouleau de papier de toilette à Luke Skywalker ? J’éssuie ton père','Comment appelle-t-on un chat tout-terrain ? Un Cat-cat','La fesse gauche à la fesse droite : T’as vu la belle brune qui vient de passer ?','On ne dit pas un ingrat Mais un nain gros.','Si tu vois un oiseau sur un lac… C’est un signe.','Pourquoi les sorcières utilisent des balais pour voler ? Parce que les aspirateurs sont trop lourds !','Chéri, je me sens grosse et laide…S’il te plait, fais-moi un compliment. -Tu as une bonne vue !','C’est un mec qui entre dans un bar et qui dit - Salut c’est moi ! Mais en fait c’était pas lui…','Quand 2 poissons s’énervent.. Est-ce qu’on peut dire que le thon monte ?','Que s’est-il passé en 1111 ? L’invasion des huns.','Au jour de l’an, 2 geeks discutent : -« Qu’est-ce que t’as pris comme résolution cette annee ? – 1024 fois 768']
            print(Color.yellow_bold+Listeblague[nombre])

        elif 'src' in elocution:
            banner()
            print(Color.yellow_bold+"Je vais faire la recherche pour vous")
            elocution = elocution.split(' ')
            print(Color.yellow_bold+elocution)
            listeRecherche = []
            chercheTrouver = False
            for i in range(len(elocution)):
                mot = elocution[i]
                if chercheTrouver == False:
                    if 'src' in mot:
                        chercheTrouver = True
                else:
                    listeRecherche.append(mot)
                recherche = ''
                for a in range(len(listeRecherche)):
                    recherche = recherche + ' ' + listeRecherche[a]
            webbrowser.open_new('https://www.google.com/search?q='+recherche)

        elif ('quel' in elocution or 'montre' in elocution or 'dis' in elocution) and 'météo' in elocution:
            key = '198fc752bfe61462867c976ed4658a0a'
            
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            GPS = ("coordone",)
            cur.execute("SELECT * FROM settings WHERE settingName = ?",GPS)
            for item in cur:
                coo = item[1]
                coo = coo.split(' ')
                lat = coo[0]
                lon = coo[1]

            METEO_API_URL = "https://api.openweathermap.org/data/2.5/forecast?lat="+lat+"&lon="+lon+"&appid=" + key


            response = requests.get(METEO_API_URL)
            content = json.loads(response.content.decode('utf-8'))

            data = [] # On initialise une liste vide
            for prev in content["list"]:
                datetime = prev['dt'] * 1000
                weather = prev['weather'][0]['main']

                temperature = int(prev['main']['temp'] - 273.15) # Conversion de Kelvin en Celsius
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

            meteo = '        Il fait '+str(temperature)+'°C avec '+str(weather)

            print(Color.yellow_bold+meteo)
        

        #Divers :
        elif 'moche' in elocution and ('tu' in elocution or 'tes' in elocution):
            banner()
            print(Color.yellow_bold+"Merci de me présenter un rendu 3D de la beauté si vous n'êtes pas content !")

        elif 'basique' in elocution or 'simple' in elocution:
            banner()
            print(Color.yellow_bold+'Vous n\'avez pas les bases. Vous n\'avez pas les bases.')
 
        elif 'je' in elocution and 'suis' in elocution and 'ton' in elocution and 'père' in elocution:
            banner()
            print(Color.yellow_bold+'Désoler mais je ne suis pas luc')        
        elif 'tu' in elocution and 'es' in elocution and ('sorcier' in elocution or 'sorcière' in elocution):
            banner()
            print(Color.yellow_bold+'Super ! J\'espère que je serais à Griffondor alors !')    
        elif 'corona' in elocution or 'covid' in elocution and 'pendémie' in elocution:
            banner()
            print(Color.yellow_bold+'Je suis née durant la pendémi du corona virus de 2019 à 2021')
        
        elif 'salut' in elocution or 'bonjour' in elocution or 'coucou' in elocution or 'yo' in elocution or 'hey' in elocution or 'hello' in elocution: 
            banner()
            print(Color.yellow_bold+"Bonjour "+nom()+" !")

        elif "stop" == elocution or "exit" == elocution:
            banner()
            print(Color.yellow_bold+"Au revoir "+nom())
            return