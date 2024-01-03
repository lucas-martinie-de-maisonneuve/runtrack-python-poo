class Student:
    def __init__(self, prenom, nom, id, credit):
        self.__prenom = prenom
        self.__nom = nom
        self.__id = id
        self.__credit = credit
        self.__level = self.__studentEval__()

    def add_credits(self, credit):
        if isinstance(credit, int) and credit > 0:
            self.__credit += credit
            self.__level = self.__studentEval__()
        else:
            print("Le nombre de crédit à ajouter doit être supérieur à 0")

    def get_prenom(self):
        return self.__prenom
    def get_nom(self):
        return self.__nom
    def get_id(self):
        return self.__id
    def get_credit(self):
        return self.__credit
    def get_level(self):
        return self.__level

    def __studentEval__(self):
        credits = self.get_credit()
        if credits >= 90:
            return 'Excellent'
        elif credits >= 80:
            return 'Très bien'
        elif credits >= 70:
            return 'Bien'
        elif credits >= 60:
            return 'Passable'
        else:
            return 'Insuffisant'

    def studentInfo(self):
        print(f"""
            Nom = {self.get_nom()}
            Prenom = {self.get_prenom()}
            id = {self.get_id()}
            Niveau = {self.get_level()}""")

eleve1 = Student(prenom='John', nom='Doe', id='145', credit=0)

eleve1.add_credits(10)
eleve1.add_credits(10)
eleve1.add_credits(10)

print(f"Le nombre de crédits de {eleve1.get_prenom()} {eleve1.get_nom()} est de {eleve1.get_credit()} points.")

eleve1.add_credits(100)
print(f"Le nombre de crédits de {eleve1.get_prenom()} {eleve1.get_nom()} est de {eleve1.get_credit()} points.")
eleve1.studentInfo()
