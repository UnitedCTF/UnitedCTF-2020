# Injection SQL #3: Mais je le vois pas!

> Web

Author: @CycleOfTheAbsurd

En général, montrer des messages d'erreurs génériques à l'utilisateur plutôt que les messages complets dans une application web est une bonne habitude à prendre. Ceci réduit les informations potentiellement utiles qui fuitent à travers ces erreurs. Par contre, ce n'est toujours pas suffisant pour se protéger des injections SQL.

Ce type d'attaque dit "à l'aveuglette" (*blind*) est plus complexe, mais est un excellent exemple de canal alternatif pour fuiter de la donnée. Elle montre aussi comment une information bénigne peut être utilisée pour reconstruire des informations potentiellement confidentielles.

Un test que l'on peut effectuer dans une injection _blind_ est de voir si le caractère à la `x`ième position d'une chaîne est égal à un caractère que l'on fournit. Par exemple, si on met dans la clause `WHERE` quelque chose comme `flag[0] == "E"` et qu'on ne reçoit aucun résultat, on sait que la première lettre n'est pas "E". Si on essaie ensuite avec la comparaison `flag[0] == F` et que l'on obtient des résultats, on sait que notre comparaison est vraie et donc que `flag` commence par la lettre "F". _Notez que le pseudo-code utilisé dans cet exemple n'est pas valide en SQL, il sert seulement à illustrer le genre de comparaison que l'on peut faire et ce qu'on peut en apprendre._

**NOTE**: Vous allez devoir écrire un script ou programme pour résoudre ce défi. Sinon vous risquez de passe le CTF au complet dessus.

Défi: Obtenez le flag contenu dans la table `challenge3`.
