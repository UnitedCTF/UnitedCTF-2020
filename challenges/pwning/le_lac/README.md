# Le lac de shellcode

> Pwn

Author: @CycleOfTheAbsurd

Comme nous l'avons vu dans le challenge précédent, il est possible d'exploiter un _buffer overflow_ de manière à rediriger le flux d'exécution du programme en écrasant l'adresse de retour d'une fonction. Par contre, il arrive que le code que l'on désire exécuter ne soit pas présent dans le programme. Il existe quelques techniques pour exécuter des instructions ne se trouvant pas dans le binaire compilé. Nous utiliserons un [_shellcode_](https://en.wikipedia.org/wiki/Shellcode).

Un _shellcode_ est un bout de code compilé qui est injecté dans une section exécutable d'un programme par un attaquant. L'attaquant cherche ensuite à rediriger le flux d'exécution pour faire exécuter ce _shellcode_. Le nom provient du fait qu'on l'utilise souvent pour lancer un _shell_, mais il est possible d'effectuer toutes sortes d'opérations.

__Il s'agit d'une technique d'exploitation et non d'une vulnérabilité.__ Il faut donc qu'une faille soit présente dans le programme pour que l'on puisse exécuter le _shellcode_. Le simple fait de pouvoir écrire un _shellcode_ dans un _buffer_ du programme n'est pas une faille en soi.

Défi: Voici un autre programme compilé vulnérable à un débordement de tampon. Vous devez exploiter cette faille pour exécuter un _shellcode_. Votre but est de lire le contenu du fichier `/flag`.

Afin d'obtenir le flag, vous devrez exploiter ce même programme via `unitedctf.ca:17002`. Utilisez `netcat` pour vous y connecter

_Note_: Pour ce challenge, nous avons désactivé certaines protections mémoires dont [NX](https://en.wikipedia.org/wiki/NX_bit#x86). Cette protection, qui est activée par défaut pour les programmes compilés avec des compilateurs Linux modernes, rend la _stack_ non-exécutable, ce qui protège spécifiquement contre les attaques par _shellcode_ dans la _stack_.

Écrire un shellcode par soi-même peut être complexe et demande une certaine connaissance du langage d'assemblage utilisé par l'architecture ciblée (x86-64). Pour cette raison, je vous recommande d'adapter un shellcode existant d'une ressource comme [shellstorm](http://shell-storm.org/shellcode/)

## Setup

Requirements:
- `docker-compose`

Start:

```
docker-compose up le_lac_pwn
```
