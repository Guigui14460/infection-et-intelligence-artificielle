from random import choice

from grille import Grille


def main(nbLignes, nbColonnes, nb_coups_avance_blanc=0):
    if nbLignes <= 1 or nbColonnes <= 1:
        raise ValueError(
            "Le nombre de lignes et de colonnes doit être supérieur ou égale à 2")
    if nb_coups_avance_blanc < 0:
        raise ValueError("On peut pas retourner en arrière")

    grille = Grille(nbLignes, nbColonnes)
    for i in range(nb_coups_avance_blanc):
        mouv = choice(grille.possibilitesJoueur(grille.joueurActuel))
        nouvelle_grille = grille.effectuerAction(mouv)
        grille.grille = nouvelle_grille.grille
        del nouvelle_grille

    print(
        f"Grille initiale (avec {nb_coups_avance_blanc} coups d'avance pour le joueur blanc):")
    print(grille)

    while not grille.estTermine():
        joueur = grille.joueurActuel
        mouvements = grille.possibilitesJoueur(joueur)
        print(mouvements)
        mouv = choice(mouvements)
        grille = grille.effectuerAction(mouv)
    print(grille.possibilitesJoueur(grille.joueurActuel))
    return grille


if __name__ == "__main__":
    import os
    import sys

    if len(sys.argv) != 4:
        print(
            f"Erreur d'usage : {os.path.basename(sys.argv[0])} <N> <M> <headstart>")
        print("Pour plus d'information sur les paramètres, regarder le fichier readme.txt")
        sys.exit(2)

    grille = main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

    print(grille)
    print(
        f"Score :\n - blanc -> {grille.pions_blanc} pions\n - noir -> {grille.pions_noir} pions")
    print(
        f"Résultat : B = {grille.evaluation('blanc')}, N = {grille.evaluation('noir')} ", end='')
    if grille.pions_blanc > grille.pions_noir:
        print("les pions blancs ont gagné !")
    elif grille.pions_noir > grille.pions_blanc:
        print("les pions noirs ont gagné !")
    else:
        print("égalité parfaite !")
