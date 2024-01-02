class Personne:

    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom
    
    def SePresenter(self):
        print(f"Je suis {self.prenom} {self.nom}")
    
john = Personne("John", "Doe")
jean = Personne("Jean", "Dupont")

john.SePresenter()
jean.SePresenter()