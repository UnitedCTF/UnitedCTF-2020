# La goutte qui fait déborder le buffer

> Pwn

Author: @CycleOfTheAbsurd

Lors de l'exécution d'un programme compilé, les variables locales sont stockées sur la [_stack_](https://fr.wikipedia.org/wiki/Pile_(informatique) (pile en français). La _stack_ est un espace mémoire contigu qui fonction en monde Dernier-Entré, Premier-Servi (comme une pile d'assiettes).

Comme il s'agit d'un espace mémoire continu, si une variable dépasse l'espace qui lui est alloué, elle empiètera potentiellement sur une autre variable sur la _stack_. Le processeur et le système d'exploitation ne vérifient pas qu'une valeur a la bonne taille avant de l'écrire ou de la modifier. Pour s'assurer qu'il n'y a pas de débordement, il faut valider la taille de la variable dans le programme. Plusieurs fonctions de la libc ont une variante qui ne valide pas la longueur (ex: `strcpy`) et une qui fait la validation (ex: `strncpy`).

Ne pas valider la taille d'un élément à taille variable peut mener à un débordement de tampon ([_buffer overflow_](https://en.wikipedia.org/wiki/Stack_buffer_overflow)). Il s'agit d'une faille commune qui peut être exploitée par un attaquant et qui peut ouvrir la voie à une modification inattendue des valeurs des variables du programme ou de son comportement.

Défi: Voici un programme compilé vulnérable à un débordement de tampon. Tentez d'abord de comprendre son comportement et de l'exploiter localement. Si vous y parvenez, il affichera un flag censuré: "FLAG-XXXXXXXXXXXXXXXXXXXXXXXXXXXXX".

Afin d'obtenir le vrai flag, vous devrez exploiter ce même programme via `unitedctf.ca:17000`

_Note_: utilisez `netcat` pour vous y connecter


## Setup

Requirements:
- `docker-compose`

Start:

```
docker-compose up la_goutte_pwn
```
