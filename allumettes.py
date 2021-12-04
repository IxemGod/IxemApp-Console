def Allumette():
    import turtle
    
    # Les constantes

    NOMBRE_ALLUMETTE = 19
    cc=[1]
    ccv = [1]
    HAUTEUR_BOIS_ALLUMETTE = 50
    HAUTEUR_ROUGE_ALLUMETTE = 10
    COULEUR_BOIS_ALLUMETTE = "#CDA88C"
    COULEUR_ROUGE_ALLUMETTE = "#DC5844"
    COULEUR_FOND = "#8CCDC4"
    TITRE = "Jeu des allumettes"
    TAILLE_ECRITURE = 26
    TAILLE_ECRITURE_2 = 16

    # Les autres variables
    etat_partie = True
    nombre_allumettes = NOMBRE_ALLUMETTE
    joueur_courant = 1

    # Les fonctions
    def deplacer_sans_tracer(x, y=None):
        """Fonction pour se déplacer à un point sans tracer"""
        turtle.up()
        if (isinstance(x, tuple) or isinstance(x, list)) and len(x) == 2:
            turtle.goto(x)
        else:
            turtle.goto(x, y)
        turtle.down()

    def initialise_fenetre():
        """Fonction pour initialiser la fenêtre"""
        turtle.hideturtle()
        turtle.screensize(500, 500) 
        turtle.setheading(90)
        turtle.title(TITRE)
        turtle.bgcolor(COULEUR_FOND)
        turtle.speed(0)

    def dessiner_allumette():
        """Fonction pour dessiner une allumette"""
        turtle.pencolor(COULEUR_BOIS_ALLUMETTE)
        turtle.forward(HAUTEUR_BOIS_ALLUMETTE)
        turtle.pencolor(COULEUR_ROUGE_ALLUMETTE)
        turtle.forward(HAUTEUR_ROUGE_ALLUMETTE)

    def dessiner_allumettes(nombre_allumettes):
        
        """Fonction pour dessiner les allumettes"""
        espace_entre_allumettes = 60 if nombre_allumettes < 8 else turtle.window_width() / 2 // nombre_allumettes
        taille_crayon = 25 if nombre_allumettes < 8 else espace_entre_allumettes // 3
        turtle.pensize(taille_crayon)
        position_allumettes = [-nombre_allumettes / 2 * espace_entre_allumettes, 0]
        deplacer_sans_tracer(position_allumettes)
        for allumette in range(nombre_allumettes):
            dessiner_allumette()
            position_allumettes[0] += espace_entre_allumettes
            deplacer_sans_tracer(tuple(position_allumettes))
        if nombre_allumettes != 1:
            afficher_nombre_allumettes(nombre_allumettes)

    def afficher_partie(nombre_allumettes, joueur_courant, nombre_retirees=None):
        """Fonction pour afficher la partie et son état"""
        turtle.clear()
        dessiner_allumettes(nombre_allumettes)
        afficher_qui_joue(joueur_courant)
        if nombre_retirees != None:
            joueur = 1 if joueur_courant == 2 else 2 
            affiche_nombre_retire(joueur, nombre_retirees)

    def affiche_nombre_retire(joueur, nombre_retirees, pos=(0, -110)):
        """Fonction pour afficher le nombre d'allumettes retirées"""
        deplacer_sans_tracer(pos)
        turtle.write("(Le Joueur {} a retiré {} allumette(s))".format(joueur, nombre_retirees),
                     align="center",
                     font=("Arial", TAILLE_ECRITURE_2, "italic"))
        

    def afficher_nombre_allumettes(nombre_allumettes, pos=(0, -80)):
        """Fonction pour afficher le nombre d'allumettes"""
        deplacer_sans_tracer(pos)
        
        turtle.write("Il y a {} allumettes.".format(nombre_allumettes),
                     align="center",
                     font=("Arial", TAILLE_ECRITURE, "normal"))
        mode_emploi()
        mode_emploi2()

    def afficher_qui_joue(joueur_courant, pos=(0, 100)):
        """Fonction pour afficher qui joue"""
        deplacer_sans_tracer(pos)
        turtle.write("C'est au Joueur {} de jouer !".format(joueur_courant),
                     align="center",
                     font=("Arial", TAILLE_ECRITURE, "normal"))        

    def mode_emploi(pos=(0, -150)):
        """Fonction pour afficher qui joue"""
        deplacer_sans_tracer(pos)
        turtle.write("Appuie sur a pour éliminer 1 allumette, ",
                     align="center",
                     font=("Arial", TAILLE_ECRITURE_2, "normal"))

    def mode_emploi2(pos=(0, -200)):
        """Fonction pour afficher qui joue"""
        deplacer_sans_tracer(pos)
        turtle.write("z pour 2 allumettes, e pour 3 allumettes",
                     align="center",
                     font=("Arial", TAILLE_ECRITURE_2, "normal"))

    def bloque_clavier():
        """Fonction pour désactiver les actions des touches a, z, e"""
        turtle.onkeyrelease(None, "a")
        turtle.onkeyrelease(None, "z")
        turtle.onkeyrelease(None, "e")

    def debloque_clavier():
        """Fonction pour associer les touches au nombre retiré"""
        turtle.onkeyrelease(lambda: joue(1), "a")
        turtle.onkeyrelease(lambda: joue(2), "z")
        turtle.onkeyrelease(lambda: joue(3), "e")

    def joue(nombre_retire=1):
        """Fonction pour prendre en compte le choix du joueur"""
        bloque_clavier()
        global nombre_allumettes, etat_partie, joueur_courant
        if cc[-1]==1:
            nombre_allumettes=19
            cc.append(0)
        if nombre_retire != 0 and nombre_allumettes - nombre_retire > 0:
            nombre_allumettes -= nombre_retire
        else:
            debloque_clavier()
            return
        if nombre_allumettes != 1:
            if ccv[-1]==1:
                joueur_courant=2
                ccv.append(0)
            joueur_courant = 1 if joueur_courant == 2 else 2
            afficher_partie(nombre_allumettes, joueur_courant, nombre_retire)
        else:
            etat_partie = victoire(joueur_courant)
            if not etat_partie:
                quitter()
            nombre_allumettes = NOMBRE_ALLUMETTE
            afficher_partie(nombre_allumettes, joueur_courant)
            turtle.listen()
        debloque_clavier()

    def victoire(joueur_courant):
        """Fonction pour le déroulement de la victoire"""
        turtle.clear()
        dessiner_allumettes(1)
        deplacer_sans_tracer(-35, -100)
        turtle.down()
        turtle.write("Le joueur " + str(joueur_courant) + " a gagné !", align="center",
                     font=("Arial", TAILLE_ECRITURE, "normal"))
        
        if (turtle.textinput("Rejouer ?", "Rejouer ? Veuillez entrer 'oui' si c'est le cas.") == 'oui'):
            return True
        return False

    def quitter(x=0, y=0):
        """Fonction pour quitter le jeu et fermer le programme"""
        turtle.bye()
        #sys.exit(0)

    def main():
        """Fonction principale"""
        initialise_fenetre()
        afficher_partie(nombre_allumettes, joueur_courant)
        turtle.listen()
        debloque_clavier()
        turtle.onscreenclick(quitter, 3)

    main()
    turtle.mainloop()