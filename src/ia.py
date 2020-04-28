class IA:
    """
        Représente une intelligence artificielle associée à un joueur.
    """

    def __init__(self, joueur, profondeur=1, elagage=False):
        self.joueur = joueur
        self.profondeur = profondeur
        self.elagage = elagage
        self.compteur_noeuds_visites = 0

    def play(self, etat):
        """
            Permet de faire jouer l'IA en appelant la meilleure méthode (en fonction de self.elagage).
        """
        if self.elagage:
            _, coup = self.alphabeta(
                etat, self.profondeur, -float('inf'), float('inf'))
        else:
            _, coup = self.minmax(etat, self.profondeur)
        return coup

    def minmax(self, etat, profondeur):
        """
            Algorithme MinMax permettant de choisir le meilleur coup possible en fonction des choix de l'adversaire.
        """
        self.compteur_noeuds_visites += 1
        if profondeur == 0 or etat.estTermine():
            return etat.evaluation(self.joueur), None
        if etat.joueurActuel == self.joueur:
            meilleur_valeur = -float('inf')
            meilleur_coup = None
            for action in etat.possibilitesJoueur(etat.joueurActuel):
                nouvel_etat = etat.effectuerAction(action)
                valeur, _ = self.minmax(nouvel_etat, profondeur-1)
                if valeur > meilleur_valeur:
                    meilleur_valeur = valeur
                    meilleur_coup = action
            return meilleur_valeur, meilleur_coup
        else:
            meilleur_valeur = float('inf')
            meilleur_coup = None
            for action in etat.possibilitesJoueur(etat.joueurActuel):
                nouvel_etat = etat.effectuerAction(action)
                valeur, _ = self.minmax(nouvel_etat, profondeur-1)
                if valeur < meilleur_valeur:
                    meilleur_valeur = valeur
                    meilleur_coup = action
            return meilleur_valeur, meilleur_coup

    def alphabeta(self, etat, profondeur, alpha, beta):
        """
            Algorithme AlphaBeta permettant de choisir le meilleur coup possible en fonction des choix de l'adversaire.
            Similaire à l'algorithme MinMax mais permet de visiter moins de noeuds.
        """
        self.compteur_noeuds_visites += 1
        if profondeur == 0 or etat.estTermine():
            return etat.evaluation(self.joueur), None
        if etat.joueurActuel == self.joueur:
            meilleur_coup = None
            for action in etat.possibilitesJoueur(etat.joueurActuel):
                nouvel_etat = etat.effectuerAction(action)
                valeur, _ = self.alphabeta(
                    nouvel_etat, profondeur-1, alpha, beta)
                if valeur > alpha:
                    alpha = valeur
                    meilleur_coup = action
                if alpha >= beta:
                    return alpha, meilleur_coup
            return alpha, meilleur_coup
        else:
            meilleur_coup = None
            for action in etat.possibilitesJoueur(etat.joueurActuel):
                nouvel_etat = etat.effectuerAction(action)
                valeur, _ = self.alphabeta(
                    nouvel_etat, profondeur-1, alpha, beta)
                if valeur < beta:
                    beta = valeur
                    meilleur_coup = action
                if beta <= alpha:
                    return beta, meilleur_coup
            return beta, meilleur_coup
