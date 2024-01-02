class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    
    def CalculerPrixTTC(self):
        prixttc = self.prixHT * (1 + self.TVA /100)
        return round(prixttc, 2) 
    
    def afficher(self):
        return f"""-----------------------------------------------------------
            Nom du produit : {self.nom}
            Prix TTC : {self.CalculerPrixTTC()} €
            (Prix Hors Taxe : {self.prixHT} € et TVA à {self.TVA} %)"""
    
    def changer(self, new_prixHT, new_nom):
        self.prixHT = new_prixHT
        self.nom = new_nom
        return self.nom, self.prixHT

    def get_nom(self):
        return self.nom

    def get_prixHT(self):
        return self.prixHT

    def get_TVA(self):
        return self.TVA

pomme = Produit(nom="pomme", prixHT=1, TVA=5.5)
orange = Produit(nom="orange", prixHT=2, TVA=5.5)
banane = Produit(nom="banane", prixHT=1.5, TVA=5.5)

print(f"""-----------------------------------------------------------
    ---->   Informations initiales  <----
{pomme.afficher()}
{orange.afficher()}
{banane.afficher()}
""")

pomme.changer(new_prixHT=1.2, new_nom="pomme bio")
orange.changer(new_prixHT=2.5, new_nom="orange luxe")
banane.changer(new_prixHT=1.8, new_nom="banane jaune")

print(f"""-----------------------------------------------------------
    ---->   Informations après modification <----
{pomme.afficher()}
{orange.afficher()}
{banane.afficher()}
""")