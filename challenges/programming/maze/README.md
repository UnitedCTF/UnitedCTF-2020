# Le classique: Labyrinthe

> Programming

Author: @xshill

Dans ce défi, un défi classique de programmation: résoudre un labyrinthe! Le serveur génère des labyrinthes aléatoires. Il vous donne une case de départ, une case d'arrivée et vous devez trouver un chemin qui se rend à la destination.

## Interpréter le labyrinthe
Le serveur vous envoie le labyrinthe sous format texte. Les caractères suivants sont utilisés:

```
# Représente un mur
0 (zéro) représente un espace vide
D représente la case départ
F représente la case d'arrivée
```

### Exemple de labyrinthe

```
8
########
#D#000##
#0#F#00#
#00##0##
#0#0000#
#0####0#
#000000#
########
```

> **NOTE**: La première case représente le nombre de lignes du labyrinthe. **Le labyrinthe est toujours carré** (nombre de lignes == nombre de colonnes).

> **NOTE**: Il y aura toujours des murs sur les 4 côtés du labyrinthe. Les murs sont "inclus" dans le labyrinthe qui vous est envoyé, c'est-à-dire que les cases de `(0, 0)` à `(0, 8)` sont des murs, les cases de `(0, 0)` à `(8, 0)` sont des murs, etc.

### Structure de données
Pour représenter le labyrinthe dans votre code, il vous sera utile d'utiliser une structure de données qui représente la position d'une case et si celle-ci peut être traversée ou non.

Une façon de faire serait d'utiliser les classes / structures et de créer un objet pour chaque case.

Une autre façon de faire (encore plus simple dans ce cas-ci) serait d'utiliser simplement un tableau à deux dimensions (X et Y). La valeur de chaque entrée du tableau serait un booléen `True|False` représentant l'état de la case (traversable ou non).

```
labyrinthe[x][y] = True // Vide
labyrinthe[x][y] = False // Mur
```

## Pistes de solution
### Backtracking
Une solution simple (mais moins efficace) de résoudre de labyrinthe est d'utiliser un algorithme de backtracking qui essaie tous les chemins jusqu'à temps qu'il trouve le bon. Si le labyrinthe n'est pas trop gros, l'algorithme pourra trouver une solution en un temps raisonnable.

Avec une version récursive, on essaie les cases une par une. Si on se retrouve coincé, alors on revient à la case précédente et on essaie toutes les autres cases qu'on n'a pas encore essayées. Si toutes ces cases mènent à des culs-de-sac, alors on revient à l'autre case d'avant, etc.

### L'algorithme A*
L'algorithme A* (A star) est un algorithme populaire utilisé dans des problèmes de pathfinding. Il est très utile à connaître, car il peut nous donner le chemin le plus court vers la destination recherchée.

Puisque l'algorithme est un peu plus complexe à expliquer, je vous laisse le soin de faire vos recherches sur Google pour en apprendre plus!

## Format de la solution
Vous devez envoyer votre solution au serveur selon le format suivant:

```
Nombre de cases du chemin
Case #1
Case #2
...
```

Exemple:

```
7
1 0
1 1
1 2
2 2
3 2
4 2
4 3
```

La case de départ et la case d'arrivée doivent être incluses dans votre réponse.

> **ATTENTION**: L'axe des Y va de **haut en bas**. Ainsi, dans un labyrinthe de 8 par 8, le coin **en haut à gauche** est (0, 0) et le coin **en bas à droite** est (8, 8). C'est une convention très souvent utilisée en informatique.

> **NOTE**: vous pouvez seulement vous déplacer horizontalement et verticalement. Pas de diagonales!

> **NOTE**: envoyez votre réponse en un seul appel réseau (concaténez toutes les lignes de la solution et envoyez la avec un seul `send`).

## Setup

Requirements:
- None

Start:

```
docker-compose up maze
```
