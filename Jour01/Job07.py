class Personnage:
    def __init__(self, x, y, plateau):
        self.x = x
        self.y = y
        self.plateau = plateau

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
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

print("Position de depart:", personnage.position())
personnage.gauche()
print("Position après un déplacement à gauche:", personnage.position())
personnage.gauche()
print("Position après un déplacement à gauche:", personnage.position())
personnage.haut()
print("Position après un déplacement en haut:", personnage.position())
personnage.droite()
print("Position après un déplacement à droite:", personnage.position())
personnage.bas()
print("Position après un déplacement en bas:", personnage.position())