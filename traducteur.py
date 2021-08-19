# -*- coding: utf8 -*
from couleur import *
import socket
from os import system, name, path
import time
import random



def bannier_traducteur1M():
    print(Color.green_bold+"""                   
                ######  ###    ###   ###                ###   ###         ###       #   #     #    #
                  ##    #  #  #   #  #  #  #   #   ###   #   #   # #   #  #  #     ##   ##   ##    #
                  ##    ####  #####  #  #  #   #  #      #   ####  #   #  ###     # #   # # # #  #####
                  ##    # #   #   #  #  #  #   #  #      #   #     #   #  # #       #   #  #  #    #
                  ##    #  #  #   #  ###    ####   ###   #    ###   ####  #  #     ###  #     #    #

            ###################################################################################################
           ##################################################################################################

                                  """)


def code(phrase,key):
    liste_phrase_binaire = []
    lettre_a_tester = ""
    phrase_code = ""
    resultat = ""
    text = phrase
    Dicoalphabet = {' ' : 664,'a' : 135,'b' : 208,'c' : 224,'d' : 233,'e' : 782,'f' : 614,'g' : 752,'h' : 274,'i' : 923,'j' : 341,'k' : 648,'l' : 200,'m' : 733,'n' : 745,'o' : 801,'p' : 355,'q' : 603,'r' : 101,'s' : 878,'t' : 407,'u' : 490,'v' : 686,'w' : 995,'x' : 403,'y' : 418,'z' : 896,'A' : 545,'B' : 281,'C' : 588,'D' : 915,'E' : 767,'F' : 338,'G' : 178,'H' : 950,'I' : 788,'J' : 693,'K' : 119,'L' : 503,'M' : 170,'N' : 364,'O' : 310,'P' : 573,'Q' : 622,'R' : 384,'S' : 979,'T' : 232,'U' : 576,'V' : 539,'W' : 600,'X' : 777,'Y' : 817,'Z' : 467,'0' : 102,'1' : 193,'2' : 217,'3' : 848,'4' : 546,'5' : 115,'6' : 516,'7' : 914,'8' : 480,'9' : 959,'!' : 535,'"' : 445,'#' : 288,'$' : 754,'%' : 768,'&' : 190,'\'' : 876,'(' : 626,')' : 156,'*' : 577,'+' : 207,',' : 838,'-' : 575,'.' : 749,'/' : 762,':' : 717,';' : 840,'<' : 593,'=' : 494,'>' : 525,'?' : 640,'@' : 387,'[' : 887,'\\' : 727,']' : 613,'^' : 570,'_' : 185,'`' : 373,'{' : 623,'|' : 196,'}' : 574,'~' : 672}
    DicoNombre = {664 : ' ',135 : 'a',208 : 'b',224 : 'c',233 : 'd',782 : 'e',614 : 'f',752 : 'g',274 : 'h',923 : 'i',341 : 'j',648 : 'k',200 : 'l',733 : 'm',745 : 'n',801 : 'o',355 : 'p',603 : 'q',101 : 'r',878 : 's',407 : 't',490 : 'u',686 : 'v',995 : 'w',403 : 'x',418 : 'y',896 : 'z',545 : 'A',281 : 'B',588 : 'C',915 : 'D',767 : 'E',338 : 'F',178 : 'G',950 : 'H',788 : 'I',693 : 'J',119 : 'K',503 : 'L',170 : 'M',364 : 'N',310 : 'O',573 : 'P',622 : 'Q',384 : 'R',979 : 'S',232 : 'T',576 : 'U',539 : 'V',600 : 'W',777 : 'X',817 : 'Y',467 : 'Z',102 : '0',193 : '1',217 : '2',848 : '3',546 : '4',115 : '5',516 : '6',914 : '7',480 : '8',959 : '9',535 : '!',445 : '"',288 : '#',754 : '$',768 : '%',190 : '&',876 : '\'',626 : '(',156 : ')',577 : '*',207 : '+',838 : ',',575 : '-',749 : '.',762 : '/',717 : ':',840 : ';',593 : '<',494 : '=',525 : '>',640 : '?',387 : '@',887 : '[',727 : '\\',613 : ']',570 : '^',185 : '_',373 : '`',623 : '{',196 : '|',574 : '}',672 : '~'}
    DicoAplaTestKey = {' ': 864,'a' : 719,'b' : 830,'c' : 966,'d' : 476,'e' : 718,'f' : 989,'g' : 244,'h' : 348,'i' : 630,'j' : 492,'k' : 234,'l' : 344,'m' : 484,'n' : 245,'o' : 205,'p' : 166,'q' : 246,'r' : 226,'s' : 740,'t' : 865,'u' : 443,'v' : 515,'w' : 468,'x' : 562,'y' : 899,'z' : 728,'A' : 223,'B' : 459,'C' : 816,'D' : 117,'E' : 276,'F' : 809,'G' : 610,'H' : 676,'I' : 723,'J' : 255,'K' : 507,'L' : 910,'M' : 191,'N' : 154,'O' : 726,'P' : 734,'Q' : 794,'R' : 861,'S' : 628,'T' : 432,'U' : 874,'V' : 691,'W' : 415,'X' : 949,'Y' : 585,'Z' : 533,'0' : 709,'1' : 586,'2' : 710,'3' : 653,'4' : 273,'5' : 294,'6' : 455,'7' : 192,'8' : 431,'9' : 447,'!' : 118,'"' : 247,'#' : 163,'$' : 558,'%' : 105,'&' : 451,'\'' : 482,'(' : 973,')' : 543,'*' : 396,'+' : 414,',' : 991,'-' : 943,'.' : 981,'/' : 395,':' : 551,';' : 668,'<' : 773,'=' : 514,'>' : 632,'?' : 206,'@' : 790,'[' : 789,'\\' : 680,']' : 359,'^' : 647,'_' : 831,'`' : 649,'{' : 671,'|' : 775,'}' : 278,'~' : 948}
    dicoNew = {}
    posi = -1
    for m in Dicoalphabet.values():
        posi+=1
        dicoNew[DicoNombre[m]] = (DicoAplaTestKey[key[posi]] * (m))
        if posi == len(key)-1:
            posi = -1
    resultat = ''
    for d in range(len(text)):
        resultat = resultat + str(dicoNew[text[d]]) + ','
    phrase = resultat
    resultat = ""
    resultat_liste = []
    table3 = {"," : "01110011","1": "00110001", "2": "00110010", "3": "00110011", "4": "00110100", "5": "00110101","6": "00110110", "7": "00110111", "8": "00111000", "9": "00111001", "0": "00110000"}
    for c in range(0, len(phrase)):
        lettre_a_tester = phrase[c]
        resultat_liste.append(table3[lettre_a_tester])
    table4 = {"01110011": "k","00110001": "0", "00110010": "1", "00110011": "2", "00110100": "3", "00110101": "4","00110110": "5", "00110111": "6", "00111000": "7", "00111001": "8", "00110000": "9"}
    for d in range(0, len(resultat_liste)):
        lettre_a_tester = resultat_liste[d]
        resultat = resultat + table4[lettre_a_tester]
    phrase = resultat
    resultat = ""
    resultat_liste = []
    table5 = {"k":"...___","1": ".____", "2": "..___", "3": "...__", "4": "...._", "5": ".....", "6": "_....", "7": "__...","8": "___..", "9": "____.", "0": "_____"}
    for e in range(0, len(phrase)):
        try:
            lettre_a_tester = phrase[e]
            resultat_liste.append(table5[lettre_a_tester])
        except:
            print('')
    table6 = {"...___":",",".____": "u", "..___": "v", "...__": "w", "...._": "x", ".....": "y", "_....": "z", "__...": "Z","___..": "Y", "____.": "X", "_____": "W"}
    for f in range(0, len(resultat_liste)):
        lettre_a_tester = resultat_liste[f]
        resultat = resultat + table6[lettre_a_tester]
    resultat = key+resultat
    return resultat



