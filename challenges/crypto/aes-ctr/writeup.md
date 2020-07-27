# Writeup

Lorsqu'on se connecte au serveur, il nous affiche un menu avec plusieurs options:

```
CTR Crypto Menu
1. Encrypt flag
2. Encrypt data
3. Exit
```

Le serveur nous donne l'option d'afficher le flag encrypté. Essayons donc:

```
> Your choice: 1
Result: daaeb9b51d2264fae16295291a3aa97cc6b118d8ff1ee3736447b5f768be8b848c620ada3b
```

Rappelez vous le fonctionnement de CTR: AES est effectué sur un groupe (nonce + compteur), et on fait un XOR du résultat avec le plaintext.

Nous avons donc: 

```
ciphertext = flag ^ AES(nonce1 + compteur)
```

Connaissant les propriétés du XOR, nous savons que si on réussit à effectuer un autre XOR avec AES(nonce1 + compteur), nous pourrons retrouver le flag de la manière suivante:

```
ciphertext ^ AES(nonce1 + compteur) = flag ^ AES(nonce1 + compteur) ^ AES(nonce1 + compteur) = flag (propriété: X ^ X = 0)
```

Comment faire pour obtenir AES(nonce1 + compteur) seul? C'est possible si on connait un plaintext assez long et que le _nonce_ est **réutilisé**:

```
ciphertext2 = plaintext ^ AES(nonce1 + compteur)
ciphertext2 ^ plaintext = plaintext ^ AES(nonce1 + compteur) ^ plaintext = AES(nonce1 + compteur)
```

Autrement dit, si le _nonce_ est réutilisé et qu'on peut chiffrer des données connues de façon arbitraire, **on peut retrouver le keystream utilisé pour chiffrer le `flag`.**

Il suffit d'envoyer des données assez longues pour avoir un keystream d'une taille supérieure ou égale à celle du flag:

```
CTR Crypto Menu
1. Encrypt flag
2. Encrypt data
3. Exit

> Your choice: 2
> Data to encrypt: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
Result: fd839993517167a8b834c77f1f39ad2bc5b41bdaae1be0246115e1f530e9d2dc88365a8e6fe05112910e29cbbadeb17697fb4f02aaa7a8e77352414e95a29e4ce98aac999fcbc581e678cf49805cc31501643a261a6f0d17516971432e7b518403b5760fc5ecc9cf88
CTR Crypto Menu
1. Encrypt flag
2. Encrypt data
3. Exit
```

Avec CyberChef, on peut retrouver le keystream (AES(nonce1 + compteur)) avec un XOR de "aaaa..." et "fd83999...":

```
9c e2 f8 f2 30 10 06 c9 d9 55 a6 1e 7e 58 cc 4a a4 d5 7a bb cf 7a 81 45 00 74 80 94 51 88 b3 bd e9 57 3b ef 0e 81 30 73 f0 6f 48 aa db bf d0 17 f6 9a 2e 63 cb c6 c9 86 12 33 20 2f f4 c3 ff 2d 88 eb cd f8 fe aa a4 e0 87 19 ae 28 e1 3d a2 74 60 05 5b 47 7b 0e 6c 76 30 08 10 22 4f 1a 30 e5 62 d4 17 6e a4 8d a8 ae e9
```

Ensuite, on fait un XOR du keystream avec le flag chiffré trouvé à la première étape:

```
daaeb9b51d2264fae16295291a3aa97cc6b118d8ff1ee3736447b5f768be8b848c620ada3b ^ 9ce2f8f2301006c9d955a61e7e58cc4aa4d57abbcf7a8145007480945188b3bde9573bef0e813073f06f48aadbbfd017f69a2e63cbc6c9861233202ff4c3ff2d88ebcdf8feaaa4e08719ae28e13da27460055b477b0e6c76300810224f1a30e562d4176ea48da8aee9
```

Le résultat est:

```
FLAG-2b38737dbe6bdbc0db6d35c9689e5155
```
