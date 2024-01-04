class Ville:
    def __init__(self, nom_ville, habitants):
        self.__nom_ville = nom_ville
        self.__habitants = habitants

    def get_nom_ville(self):
        return self.__nom_ville
    def get_habitants(self):
        return self.__habitants
    
    def set_nom_ville(self, nom_ville):
        self.__nom_ville = nom_ville
    def set_habitants(self, habitants):
        self.__habitants = habitants

class Personne:
    def __init__(self, nom, age, objet_ville):
        self.__nom = nom
        self.__age = age
        self.__objet_ville = objet_ville
        
    def get_nom(self):
        return self.__nom
    def get_age(self):
        return self.__age
    def get_objet(self):
        return self.__objet_ville
    
    
    def set_nom(self, nom):
        self.__nom = nom
    def set_age(self, age):
        self.__age = age
    def set_objet(self, objet_ville):
        self.__objet_ville = objet_ville

    def ajouterPopulation(self):
            self.__objet_ville.set_habitants(self.__objet_ville.get_habitants() + 1)

ville1 = Ville('Paris', 1000000)
ville2 = Ville('Marseille', 861635)

print (f"Population de {ville1.get_nom_ville()} : {ville1.get_habitants()} habitants")
print (f"Population de {ville2.get_nom_ville()} : {ville2.get_habitants()} habitants")

habitant1 = Personne('John', 45, ville1)
habitant2 = Personne('Myrtille', 4, ville1)
habitant3 = Personne('Chloe', 18, ville2)


habitant1.ajouterPopulation()
habitant2.ajouterPopulation()
habitant3.ajouterPopulation()

print (f"Population de Paris : {ville1.get_habitants()} habitants")

print (f"Population de Marseille : {ville2.get_habitants()} habitants")
