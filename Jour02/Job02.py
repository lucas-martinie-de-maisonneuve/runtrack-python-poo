class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_pages(self):
        return self.__nombre_pages

    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nombre_pages(self, nombre_pages):
        if isinstance(nombre_pages, int) and nombre_pages > 0:
            self.__nombre_pages = nombre_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

livre = Livre(titre="Le python", auteur="Lucas", nombre_pages=100)

print(f"""
        Titre: {livre.get_titre()}
        Auteur: {livre.get_auteur()}
        Nombre de pages : {livre.get_nombre_pages()}
""")

livre.set_titre("Le python 2")
livre.set_auteur("Martinie")

livre.set_nombre_pages(-50)

livre.set_nombre_pages(150)

print(f"""
        Nouveau Titre: {livre.get_titre()}
        Nouvel Auteur: {livre.get_auteur()}
        Nouveau nombre de pages : {livre.get_nombre_pages()}""")
