# passwordcheck

> reverse

Author: [Alexandre-Xavier Labonté-Lamoureux (AXDOOMER)](https://github.com/axdoomer)

Essayez de trouver la solution à ce binaire en utilisant l'utilitaire `strings` et Ghidra.

Le décompilateur de Ghidra est très utile pour voir ce que le programme fait.

Un bon tutoriel à regarder avant de commencer: [Ghidra quickstart & tutorial: Solving a simple crackme](https://youtu.be/fTGTnrgjuGA)

## Setup

Requirements:
- Une distribution basée sur Linux
- [Ghidra](https://ghidra-sre.org/)

# Writeup

On exécute le programme et on voit qu'il demande un mot de passe. 

On peut exécuter l'utilitaire `strings` sur le programme. On remarque une chaîne de charactères intéressante (`goobers`). 

On décompile le binaire à l'aide de Ghidra. On remarque une comparaison avec la chaîne de charactère `goobers`. 

![image](https://user-images.githubusercontent.com/6194072/87111899-80052780-c238-11ea-9eb8-f5d9600db7e1.png)

Le code de la fonction `flag()` est obscure, on ne cherche donc pas à la comprendre. Pour les curieux, la fonction pige pseudo-aléatoirement des caractères dans un tableau à l'aide de la fonction `rand()`. Il n'est donc pas possible de connaître quels caractères seront pigés sans l'exécuter.

![image](https://user-images.githubusercontent.com/6194072/87111939-a3c86d80-c238-11ea-9380-eb97aa9e6ad3.png)

On entre le code `goobers` à l'exécution et on obtient le flag `flag-g077h47p455w0rd`.

