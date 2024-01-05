class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def perimetre(self):
        peri = self.__longueur * 2 + self.__largeur * 2
        return peri

    def surface(self):
        aire = self.__longueur * self.__largeur
        return aire


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def volume(self):
        vol = self.get_longueur() * self.get_largeur() * self.hauteur
        return vol

rect = Rectangle(4, 5)
paral = Parallelepipede(4, 5, 2)

print(f"""      
Rectangle:
    Périmètre: {rect.perimetre()} cm
    Surface: {rect.surface()} cm carré""")

print(f"""
Parallélépipède:
    Volume: {paral.volume()} cm cube
""")
