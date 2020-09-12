# Injection SQL #4: Quand est-ce qu'on arrive?

Même tout cacher à l'utilisateur n'est pas suffisant pour se protéger d'une injection SQL (et limite pas mal l'utilité de l'application...). Il est important de se protéger à la base contre l'injection. Dès que l'attaquant a un moyen d'affecter le comportement de l'application par son injection. Il peut utiliser ce différentiel de comportement pour apprendre des choses sur le contenu de la base de données. Ceci peut jusqu'à en apprendre le contenu.

**NOTE**: Regardez la liste des [fonctions prédéfinies dans MySQL/MariaDB](https://dev.mysql.com/doc/refman/8.0/en/sql-function-reference.html). Certaines d'entre elles pourraient vous permettre de créer un comportement observable pour faire fuiter des données.

**NOTE**: Vous allez devoir écrire un script ou programme pour résoudre ce défi. Sinon vous risquez de ne pas avoir le temps de le finir avant la fin du CTF.

Défi: On ne vous montre rien en rapport avec le résultat de votre requête. Trouvez un moyen d'avoir quand-même le flag contenu dans la table `challenge4`.
