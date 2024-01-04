class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plat_commande = []
        self.__statut_commande = "en cours"

    def get_numero_commande(self):
        return self.__numero_commande
    
    def get_statut_commande(self):
        return self.__statut_commande
    
    def get_plats_commandes(self):
        return self.__plat_commande

    def annuler_commande(self):
        self.__plat_commande = []
        self.__statut_commande = "annulée"
        print(f"Annulation de commande, Statut: {self.get_statut_commande()}")

    def ajouter_plat(self, nom_plat, prix, statut="en cours"):
        self.__plat_commande.append({"nom": nom_plat, "prix": prix, "statut": statut})
        self.__statut_commande = "en cours"

    def __calculer_total(self):
        total = 0
        for plat in self.__plat_commande:
            total += plat["prix"] 
        return total
    
    def calculer_tva(self, taux_tva=0.2):
        total = self.__calculer_total()
        tva = total * taux_tva
        return tva

    def afficher_commande(self):
        tva = self.calculer_tva()
        total = self.__calculer_total()
        if self.__plat_commande != []:
            print(f"\n      Commande #{self.__numero_commande}")
            for plat in self.__plat_commande:
                print(f" - {plat['nom']}: {plat['prix']} € ({plat['statut']})")
            print(f"Total à payer: {total} € (TVA incluse: {tva} €)\n")
        else:
            print(f"Aucun plat pour la Commande #{self.__numero_commande}\n")

commande1 = Commande(numero_commande=1)

commande1.ajouter_plat("Pizza", prix=10.0)
commande1.ajouter_plat("Salade César", prix=7.5)
commande1.ajouter_plat("Tiramisu", prix=5.0)

commande1.afficher_commande()

print(f"TVA à payer pour la commande #{commande1.get_numero_commande()}: {commande1.calculer_tva()} €\n")

commande1.annuler_commande()
commande1.afficher_commande()
