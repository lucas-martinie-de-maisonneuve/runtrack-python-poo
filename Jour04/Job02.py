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
        print(f"Hello")

    def modifierAge(self, age):
        self.set_age(int(age))

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")

class Professeur(Personne):
    def __init__(self, matiere_enseignee):
        self.__matiereEnseignee = matiere_enseignee

    def getMatiereEnseignee(self):
        return self.__matiereEnseignee

    def enseigner(self):
        print(f"Le cours de {self.__matiereEnseignee} va commencer")


personne1 = Personne()
eleve1 = Eleve()
professeur = Professeur('math')

eleve1.afficherAge()
eleve1.bonjour()
eleve1.allerEnCours()
eleve1.modifierAge(15)
eleve1.afficherAge()
professeur.bonjour()
professeur.modifierAge(40)
professeur.enseigner()
professeur.afficherAge()
