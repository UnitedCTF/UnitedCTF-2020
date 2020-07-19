# Mémoire Volatile 1

> Forensics

Author: @CycleOfTheAbsurd

Un _Memory Dump_ (dump mémoire en bon français) est un ensemble d'un ou plusieurs fichiers dans lequel on retrouve tout que ce qui était contenu dans la mémoire vive (_RAM_) d'un ordinateur à un instant précis. Les dumps mémoire sont très utiles dans l'analyse forensique informatique, car ils contiennent des informations sur l'état de la machine au moment du dump. Ceci inclut les processus en cours, les fichiers chargés en mémoire, les utilisateurs connectés, les fenêtres ouvertes, etc.

[Volatility](https://github.com/volatilityfoundation/volatility) est un outil créé expressement pour l'analyse forensique de mémoire volatile. Dans cette série de 4 défis, vous aurez à utiliser cet outil pour récupérer des informations à partir du dump mémoire d'une machine virtuelle Windows XP. Le [wiki du projet](https://github.com/volatilityfoundation/volatility/wiki) vous sera très utile; il contient les instructions d'installation ainsi qu'une liste des opérations supportées par l'outil.

Voici le dump mémoire de la machine virtuelle: https://drive.google.com/file/d/1ds_PR_oCVqBIiAeOSBBJE_7Fb-HtHg_6/view?usp=sharing
Le même fichier est utilisé pour les 4 défis.

Note: Les flags ne sont __pas__ au format `FLAG-.*`


Défi #1: Quel est le dernier processus qui a été lancé à partir de la ligne de commande. Le flag est le nom du fichier exécutable sans le chemin l'extension (le `.exe`).


## Setup

Requirements:
- None

Start:

```
(Not an interactive challenge)
```
