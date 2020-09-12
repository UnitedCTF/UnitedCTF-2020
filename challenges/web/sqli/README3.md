# Injection SQL #3: Mais je le vois pas!

En général, montrer des messages d'erreurs génériques à l'utilisateur plutôt que les messages complets dans une application web est une bonne habitude à prendre. Ceci réduit les informations potentiellement utiles qui fuitent à travers ces erreurs. Par contre, ce n'est toujours pas suffisant pour se protéger des injections SQL.

Ce type d'attaque dit "à l'aveuglette" (*blind*) est plus complexe, mais est un excellent exemple de canal alternatif pour fuiter de la donnée. Elle montre aussi comment une information bénigne peut être utilisée pour reconstruire des informations potentiellement confidentielles.

**NOTE**: Vous allez devoir écrire un script ou programme pour résoudre ce défi. Sinon vous risquez de passe le CTF au complet dessus.

Défi: Obtenez le flag contenu dans la table `challenge3`.
