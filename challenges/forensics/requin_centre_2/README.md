# Requin au Centre 2
> Forensics
Author: @CycleOfTheAbsurd

Une capture réseau contient les paquets qui ont été échangés sur le réseau pendant une période de temps. Ceci permet de voir ce qui a été échangé, entre qui et, s'il n'est pas chiffré, le contenu de ces échanges. [`Wireshark`](https://www.wireshark.org/) est un logiciel libre qui permet de créer et d'analyser de telles captures. Les [filtres de Wireshark](https://wiki.wireshark.org/DisplayFilters) vous seront grandement utiles.

Dans cette série de défis, vous devrez utiliser cet outil pour récupérer les informations demandées dans cette capture réseau. Tous les défis utilise le même fichier: [requin\_au\_centre.pcapng](https://drive.google.com/file/d/1qnCaylIjn5Hhu3uXPrar1u7z43BQOWIe/view?usp=sharing)

----

Dans le protocole TCP les participants assignent des [numéros de séquence](https://packetlife.net/blog/2010/jun/7/understanding-tcp-sequence-acknowledgment-numbers/) à chacun des paquets transmis. Ceux-ci sont utiles pour vérifier qu'aucun paquet n'a été perdu en transit.

Le protocol HTTP utilise TCP comme couche de transport. Ce n'est pas nécessaire pour ce défi, mais vous pouvez lire l'article sur le [Modèle OSI](https://fr.wikipedia.org/wiki/Mod%C3%A8le_OSI) si vous voulez en apprendre plus sur les couches réseaux.

Dans le protocole HTTP (celui qui est utilisé pour accéder à des pages web), le serveur retourne un [code de statut](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) avec chaque réponse afin d'indiquer si la requête a été complétée correctement et pour fournir des informations par rapport à ce résultat.

Note: Ce flag n'est __pas__ au format `FLAG-.*`

Défi #2: Dans la capture, une requête envoyée au serveur `united-ctf.can` s'est résultée en une erreur parce que la page n'a pas pu être trouvée. Quel est le numéro de séquence de la requête qui a causé cette erreur?


## Setup

Requirements:
- None

Start:

```
(Not an interactive challenge)
```
