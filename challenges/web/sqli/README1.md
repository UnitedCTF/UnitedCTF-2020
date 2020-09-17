# Injection SQL #1: Va me falloir un SCHEMA

Les bases de données MySQL et MariaDB exposent une BD virtuelle nommée [`INFORMATION_SCHEMA`](https://dev.mysql.com/doc/refman/8.0/en/information-schema.html). Cette dernière possède des tables qui contiennent les métadonnées sur ce qui est accessible à l'utilisateur courant; entre autres, les propriétés des tables et de leurs colonnes. Ceci est très utile pour découvrir les données auxquelles nous avons accès. Particulièrement dans un contexte d'injection SQL où on ne connait généralement pas le schéma de la base de données.

SQL possède une clause [`UNION`](https://mariadb.com/kb/en/union/) qui permet de combiner les résultats de plusieurs requêtes. Ceci pourrait vous servir.

Défi: Obtenez le flag qui se cache dans une table que vous pouvez lire.
