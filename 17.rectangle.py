class rectangle:
    def __init__(self,longeur,largeur,couleur="red"):
        self.longeur=longeur
        self.largeur = largeur
        self.couleur = couleur


    def calculer_surface(self):
        return self.largeur * self.largeur

rectangle=rectangle(2,3)
print(f"il a comme couleur \"{rectangle.couleur}\" et a comme surface: {rectangle.calculer_surface()}")
