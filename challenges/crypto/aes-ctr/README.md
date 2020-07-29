# AES CTR

> Crypto

Author: @xshill

Le mode CTR est un mode de chiffrement permettant de chiffrer des données en continu (_streaming_) plutôt que par blocs comme ECB et CBC. Ainsi, il est possible de chiffrer des données plus courtes qu'un bloc sans avoir à ajouter de padding.

Avec le mode CTR, on utilise AES non pas sur le texte à chiffrer, mais sur un bloc composé d'un **nonce** (_number used once_, différent pour chaque plaintext chiffré) et d'un compteur qui s'incrémente à chaque bloc. Le résultat de cette opération est un _keystream_. On fait ensuite un XOR de chaque octet des données à chiffrer avec chaque octet du _keystream_.

```
# Génération du keystream:
keystream = AES(nonce + compteur) # 16 premiers bytes de keystream
keystream += AES(nonce + compteur + 1) # 16 bytes de keystream suivants
keystream += AES(nonce + compteur + 2) # etc.
# ...
# Jusqu'à ce que longueur(keystream) >= longueur(plaintext).

# Chiffrement des données
Pour chaque byte de plaintext (p) et de keystream (k):
    ciphertext += p ^ k
```

La sécurité de ce mode repose sur la sécurité du _keystream_. Cette sécurité est assurée par le compteur et le _nonce_: le compteur s'assure que les blocs du _keystream_ seront différents les uns des autres. Le _nonce_ s'assure que le _keystream_ au complet sera différent pour chaque _plaintext_ à chiffrer, tant et aussi longtemps que chaque _nonce_ n'est utilisé **qu'une seule fois**.

La question que vous devez vous poser pour ce challenge: qu'est-ce qui arrive si le _nonce_ est utilisé **plus qu'une fois**?

# Setup

Requirements:
- None

Start:

```
docker-compose up aes-ctr
```
