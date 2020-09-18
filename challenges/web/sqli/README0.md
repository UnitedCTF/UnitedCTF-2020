# Injection SQL #0: Toute la vérité

> Web

Author: @CycleOfTheAbsurd

[SQL](https://en.wikipedia.org/wiki/SQL) est un langage pour interagir avec des bases de données relationnelles. C'est un langage extrêmement commmun que l'on retrouve entre autres dans une grand partie des applications web.

Les vulnérabilités de type *injection* surviennent lorsqu'une donnée contrôlée par l'utilisateur est utilisée de manière insécuritaire dans un contexte où cette entrée peut causer une confusion et être interprétée comme une commande ou du code. Il s'agit du [#1 dans le Top 10 des vulnérabilités web selon l'OWASP](https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A1-Injection).

L'injection SQL est un type d'injection dans laquelle l'entrée de l'utilisateur peut être partiellement interprétée comme du code SQL et ainsi modifier la requête effectuée. Cette vulnérabilité est très facile à éviter et pourtant elle est encore très fréquente. SQL fournit un mécanisme appelé [*Prepared Statements*](https://en.wikipedia.org/wiki/Prepared_statement) qui permet d'éviter presque toutes les injections SQL. Ce mécanisme permet d'assurer que l'entrée de l'utilisateur est traitée exclusivement comme de la donnée.

Une des injections SQL les plus simples consiste à rendre une condition (dans une clause `WHERE`) toujours vraie de manière à voir l'entièreté du contenu d'une table.

**NOTE**: Tous les défis de cette série utilisent [MariaDB](https://mariadb.com/kb/en/training-tutorials/) comme moteur de base de données. Certaines commandes peuvent différer selon le moteur utilisé. Lorsque c'est le cas, utilisez la version MariaDB/MySQL.

Défi: Obtenez le flag contenu dans la table `challenge0`.


## Setup

Le même pour toute la série de défis.

Requirements:
- `docker-compose`

Start:

```
docker-compose up sqli_web sqli_db
```
