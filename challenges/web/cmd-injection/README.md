# Injection de commandes

> Web

Author: @xshill

Saviez-vous que la plupart des langages de programmation permettent d'appeler des commandes shell externes? Ça peut être pratique... mais attention à ne pas rendre votre site vulnérable. ;)

Ce challenge montre un exemple de vulnérabilité appelée injection de commandes. Elle se produit lorsqu'il est possible pour un attaquant de modifier la commande qui sera effectuée par le programme.

Votre défi est d'exploiter cette vulnérabilité afin de lire le contenu du fichier `flag`. Bonne chance!

> **NOTE**: le serveur roule sur Ubuntu 18.04 et le shell est `/bin/bash`.

## Setup

Requirements:
- None

Start:

```
docker-compose up cmd-injection
```
