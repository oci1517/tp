##########################
POO : TP évalué
##########################

Préparation
-----------

* Créer un dossier ``poo-bases`` dans votre dépôt TP
* Travailler dans ce dossier ``poo-bases``

Un peu de géométrie
-------------------

Définition de la classe ``Point``
+++++++++++++++++++++++++++++++++

Définir une classe ``Point`` représentant un point géométrique. Cette classe
doit permettre de créer des points qui fonctionnent comme le montre le code
suivant et doit être une "New Style class" (consulter l'article suivant pour
plus d'informations : https://wiki.python.org/moin/NewClassVsClassicClass) :

Exemples d'utilisation
......................

De plus, les exemples suivants devront être fonctionnels :

::

    >>> A = Point(-3, 4)
    >>> B = Point(2, 16)
    >>> O = Point()
    >>> A
    Point(-3, 4)
    >>> O
    Point(0, 0)
    >>> str(A)
    '(-3, 4)'
    >>> print("Distance = ", A.distance(B))
    Distance = 13.0
    >>> print("Distance = ", B.distance(A))
    Distance = 13.0


La classe ``Point`` contient donc une méthode ``distance(other)`` prenant comme
unique paramètre un autre point ``other`` et calculant la distance séparant l'instance
considérée et le point ``other``.

Constructeur
............

* Le constructeur de la classe ``Point`` prend en paramètre les coordonnées du point dans un repère cartésien.
* Si aucun argument n'est fourni, le point représentera l'origine du repère.

Méthodes publiques
..................

* ``distance(self, other)`` : calcule la distance entre le point considéré (``self``) et un autre point ``other``
* ``count()`` : retourne le nombre d'instances de la classe ``Point`` créées. Le nombre d'instances doit s'incrémenter automatiquement à chaque fois qu'une nouvelle instance est créée

Méthodes surchargées
....................

* ``__str__``
* ``__repr__``

Définition de la classe ``Rectangle``
+++++++++++++++++++++++++++++++++++++

Définir une classe ``Rectangle`` qui s'utilise de la manière suivante (tous les exemples doivent fonctionner) :

Exemple d'utilisation
.....................

::

    >>> corner = Point(12, 27)
    >>> rect = Rectangle(corner, 50, 36)
    >>> copie = rect.clone()
    >>> rect == copie
    False
    >>> rect
    <__main__.Rectangle object at 0x15ed590>
    >>> copy
    <__main__.Rectangle object at 0x15edc50>
    >>> rect.area()
    1750
    >>> rect.get_center()
    Point(37, 9)

Constructeur
............

Le constructeur prend trois paramètres :

* ``corner : Point`` : instance de la classe ``Point`` qui désigne les coordonnées du point supérieur gauche
* ``width : float`` : détermine la largeur du rectangle
* ``height : float`` : détermine la hauteur du rectangle

Méthodes publiques
..................

* ``clone()`` : effectue une copie profonde du rectangle
* ``area()`` : retourne l'aire du rectangle en question

Définition de la classe ``Square``
++++++++++++++++++++++++++++++++++

Définir une classe ``Square`` d'après le diagramme de classe suivant :

..  figure:: figures/square-rectangle-relationship.png
    :width: 80%
    :align: center

Constructeur
............

* ``Circle(center : Point, radius : float) => Circle`` : constructeur de la classe

Méthodes publiques
..................

* ``area() => float`` : calcule l'aire du cercle
* ``get_center() => Point`` : retourne le centre du cercle

Les exemples suivants doivent être fonctionnels :

..  code-block:: python

    >>> corner = Point(10, 5)
    >>> square = Square(corner, side=10)
    >>> square
    Square(10)
    >>> square.area()
    100
    >>> square.get_center()
    Point(15, 0)


..  admonition:: Attention

    Pour éviter toute dupplication de code, il faut vous débrouiller pour ne pas
    réimplémenter une deuxième méthode ``area()`` pour caluler l'aire du carré.
    Le carré est en effet un rectangle particulier et il est possible d'utiliser
    la formule d'aire du rectangle pour calculer l'aire d'un carré.


Multiplier un rectange par un scalaire
++++++++++++++++++++++++++++++++++++++

Modifier la classe ``Rectangle`` pour qu'il soit possible de le multiplier par
un nombre positif ``n``. Ceci aura pour effet de générer un nouveau rectangle de
même centre mais de côté ``n`` fois plus grand.


Définition de la classe ``Circle``
++++++++++++++++++++++++++++++++++

Définir une classe ``Circle`` qui supporte les opérations suivantes

>>> center = Point(0,0)
# Crée un cercle de centre ``center`` et de rayon ``radius``
>>> c = Circle(center, radius=10)
# calcule l'aire du cercle
>>> c.area()
314.15926
# retourne le centre du cercle
>>> c.get_center()
Point(0, 0)
# détermine si un point se trouve à l'intérieur du cercle ou non
>>> p1 = Point(3,4)
>>> p2 = Point(20, 0)
>>> p1 in c
True
>>> p2 in c
False

..  tip::

    Consulter la documentation Python pour voir comment faire en sorte de
    pouvoir implémenter l'opérateur ``in`` permettant de déterminer si un point
    ``P(x;y)`` se trouve dans le cercle de centre ``center`` et de rayon
    ``radius``.




























..  comment::
    Question 3
    ++++++++++

    Définissez une classe ``Account``, qui permette d’instancier des objets tels que ``compte1``,
    ``compte2``, etc. Le constructeur de cette classe initialisera deux attributs d’instance ``nom`` et ``solde``. Trois autres méthodes seront définies :

    * ``depot(amount)`` permettra d’ajouter la somme ``amount`` au solde ;
    * ``retrait(amount)`` permettra de retirer, si possible, une certaine somme du solde ;
    * ``affiche()`` permettra d’afficher le nom du titulaire et le solde de son compte.

    Exemples d’utilisation de ``Account``
    .....................................

    ::

        >>> compte1 = CompteBancaire('Duchmol', 800)
        >>> compte1.depot(350)
        >>> compte1.retrait(200)
        >>> compte1.affiche()

    Le solde du compte bancaire de Duchmol est de 950 euros.

    ::

        >>> compte2 = CompteBancaire()
        >>> compte2.depot(25)
        >>> compte2.retrait(3000)

    Le solde du compte de Dupont est insuffisant pour ce retrait.

    ::

        >>> compte2.affiche()

    Le solde du compte bancaire de Dupont est de 1025 euros.
