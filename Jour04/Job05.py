from math import pi
class Forme:
    def __init__(self):
        pass

    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    def aire(self):
        aire_rectangle = self.largeur * self.hauteur
        return aire_rectangle
    
class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        aire_cercle = pi * self.radius * self.radius
        return aire_cercle
    
forme = Forme()
rectangle = Rectangle(5, 3)
cercle = Cercle(5)

print(f"""
    Aire de Forme : {forme.aire()}
    Aire d'un rectangle 5x3 : {rectangle.aire()}
    Aire d'un cercle de rayon 5 : {cercle.aire()}
""")