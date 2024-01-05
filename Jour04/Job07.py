import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = []

    def initialiser_jeu(self):
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        self.paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(self.paquet)

    def tirer_carte(self):
        if not self.paquet:
            print("Le paquet est vide. Mélangez et redistribuez.")
            return None
        else:
            return self.paquet.pop()

    def calculer_points(self, main):
        points = 0
        nombre_as = 0

        for carte in main:
            if carte.valeur in ['2', '3', '4', '5', '6', '7', '8', '9']:
                points += int(carte.valeur)
            elif carte.valeur in ['10', 'J', 'Q', 'K']:
                points += 10
            elif carte.valeur == 'A':
                points += 11
                nombre_as += 1

        return points

    def jouer_partie(self):
        self.initialiser_jeu()
        main_joueur = [self.tirer_carte(), self.tirer_carte()]
        main_croupier = [self.tirer_carte(), self.tirer_carte()]
        points_joueur = self.calculer_points(main_joueur)
        game = True
        replay = False
        print(f"""
        Début de la partie, Vos cartes sont :""")
        for carte in main_joueur:
            print(f"| {carte.valeur} de {carte.couleur} |",end="   ")

        while game:
            if points_joueur == 21:
                print("\n---------------------->  !! BLACK JACK !! <----------------------")
                break
            choix = input(f"""        
        |--------------------------------------------|
                     Vous avez : {points_joueur} points           
        |    Voulez-vous piochez une nouvelle carte  |
                    Entrez 'O' pour Oui              
        |           Entrez 'N' pour Non              |
        |--------------------------------------------|
""").upper()
            if choix == 'O':
                nouvelle_carte = self.tirer_carte()
                if nouvelle_carte:
                    main_joueur.append(nouvelle_carte)
                    print(f"Votre nouvelle carte est : {nouvelle_carte.valeur} de {nouvelle_carte.couleur}")
                    for carte in main_joueur:
                         print(f"| {carte.valeur} de {carte.couleur} | ", end=" ")
                    points_joueur = self.calculer_points(main_joueur)

                    if points_joueur > 21:
                        game = False
            elif choix == 'N':
                game = False
            else:
                print("Choix invalide. Veuillez entrer 'O' ou 'N'.")

        while self.calculer_points(main_croupier) <= 17:
            nouvelle_carte_croupier = self.tirer_carte()
            if nouvelle_carte_croupier:
                main_croupier.append(nouvelle_carte_croupier)

        points_joueur = self.calculer_points(main_joueur)
        points_croupier = self.calculer_points(main_croupier)

        print("\nMain croupier -->",end=" ")
        for carte in main_croupier:
            print(f"|{carte.valeur} de {carte.couleur} |",end=" ")
        print(f"({points_croupier} points)",end=" ")
        print("\nVotre main -->",end=" ")
        for carte in main_joueur:
            print(f"|{carte.valeur} de {carte.couleur} |",end=" ")
        print(f"({points_joueur} points)",end=" ")
        if points_joueur > 21:
            print(""" 
      ---Vous avez dépassé 21 points. Vous avez perdu---""")
        elif points_croupier > 21 or points_joueur > points_croupier:
            print(""" 
          ----------- Vous avez gagné ! ------------""")
        elif points_joueur < points_croupier:
            print(""" 
          ---------- Le croupier a gagné ---------""")
        else:
            print(""" 
             ------------ Égalité ---------------""")

        while replay is False:
            rejouer = input(f"""        |           Voulez-vous rejouer ?            | 
        | Entrez 'O' pour Oui ou Entrez 'N' pour Non |
        |--------------------------------------------|
""").upper()
            if rejouer == 'O':
                partie = Jeu()
                partie.jouer_partie()
            elif rejouer == 'N':
                replay = True
                break
            else:
                print("Veuillez entrer 'O' ou 'N'")
partie = Jeu()
partie.jouer_partie()          