class CompteBancaire:
    def __init__(self, num_compte, nom, prenom, solde, decouvert=True):
        self.__num_compte = num_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def get_num_compte(self):
        return self.__num_compte
    def get_nom(self):
        return self.__nom
    def get_prenom(self):
        return self.__prenom
    def get_solde(self):
        return self.__solde
    def get_decouvert(self):
        return self.__decouvert
    
    def set_num_compte(self, num_compte):
        self.__num_compte = num_compte
    def set_nom(self, nom):
        self.__nom = nom
    def set_prenom(self, prenom):
        self.__prenom = prenom
    def set_solde(self, solde):
        self.__solde = solde
    def set_decouvert(self, decouvert):
        self.__decouvert = decouvert

    def afficher_info(self):
        print(f"""
    | Prénom : {self.get_prenom()} 
    | Nom : {self.get_nom()}
    | Numéro de compte : {self.get_num_compte()}
    | Solde du compte: {self.get_solde()} €
    """)
    
    def afficher_solde(self):
        print(f"--> Le solde du compte n°{self.get_num_compte()} est de : {self.get_solde()} €")

    def versement(self, montant):
        self.set_solde(self.get_solde() + montant)
        print(f"{montant} € ont bien été crédités au compte n°{self.get_num_compte()}")
    
    def retrait(self, montant_retrait):
        if (self.get_solde() - montant_retrait >= 0 or self.get_decouvert()) and isinstance(montant_retrait, int):
            self.set_solde(self.get_solde() - montant_retrait)
            print(f"{montant_retrait} € ont bien été débités du compte n°{self.get_num_compte()}")
            self.agios()
        else:
            if not isinstance(montant_retrait, int):
                print(f"Impossible de retirer {montant_retrait} € Le montant doit être un entier")
            else:
                print(f"Impossible de retirer {montant_retrait} €, le solde est insuffisant ({self.get_solde()} €)")

    def agios(self):
        if self.get_solde() < 0:
            self.set_solde(self.get_solde() - 10)
            print("Des agios de 10€ ont été appliqués au compte")

    def virement(self, reference, compte_destinataire, montant):
        if (self.get_solde() - montant >= 0 and isinstance(montant, int)):
            self.retrait(montant)
            compte_destinataire.versement(montant)
            print(f"""
        Virement du Compte n°{self.get_num_compte()}({self.get_prenom()}) vers le compte n°{compte_destinataire.get_num_compte()}({compte_destinataire.get_prenom()})
                {montant} € effectué avec succès (Ref : n°{reference})
            """)
        else:
            print("Impossible de réaliser le virement, solde insuffisant.")

compte1 = CompteBancaire(105200, 'Doe', 'John', 1200)
compte2 = CompteBancaire(252161, 'Smith', 'Alice', -500)

compte1.afficher_info()
compte1.retrait(1000)
compte1.afficher_solde()
compte1.retrait(10.5)
compte1.retrait(350)
compte1.afficher_solde()
compte1.versement(4000)
compte1.afficher_solde()

compte2.afficher_info()
compte1.virement('65654', compte2, 500)
compte1.afficher_solde()
compte2.afficher_solde()