# Sysadmin-101

> sysadmin

Author: Vincent Laferrière

Une introduction au différentes commandes linux pour tout bon sysadmin débutant

## Setup

Requirements:

-   docker
-   docker-compose

Start:

```bash
docker-compose up
```

## Writeup

### FLAG0

#### Description

Tout bon futur sysadmin doit pouvoir utiliser la commande ssh pour gérer des systèmes à distance.
Ta première tâche sera de te connecter à la machine [HOST]:[PORT] avec l'utilisateur [USER0] et le mot de passe [PASS0].

#### Solution

Il suffit d'entrer la commande suivante et de taper le bon mot de passe:

```bash
ssh [USER0]@[HOST] -p [PORT]
```

### FLAG1

#### Description

C'est bien d'utiliser un mot de passe, mais utiliser une clé privée, c'est encore mieux!
Connecte-toi à la même machine avec l'utilisateur [USER1] et la clé fournie au dernier challenge.

#### Solution

Il faut utiliser la clé privée donnée par le dernier challenge

```bash
# Ne pas oublier d'avoir les bonnes permissions sur la clé privée
chmod 600 user1.pem
ssh -i user1.pem [USER1]@[HOST] -p [PORT]
```

### FLAG2

#### Description

Ce flag se trouve dans l'un des fichiers exécuté par bash pour configurer l'environment.

#### Solution

Le flag est caché à la fin du fichier `~/.bashrc`

### FLAG3

#### Description

Ce flag se trouve dans l'un des fichiers les plus visé par les LFI et les path traversals. Il contient les informations de tous les utilisateurs.

#### Solution

Le flag est caché dans la description de l'utilisateur dans le fichier `/etc/passwd`
