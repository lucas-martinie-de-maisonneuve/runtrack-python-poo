from math import pi

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, new_rayon):
        self.rayon = new_rayon
    
    def afficherInfos(self):
        print (f"""
        Le rayon du cercle est : {self.rayon}
        Le diametre du cercle est : {cercle.diametre()}
        L'aire du cercle est : {cercle.aire()}
        La circonference du cercle est: {cercle.circonference()}
        """)

    def circonference(self):
        circonference_cercle = self.rayon * 2 * pi
        return circonference_cercle
    
    def aire(self):
        aire_cercle = self.rayon * self.rayon * pi
        return aire_cercle
    
    def diametre(self):
        diametre_cercle = self.rayon * 2
        return diametre_cercle
    
cercle = Cercle(4)
cercle.afficherInfos()
cercle.changerRayon(7)
cercle.afficherInfos()