# Goland

> reverse

Author: [Alexandre-Xavier Labonté-Lamoureux (AXDOOMER)](https://github.com/axdoomer)

Défi "hardcore". Ne vous sentez pas mal si vous ne le réussissez pas.

Vous devez utiliser toutes les compétences acquises durant les défis précédants et faire vos propres recherches pour le réussir.

Utilisez Ghidra... peut-être qu'un plugin supplémentaire pourrait vous aider. Il est codé dans un langage compilé qui ne respecte pas exactement les conventions d'appel de fonction.

Vous pouvez aussi utiliser IDA Free si vous êtes à l'aise avec l'assembleur x86-64 et les graphiques (Ghidra fait aussi des graphs, il y a un petit icône pour ça).

## Setup

Requirements:
- Une distribution basée sur Linux
- [Ghidra](https://ghidra-sre.org/)

# Writeup

En ligne de commande, si on exécute le commande `file` sur le binaire, on voit un `Go BuidID`. On sait que c'est un exécutable codé en langage Go. La fonction `main` sera donc `main.main`. On peut regarder cette fonction dans Ghidra, mais pour mieux comparer ce qu'on obtient au _runtime_ au _code flow_, il est mieux d'installer le plugin [https://github.com/felberj/gotools](https://github.com/felberj/gotools) qui permet à Ghidra de faire plus du sens du code. 

On verra que la logique de validation est effectuée dans `main.stuff`. En examinant la fonction dans IDA Free ou Ghidra, on peut voir une variable nommée `main_gfal` être chargée dans la boucle. On peut suivre les données pointée à `dq offset unk_54E900` et on remarque déjà un pattern. La chaîne d'octets a une longeur de 49. Cette chaîne est potentiellement le flag obscurci. Notez que `gfal` sont les lettres `flag` dans le désordre. 

![image](https://user-images.githubusercontent.com/6194072/93265663-ef3a5300-f776-11ea-9c1e-bd0d0c5d3b70.png)

Les octets pointés:

```
0xe6,0xf2,0x68,0xe8,0x5a,0x6e,0xd0,0xbe,0x66,0xcc,0x6e,0xbe,0x6e,0xca,0x60,0xc6,
0xbe,0xe0,0x60,0xf4,0xc6,0x66,0x6e,0x68,0xc2,0x6e,0xbe,0xc6,0x60,0xd0,0xca,0xbe,
0x66,0x6e,0xca,0x66,0xbe,0x68,0xd0,0xbe,0xd0,0xc2,0x62,0xce,0x66,0xe2,0xe0,0x6e,0xe6
```

Son adresse est chargée dans le registre `rbx` qu'on voit utilisé plus loin avec l'instruction `movzx eax, byte ptr [rbx+rsi]`. `rsi` est utilisé comme un offset (décalage) et est peut-être l'indice de la boucle qui itère sur la chaîne. Deux instruction sous `mov rbx, cs:main_gfal`, on voyait le contenu de `rdx` mis dans `rdi`. Le contenu de `rdx` était assigné trois instructions plus haut. `mov rdx, cs:qword_55AAB8` copie la valeur 0x31 (49). 

Si on continue à suivre comment le flag est manipulé, on voit `movzx eax, byte ptr [rbx+rsi]` suivi de l'instruction `shr al, 1`. La comparaison qui suit mène un un retour de la fonction. La comparaison est donc potentiellement ce qui détermine que le flag entré dans le programme est le bon. 

![image](https://user-images.githubusercontent.com/6194072/93266525-307f3280-f778-11ea-9f47-1b4db61105ce.png)

On peut suivre le registre `edi`/`dil`. Juste un peu plus haut, il semble y avoir un bloc de traitement qui fait une opération inconnue. Il est un peu difficile de savoir exactement ce qui se passe. 

![image](https://user-images.githubusercontent.com/6194072/93266636-5573a580-f778-11ea-936a-fe524565f1c1.png)

On préférera regarder la sortie du décompilateur Ghidra pour mieux comprendre. 

![Screenshot_2020-09-15_12-30-55](https://user-images.githubusercontent.com/6194072/93264186-be591e80-f774-11ea-9d64-2a4952210608.png)

On voit que ces opérations correspondent à l'algorithme [ROT13](https://fr.wikipedia.org/wiki/ROT13). Avons-nous maintenant toute l'information nécessaire pour décoder le flag? 

* Nous savons qu'un `shift right` de `1` est fait sur la valeur du flag encodé. 
* La valeur entrée dans le programme est passée à travers de l'algorithme ROT13.

![image](https://user-images.githubusercontent.com/6194072/93267169-39bccf00-f779-11ea-8b34-fca3a8e926cc.png)

Essayons. Utilisons CyberChef pour obtenir le flag rapidement. 

![image](https://user-images.githubusercontent.com/6194072/93267395-a0da8380-f779-11ea-9e10-fbb29c00d67c.png)

Flag: `fl4g-7u_3s7_7r0p_c0mp374n7_p0ur_37r3_4u_un1t3dc7f`

