# Requin au Centre
> Forensics
Author: @CycleOfTheAbsurd

Une capture réseau contient les paquets qui ont été échangés sur le réseau pendant une période de temps. Ceci permet de voir ce qui a été échangé, entre qui et, s'il n'est pas chiffré, le contenu de ces échanges. [`Wireshark`](https://www.wireshark.org/) est un logiciel libre qui permet de créer et d'analyser de telles captures. Les [filtres de Wireshark](https://wiki.wireshark.org/DisplayFilters) vous seront grandement utiles.

Dans cette série de défis, vous devrez utiliser cet outil pour récupérer les informations demandées dans cette capture réseau. Tous les défis utilise le même fichier: [requin\_au\_centre.pcapng](https://drive.google.com/file/d/1qnCaylIjn5Hhu3uXPrar1u7z43BQOWIe/view?usp=sharing)

----

Le protocole DNS est ce qui permet d'obtenir l'address IP associée à un nom de domaine (ex: aaaa.com). Les échanges dans ce protocole se font en clair dans un format lisible par les humains.

Note: Ce flag n'est __pas__ au format `FLAG-.*`

Défi #1: Quel est le nom de domaine associé à l'addresse IP `217.70.184.55`?


## Setup

Requirements:
- None

Start:

```
(Not an interactive challenge)
```
