class Personnage:
    def __init__(self, x, y, plateau):
        self.x = x
        self.y = y
        self.plateau = plateau

    def gauche(self):
        if self.x > 0:
            self.x -= 1

    def droite(self):
        if self.x < len(self.plateau[0]) - 1:
            self.x += 1

    def haut(self):
        if self.y > 0:
            self.y -= 1

    def bas(self):
        if self.y < len(self.plateau) - 1:
            self.y += 1

    def position(self):
        return (self.x, self.y)

plateau_de_jeu = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

personnage = Personnage(x=2, y=2, plateau=plateau_de_jeu)

print("Position initiale:", personnage.position())
personnage.gauche()
print("Position après déplacement à gauche:", personnage.position())
personnage.droite()
print("Position après déplacement vers le haut:", personnage.position())