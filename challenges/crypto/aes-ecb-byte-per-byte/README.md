# AES ECB Byte Per Byte

> Crypto

Author: @xshill

Dans ce challenge, vous devrez déchiffrer un flag chiffré avec AES en mode ECB en utilisant seulement une fonction de chiffrement.

Le serveur vous demande votre nom, puis chiffre le plaintext suivant:

```
{nom}{flag}
```

Sachant cela, comment ferez-vous pour déchiffrer le flag? Sachant que le mode est ECB et que vous pouvez entrer un nom aussi long que vous voulez, vous êtes capables de déchiffrer le flag un byte à la fois du début jusqu'à la fin. Bonne chance! ;)


**Flag format**: `/FLAG-[0-9a-f]+/`

> N.B: Ce flag n'a pas la même longueur que les autres. Découvrez-la vous-même! ;)

# Setup

Requirements:
- None

Start:

```
docker-compose up aes-ecb-byte-per-byte
```
