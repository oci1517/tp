
Exponentiation rapide
#####################

Informations
============

*  Délai : lundi 22 février 12h
*  Durée estimée par groupes : 1h30 - 2h
*  À rendre : dépôt bitbucket du travail pratique

Composition des groupes
-----------------------

* Équipe 1 : Quentin et Aleandro
* Équipe 2 : Samuel et Lucien
* Équipe 3 : Maxime et Bruno


Préparation
===========

#. Créer un nouveau dépôt privé ``oci-tp`` sur votre compte bitbucket et clonez-le sur votre machine locale (de préférence) ou sur Cloud9. Vous y effectuerez tous vos futurs travaux pratiques.
#. Créer un dossier ``01-power-optim`` à la racine de votre dépôt
#. Créer dans le dossier ``01-power-optim`` un fichier :file:`power.py` que vous utiliserez pour effectuer ce TP
#. Si nécessaire, vous pouvez créer d'autres fichiers Python et les importer dans votre script
#. Rendre un rapport d'expérience (réponses aux questions posées) au format PDF. Nommer le fichier :file:`rapport.pdf` et le placer à la racine du dossier de TP.

Contexte
========

..  time:: 10 min

On donne la fonction récursive  ``power(a, n)`` qui permet d'élever le nombre réel :math:`a` à la puissance entière :math:`n \in \mathbb{N}` :

**Version récursive**

.. code-block:: python
    :linenos:

    def power(a, n):
        if n == 0:
            return 1
        if n < 0:
            return 1 / power(a, -n)

        return a * power(a, n-1)


Voici quelques exemples d'utilisation de cette fonction

::

    >>> power(2, 5)
    32
    >>> power(2, -5)
    0.03125
    >>> power(1.456, 152)
    6.317263563052873e+24
    >>> power(1.456, 1520)
    Traceback (most recent call last):
      File "<script>", line 1, in <module>
      File "C:\Users\cedon_000\Desktop\tigerjython\untitled 1", line 7, in power
      File "C:\Users\cedon_000\Desktop\tigerjython\untitled 1", line 7, in power
      ...
    RuntimeError: maximum recursion depth exceeded


Mesure des performances
-----------------------

Votre première tâche sera de mesurer les performances de la fonction
``power(a, n)`` ainsi définie. Pour ce faire, il faut utiliser la fonction
``time`` du module :mod:`time` :

..  code-block:: python

    >>> from time import time

    >>> time()
    0.00300002098083

La valeur de retour de la fonction ``time`` correspond au nombre de secondes
qui se sont écoulées depuis le début de l'époque UNIX, à savoir le 1er janvier
1970 à 0h00. On peut utiliser cette fonction pour mesurer le temps nécessaire
pour exécuter une fonction.

..  code-block:: python

    # ligne nécessaire pour pouvoir utiliser la fonction print de Python 3 dans TigerJython
    from __future__ import print_function

    # fonction permettant de chronométrer la durée d'exécution d'un bout de code
    from time import time

    def power(a, n):
        if n == 0:
            return 1
        if n < 0:
            return 1 / power(a, -n)

        return a * power(a, n-1)

    t0 = time()
    result = power(1.5123, 512)
    t1 = time()
    print("Computation result :", result)
    print("Elapsed time [s] :", t1 - t0)

..  admonition:: Sortie

    ::

        Computation result : 9.43260188343e+91
        Elapsed time [s] : 0.00200009346008

    Dans la sortie précédente, le résultat ``9.43260188343e+91`` est à interpréter commme :math:`9.43260188343 \times 10^{91}`.



Problème 1 : fonction ``timeit``
================================

..  time:: 10 min

Développer une fonction ``timeit(function)`` qui prend en argument la fonction ``function`` et qui chronomètre sa durée d'exécution à l'aide de la fonction ``time.time``

..  admonition:: Exemples d'utilisation

    La fonction ``timeit`` devrait pouvoir s'utiliser de la manière suivante

    ::

        >>> timeit(ma_fonction)
        0.00300002098083

..  attention::

    Il ne faut pas croire que cette mesure est fiable. On ne fait en effet que
    de mesurer le temps nécessaire à l'exécution de la fonction, mais sans
    tenir compte de toutes les activités simultanées effectuées par le CPU.

    Plusieurs mesures successives donnent en effet des résultats assez
    différents qui peuvent varier du simple au double. Pour vous en
    convaincre, testez le code suivant qui va chronométrer dix *runs*
    différents de la fonction ``experience``

    ::

        def experience():
            result = power(1.5123, 512)

        for i in range(10):
            print(timeit(experience))

    ..  admonition:: Sortie

        ::

            0.00200009346008
            0.00100016593933
            0.00200009346008
            0.000999927520752
            0.000999927520752
            0.00100016593933
            0.000999927520752
            0.00100016593933
            0.000999927520752
            0.00100016593933

    ..  admonition:: Remarque

        On aurait pu obtenir le même résultat avec une expression ``lambda`` qui
        définit une fonction anonyme de la manière suivante :

        ..  code-block:: python

            for i in range(10):
                print(timeit(lambda : power(1.5123, 512)))