def decode(phrase,key):
    lettre_a_tester = ""
    resultat_liste = []
    phrase = phrase + 's'
    phrase = phrase[4:-1]
    table7 = {",":"...___" ,"u": ".____", "v": "..___", "w": "...__", "x": "...._", "y": ".....", "z": "_....", "Z": "__...","Y": "___..", "X": "____.", "W": "_____"}
    for g in range(0, len(phrase)):
        lettre_a_tester = phrase[g]
        if lettre_a_tester in table7:
            resultat_liste.append(table7[lettre_a_tester])
        else:
            erreur = 'Erreur, Vous avez entrez un caractère indécodable'
            return erreur
    resultat = ""
    table8 = {"...___" : "k" , ".____": "1", "..___": "2", "...__": "3", "...._": "4", ".....": "5", "_....": "6", "__...": "7","___..": "8", "____.": "9", "_____": "0"}
    for h in range(0, len(resultat_liste)):
        lettre_a_tester = resultat_liste[h]
        resultat = resultat + (table8[lettre_a_tester])
    resultat_liste = []
    table9 = {"k" : "01110011", "0": "00110001", "1": "00110010", "2": "00110011", "3": "00110100", "4": "00110101","5": "00110110", "6": "00110111", "7": "00111000", "8": "00111001", "9": "00110000"}
    for i in range(0, len(resultat)):
        lettre_a_tester = resultat[i]
        resultat_liste.append(table9[lettre_a_tester])
    resultat = ""
    table10 = {"01110011": "," ,"00110001": "1", "00110010": "2", "00110011": "3", "00110100": "4", "00110101": "5","00110110": "6", "00110111": "7", "00111000": "8", "00111001": "9", "00110000": "0"}
    for j in range(0, len(resultat_liste)):
        lettre_a_tester = resultat_liste[j]
        resultat = resultat + table10[lettre_a_tester]

    text = resultat
    Dicoalphabet = {' ' : 664,'a' : 135,'b' : 208,'c' : 224,'d' : 233,'e' : 782,'f' : 614,'g' : 752,'h' : 274,'i' : 923,'j' : 341,'k' : 648,'l' : 200,'m' : 733,'n' : 745,'o' : 801,'p' : 355,'q' : 603,'r' : 101,'s' : 878,'t' : 407,'u' : 490,'v' : 686,'w' : 995,'x' : 403,'y' : 418,'z' : 896,'A' : 545,'B' : 281,'C' : 588,'D' : 915,'E' : 767,'F' : 338,'G' : 178,'H' : 950,'I' : 788,'J' : 693,'K' : 119,'L' : 503,'M' : 170,'N' : 364,'O' : 310,'P' : 573,'Q' : 622,'R' : 384,'S' : 979,'T' : 232,'U' : 576,'V' : 539,'W' : 600,'X' : 777,'Y' : 817,'Z' : 467,'0' : 102,'1' : 193,'2' : 217,'3' : 848,'4' : 546,'5' : 115,'6' : 516,'7' : 914,'8' : 480,'9' : 959,'!' : 535,'"' : 445,'#' : 288,'$' : 754,'%' : 768,'&' : 190,'\'' : 876,'(' : 626,')' : 156,'*' : 577,'+' : 207,',' : 838,'-' : 575,'.' : 749,'/' : 762,':' : 717,';' : 840,'<' : 593,'=' : 494,'>' : 525,'?' : 640,'@' : 387,'[' : 887,'\\' : 727,']' : 613,'^' : 570,'_' : 185,'`' : 373,'{' : 623,'|' : 196,'}' : 574,'~' : 672}
    DicoNombre = {664 : ' ',135 : 'a',208 : 'b',224 : 'c',233 : 'd',782 : 'e',614 : 'f',752 : 'g',274 : 'h',923 : 'i',341 : 'j',648 : 'k',200 : 'l',733 : 'm',745 : 'n',801 : 'o',355 : 'p',603 : 'q',101 : 'r',878 : 's',407 : 't',490 : 'u',686 : 'v',995 : 'w',403 : 'x',418 : 'y',896 : 'z',545 : 'A',281 : 'B',588 : 'C',915 : 'D',767 : 'E',338 : 'F',178 : 'G',950 : 'H',788 : 'I',693 : 'J',119 : 'K',503 : 'L',170 : 'M',364 : 'N',310 : 'O',573 : 'P',622 : 'Q',384 : 'R',979 : 'S',232 : 'T',576 : 'U',539 : 'V',600 : 'W',777 : 'X',817 : 'Y',467 : 'Z',102 : '0',193 : '1',217 : '2',848 : '3',546 : '4',115 : '5',516 : '6',914 : '7',480 : '8',959 : '9',535 : '!',445 : '"',288 : '#',754 : '$',768 : '%',190 : '&',876 : '\'',626 : '(',156 : ')',577 : '*',207 : '+',838 : ',',575 : '-',749 : '.',762 : '/',717 : ':',840 : ';',593 : '<',494 : '=',525 : '>',640 : '?',387 : '@',887 : '[',727 : '\\',613 : ']',570 : '^',185 : '_',373 : '`',623 : '{',196 : '|',574 : '}',672 : '~'}
    DicoAplaTestKey = {' ': 864,'a' : 719,'b' : 830,'c' : 966,'d' : 476,'e' : 718,'f' : 989,'g' : 244,'h' : 348,'i' : 630,'j' : 492,'k' : 234,'l' : 344,'m' : 484,'n' : 245,'o' : 205,'p' : 166,'q' : 246,'r' : 226,'s' : 740,'t' : 865,'u' : 443,'v' : 515,'w' : 468,'x' : 562,'y' : 899,'z' : 728,'A' : 223,'B' : 459,'C' : 816,'D' : 117,'E' : 276,'F' : 809,'G' : 610,'H' : 676,'I' : 723,'J' : 255,'K' : 507,'L' : 910,'M' : 191,'N' : 154,'O' : 726,'P' : 734,'Q' : 794,'R' : 861,'S' : 628,'T' : 432,'U' : 874,'V' : 691,'W' : 415,'X' : 949,'Y' : 585,'Z' : 533,'0' : 709,'1' : 586,'2' : 710,'3' : 653,'4' : 273,'5' : 294,'6' : 455,'7' : 192,'8' : 431,'9' : 447,'!' : 118,'"' : 247,'#' : 163,'$' : 558,'%' : 105,'&' : 451,'\'' : 482,'(' : 973,')' : 543,'*' : 396,'+' : 414,',' : 991,'-' : 943,'.' : 981,'/' : 395,':' : 551,';' : 668,'<' : 773,'=' : 514,'>' : 632,'?' : 206,'@' : 790,'[' : 789,'\\' : 680,']' : 359,'^' : 647,'_' : 831,'`' : 649,'{' : 671,'|' : 775,'}' : 278,'~' : 948}

    dicoNew = {}
    text = text.split(",")
    posi = -1
    for m in Dicoalphabet.values():
        posi +=1
        dicoNew[(DicoAplaTestKey[key[posi]] * (m))] =DicoNombre[m] 
        if posi == len(key)-1:
            posi = -1
    resultat = ''
    for d in text:
        if d != '':
            try:
                resultat = resultat + str(dicoNew[int(d)])
            except:
                return 'Mauvaise clée !'
    return resultat

