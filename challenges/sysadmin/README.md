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
Ta première tâche sera de te connecter à la machine [HOST]:[PORT] avec l'utilisateur `flag0` et le mot de passe `unitedctf`.

#### Solution

Il suffit d'entrer la commande suivante et de taper le bon mot de passe:

```bash
ssh flag0@[HOST] -p [PORT]
```

### FLAG1

#### Description

C'est bien d'utiliser un mot de passe, mais utiliser une clé privée, c'est encore mieux!
Connecte-toi à la même machine avec l'utilisateur `flag1` et la clé fournie au dernier challenge.

#### Solution

Il faut utiliser la clé privée donnée par le dernier challenge

```bash
# Ne pas oublier d'avoir les bonnes permissions sur la clé privée
chmod 600 flag1.pem
ssh -i flag1.pem flag1@[HOST] -p [PORT]
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

### FLAG4

#### Description

Ce flag se trouve dans votre dossier d'utilisateur, caché à la vue de tous.

#### Solution

Le flag est caché dans le fichier caché `~/.flag`

### FLAG5

#### Description

Par défaut, ubuntu utilise un umask de 002 ce qui n'est pas très "secret".

#### Solution

Le flag est simplement dans le fichier nommé `secret` dans le dossier du second utilisateur

### FLAG6

#### Description

Quand il y a trop de fichiers il faut absolument globally search for a regular expression and print matching pour éviter de devenir fou.

#### Solution

Le flag est dans l'un des fichiers de code source

```bash
grep -R FLAG- .
```

### FLAG7

#### Description

Parfois, il être capable d'impersonifier d'autres utilisateurs pour exécuter d'autres commandes sans compromettre la sécurité une machine.

#### Solution

Le flag se trouve dans le dossier d'un autre utilisateur et il faut utiliser sudo pour y avoir accès

```bash
sudo -u superuser /home/superuser/secret.sh
```

### FLAG8

#### Description

Certaines commandes administratives peuvent être très utiles pour déboguer et observer le comportement d'un programme.

#### Solution

Le flag est envoyé chaque seconde au binaire `/keyrecv`. Il est possible de le récupérer en utilisant la commande `strace`

```bash
# Le PID va changer, mais il devrait être proche de 9
strace -p <PID de /keyrecv>
```

### FLAG9

#### Description

Un petit mélange des connaissances des derniers flags.

#### Solution

Le script `/home/secretuser/rotatekeys.sh` contient une race condition où la commande openssl prend un peu trop de temps et la clé secrète est exposée

```bash
sudo -u secretuser /home/secretuser/rotatekeys.sh &
cat /tmp/secret > secret
openssl enc -aes-256-cbc -d -pbkdf2 -iter 100000 -salt -md sha512 -pass file:secret -in /home/secretuser/flag.enc -out -
```
