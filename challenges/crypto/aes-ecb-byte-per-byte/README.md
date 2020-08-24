# AES ECB Byte Per Byte

> Crypto

Author: @xshill

Dans ce challenge, vous devrez déchiffrer un flag chiffré avec AES en mode ECB en utilisant seulement une fonction de chiffrement.

Le serveur vous demande votre nom, puis chiffre le plaintext suivant:

```
{nom}{flag}
```

Sachant cela, comment ferez-vous pour déchiffrer le flag? Sachant que le mode est ECB et que vous pouvez entrer un nom aussi long que vous voulez, vous êtes capables de déchiffrer le flag un byte à la fois du début jusqu'à la fin. Bonne chance! ;)

## Note sur le padding
Puisque AES fonctionne par blocs de 16 caractères, il est nécessaire d'ajouter du padding pour remplir les données avant de les chiffrer si leur taille n'est pas un multiple de 16. Le padding est ajouté comme suit: si le bloc est plus petit que 16, on remplit le reste de l'espace avec une valeur d'octet correspondant au nombre de bytes manquant. Par exemple, pour 12 bytes, le padding serait 4 bytes valant `\x04`, puisqu'il manque 4 bytes pour arriver à 16:

```
ABCDEFGHIJKL\x04\x04\x04\x04
```

Dans le cas où on utilise la fonction de padding sur des données dont la taille est déjà un multiple de 16 bytes, un bloc complet de padding sera ajouté avec la valeur `\x10` (16 en hexadécimal):

```
<--  BLOC 1  --> <--------------------------  BLOC 2  -------------------------->
ABCDEFGHIJKLMNOP \x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10
```

**Flag format**: `/FLAG-[0-9a-f]+/`

> N.B: Ce flag n'a pas la même longueur que les autres. Découvrez-la vous-même! ;)

# Setup

Requirements:
- None

Start:

```
docker-compose up aes-ecb-byte-per-byte
```
