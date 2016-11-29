##########################
Examen 3 : partie pratique
##########################

Préparation
-----------

* Créer dossier ``exa3`` dans votre dépôt TP
* Travailler dans ce dossier ``exa3``

Contexte
--------

Développer un programme capable de faire une requête GET avec le module
``urllib2`` et d'analyser le code HTML renvoyé pour en extraire le taux de
change du CHF avec d’autres devises en utilisant le site de la BNS
(http://www.snb.ch/fr/).

Cet exercice doit être réalisé dans le fichier ``currencies.py``

Étape 1
-------

Développer une fonction ``get_html(url : str) ==> str`` qui retourne le code
HTML de la page indiquée par ``url``.

..  admonition:: Signature
    :class: note

    * Paramètre 1 : ``str : url`` : URL de la page à visiter et dont il faut renvoyer le code HTML

    * Valeur de retour : ``str`` : code HTML renvoyé par le serveur HTTP

..

    Test
    ++++

    Voici une fonction permettant de tester votre fonction ``get_html()``

Étape 2
-------

Développer une fonction ``exchange_rate(html, currency)`` qui prend en argument une
chaine de caractères parmi les suivantes

::

    EUR
    USD
    JPY
    GBP

et qui retourne la valeur de la devise en question en francs suisses contenue dans le code . Si la
devise spécifié n'est pas mentionnée, la fonction lève une exception de type
``ValueError`` en indiquant un message qui spécifie les devises autorisées.

Exemple d'utilisation
+++++++++++++++++++++

..  code-block:: python

    >>> exchange_rate('EUR')
    1.0999
    >>> exchange_rate('RUB')
    ValueError


Étape 3
-------

Développer un programme TigerJython qui contient un champ de saisie ``amount``
dans lequel on peut saisir un montant en CHF ainsi ainsi qu'un champ
``foreign_cur`` dans lequel on peut saisir la chaine de caractère correspondant à
la devise étrangère visée.

L'interface contiendra également un bouton "Go" permettant de lancer la
conversion qui sera effectuée de la manière suivante

1) Chercher le taux de change actuel sur le site de la BNS
2) Effectuer le calcul nécessaire à partir du taux de change et de la valeur saisie dans le champ ``amount``
3) Afficher le résultat dans un champ textuel ``result``
