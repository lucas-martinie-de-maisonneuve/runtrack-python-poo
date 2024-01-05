class Personne:
    def __init__(self, age=14):
        self.age = age

    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age

    def afficherAge(self):
        print(f"L'âge de la personne est : {self.age} ans")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, age):
        self.set_age(int(age))

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")

class Professeur:
    def __init__(self, matiere_enseignee):
        self.__matiereEnseignee = matiere_enseignee

    def enseigner(self):
        print("Le cours va commencer")

    def getMatiereEnseignee(self):
        return self.__matiereEnseignee


personne1 = Personne()
personne1.afficherAge()

eleve1 = Eleve()
eleve1.afficherAge()
