class Tache:
    def __init__(self, titre, description):
        self.__titre = titre
        self.__description = description
        self.__statut = "A faire"

    def get_titre(self):
        return self.__titre
    def get_description(self):
        return self.__description
    def get_statut(self):
        return self.__statut
    
    def set_titre(self, titre):
        self.__titre = titre
    def set_description(self, description):
        self.__description = description
    def set_statut(self, statut):
        self.__statut = statut

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouter_tache(self, tache):
        self.taches.append(tache)
        print(f"[--ADD--] Tâche '{tache.get_titre()}' ajoutée à la liste.")

    def supprimer_tache(self, tache):
        self.taches.remove(tache)
        print(f"[--DEL--] Tâche '{tache.get_titre()}' supprimée de la liste.")
        
    def marquer_comme_finie(self, tache):
        tache.set_statut("Terminée")
        print(f"[--TER--] Tâche '{tache.get_titre()}' marquée comme terminée.")

    def afficher_taches(self):
        if self.taches != []:
            for tache in self.taches:
                print(f"---> {tache.get_titre()} : {tache.get_description()} - ({tache.get_statut()})")
        else:
            print("Il n'y a pas encore de tache prévu")

    def filterListe(self):
        print("[-TO DO-] ------Les taches à faire sont :-------")
        for tache in self.taches:
            if tache.get_statut() == "A faire":
                print(f"[-TO DO-] ---> {tache.get_titre()} : {tache.get_description()} ({tache.get_statut()})")

tache1 = Tache("Courses", "de la semaine")
tache2 = Tache("Jardiner", "arroser les plantes")
tache3 = Tache("Faire du sport", "jogging pendant 30 minutes")
tache4 = Tache("Lire", "un livre pendant une heure")
tache5 = Tache("Apprendre", "une nouvelle compétence")

liste_taches = ListeDeTaches()

liste_taches.afficher_taches()
liste_taches.ajouter_tache(tache1)
liste_taches.ajouter_tache(tache2)
liste_taches.ajouter_tache(tache3)
liste_taches.ajouter_tache(tache4)
liste_taches.ajouter_tache(tache5)
liste_taches.afficher_taches()

liste_taches.marquer_comme_finie(tache1)
liste_taches.marquer_comme_finie(tache3)
liste_taches.marquer_comme_finie(tache5)
liste_taches.afficher_taches()
liste_taches.filterListe()

liste_taches.supprimer_tache(tache1)
liste_taches.supprimer_tache(tache3)
liste_taches.supprimer_tache(tache5)
liste_taches.afficher_taches()