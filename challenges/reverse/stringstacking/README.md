# stringsstacking

> reverse

Author: [Alexandre-Xavier Labonté-Lamoureux (AXDOOMER)](https://github.com/axdoomer)

Essayez de trouver la solution à ce binaire en utilisant Ghidra.

Le décompilateur de Ghidra est très utile pour voir ce que le programme fait, mais le code décompilé n'est pas toujours facile à comprendre. Essayez de vous aider à l'aide du désassembleur.

## Setup

Requirements:
- Une distribution basée sur Linux
- [Ghidra](https://ghidra-sre.org/)

# Writeup

Le contenu de la fonction `main` nous indique qu'il faudrait chercher plus. 

On trouve une fonction nommée `solveme`. Celle-ci affiche à l'écran des parties de string. 

Par exemple, `%.4s` dans la fonction `printf` indique que quatre caractères seront lus et affichés. L'adresse qui suit est celle à partir de où la fonction va lire les caractères dans la string. 

![image](https://user-images.githubusercontent.com/6194072/87112170-2c470e00-c239-11ea-8b84-5382d294fd16.png)

Le code désassemblé rend la lecture des parties de string plus facile. Ici on voit que les premiers caractères seront `flag`.

![image](https://user-images.githubusercontent.com/6194072/87112429-c27b3400-c239-11ea-8504-b6bf246774a4.png)

On continue de lire et on voit la partie suivante du flag `-oup`. 

![image](https://user-images.githubusercontent.com/6194072/87112569-30276000-c23a-11ea-9ad5-55131fe94dfd.png)

On continue pour les parties suivantes. Il faut faire attention à la partie où `printf` ne lira que trois caractères. 

Quand on a recontruit le string, on obtient le flag `flag-oupssuperandomizerooofitssuperlong`.

