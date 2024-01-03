class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages
        self.__disponible = True

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_pages(self):
        return self.__nombre_pages

    def set_titre(self, new_titre):
        self.__titre = new_titre

    def set_auteur(self, new_auteur):
        self.__auteur = new_auteur

    def set_nombre_pages(self, new_nombre_pages):
        if isinstance(new_nombre_pages, int) and new_nombre_pages > 0:
            self.__nombre_pages = new_nombre_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("     Livre emprunté avec succès.")
            return True
        else:
            return False

    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("     Livre rendu avec succès.")
            return True
        else:
            return False

livre = Livre(titre="Le python", auteur="Lucas", nombre_pages=100)

print(f"""
        Titre: {livre.get_titre()}
        Auteur: {livre.get_auteur()}
        Nombre de pages : {livre.get_nombre_pages()}
        Disponible : {livre.verification()}
""")

livre.set_titre("Le python 2")
livre.set_auteur("Martinie")

livre.set_nombre_pages(-50)

livre.set_nombre_pages(150)

print(f"""
        Nouveau Titre: {livre.get_titre()}
        Nouvel Auteur: {livre.get_auteur()}
        Nouveau nombre de pages : {livre.get_nombre_pages()}
        Disponible : {livre.verification()}
""")

{livre.emprunter()}
print (f"     Disponible : {livre.verification()}")
{livre.rendre()}
print(f"     Disponible : {livre.verification()}")
