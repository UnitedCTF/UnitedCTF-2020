# Writeup

Sachant que la clé est de 4 caractères et que le secret déchiffré commencera par "FLAG", on peut trouver les 4 caractères de la clé:

```
J - F = 4
K - L = 25
P - A = 15
F - G = 25
```

Les chiffres à droite correspondent à la rotation par rapport à A. Pour avoir les caractères de la clé, on fait:

```
A + 4  = E
A + 25 = Z
A + 15 = P
A + 25 = Z
```

Avec CyberChef, on peut décrypter le reste avec le module `Vigenère Decode`.

On obtient le flag suivant: `FLAG-CAESARGOTNOTHINGONTHIS`
