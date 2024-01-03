class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, new_longueur):
        self.__longueur = new_longueur

    def set_largeur(self, new_largeur):
        self.__largeur = new_largeur

rect = Rectangle(longueur=10, largeur=5)

print(f"""
    Longueur initiale : {rect.get_longueur()}
    Largeur initiale : {rect.get_largeur()}""")

rect.set_longueur(15)
rect.set_largeur(6)

print(f"""
    Longueur modifié : {rect.get_longueur()}
    Largeur modifié : {rect.get_largeur()}
""")