Problème 2 : moyenne des *runs*
===============================

..  time:: 10 min

Raffiner la fonction ``timeit`` pour qu'elle chronomètre ``n`` fois de suite le temps d'exécution de la fonction ``function``
et qu'elle retourne la moyenne arithmétique des *runs*

..  admonition:: Exemples d'utilisation

    ::

        >>> timeit(lambda : power(1.5, 512), n=10)
        0.000400018692017


Problème 3 : déterminer le nombre de *runs*
===========================================

..  time:: 5 min

Le temps indiqué pour ``n=10`` n'est pas très fiable non plus, ce dont on peut se convaincre en effectuant plusieurs groupes de 10 runs différents :

::

    for i in range(20):
        print( timeit(lambda : power(1.5, 512), n=10) )

Déterminer expérimentalement une valeur ``n`` adaptée pour obtenir des résultats fiables comportant au moins 1 chiffre significatif.


Problème 4 : optimisation de la fonction ``power``
==================================================

..  time:: 20 min

Pour le moment, notre fonction ``power`` n'est pas très rapide. Voici une
comparaison avec une fonction ``fast_power`` qui apporte une simple optimisation à la version ``power`` utilisée ci-dessus et qui est environ 16 fois plus rapide (le deuxième résultat est bien :math:`\approx 1.1 \times 10^{-5}` secondes :

::

    >>> timeit(lambda: power(1.5, 600))
    0.000180999994278
    >>> timeit(lambda: fast_power(1.5, 600))
    1.10001564026e-05
    >>> optimization_ratio = 0.000180999994278 / 1.10001564026e-05
    >>> optimization_ratio
    16.45431098008923

D'autre part, la fonction ``power`` a un gros problème :

::

    >>> power(1.5, 1500)
    Traceback (most recent call last):
      File "<script>", line 1, in <module>
      File "C:\Users\cedon_000\Desktop\tigerjython\untitled 1", line 10, in power
      ...
      RuntimeError: maximum recursion depth exceeded




..  admonition:: Consigne

    #.  Expliquer le problème rencontré lorsque l'exposant ``n`` est très grand
    #.  Définir une fonction récursive ``fast_power(a, n)`` qui utilise la propriété mathématique suivante

        ..  math::

            a^{2n} = \left( a^n \right)^n

    #.  Chronométrer la fonction ``fast_power`` pour ``n=511`` et ``n=512``. Expliquer pourquoi la fonction met systématiquement plus de temps pour ``n=511``.


Problème 5 : itératif vs récurisf
=================================

..  time:: 10 min

Comparer les performances de la fonction récursive ``power`` avec son pendant
itératif ``power_iter`` pour ``n`` dans ``[10, 100, 200, 500]``

::

    def power_iter(a, n):
        result = 1

        if n < 0:
            return 1 / power_iter(a, -n)

        for i in range(n):
            result = result * a

        return result


..  admonition:: Questions à répondre

    #.  Pourquoi la version itérative est-elle plus rapide que la version récursive alors qu'au fond, elles font les deux exactement la même chose au niveau mathématique :

    ..  math::

        a^n = a \cdot a \cdot a \cdots a

..  comment

    Problème 6
    ==========

    On donne une liste de :math:`10^5` nombres aléatoires réels :math:`a_i \in [0;1]` dans le
    fichier :download:`a_list.py` et une liste d'exposants entiers :math:`n_i \in \mathbb{N}^+` dans le fichier :download:`n_list.py`. Placez ces deux fichiers dans le même dossier que votre programme et importez ces listes de nombres avec

    ::

        from a_list import a_list
        from n_list import n_list

    Développer une fonction ``job(alist, nlist)`` qui construit la liste
    ``x_list`` le plus efficacement possible de sorte que

    ..  math::

        x_i = a_i^{n_i}

    pour :math:`0 \leq i \leq n` où :math:`n = 10^5` est le nombre d'éléments dans les listes ``a_list`` et ``n_list``.

    ..  admonition:: Exemples d'utilisation

        ::

            from a_list import a_list
            from n_list import n_list

            x_list = job(a_list, n_list)

            for i in len(a_list):
                # condition qui doit être vérifiée pour la liste `x_list`
                assert(x_list[i] == power(a_list[i], n_list[i]))

            print(x_list[:10])

        ..  admonition:: Sortie

            ::





.. comment.code-block:: python
    :linenos:

    def fast_power(a, n):
        if n < 0:
            return 1 / power(a, -n)
        if n == 0:
            return 1
        if n % 2 == 0:
            tmp = power(a, n // 2)
            return tmp ** 2
        else:
            return a * power(a, n-1)
