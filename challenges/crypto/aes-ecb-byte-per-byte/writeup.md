# Writeup
## Pour trouver la longueur du flag
On peut trouver la longueur du flag en entrant des noms de plus en plus longs et en regardant la taille du ciphertext. Tout d'abord, en entrant un nom vide, on peut avoir une idée de la longueur. Dans ce cas, le serveur nous retourne un ciphertext de 32 caractères (2 blocs AES). Donc, on peut en déduire que sa taille se trouve entre 16 et 31 (car avec 32 caractères, il y aurait un troisième bloc contenant uniquement du padding). Ensuite, on peut ajouter un caractère à notre nom et rechiffrer le flag, jusqu'à ce qu'on remplisse les deux premiers blocs AES. Nous saurons quand les deux premiers blocs seront remplis car nous verrons apparaître un troisième bloc (dont le plaintext sera uniquement du padding). Une fois qu'on a un troisième bloc, on trouve la longueur exacte du flag en calculant `32 - longueur du nom % 16`.

> Pourquoi `% 16`? Car si ça prend 16 caractères avant d'obtenir un autre bloc de ciphertext, c'est parce que le flag avait déjà une taille qui était un multiple de 16! Donc, il y avait déjà un dernier bloc contenant uniquement du padding dans le ciphertext original.

```
ECB Crypto Menu
1. Encrypt flag
2. Encrypt flag (hex name)
3. Exit

> Your choice: 1
> Please enter your name:   
Result: 10cd9b0b417444759638b53c081b4d6faa5843237ef8fee2bb9107ebc3f25567
ECB Crypto Menu
1. Encrypt flag
2. Encrypt flag (hex name)
3. Exit

> Your choice: 1
> Please enter your name: a
Result: ab2b1f5b133bda9aee4feee4d9029952f598f65a65455395341a860594b76a8d
ECB Crypto Menu
1. Encrypt flag
2. Encrypt flag (hex name)
3. Exit

> Your choice: 1
> Please enter your name: aa
Result: a2ab3069414cfe5bdd8684e2e64f235d108ca08a40c8a22e79ac62951117a4ed
ECB Crypto Menu
1. Encrypt flag
2. Encrypt flag (hex name)
3. Exit

[...]

> Your choice: 1
> Please enter your name: aaaaa
Result: 0faa2daf46c2dd4f4c3c9f60bdc5e29309e6738112281f1e27bfa1f047d4ec1f62e9c13115c6ffb2da9bfa44d802c671
```

On obtient un troisième bloc quand on entre un nom à 5 caractères. Donc, le flag a une longueur de 32 - 5 = 27 caractères.

## Pour déchiffrer le flag
Commençons par regarder comment les blocs de données sont formés avant d'être envoyés au serveur. Rappelons que le flag a 27 caractères. Avec le nom "SIMON", voici comment le flag sera séparé:

```
[SIMON + 11 caractères de flag] [16 caractères de flag] [16 bytes de padding]
```

Avec un nom vide, il sera plutôt séparé comme suit:

```
[16 caractères de flag] [11 caractères de flag + 5 bytes de padding]
```

Il est donc possible de modifier la séparation du flag selon la longueur du nom qu'on rentre. Cela est crucial pour cette attaque!

Supposons que nous entrons un nom à 6 caractères, par exemple "SIMONE", voici ce qu'on obtiendra:

```
[SIMONE + 10 caractères de flag] [16 caractères de flag] [1 caractère de flag + 15 bytes de padding]
```

Sachant que le dernier bloc a uniquement 1 caractère inconnu, il serait facile de le bruteforcer si on avait moyen de chiffrer tous les choix possibles. Comment faire pour chiffrer les choix? Il suffit d'envoyer le bloc à tester avant le nom!

```
[a + 15 bytes de faux padding] [SIMONE + 10 caractères de flag] [16 caractères de flag] [1 caractère de flag + 15 bytes de padding]
[b + 15 bytes de faux padding] [SIMONE + 10 caractères de flag] [16 caractères de flag] [1 caractère de flag + 15 bytes de padding]
[c + 15 bytes de faux padding] [SIMONE + 10 caractères de flag] [16 caractères de flag] [1 caractère de flag + 15 bytes de padding]

etc.
```

> NOTE: Pour réussir à envoyer le padding correctement, il faut envoyer le nom en hexadécimal au lieu d'en clair, car le caractère `\x0a` (newline) est perçu par Python comme la fin des données d'entrée.

Ensuite, on peut comparer le premier bloc et l'avant dernier bloc chiffrés pour voir s'ils sont identiques. Si c'est le cas, on a trouvé un premier caractère du flag (le dernier)! Dans ce cas-ci, le dernier caractère est `6`.

On procède de la même façon pour le 2e caractère (l'avant-dernier) et les suivants. **Il faut bien s'assurer d'ajouter un caractère au nom qu'on envoie à chaque nouveau caractère à déchiffrer pour déplacer le flag**. Pour le 2e caractère:

```
[a6 + 14 bytes de faux padding] [SIMONEA + 9 caractères de flag] [16 caractères de flag] [2 caractères de flag + 14 bytes de padding]
[b6 + 14 bytes de faux padding] [SIMONEA + 9 caractères de flag] [16 caractères de flag] [2 caractères de flag + 14 bytes de padding]
[c6 + 14 bytes de faux padding] [SIMONEA + 9 caractères de flag] [16 caractères de flag] [2 caractères de flag + 14 bytes de padding]

etc.
```

Lorsqu'on a trouvé au moins 15 caractères du flag, on peut éviter d'ajouter du faux padding au premier bloc. On prend uniquement le caractère à tester + les 15 caractères du flag qu'on vient de trouver:

```
[a + ceaf52147983c56] [SIMONE + "A" * 16 + N caractères de flag] [N caractères de flag + padding]
[b + ceaf52147983c56] [SIMONE + "A" * 16 + N caractères de flag] [N caractères de flag + padding]
[c + ceaf52147983c56] [SIMONE + "A" * 16 + N caractères de flag] [N caractères de flag + padding]

etc.
```

Le caractère que l'on trouve est 7. Pour le prochain caractère, on shift de 1 (on ajoute le caractère qu'on vient de trouver, `7`, et on enlève le dernier caractère qu'on avait avant, `6`):

```
[a + 7ceaf52147983c5] [SIMON + "A" * 17 + N caractères de flag] [N caractères de flag + padding]
[b + 7ceaf52147983c5] [SIMON + "A" * 17 + N caractères de flag] [N caractères de flag + padding]
[c + 7ceaf52147983c5] [SIMON + "A" * 17 + N caractères de flag] [N caractères de flag + padding]

etc.
```

On réussit de cette façon à déchiffrer le flag: `FLAG-bac9317ceaf52147983c56`

> NOTE: Pour améliorer la vitesse du bruteforce, on peut limiter les caractères à tester au range hexadécimal et au tiret (`-`) tel que spécifié par le flag format.
