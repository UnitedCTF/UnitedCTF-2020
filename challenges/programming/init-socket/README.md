# Initiation aux sockets

> Programming

Author: @xshill

Le but du challenge est simplement d'ouvrir un socket vers le serveur et d'envoyer exactement le même texte qu'il vous envoie.

Ce défi de programmation a pour but de vous initier à la programmation de sockets.

Les sockets permettent d'ouvrir des connexions réseau à d'autres machines. Pour créer un socket en tant que client, il vous faut au minimum:

- L'adresse IP du serveur à contacter
- Le port de destination

Vous êtes libres de faire ce challenge avec le langage de votre choix. Un excellent langage pour faire ce genre de script est Python. Vous pouvez utiliser soit la librairie standard ou, pour être encore plus efficace, la librairie pwntools!

## Installer pwntools
```
python -m pip install --upgrade pwntools
```

## Fonctions de base dans pwntools
```python
from pwn import * # Importer pwntools

connection = remote("127.0.0.1", 3000) # Ouvrir une connexion vers l'adresse IP 127.0.0.1 et le port 3000
connection = remote("localhost", 3000) # Vous pouvez aussi mettre l'hôte du serveur (e.g: www.google.com)
connection.recv(1024) # Recevoir 1024 MAXIMUM (il est possible que vous en receviez moins)
connection.recvline() # Lire des données jusqu'à temps qu'on recoive un saut de ligne ('\n')
connection.send("allo") # Envoyer du texte
connection.sendline("allo") # Envoyer du texte et ajouter un saut de ligne à la fin ('\n')
connection.send(b"allo") # Envoyer du texte, mais sous formes de données brutes. À utiliser pour envoyer des données non lisibles.
connection.sendline(b"allo") # Envoyer du texte, mais sous formes de données brutes. À utiliser pour envoyer des données non lisibles. Ajoute une saut de ligne à la fin ('\n').
connection.interactive() # Interagir avec la connexion comme une console (vous tapez les données à envoyer au clavier et les données reçues s'affichent en console).
```

## Setup

Requirements:
- None

Start:

```
docker-compose up init-socket
```
