class BoiteOutil:
    def __init__(self,identifiant):
        self.identifiant=identifiant

    def Ajouter_Outil(self):
        print("Outil ajouter")

    def Enlever_Outil(self):
        print("Outil enlever")


class Marteaux:
    def __init__(self,couleur):
        self.couleur=couleur

    def Planter(self):
        print("Clous planter")

    def Retirer(self):
        print("Clous retirer")

    def Paindre(self):
        print("Couleur à etait changer")

class Tournevis:
    def __init__(self,taille):
        self.taille=taille

    def Serer(self):
        print("vis serré")

    def Desserer(self):
        print("vis desseré")