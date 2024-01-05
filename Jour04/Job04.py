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

forme = Forme()
rectangle = Rectangle(5, 3)

print(f"""
    Aire de Forme : {forme.aire()}
    Aire d'un rectangle 5x3 : {rectangle.aire()}
""")