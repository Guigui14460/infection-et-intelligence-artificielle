# Jeu d'infection et algorithmes d'intelligence artificielle

Projet universitaire donné dans l'UE Sécurité et Aide à la Décision en L2 Informatique à l'Université de Caen Normandie.

<img src="logo-UNICAEN.jpg" style="width: 100px;" />


## Table des matières
1. [Introduction au sujet](#introduction)
2. [Setup](#setup)
3. [Utilisation](#utilisation)
4. [Auteurs](#auteurs)

## Introduction
Le but du projet est de créer un jeu d'infection basique entre des pions de 2 couleurs différentes. Les règles sont :
- se déplacer de 2 cases sur chaque directions (autre que diagonales)
- se déplacer d'une case sur chaque directions (autre que diagonales) et infecter tous les pions se trouvant autourde la case d'arrivée.

Le jeu se termine uniquement lorsqu'il n'y a plus de place sur le plateau ou lorsque l'un des joueurs ne possède plus de pion.

L'autre but était d'implémenter des algorithmes d'intelligence artificielle tels que minimax (ou appelé MinMax) ou encore alphabeta, et si l'on souhaitait, leur version Négamax. Sur ce dépôt, les versions négamax des algotithmes ne sont pas présentes. Ces deux algorithmes permettent d'explorer chaque possibilités de chaque coup pour un état de jeu donné. Cela va donc permettre d'effectuer le meilleur coup pour le joueur utilisant l'algorithme.

## Setup
Python 3 doit être installé ainsi que les librairies `numpy` et `matplolib`.
```bash
pip install numpy matplotlib
```
ou
```bash
pip3 install numpy matplotlib
```

## Utilisation
Pour utiliser notre jeu, il faut utiliser la commande suivante :
Windows : 
```bash
python jeu.py <N> <M> <headstart> <black_player_reasoning> <white_player_reasoning> <alphabeta_use>
```

Linux/MasOS :
```bash
python3 jeu.py <N> <M> <headstart> <white_player_reasoning> <black_player_reasoning> <alphabeta_use>
```

- `<N>` : nombre de lignes de la grille (nombre entier strictement positif)
- `<M>` : nombre de colonnes de la grille (nombre entier strictement positif
- `<headstart>` : nombre de coups d'avance donné au joueur blanc (nombre entier positif)
- `<white_player_reasoning>` : profondeur de raisonnement du joueur blanc (nombre entier strictement positif)
- `<black_player_reasoning>` : profondeur de raisonnement du joueur noir (nombre entier strictement positif)
- `<alphabeta_use>` : utilisation d'un élagage alphabeta (0 ou 1)

## Auteurs
[MOK William](https://github.com/Akbeeh)
[LETELLIER Guillaume](https://github.com/Guigui14460)