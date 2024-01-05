import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(1, 10)
        print(f"[{self.nom}] inflige {degats} degats à {adversaire.nom}")
        adversaire.vie -= degats

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        self.niveau = int(input("""
            Choisissez votre niveau de difficulté 
                Entrez '1' pour facile 
                Entrez '2' pour moyen
                Entrez '3' pour difficile
"""))

    def lancerJeu(self):
        self.choisirNiveau()

        if self.niveau == 1:
            vie_joueur = random.randint(15, 25)
            vie_ennemi = random.randint(15, 25)
        elif self.niveau == 2:
            vie_joueur = random.randint(25, 35)
            vie_ennemi = random.randint(25, 35)
        elif self.niveau == 3:
            vie_joueur = random.randint(35, 40)
            vie_ennemi = random.randint(35, 40)

        joueur = Personnage("Joueur", vie_joueur)
        ennemi = Personnage("Ennemi", vie_ennemi)

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            if ennemi.vie <= 0:
                print(f"\n-------> {ennemi.nom} a été vaincu. {joueur.nom} a gagné! <-------")
                break

            ennemi.attaquer(joueur)
            if joueur.vie <= 0:
                print(f"\n-------> {joueur.nom} a été vaincu. {ennemi.nom} a gagné! <-------")
                break

            print(f"\n{joueur.nom} - Vie : {joueur.vie} | {ennemi.nom} - Vie : {ennemi.vie}\n")

jeu = Jeu()
jeu.lancerJeu()
