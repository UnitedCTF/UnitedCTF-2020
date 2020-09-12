# Injection SQL #2: ERREUR: TITRE INVALIDE

Cacher les résultats d'une requête à l'utilisateur n'est pas une méthode suffisante pour se protéger des injections SQL. Il existe plusieurs canaux alternatifs qu'un attaquant peux utiliser pour exfiltrer les données qu'il désire obtenir. Les messages d'erreurs sont un exemple d'output qui peut sembler inoffensif, mais qui peut faire fuiter des données.

Défi: Les résultats de la requête effectuée ne sont pas affichés, mais il est possible d'avoir les messages d'erreurs retournés par le moteur de la base de données. Utilisez-les pour obtenir le flag qui se cache dans une table.
