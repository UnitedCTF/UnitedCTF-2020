# Writeup

On commence par déchiffrer le message en base64, ce qui nous donne les valeurs d'octets suivantes:

```
17, 27, 22, 16, 122, 24, 57, 7, 50, 34, 35, 22, 34, 36, 36, 62, 17, 54, 52, 62, 59, 50, 58, 50, 57, 35, 21, 37, 34, 35, 50, 49, 56, 37, 52, 50, 37
```

Comme on sait que le plaintext commence par `FLAG-`, on peut facilement retrouver la clé en utilisant les propriétés du XOR.
Il suffit de faire un XOR avec `F` du premier octet chiffré (valeur décimale de `70`) (équation 3):

```
B = C ^ A  =>  B = 17 ^ 46 = 87 = 'W'
```

On sait maintenant que la clé est 'W'. On peut alors déchiffrer le message avec l'équation 2 pour chaque caractère:

```
A = C ^ B  =>  A = 27  ^ 87 = 76 = 'L'
A = C ^ B  =>  A = 22  ^ 87 = 65 = 'A'
A = C ^ B  =>  A = 16  ^ 87 = 71 = 'G'
A = C ^ B  =>  A = 122 ^ 87 = 45 = '-'
...
```

Note: sachant la clé, il est possible de déchiffrer le flag complet en enchaînant les fonctions "From Base64" et "XOR" sur CyberChef.

Après avoir fait tous les caractères, on obtient le flag complet: `FLAG-OnPeutAussiFacilementBruteforcer`.

Comme le flag le suggère, il est aussi facile de bruteforcer la clé de chiffrement. Puisqu'elle ne fait qu'un octet de long, il y a uniquement 256 clés de chiffrement possibles.
