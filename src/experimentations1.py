import matplotlib.pyplot as plt

from jeu import main


profondeur = 1
resultats_minimax, resultats_alphabeta = [], []
for i in range(10):
    print("Profondeur :", profondeur)
    grille_minimax, ia_blanc_minimax, ia_noir_minimax = main(
        4, 3, 0, profondeur, profondeur, False)
    resultats_minimax.append(
        (ia_blanc_minimax.compteur_noeuds_visites, ia_noir_minimax.compteur_noeuds_visites))

    grille_alphabeta, ia_blanc_alphabeta, ia_noir_alphabeta = main(
        4, 3, 0, profondeur, profondeur, True)
    resultats_alphabeta.append(
        (ia_blanc_alphabeta.compteur_noeuds_visites, ia_noir_alphabeta.compteur_noeuds_visites))
    profondeur += 1


plt.figure()
plt.plot([i for i in range(1, profondeur)], [
         b for b, n in resultats_minimax], color='r', label="Blanc")
plt.plot([i for i in range(1, profondeur)], [
         n for b, n in resultats_minimax], color='b', label="Noir")
plt.grid()
plt.legend()
plt.title("Nombre de noeuds explorés par MinMax")
plt.ylabel("Nombre de noeuds explorés")
plt.xlabel("Profondeur")

plt.figure()
plt.plot([i for i in range(1, profondeur)], [
         b for b, n in resultats_alphabeta], color='r', label="Blanc")
plt.plot([i for i in range(1, profondeur)], [
         n for b, n in resultats_alphabeta], color='b', label="Noir")
plt.grid()
plt.legend()
plt.ylabel("Nombre de noeuds explorés")
plt.xlabel("Profondeur")
plt.title("Nombre de noeuds explorés par AlphaBeta")

plt.figure()
plt.plot([i for i in range(1, profondeur)], [b+n for b,
                                             n in resultats_minimax], color='r', label="MinMax")
plt.plot([i for i in range(1, profondeur)], [b+n for b,
                                             n in resultats_alphabeta], color='b', label="AlphaBeta")
plt.grid()
plt.legend()
plt.ylabel("Nombre de noeuds explorés")
plt.xlabel("Profondeur")
plt.title("Nombre de noeuds explorés par chaque algorithme")
plt.show()
