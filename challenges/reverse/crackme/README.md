# Crackme

> reverse

Author: [Alexandre-Xavier Labonté-Lamoureux (AXDOOMER)](https://github.com/axdoomer)

Explorez ce binaire et essayez de trouver la solution en utilisant Ghidra.

Le décompilateur de Ghidra est très utile pour voir ce que le programme fait. Explorez le programme afin de voir ce qu'il fait.

N'oubliez pas que les chaînes de caractères dans le langage de programmation `C` finissent par un zéro (*null terminator*).

Les sites web suivants peuvent vous aider: 

* https://www.rapidtables.com/convert/number/
* http://www.asciitable.com/
* https://bit-calculator.com/bit-shift-calculator
* https://onlinetoolz.net/bitshift

Notez que la partie hexadécimale du `flag` doit être en majuscules. Ne mettez pas `0x` devant la partie hexadécimale.

## Setup

Requirements:
- Une distribution basée sur Linux
- [Ghidra](https://ghidra-sre.org/)

# Writeup

La première chose que l'on remarque est la fonction `sscanf` qui lit de données dans une string et les stock dans des variables selon un certain format.

![image](https://user-images.githubusercontent.com/6194072/89106799-c2b2bd80-d3fa-11ea-995c-4d9d911afe71.png)

Le string source vient du paramètre qu'on a passé à la ligne de commande comme premier argument. La fonction `strncpy` copie un maximum de 199 caractères du premier argument en ligne de commande vers le tableau qui est utilisé comme source pour la fonction `sscanf`. Il faut noter que si `strncpy` lit moins de 199 caractères, le reste du tableau est rembourré par des zéros (byte `0x00`). 

![image](https://user-images.githubusercontent.com/6194072/89106858-01e10e80-d3fb-11ea-87dc-c01c3e6cb663.png)

Si on modifie le type du deuxième argument du `main`, on verra plus facilement quel paramètre sera lu dans le code précédant.

![image](https://user-images.githubusercontent.com/6194072/89107019-eb878280-d3fb-11ea-8b2e-bf384b887d1e.png)

Il y a plusieurs constantes (variables assignées et jamais modifiées par la suite). On peut tout de suite les identifier. 

![image](https://user-images.githubusercontent.com/6194072/89107286-f17e6300-d3fd-11ea-946a-05ebeff1e070.png)

La fonction `check` sert à afficher si on a le bon mot de passe ou non. On peut identifier la variable qu'elle utilise comme étant la variable qui identifie si on a réussi.

![image](https://user-images.githubusercontent.com/6194072/89107310-1e327a80-d3fe-11ea-8f8b-9ecc8230a06a.png)

On remarque qu'il y a quelques variables sur la stack utilisées mais auxquelles rien n'est jamais assigné. Cela est un indication que le type de `astring` devrait être modifié pour être un tableau. Cela fait encore plus de sens parce que `astring` est la partie « chaîne de caractères » du mot de passe et les fois où on voit ces variables sont sûrement des accès aux index de ce tableau. On peut lui donner la taille `7`. Même si le tableau est possiblement plus grand, c'est assez pour que Ghidra fasse du sens à partir du code. 

![image](https://user-images.githubusercontent.com/6194072/89107372-aca6fc00-d3fe-11ea-8331-bd2683b4114a.png)

Avec notre dernier changement de type, la dernière condition de validation fait encore plus de sens. 

![image](https://user-images.githubusercontent.com/6194072/89107556-cdbc1c80-d3ff-11ea-91d8-f667d040312e.png)

On peut maintenant commencer à chercher le mot de passe.

![image](https://user-images.githubusercontent.com/6194072/89107647-7cf8f380-d400-11ea-95fb-85f4a51ae639.png)

Cette première condition s'assure que les trois éléments attendus ont été lus. 

Pour retrouver la valeur de `decimal`, on doit inverser l'ordre des opérations. On obtiendra donc `(0x98000 >> 2) ^ 0x17337`, ce qui donne la valeur décimale `201527`.

![image](https://user-images.githubusercontent.com/6194072/89107755-322bab80-d401-11ea-9342-9857c83c2b74.png)

Pour cette deuxième condition, on réutilise la variable `decimal` pour calculer ce à quoi on s'attend. `0x20` correspond à la valeur `32`, ce qui est la taille d'un nombre entier. Le code simplifié ressemble à cela: `(hexnum >> 3 | hexnum << (32 - 3))`. Le code effectue donc une rotation des bits de trois vers la droite.

Pour obtenir la valeur de `hexnum`, xorer `0xdfdeab2c` avec la valeur de `decimal`, on obtient `0xdfddb81b`. Après avoir fait une rotation des bits vers la gauche, on obtient `0xfeedc0de`. Selon les directives du défi, cette partie du drapeau sera en majuscules. On ne doit pas entrer le `0x` pour spécifier que c'est hexadécimal quand on entre le code.

![image](https://user-images.githubusercontent.com/6194072/89107956-c0ecf800-d402-11ea-87b1-94d5efa0b921.png)

Pour la dernière partie du `flag`, on doit calcululer les valeurs auxquelles doit correspondre les caractères ASCII de la string. 

* [0]: `0x59` est égal à `89`. `89 + 33 = 122`. Selon la table ASCII, c'est `z`. 
* [1]: Doit être égal à `9`.
* [2]: C'est la valeur qui correspond à `4` shifté vers la gauche de `4`. Cela donne `64`, ce qui correspond au caractère `@`.
* [3]: `100 - 0`. Le caractère qui correspond à `100` est `d`. C'est zéro car le caractère à l'index 6 sera un caractère nul. 
* [4]: C'est un caractère nul, donc il n'y a plus aucun caractère qui suit le caractère précédant. 

Le `flag` est donc `flag-201527-FEEDC0DE.z9@d`. On peut le vérifier avec l'exécutable.

