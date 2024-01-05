class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f"L'âge de la personne est : {self.age} ans")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, age):
        self.age = int(age)

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
personne1.modifierAge(20)
personne1.afficherAge() 

eleve1 = Eleve()
eleve1.afficherAge()
eleve1.allerEnCours()
eleve1.modifierAge(16)
eleve1.afficherAge()