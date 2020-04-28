from pion import Pion


class Grille:
    """
        Représente la grille du jeu.
    """

    def __init__(self, nbLignes, nbColonnes, joueurInitial='blanc'):
        self.nbLignes = nbLignes
        self.nbColonnes = nbColonnes
        self.joueurActuel = joueurInitial
        self.grille = [[None for j in range(nbColonnes)]
                       for i in range(nbLignes)]
        self.ajoutePion(Pion("noir"), 0, 0)
        self.ajoutePion(Pion("blanc"), nbLignes - 1, nbColonnes - 1)
        self.pions_blanc = 1
        self.pions_noir = 1

    def __str__(self):
        """
            Permet d'afficher la grille proprement en passant l'objet dans la fonction print().
        """
        object_repr = ""
        for i in range(self.nbLignes):
            for j in range(self.nbColonnes):
                if self.grille[i][j] == None:
                    object_repr += " x "
                else:
                    object_repr += f" {str(self.grille[i][j])} "
                if j != self.nbColonnes - 1:
                    object_repr += "|"
            object_repr += "\n"
        return object_repr

    def __eq__(self, value):
        """
            Permet de vérifier si deux grilles sont équivalentes ou non.
        """
        for i in range(self.nbLignes):
            for j in range(self.nbColonnes):
                if value.grille[i][j] != self.grille[i][j]:
                    return False
        return True

    def copieGrille(self):
        """
            Copie l'objet Grille vers un nouvel objet.
            Les deux copies sont indépendants.
            Deux pions se trouvant au même endroit de la grille sont différents l'un de l'autre.
        """
        nouvelleGrille = Grille(
            self.nbLignes, self.nbColonnes, joueurInitial=self.joueurActuel)
        for i in range(self.nbLignes):
            for j in range(self.nbColonnes):
                pion_ancienne_grille = self.getObjetParPosition(i, j)
                if pion_ancienne_grille != None:
                    nouvelleGrille.setObjetParPosition(
                        Pion(pion_ancienne_grille.couleur), i, j)
        return nouvelleGrille

    def getObjetParPosition(self, ligne, colonne):
        """
            Récupère un objet en donnant ses coordonnées.
        """
        return self.grille[ligne][colonne]

    def setObjetParPosition(self, objet, ligne, colonne):
        """
            Place un objet aux coordonnées données.
        """
        self.grille[ligne][colonne] = objet

    def estTermine(self):
        """
            Vérifie que le jeu est terminé.
        """
        if self.evaluation(self.joueurActuel) == 1 or self.pions_noir == 0 or self.pions_blanc == 0 or self.pions_blanc+self.pions_noir == self.nbLignes*self.nbColonnes or len(self.possibilitesJoueur(self.joueurActuel)) == 0:
            return True
        return False

    def joueurSuivant(self):
        """
            Permet de changer le joueur actuel.
        """
        if self.joueurActuel == 'blanc':
            self.joueurActuel = 'noir'
        else:
            self.joueurActuel = 'blanc'

    def evaluation(self, joueur):
        """
            Permet d'évaluer la proportion de pion du joueur actuel.
        """
        if joueur == 'blanc':
            pions_joueur_actuel = self.pions_blanc
        else:
            pions_joueur_actuel = self.pions_noir
        return pions_joueur_actuel / (self.pions_blanc + self.pions_noir)

    def pionCompteur(self, joueur=None):
        """
            Renvoie le nombre de pions de chaque couleur.
        """
        cpt_noir = 0
        cpt_blanc = 0
        for i in range(self.nbLignes):
            for j in range(self.nbColonnes):
                if self.getObjetParPosition(i, j) != None:
                    if self.getObjetParPosition(i, j).couleur == 'noir':
                        cpt_noir += 1
                    else:
                        cpt_blanc += 1
        if joueur == None:
            return cpt_blanc, cpt_noir
        if joueur == 'blanc':
            return cpt_blanc
        return cpt_noir

    def ajoutePion(self, objet, ligne, colonne):
        """
            Ajoute un pion aux coordonnées données.
            Cette méthode permet de vérifier que les coordonnées sont correctes avant de placer le pion sur celles-ci.
        """
        if (ligne >= self.nbLignes or ligne < 0) or (colonne >= self.nbColonnes or colonne < 0) or self.getObjetParPosition(ligne, colonne) != None:
            return False
        self.setObjetParPosition(objet, ligne, colonne)
        return objet

    def dupliquerPion(self, ancienne_ligne, ancienne_colonne, ligne, colonne):
        """
            Permet de dupliquer le pion sur un des quatre points cardinaux.
        """
        resultat = self.ajoutePion(Pion(self.getObjetParPosition(
            ancienne_ligne, ancienne_colonne).couleur), ligne, colonne)
        # Vérification que le pion est placé/ajouté
        if resultat:
            self.contamination(resultat, ligne, colonne)

    def contamination(self, objet, ligne, colonne):
        """
            Permet de contaminer les pions adverses se trouvant à une distance de une case aux quatre points cardianaux.
        """
        # Contamine le pion du haut
        if ligne > 0 and self.getObjetParPosition(ligne-1, colonne) != None:
            self.setObjetParPosition(Pion(objet.couleur), ligne-1, colonne)
        # Contamine le pion du bas
        if ligne < self.nbLignes-1 and self.getObjetParPosition(ligne+1, colonne) != None:
            self.setObjetParPosition(Pion(objet.couleur), ligne+1, colonne)
        # Contamine le pion de gauche
        if colonne > 0 and self.getObjetParPosition(ligne, colonne-1) != None:
            self.setObjetParPosition(Pion(objet.couleur), ligne, colonne-1)
        # Contamine le pion de droit
        if colonne < self.nbColonnes-1 and self.getObjetParPosition(ligne, colonne+1) != None:
            self.setObjetParPosition(Pion(objet.couleur), ligne, colonne+1)

    def deplacerPion(self, ancienne_ligne, ancienne_colonne, ligne, colonne):
        """
            Permet de déplacer un pion d'une coordonnée à une autre.
        """
        pion = self.getObjetParPosition(ancienne_ligne, ancienne_colonne)
        if pion != None:
            resultat = self.ajoutePion(pion, ligne, colonne)
            if resultat:
                self.setObjetParPosition(
                    None, ancienne_ligne, ancienne_colonne)

    def possibilitesJoueur(self, joueur):
        """
            Permet de lister tous les coups possibles du joueur passé en argument.
        """
        liste_possibilite = []

        for i in range(self.nbLignes):
            for j in range(self.nbColonnes):
                if self.getObjetParPosition(i, j) != None and self.getObjetParPosition(i, j).couleur == joueur:
                    pion = self.getObjetParPosition(i, j)
                    # Partie duplication
                    if i-1 >= 0 and self.getObjetParPosition(i-1, j) == None:
                        liste_possibilite.append({'position': (
                            i, j), 'action': 'dupliquer', 'position_suivante': (i-1, j)})
                    if i+1 < self.nbLignes and self.getObjetParPosition(i+1, j) == None:
                        liste_possibilite.append({'position': (
                            i, j), 'action': 'dupliquer', 'position_suivante': (i+1, j)})
                    if j-1 >= 0 and self.getObjetParPosition(i, j-1) == None:
                        liste_possibilite.append({'position': (
                            i, j), 'action': 'dupliquer', 'position_suivante': (i, j-1)})
                    if j+1 < self.nbColonnes and self.getObjetParPosition(i, j+1) == None:
                        liste_possibilite.append({'position': (
                            i, j), 'action': 'dupliquer', 'position_suivante': (i, j+1)})

                    # Partie déplacement
                    if i-2 >= 0 and self.getObjetParPosition(i-2, j) == None:
                        liste_possibilite.append({'position': (
                            i, j), 'action': 'déplacer', 'position_suivante': (i-2, j)})
                    if i+2 < self.nbLignes and self.getObjetParPosition(i+2, j) == None:
                        liste_possibilite.append({'position': (
                            i, j), 'action': 'déplacer', 'position_suivante': (i+2, j)})
                    if j-2 >= 0 and self.getObjetParPosition(i, j-2) == None:
                        liste_possibilite.append({'position': (
                            i, j), 'action': 'déplacer', 'position_suivante': (i, j-2)})
                    if j+2 < self.nbColonnes and self.getObjetParPosition(i, j+2) == None:
                        liste_possibilite.append({'position': (
                            i, j), 'action': 'déplacer', 'position_suivante': (i, j+2)})
        return liste_possibilite

    def effectuerAction(self, action_dict):
        """
            Permet d'effectuer une action donnée et donc de créer un nouvel état de jeu.
        """
        if action_dict is None:
            self.joueurSuivant()
            return self
        nouvelle_grille = self.copieGrille()
        if action_dict is not None:
            if action_dict['action'] == 'dupliquer':
                nouvelle_grille.dupliquerPion(
                    action_dict['position'][0], action_dict['position'][1], action_dict['position_suivante'][0], action_dict['position_suivante'][1])
            else:
                nouvelle_grille.deplacerPion(
                    action_dict['position'][0], action_dict['position'][1], action_dict['position_suivante'][0], action_dict['position_suivante'][1])
        nouvelle_grille.joueurSuivant()
        nouvelle_grille.pions_blanc, nouvelle_grille.pions_noir = nouvelle_grille.pionCompteur()
        return nouvelle_grille
