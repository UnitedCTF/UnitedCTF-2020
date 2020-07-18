# Writeup

Le flag se trouve dans le nom du fichier exécutable d'un processus.

Si on fait simplement

```shell
volatility pslist -f /path/to/volatile_mem.dmp
```

Le nom est tronqué à seulement `FLAG-PSLIST_eve`.

Par contre, on spécifie que le processus a été lancé par la ligne de commande, donc on peut utiliser le module `cmdline`:

```shell
$ volatility cmdline -f /path/to/volatile_mem.dmp
[...]
************************************************************************
FLAG-PSLIST_eve pid:   3848
Command line : C:\FLAG-PSLIST_everytime_4sa3r8uj.exe
```

Avec seulement le nom de fichier sans extension ça donne `FLAG-PSLIST_everytime_4sa3r8uj`
