# Writeup

Le chiffre de César original utilisait un alphabet décalé de trois lettres. On a donc la correspondance suivante:

```
A - D
B - E
C - F
D - G
E - H
F - I
G - J
H - K
I - L
J - M
K - N
L - O
M - P
N - Q
O - R
P - S
Q - T
R - U
S - V
T - W
U - X
V - Y
W - Z
X - A
Y - B
Z - C
```

Pour déchiffrer, il faut prendre chaque caractère du flag, partir de la colonne de droite et se rendre à la colonne de gauche:
- `I` devient `F`
- `O` devient `L`
- `D` devient `A`
- `J` devient `G`
- `-` reste identique
- `Y` devient `V`
- `H` devient `E`

Ainsi de suite, jusqu'à ce qu'on ait le flag complet: `FLAG-VENIVIDIVICI`.