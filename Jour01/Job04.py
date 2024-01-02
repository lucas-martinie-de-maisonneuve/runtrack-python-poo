class Personne:

    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom
    
    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}"
    
john = Personne("John", "Doe")
jean = Personne("Jean", "Dupont")

print (john.SePresenter())
print (jean.SePresenter())