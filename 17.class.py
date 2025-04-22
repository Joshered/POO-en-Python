class rectangle:
    def __init__(self,longeur,largeur,couleur="red"):
        self.longeur=longeur
        self.largeur = largeur
        self.couleur = couleur


    def calculer_surface(self):
        return self.largeur * self.hauteur