# Writeup
Commençons par regarder comment les blocs de données sont formés avant d'être envoyés au serveur. Supposons que le flag a 28 caractères, par exemple. Avec le nom "Yvon", voici comment le flag serait séparé:

```
[YVON + 12 caractères de flag] [16 caractères de flag] [16 bytes de padding]
```

Avec un nom vide, il serait plutôt séparé comme suit:

```
[16 caractères de flag] [12 caractères de flag + 4 bytes de padding]
```

Il est donc possible de modifier la construction du flag selon la longueur du nom qu'on rentre. Cela est crucial pour cette attaque!

Supposons que nous entrons un nom à 5 caractères, par exemple "Simon", voici ce qu'on obtiendrait:

```
[SIMON + 11 caractères de flag] [16 caractères de flag] [1 caractère de flag + 15 bytes de padding]
```

Sachant que le dernier bloc a uniquement 1 caractère inconnu, il serait facile de le bruteforcer si on avait moyen de chiffrer tous les choix possibles. Comment faire? Il suffit d'envoyer le bloc à chiffrer avant le nom!

```
[a + 15 bytes de padding] [SIMON + 11 caractères de flag] [16 caractères de flag] [1 caractère de flag + 15 bytes de padding]
[b + 15 bytes de padding] [SIMON + 11 caractères de flag] [16 caractères de flag] [1 caractère de flag + 15 bytes de padding]
[c + 15 bytes de padding] [SIMON + 11 caractères de flag] [16 caractères de flag] [1 caractère de flag + 15 bytes de padding]

etc.
```

Ensuite, on peut comparer le premier bloc et l'avant dernier bloc pour voir s'ils sont identiques. Si c'est le cas, on a trouvé un premier caractère du flag!
