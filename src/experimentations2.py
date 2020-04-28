from jeu import main


def gagnant(grille):
    if grille.pions_blanc > grille.pions_noir:
        return "B"
    elif grille.pions_noir > grille.pions_blanc:
        return "N"
    else:
        return "E"


for h in [4, 5]:
    for i in range(1, 11):
        for j in range(1, 7):
            grille, ia_blanc, ia_noir = main(h, h, i, j, 1, True)
            print(f"({h},{h})Avance {i}, Profondeur {j} == > {gagnant(grille)}")
    print()
