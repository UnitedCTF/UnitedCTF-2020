# Rediriger le ruisseau d'exécution

> Pwn

Author: @CycleOfTheAbsurd

Lorsque l'on effectue un appel de fonction dans un programme compilé, l'adresse de l'exécution suivant cet appel est mise sur la stack (par l'instruction [`CALL`](https://www.felixcloutier.com/x86/call)). Celle-ci est ensuite utilisée comme adresse de retour (par l'instruction [`RET`](https://www.felixcloutier.com/x86/ret)) pour continuer le flux d'exécution en assignant le pointeur d'instruction RIP à cette valeur.

_Note_: Le fonctionnement des appels de fonctions et retours est différent dans certaines architectures de processeur autres que x86 et x86-64, mais ceci est hors de portée du présent challenge et ne nous importe pas ici.

Comme nous l'avons vu dans le précédent challenge, la _stack_ fonctionne en mode Dernier-Arrivé, Premier-Sorti. L'adresse de retour est placé sur la pile avant les variables locales, il est donc possible d'exploiter le même genre de débordement de tampon pour rediriger l'exécution d'un programme en modifiant l'adresse de retour. Ceci peut être exploité de manière pour appeler une autre fonction, à sauter par dessus une condition pour éviter sa vérification et bien plus encore.

Défi: Voici un autre programme compilé vulnérable à un débordement de tampon. Tentez d'abord de comprendre son comportement et de l'exploiter localement. Si vous y parvenez, il affichera un flag censuré: "FLAG-XXXXXXXXXXXXXXXXXXXXXXXXXXXXX".

Afin d'obtenir le vrai flag, vous devrez exploiter ce même programme via `unitedctf.ca:17001`

_Note_: Nous avons désactivé certaines protections mémoires dont [PIE](https://en.wikipedia.org/wiki/Position-independent_code). Pour cette raison, les adresses de fonctions du binaire sont constantes. Elles ne changeront pas entre les différentes machines ni entre les exécutions.

_Note_: utilisez `netcat` pour vous y connecter


## Setup

Requirements:
- `make`
- `gcc`
- `docker-compose`

Start:

```
make all
docker-compose up le_ruisseau_pwn
```
