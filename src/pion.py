class Pion:
    """
        Représente un simple pion.
        La couleur représente le joueur qui possède le pion.
    """

    def __init__(self, couleur):
        self.couleur = couleur

    def __str__(self):
        """
            Permet d'afficher clairement le pion.
        """
        if self.couleur == 'noir':
            return "N"
        return "B"
