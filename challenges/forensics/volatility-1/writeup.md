# Writeup

Le flag se trouve dans le nom du fichier exécutable d'un processus.

Si on fait simplement

```shell
volatility pslist -f /path/to/volatile_mem.dmp
```

Le nom est tronqué à seulement `b6eTMrzqNIvb31x`.

Par contre, on spécifie que le processus a été lancé par la ligne de commande, donc on peut utiliser le module `cmdline`:

```shell
$ volatility cmdline -f /path/to/volatile_mem.dmp
[...]
************************************************************************
b6eTMrzqNIvb31x pid:   1036
Command line : C:\b6eTMrzqNIvb31xnIdosZtrwl6njxxAPGJOAGOj8y5Pj5khLeWNiufQM3a3XL8KUGkhwOnVUM3A.exe
```

Avec seulement le nom de fichier sans extension ça donne `b6eTMrzqNIvb31xnIdosZtrwl6njxxAPGJOAGOj8y5Pj5khLeWNiufQM3a3XL8KUGkhwOnVUM3A`
