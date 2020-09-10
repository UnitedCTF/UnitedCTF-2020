# One-time pad

> reverse

Author: [Alexandre-Xavier Labonté-Lamoureux (AXDOOMER)](https://github.com/axdoomer)

Explorez ce binaire et essayez de trouver la solution en utilisant Ghidra.

Le décompilateur de Ghidra est très utile pour voir ce que le programme fait. Explorez le programme afin de voir ce qu'il fait.

Ceci pourra vous aider: http://xor.pw/

Notez qu'il y a une difficulté supplémentaire à ce défi. Ghidra ne décompilera pas le programme de manière optimale. Vous pouvez changer les types de variables pour que Ghidra génère du code plus compréhensible.

## Setup

Requirements:
- Une distribution basée sur Linux
- [Ghidra](https://ghidra-sre.org/)

# Writeup

Ce défi est très similaire à `useghidra`. Au lieu d'additionner les valeurs de deux tableaux, on utilise l'opération XOR sous la forme d'un [one-time pad](https://wiki.mattrude.com/One-Time_Pad) sur le mot de passe entré afin de le vérifier. Dû aux propriétés de l'opération XOR, on peut récupérer le mot de passe à partir des tableaux utilisés pour le vérifier qui sont contenus dans l'exécutable. 

On n'a pas à faire de recherche pour trouver la logique de validation. Tout se trouve dans la fonction `main`.

On voit plusieurs variables qui sont initialisées avec des nombres hexadécimaux au début de la fonction. On voit ensuite une phrase demandant d'entrer le _mot de passe super secret_ ainsi que d'autres variables qui sont cette fois-ci initialisées à la valeur zéro. 

![image](https://user-images.githubusercontent.com/6194072/88617620-1d4bc280-d065-11ea-92b5-cb91a6738316.png)

On voit les variables `local_38`, `local_98` et `local_68` qui correspondent à certaines de ces variables. `local_9c` est additionné à la référence de ces variables en débutant par 0x22 (32 en décimal), ce qui est un décalage trop grand par rapport à la taille de ces variables. Cela nous indique que ce sont sûrement des tableaux et que le décompilateur de Ghidra n'as pas réussi à les identifier comme tel. Il faut donc convertir ces variables. 

Il faut donc modifier le type de ces variables. On clique sur leur type avec le bouton droit et on appuie sur "Retype variable". On modifie le type pour un tableau et on spécifie sa taille.

![image](https://user-images.githubusercontent.com/6194072/88618219-83851500-d066-11ea-83e6-e1ec41b96f0e.png)

Le code de validation devient plus facile à lire. 

![image](https://user-images.githubusercontent.com/6194072/88618315-cd6dfb00-d066-11ea-8e94-276e362861c2.png)

Il reste toujours un tableau et c'est celui composé de zéros. Ce sont cinq variables de type `undefined8`, donc `5 x 8 = 40`. C'est un tableau de 40 bytes. On peut confirmer sa taille en regardant la fonction `isoc99_scanf` pour voir si elle limite le nombre de caractères lus. Si on regarde le contenu de `DAT_00102029`, on voit `%39s`, ce qui indique à `scanf` d'effectuer la lecture de 39 caractères. Cela laisse assez de place pour insérer la valeur `null` après la string pour éviter des bugs de dépassement de tampon. 

Après avoir corrigé le type du dernier tableau, le code devient beaucoup plus clair. Il ne reste plus qu'à renommer les variables pour plus de clarté. 

![image](https://user-images.githubusercontent.com/6194072/88618857-2ab67c00-d068-11ea-81e8-b3259ac4a9e7.png)

On sait maintenant que le mot de passe sera validé dans l'ordre inverse. Le mot de passe est xoré avec le contenu de `array1` et doit être égal à `array2`. Avec la propriété de XOR, on sait qu'en xorant un array avec l'autre, on obtiendra ce qui est supposé être le mot de passe. 

En utilisant un outil comme [CyberChef](https://gchq.github.io/CyberChef/), on peut effectuer l'opération nécessaire pour récupérer le mot de passe. 

On obtient: `flag-y0ur3aM4st3rp455w0rdd3cyph3r3r`

On peut l'entrer comme mot de passe pour le valider. On voit alors le message `That's the good password!`. 
