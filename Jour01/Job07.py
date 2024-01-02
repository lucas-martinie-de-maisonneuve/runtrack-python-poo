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
        for i in range(len(self.plateau)):
            for j in range(len(self.plateau[i])):
                if i == self.y and j == self.x:
                    self.plateau[i][j] = 1
                else:
                    self.plateau[i][j] = 0
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

print (f"""
    {plateau_de_jeu[0]}
    {plateau_de_jeu[1]}
    {plateau_de_jeu[2]}
    {plateau_de_jeu[3]}
       """)