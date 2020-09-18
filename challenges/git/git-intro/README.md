# Introduction à Git, partie 1: le flag perdu

> Git

Author: @xshill

Git est un outil de contrôle de version de code source très répandu. Il permet entre autres de garder un historique des modifications de votre code et d'autres fichiers connexes. Par exemple, si vous supprimez un fichier de votre repo (répertoire Git, souvent appelé _repository_ de par son nom anglais), Git vous permettra de faire un "reset" (😉) et de retourner en arrière avant la suppression, tant que ce fichier était auparavant "commité".

Pour cette première partie, ouvrez le repo et retrouvez le flag perdu. [Ce tutoriel sur Git](https://openclassrooms.com/fr/courses/1233741-gerez-vos-codes-source-avec-git) devrait vous être utile.

Les 4 premiers flags de cette catégorie se font tous avec le même répertoire Git, que vous pouvez télécharger en pièce jointe du challenge.

# Introduction à Git, partie 2: le flag communiqué

> Git

Author: @xshill

Quand on fait un commit sur Git, c'est important de mettre un message pertinent! ;)

# Introduction à Git, partie 3: le flag séparé

> Git

Author: @xshill

Avec Git, on peut créer des branches. Chaque branche est comme une version séparée de l'historique: vous pouvez faire des commits dessus sans que les modifications soient apportées aux autres branches. Vous pouvez par la suite fusionner des branches ensemble pour regrouper leur historique. 

En pratique, les repo Git ont souvent une branche `master` qui représente la version de production, et plusieurs branches de développement qui servent à mettre les fonctionnalités qui ne sont pas encore terminées ou intégrées correctement.

# Introduction à Git, partie 4: le flag sauvegardé

> Git

Author: @xshill

Parfois, on commence à faire des modifications dans notre code, puis on décide de revenir en arrière pour une raison quelconque: intégrer du nouveau code avant de continuer à programmer, essayer une autre implémentation... Plutôt que de perdre vos changements ou de les mettre dans un fichier séparé, vous pouvez utiliser le `stash`: une fonctionnalité de Git qui permet de stocker des modifications et de les retrouver plus tard.

## Setup

Requirements:
- None

Start:

```
(Not an interactive challenge)
```
