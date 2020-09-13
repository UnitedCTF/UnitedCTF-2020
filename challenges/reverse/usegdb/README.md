# Use GDB

> reverse

Author: [Alexandre-Xavier Labonté-Lamoureux (AXDOOMER)](https://github.com/axdoomer)

Explorez ce binaire avec Ghidra. Vous devrez obtenir la solution en utilisant [GDB](https://fr.wikipedia.org/wiki/GNU_Debugger), le débogueur.

Vous verrez que le décompilateur de Ghidra n'est pas très utile pour comprendre exactement ce que le programme fait, mais vous pourrez en avoir une idée. Vous devrez jetter un oeil à l'assembleur pour résoudre ce défi. Vous devrez aussi utiliser GDB pour surveiller le contenu des registres. 

Dans le programme, il y a une fonction qui fait 100 itérations, de 99 à 0. Lorsque l'index de la boucle vaut 58, le flag sera décodé à l'intérieur de la boucle (pour cette seule et unique itération seulement). Utilisez GDB pour déboguer le programme et voir ce qui se passe à l'intérieur. Vous pouvez utiliser des points d'arrêt conditionnels comme lorsque vous déboguez du code source lorsque vous développez dans un IDE. 

Voici une cheat sheet pour débuter avec GDB: https://users.ece.utexas.edu/~adnan/gdb-refcard.pdf

L'outil pwndbg pourra vous aider: https://github.com/pwndbg/pwndbg

Sinon essayez peda: https://github.com/longld/peda

## Setup

Requirements:
- Une distribution basée sur Linux
- [Ghidra](https://ghidra-sre.org/)

# Writeup

Lorsqu'on décompile la fonction `main`, on remarque une boucle `while` qui part de `99` et qui arrêtera de s'exécuter lorsque son index vaudra `-1`. 

Dans la boucle, on voit un appel à `mersenne_twister_engine`, ce qui nous indique que des nombres aléatoires seront générés. On ne peut pas les connaître en analysant le binaire dans Ghidra. On déduit que ces nombres aléatoires seront utilisés par la fonction `crypt` qui vient juste après. 

Quand on examine la fonction `crypt`, on voit qu'elle retourne une variable de type `basic_string`. Lorsqu'on retourne dans la boucle dans la fonction `main`, on voit l'utilisation de la fonction `c_str()` qui sert à récupérer la string dans un object de type `string`. 

Lorsqu'on souligne cette fonction, on voit le code assembleur correspondant à gauche. On voit le code `qword ptr [RBP + local_1438],RAX` utilisé juste après, ce qui est un indicateur que `RAX` est le registre qui contient la valeur de retour.

![image](https://user-images.githubusercontent.com/6194072/89142451-76a86b80-d515-11ea-9fbb-29cd03313c7f.png)

Maintenant qu'on a identifié l'endroit où on pourrait récupérer le flag, il faut trouver comment on pourra déterminer l'itération à laquelle on se situe dans le programme. En soulignant l'index de la boucle, on trouve le registre où sa valeur sera stockée à l'exécution (EBX). 

![image](https://user-images.githubusercontent.com/6194072/89142689-1c5bda80-d516-11ea-9ae5-e80d384cba8a.png)

On est prêt à aller chercher le flag. 

Premièrement, on charge l'exécutable dans GDB: `gdb usegdb`. On écrit ensuite `start`, ce qui démarre le programme. 

Ensuite, il faut insérer un point d'arrêt conditionnel. On peut le faire de cette façon: `watch $ebx == 58`. On écrit `continue` pour que le programme poursuive son exécution après la fonction `main`. 

Lorsque l'exécution s'arrête, on écrit `disas` pour voir l'assembleur. On le compare à celui de Ghidra pour se repérer dans le code. On trouve `mov QWORD PTR [rbp-0x1430],rax`, ce qui est le code qui suit l'appel à `c_str`. On met un point d'arrêt dessus en écrivant l'adresse de l'instruction de la façon suivante: `b *0x0000555555556868`. Cette adresse peut varier d'un ordinateur à l'autre et d'une exécution à l'autre. 

`info b` nous montre les points d'arrêt présentement en place. On ne veut pas que l'exécution du programme s'arrête à chaque fois que la condition pour `watch $ebx == 58` est rencontrée, car sa valeur ne changera pas avant l'itération suivante. On doit donc l'enlever. Si on entre la commande `info b`, ce devrait être le point d'arrêt `2`. On écrit `del 2` pour l'enlever. On peut poursuivre l'exécution avec `continue`. 

Le code a maintenant arrêté son exécution à l'adresse `0x555555556868 `. Si vous utilisez PEDA, vous voyez le flag `flag-gdb1s4wes0m` dans le registre RAX. Sans utiliser PEDA, la commande `x/s $rax` nous affiche le flag.

Bien sûr, on aurait pu utiliser des commandes comme `stepi` et `nexti` pour passer à travers toute l'exécution du programme jusqu'à temps qu'on arrive où on voulait pour voir le flag, mais cela serait extrêmement lent et inefficace. En plus, on devrait recommencer au début si on passait tout droit.
