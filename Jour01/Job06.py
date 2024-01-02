class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1
        print(f"L'âge de l'animal est : {animal.age}")


    def nommer(self, nouveau_nom):
        self.prenom = nouveau_nom
        print(f"Le nom de l'animal est : {animal.prenom}")


animal = Animal()

print(f"L'âge de l'animal est : {animal.age}")
animal.vieillir()
animal.nommer("Luna")
animal.vieillir()
animal.vieillir()
animal.vieillir()

