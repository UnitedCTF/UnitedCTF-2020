# Requin au Centre 3
> Forensics
Author: @CycleOfTheAbsurd

Une capture réseau contient les paquets qui ont été échangés sur le réseau pendant une période de temps. Ceci permet de voir ce qui a été échangé, entre qui et, s'il n'est pas chiffré, le contenu de ces échanges. [`Wireshark`](https://www.wireshark.org/) est un logiciel libre qui permet de créer et d'analyser de telles captures. Les [filtres de Wireshark](https://wiki.wireshark.org/DisplayFilters) vous seront grandement utiles.

Dans cette série de défis, vous devrez utiliser cet outil pour récupérer les informations demandées dans cette capture réseau. Tous les défis utilise le même fichier: [requin\_au\_centre.pcapng](https://drive.google.com/file/d/1qnCaylIjn5Hhu3uXPrar1u7z43BQOWIe/view?usp=sharing)

----

La méthode d'authentification HTTP [_Basic-Auth_](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication) permet de s'authentifier à un serveur de manière simple en envoyant un _header_ HTTP bien formatté. Si celui-ci contient les bons identifiants, l'accès à la page est authorisé, sinon le serveur retourne un code de status indiquant que l'utilisateur n'est pas authorisé à accéder à la page.

Note: Ce flag n'est __pas__ au format `FLAG-.*`

Défi #3: Plusieurs tentatives de se connecter au serveur `united-ctf.can` en utilisant la méthode _Basic-Auth_ ont été effectuées. Quelle est le mot de passe utilisé dans la connection qui a fonctionné (le bon mot de passe pour s'authentifier)?


## Setup

Requirements:
- None

Start:

```
(Not an interactive challenge)
```
