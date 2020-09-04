# Too slow

> reverse

Author: [Alexandre-Xavier Labonté-Lamoureux (AXDOOMER)](https://github.com/axdoomer)

Explorez ce binaire et essayez de trouver la solution en utilisant Ghidra.

Vous verrez que le décompilateur de Ghidra n'est pas très utile pour comprendre exactement ce que le programme fait, mais vous pourrez en avoir une idée. Trouvez une faiblesse à exploiter dans son fonctionnement.

Indice: Renseignez-vous sur le truc possible avec `LD_PRELOAD`. Vous devrez l'utiliser pour résoudre le défi de la façon la plus simple.

## Setup

Requirements:
- Une distribution basée sur Linux
- [Ghidra](https://ghidra-sre.org/)

# Writeup

En examinant le code du programme, on remarque un appel aux fonctions `sleep` et `usleep`. Cela nous indique que la vitesse du programme est ralentie, car ces fonctions imposent un délai à l'exécution du code. 

En se renseignant sur `LD_PRELOAD`, on apprend qu'il s'agit d'un truc pour [charger les fonctions d'une bibliothèque avant celles d'une autre](https://stackoverflow.com/a/426260). En cherchant le rapport avec les fonctions sleep, on trouve [un moyen de les remplacer pour nullifier leur comportement](https://stackoverflow.com/a/9302942).

On implémente donc nos fonctions de remplacement en vue d'utiliser ce truc.

```
#include <time.h>
#include <unistd.h>

unsigned int sleep(unsigned int seconds)
{
	return 0;
}

int usleep(useconds_t usec)
{
	return 0;
}
```

On compile ce code avec la commande `gcc -o libnosleep.so -shared nosleep.c -fpic`. Après on exécute `LD_PRELOAD=./libnosleep.so ./tooslow`. Le texte que le programme affichait s'affiche beaucoup plus vite et on obtient le flag `flag-g0dD0Ilik3libN0Sl33p` à la fin de son exécution. 
