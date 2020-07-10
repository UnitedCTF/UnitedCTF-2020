# useghidra

> reverse

Author: [Alexandre-Xavier Labonté-Lamoureux (AXDOOMER)](https://github.com/axdoomer)

Explorez ce binaire et essayez de trouver la solution en utilisant Ghidra.

Le décompilateur de Ghidra est très utile pour voir ce que le programme fait. Explorez les fonctions du programme afin de voir ce qu'il devrait faire.

Ceci pourra vous aider: http://www.asciitable.com/

## Setup

Requirements:
- Une distribution basée sur Linux
- [Ghidra](https://ghidra-sre.org/)

# Writeup

La fonction `main` contient un message. On clique dessus et un indice révèle qu'il manquerait un appel de fonction. 

![image](https://user-images.githubusercontent.com/6194072/87111585-b1312800-c237-11ea-96d6-1c023322a652.png)

En explorant le binaire, on trouve la fonction `fun_03919` qui fait quelque chose d'intéressant. Il y a deux tableaux sur la stack. 

`local_48` et `local_28`. Quand on regarde les deux tableaux, ils ont chacun 24 nombres qui leur sont assignés. 

![image](https://user-images.githubusercontent.com/6194072/87111470-7202d700-c237-11ea-8c90-013368a2d568.png)

Plus loin dans la fonction, on voit une boucle qui itère sur les tableaux et additionne les nombres. 

![image](https://user-images.githubusercontent.com/6194072/87111655-dde53f80-c237-11ea-9e0c-b777141b62d0.png)

Chaque nombre est affiché à l'écran sous forme de caractère ASCII par la fonction `putchar`. 

Lorsqu'on additionne tous les nombres, on obtient le flag `flag-n0tw3llH1dd3nIsn7i7`.