def traducteur_1M():
    system('clear')

    bannier_traducteur1M()
    


    #On demande si l'utilisateur / l'utilisatrice souhaite coder ou décoder un message.
    print(Color.red_bold+"                 [1] "+Color.white_bold+"""Coder"""+Color.red_bold+"           [2] "+Color.white_bold+"""Décoder\n""")
    choix_CodeDecode = input(Color.cyan_bold+"           [?]"+Color.white_bold+"Choisis un chifre."+ Color.blue_bold)
    
    system('clear')
    bannier_traducteur1M()


    #On demande la phrase à traiter.
    phrase = raw_input(Color.cyan_bold+"           [?]"+Color.white_bold+" Tapez votre phrase. "+Color.blue_bold)


    #On test la réponse du choix de l'utilisateur / l'utilisatrice.
    if choix_CodeDecode == 1 or choix_CodeDecode == "1":


        if len(phrase) > 0:
            key = ''
            for i in range(4):
                choix = ['Z',"z","x", "X", 'w', 'W','u', 'v', 'Y']
                key = key + random.choice(choix)
            system('clear')
            bannier_traducteur1M()
            print(Color.purple_bold+"         [output] "+Color.white_bold+code(phrase,key))
            fin = raw_input("")
            return


        else:
            print(Color.red_bold+"           [!]"+Color.white_bold+"La phrase à coder doit faire plus de 0 caractère.")
            time.sleep(2)
            traducteur_1M()


    elif(choix_CodeDecode == 2 or choix_CodeDecode == "2"):


        if len(phrase) > 0:
            system('clear')
            bannier_traducteur1M()
            print(Color.purple_bold+"         [output] "+Color.white_bold+decode(phrase, phrase[0:4]))
            fin = raw_input("")
            return


        else:
            print(Color.red_bold+"           [!]"+Color.white_bold+"La phrase à décoder doit faire plus de 0 caractère.")
            time.sleep(2)
            traducteur_1M()


    #Si le choix entré est vide ou inexistant.
    else:
        print(Color.red_bold+"           [!]"+Color.white_bold+"Choix Inexistant.")
        time.sleep(2)
        traducteur_1M()