class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.en_marche = False
        self.__reservoir = 50

    def get_marque(self):
        return self.__marque
    def get_modele(self):
        return self.__modele
    def get_annee(self):
        return self.__annee
    def get_kilometrage(self):
        return self.__kilometrage
    def get_en_marche(self):
        return self.en_marche
    def get_reservoir(self):
        return self.__reservoir
    
    def set_marque(self, marque):
        self.__marque = marque
    def set_modele(self, modele):
        self.__modele = modele
    def set_annee(self, annee):
        self.__annee = annee
    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage
    def set_reservoir(self, reservoir):
        self.__reservoir = reservoir
    
    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.en_marche = True
            print(f"        La voiture est démarré")
        else:
            print(f"        Il n'y a pas assez d'essence pour démarrer")

    def arreter(self):
        self.en_marche = False
        print(f"        La voiture s'arrête")

    def __verifier_plein(self):
        print(f"        Le réservoir est de {self.get_reservoir()} litres")
        return self.get_reservoir()

voit = Voiture(marque='Renault', modele='Twingo', annee=1995, kilometrage=500000)

print(f"""
        Voiture : {voit.get_marque()} {voit.get_modele()} de {voit.get_annee()} avec {voit.get_kilometrage()} Km
        """)
voit.demarrer()
voit.arreter()
voit.set_reservoir(5)
voit.demarrer()