# Writeup

Le flag se trouve dans un fichier `.rtf` ouvert dans wordpad. Il y a plusieurs façons de le récupérer. Nous allons utiliser les modules `filescan` et `dumpfiles`

```shell
$ volatility filescan -f /path/to/volatile_mem.dmp

[...]
0x0000000009faa028      1      0 RW---- \Device\HarddiskVolume1\Documents and Settings\Mauv\Desktop\fanion_etandard_oriflamme.rtf
```

Avec cette addresse, nous pouvons utiliser `dumpfiles` pour récupérer le fichier.

```shell
volatility dumpfiles -Q 0x09faa028 -f /path/to/volatile_mem.dmp -D /output/path/for/files/
```

On obtient un fichier RTF qu'on peut ouvrir avec word ou un éditeur de texte pour voir le flag: `79YNkIqsSFRBDOLtLxzwPUHcnzEoiKC2ALlUNJVvEqUjsIbsKO4f0Wc1i471kWAuAM1RqsfcW1c`
