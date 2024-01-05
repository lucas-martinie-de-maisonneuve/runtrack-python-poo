class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def demarrer(self):
        print('Attention, je roule')

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.portes = portes 

    def informationsVehicule(self):
        print(f""" 
            Marque du vehicule : {self.marque}
            Modele du vehicule : {self.modele}
            Annee du vehicule :  {self.annee}
            Prix du vehicule :   {self.prix} €
            Nombre de portes  :  {self.portes}
""")
    def demarrer(self):
        print('Attention, je roule avec ma belle Voiture')
        

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roue=2):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.roue = roue

    def informationsVehicule(self):
        print(f""" 
            Marque du vehicule : {self.marque}
            Modele du vehicule : {self.modele}
            Annee du vehicule :  {self.annee}
            Prix du vehicule :   {self.prix} €
            Nombre de roues  :  {self.roue}
""")
    def demarrer(self):
        print('Attention, je roule avec ma vieille moto\n')
        

voiture = Voiture('Mercedes', 'Classe A', 2020, 18500)
moto = Moto('Yamaha', '1200 Vmax', 1987, 4500)

voiture.informationsVehicule()
voiture.demarrer()
moto.informationsVehicule()
moto.demarrer()