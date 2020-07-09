# AES client

> Crypto

Author: @xshill

Ce défi se présente comme votre introduction au monde de la "vraie" cryptographie avec le chiffrement AES. Avant de vous présenter les attaques sur AES, nous pensons que vous devriez apprendre à utiliser les fonctions qui se trouvent dans votre langage de programmation favori afin d'être capable de vous en servir. Pour ce défi, vous aurez donc à écrire un client dont la tâche sera de réaliser le chiffrement AES avec 3 modes différents (ECB, CBC et CTR) avec des paramètres aléatoires: clé, IV, compteur, données...

Nous vous recommandons fortement de lire la documentation sur AES et ses modes avant de faire ce défi.

Les opérations à réaliser sont les suivantes (dans l'ordre):

- Chiffrement ECB
- Déchiffrement ECB
- Chiffrement CBC
- Déchiffrement CBC
- Chiffrement CTR
- Déchiffrement CTR

Tous les messages du serveur sont au format JSON. Le message contenant les données pour une opération a le format suivant:

```
{
    "mode": mode de chiffrement (string),
    "key": clé de chiffrement (string hexadécimale),
    "iv_or_counter": IV ou compteur, selon le mode (string hexadécimale ou null pour ECB),
    "operation": "encrypt"|"decrypt",
    "data": plaintext pour le chiffrement (string), et ciphertext pour le déchiffrement (string hexadécimale)
}
```

NOTE: Le champ `data` aura toujours une longueur d'un multiple de 16. Vous n'avez donc pas à vous soucier d'implémenter un padding quelconque.

ATTENTION: notez que le champ data contient une string normale si l'opération est "encrypt", et une string *hexadécimale* si l'opération est "decrypt". Vous devrez donc décoder les données avant de faire l'opération de déchiffrement.

Pour envoyer le résultat de votre opération, envoyez la string en clair s'il s'agit d'un déchiffrement, et envoyez la string hexadécimale s'il s'agit d'un chiffrement. Pseudocode:

```
# Chiffrement
ciphertext = encrypt_aes(data, key, iv)
server.send(ciphertext.hex())

# Déchiffrement
plaintext = decrypt_aes(data, key, iv)
server.send(plaintext)
```

Le message envoyé pour signaler le résultat d'une opération est le suivant:

```
{
    "success": bool
}
```

Enfin, après avoir complété la dernière opération, vous recevrez le message suivant:

```
{
    "flag": string
}
```

## Setup

Requirements:
- None

Start:

```
docker-compose up aes-client
```
