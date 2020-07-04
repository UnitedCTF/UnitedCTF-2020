# 1 Byte XOR

> Crypto

Author: @xshill

Connaissez-vous l'opération XOR? Il s'agit d'un OU exclusif effectué bit par bit.

On prend deux nombres, par exemple `57` et `154`. Au format binaire, on obtient les nombres suivants:

```
0 0 1 1 1 0 0 1 (57)
1 0 0 1 1 0 1 0 (154)
```

Pour obtenir le résultat, on compare chaque paire de bits. Le résultat est 1 si UN SEUL bit est à 1, et 0 sinon.

```
  0 0 1 1 1 0 0 1 (57)
^ 1 0 0 1 1 0 1 0 (154)
= 1 0 1 0 0 0 1 1 (163)
```

Une propriété intéressante du XOR est que si on connaît deux des trois parties du chiffrement (plaintext, clé et ciphertext), on peut facilement retrouver l'autre partie:

```
A ^ B = C (équation 1: ciphertext)
A = C ^ B (équation 2: plaintext)
B = C ^ A (équation 3: clé de chiffrement)
```

Cette opération est beaucoup utilisée en cryptographie. Pour votre introduction à cette technique, déchiffrez le message suivant, sachant qu'il a été chiffré avec une clé XOR de longueur 1:

```
ERsWEHoYOQcyIiMWIiQkPhE2ND47MjoyOSMVJSIjMjE4JTQyJQ==
```

ATTENTION: Le message est au format base64, vous devrez donc le décoder avant de le déchiffrer.

Un indice: le flag format est `FLAG-...`

## Setup

Requirements:
- None

Start:

```
(Not an interactive challenge)
```
