# La molecule de tous les maux

> Pwn

Author: [Alexandre-Xavier Labonté-Lamoureux (AXDOOMER)](https://github.com/axdoomer)

Il y a une vulnérabilité qui affecte toujours trop de programmes encore aujourd'hui. Cette vulnérabilité peut mener à des plantages, mais aussi à l'exécution de code à distance (RCE, Remote Code Execution en anglais). Cela permet à des hackers d'exécuter leur propre code à l'intérieur des logiciels affectés. Pour les logiciels connectés à un réseau, cela représente un risque énorme comme son exploitation peut être automatisée et afin de compromettre des systèmes en masse. 

Le programme auquel vous devez vous connecter est vulnérable et vous pouvez le planter. Ce défi vise à vous introduire aux défis suivants où vous irez jusqu'à lire des fichiers sur l'ordinateur compromis. Vous serez même capable d'exécuter des commandes via un shell (Sh ou Bash). Des explications techniques viendront avec les défis suivants.

Utilisez `netcat` pour vous connecter à `challenges.unitedctf.ca:16999`. Pour les défis suivants, on vous suggère d'utiliser `pwntools` si vous connaissez Python. 

Vous obtiendrez un flag débutant par `FLAG-` lorsque vous le planterez avec succès.

## Setup

Requirements:
- `docker-compose`

Start:

```
docker-compose up la_molecule_pwn
```
