# Exercice de prise en main

Voici un exercice de prise en main du langage Python :

> Ecrivez un programme qui demande un nombre à l'utilisateur, qui détermine si le nombre est un nombre premier et qui affiche le résultat.

Quelques conseils :

* Ecrivez du code clair (nommage des fonctions, variables, etc...)
* Documentez votre code correctement (documentez quand celà est utile, la documentation ne doit pas compenser un code qui n'est pas clair)
* Gérez les erreurs possibles de votre programme.
* Ecrivez des tests unitaires.
* En règle général, mettre tout son code dans le même fichier n'est pas une bonne idée !

## Allons-y pas à pas

### Fonction `estPremier(n)`

Créez dans un premier temps un fichier `premier.py` qui contient la fonction permettant de déterminer si un nombre est premier :

```python
def estPremier(n) :
    if n <= 1 :
        return False
    for i in range(2, n) :
        if (n % i == 0) :
            return False
    return True
```

### Programme `main`

Créez ensuite le fichier `main.py` qui permet de demander un nombre à l'utilisateur et qui dit si ce nombre est premier ou non :

```python
import sys
from premier import estPremier

userInput = input('Choisissez un nombre : ')

n = int(userInput)

if estPremier(n) :
    print("{} est un nombre premier".format(n))
else :
    print("{} n'est pas un nombre premier".format(n))
```

### Tests unitaires

Vous pouvez maintenant compléter `premier.py` en ajoutant des commentaires et des tests unitaires basés sur [`doctest`](https://docs.python.org/3.6/library/doctest.html) :

```python
def estPremier(n) :
    """
    Retourne True si n est premier, False sinon. n doit être un entier.

    Les nombres négatifs ne sont pas premiers :
    >>> estPremier(-1)
    False

    Les nombres 0 et 1 ne sont pas premiers :
    >>> estPremier(0)
    False

    >>> estPremier(1)
    False

    Un nombre premier n'est divisible que par 1 et par lui-même :
    >>> estPremier(2)
    True

    >>> estPremier(4)
    False

    >>> estPremier(11)
    True
    """
    if n <= 1 :
        return False
    for i in range(2, n) :
        if (n % i == 0) :
            return False
    return True
```

Pour lancer l'exécution des tests unitaires : `python3 premier.py -v`

### Gestion des erreurs

Posez-vous les questions suivantes :
* Que se passe-t-il au niveau du programme `main.py` si l'utilisateur saisit autre chose qu'un nombre ?
* Que se passe-t-il au niveau de la fonction `estPremier(n)` si `n` n'est pas un nombre ?

Faites en sorte que votre programme gère correctement les erreurs possibles.

Au niveau de `main.py` :

```python
try:
    n = int(userInput)
except ValueError:
    print("Oops ! Ceci n'est pas un nombre...")
    sys.exit()
```

Au niveau de `premier.py` :

```python
if (not(type(n) is int)) :
    raise ValueError("n doit etre un entier")
```

## Solution complète

La solution complète est disponible dans le dossier [`src`](./src)
