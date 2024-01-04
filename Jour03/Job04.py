class Joueur:
    def __init__(self, nom, numero, position):
        self.__nom = nom
        self.__numero = numero
        self.__position = position
        self.__but = 0
        self.__passe = 0
        self.__carton_j = 0
        self.__carton_r = 0

    def get_nom(self):
        return self.__nom
    def get_numero(self):
        return self.__numero
    def get_position(self):
        return self.__position
    def get_but(self):
        return self.__but
    def get_passe(self):
        return self.__passe
    def get_carton_j(self):
        return self.__carton_j
    def get_carton_r(self):
        return self.__carton_r
    
    def set_but(self, but):
        self.__but = but
    def set_passe(self, passe):
        self.__passe = passe
    def set_carton_j(self, carton_j):
        self.__carton_j = carton_j
    def set_carton_r(self, carton_r):    
        self.__carton_r = carton_r

    def marquer_but(self):
        self.set_but(self.__but + 1)
        print(f"[---BUT---]{self.get_nom()} marque un but!")
    def effectuer_passe_decisive(self):
        self.set_passe(self.__passe + 1)
        print(f"[--PASSE--]{self.get_nom()} effectue une passe decissive!")
    def recevoir_carton_jaune(self):
        self.set_carton_j(self.__carton_j + 1)
        print(f"[--JAUNE--]{self.get_nom()} reçois un carton jaune !")
        if self.__carton_j == 2:
            self.set_carton_j(0)
            self.recevoir_carton_rouge()
            print("Deuxième carton jaune ! C'est le rouge!")
    def recevoir_carton_rouge(self):
        self.set_carton_r(self.__carton_r + 1)
        print(f"[--ROUGE--]{self.get_nom()} reçois un carton rouge !")

    def afficher_stat(self):
        print(f"""
        Nom : {self.get_nom()}  || Numéro: {self.get_numero()}  || Position : {self.get_position()}
    But marqué : {self.get_but()}   ||  Passe décisive: {self.get_passe()} || Carton Jaune : {self.get_carton_j()} || Carton Rouge : {self.get_carton_r()}""")

class Equipe:
    def __init__(self, nom_equipe):
        self.__nom_equipe = nom_equipe
        self.liste_equipe = []

    def get_nom_equipe(self):
        return self.__nom_equipe

    def ajouter_joueur(self, joueur):
        self.liste_equipe.append(joueur)
        print(f"{joueur.get_nom()} a été ajouté à l'équipe {self.get_nom_equipe()}")

    def afficher_statistiques_joueurs(self):
        print(f"\n Statistiques de l'équipe {self.__nom_equipe}:")
        for joueur in self.liste_equipe:
            joueur.afficher_stat()

    def mettre_a_jour_statistiques_joueur(self, joueur, buts, passes, carton_jaune, carton_rouge):
        joueur.set_but(joueur.get_but() + buts)
        joueur.set_passe(joueur.get_passe() + passes)
        joueur.set_carton_j(joueur.get_carton_j() + carton_jaune)
        joueur.set_carton_r(joueur.get_carton_r() + carton_rouge)

equipe1 = Equipe("Équipe 1")
joueur1 = Joueur("John", 10, "Attaquant")
joueur2 = Joueur("Peter", 7, "Gardien")

equipe2 = Equipe("Équipe 2")
joueur3 = Joueur("Bob", 5, "Attaquant")
joueur4 = Joueur("Thomas", 12, "Gardien")

equipe1.ajouter_joueur(joueur1)
equipe1.ajouter_joueur(joueur2)
equipe2.ajouter_joueur(joueur3)
equipe2.ajouter_joueur(joueur4)

equipe1.afficher_statistiques_joueurs()
equipe2.afficher_statistiques_joueurs()

joueur2.effectuer_passe_decisive()
joueur1.marquer_but()
joueur3.recevoir_carton_jaune()
joueur2.effectuer_passe_decisive()
joueur1.marquer_but()
joueur3.effectuer_passe_decisive()
joueur4.marquer_but()
joueur3.recevoir_carton_jaune()
equipe1.mettre_a_jour_statistiques_joueur(joueur2, buts=1, passes=0, carton_jaune=1, carton_rouge=0)

equipe1.afficher_statistiques_joueurs()
equipe2.afficher_statistiques_joueurs()