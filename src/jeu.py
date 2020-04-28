from grille import Grille
from ia import IA


def main(nbLignes, nbColonnes, nb_coups_avance_blanc=0, profondeur_raisonnement_noir=1, profondeur_raisonnement_blanc=1, alphabeta_utilisation=True):
    if nbLignes <= 1 or nbColonnes <= 1:
        raise ValueError(
            "Le nombre de lignes et de colonnes doit être supérieur ou égale à 2")
    if nb_coups_avance_blanc < 0:
        raise ValueError("On peut pas retourner en arrière")
    if profondeur_raisonnement_blanc < 1:
        raise ValueError(
            "Il faut que l'IA puisse réfléchir. Mettez un nombre >= 1")
    if profondeur_raisonnement_noir < 1:
        raise ValueError(
            "Il faut que l'IA puisse réfléchir. Mettez un nombre >= 1")

    historique_grille = []

    grille = Grille(nbLignes, nbColonnes)
    ia_blanc = IA('blanc', profondeur_raisonnement_blanc,
                  alphabeta_utilisation)
    ia_noir = IA('noir', profondeur_raisonnement_noir, alphabeta_utilisation)
    for i in range(nb_coups_avance_blanc):
        mouv = ia_blanc.play(grille)
        nouvelle_grille = grille.effectuerAction(mouv)
        grille.grille = nouvelle_grille.grille
        del nouvelle_grille

    print(
        f"Grille initiale (avec {nb_coups_avance_blanc} coups d'avance pour le joueur blanc):")
    print(grille)

    while not grille.estTermine() and not any([grille == h for h in historique_grille]):
        historique_grille.append(grille)
        joueur = grille.joueurActuel
        if joueur == 'blanc':
            mouvement = ia_blanc.play(grille)
        else:
            mouvement = ia_noir.play(grille)
        grille = grille.effectuerAction(mouvement)
    return grille, ia_blanc, ia_noir


if __name__ == "__main__":
    import os
    import sys

    if len(sys.argv) != 7:
        print(
            f"Erreur d'usage : {os.path.basename(sys.argv[0])} <N> <M> <headstart> <black_player_reasoning> <white_player_reasoning> <alphabeta_use>")
        print("Pour plus d'information sur les paramètres, regarder le fichier readme.txt")
        sys.exit(2)

    grille, ia_blanc, ia_noir = main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(
        sys.argv[4]), int(sys.argv[5]), bool(int(sys.argv[6])))

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

    print("Nombre de noeuds visités :", ia_blanc.compteur_noeuds_visites,
          ia_noir.compteur_noeuds_visites)
