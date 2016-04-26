#################################
Dictionnaires et analyse de texte
#################################

Informations
============

*  Délai : vendredi 15 avril 23h59
*  Durée estimée : environ 3h
*  À rendre : dépôt bitbucket du travail pratique

Composition des groupes
-----------------------

Vous pouvez travailler à deux mais chacun me rend sa propre version du code et
son propre rapport.

La dernière question se fait par groupes de 2 lors du cours d'OC du mardi 12
avril. Les groupes seront déterminés lors du cours.

..  attention::

    Je ne veux aucun absent lors de ce cours !!!!

Préparation
===========

#.  Vous travaillerez dans votre dossier  ``oci-tp`` créé lors du premier TP.
#.  Créer un dossier ``02-dicos-text-parsing`` à la racine de votre dépôt
#.  Créer dans le dossier ``02-dicos-text-parsing`` un fichier :file:`main.py` que vous utiliserez pour effectuer ce TP. Si nécessaire, vous pouvez créer d'autres fichiers Python et les importer dans votre script
#.  Rendre un rapport d'expérience (réponses aux questions posées) au format PDF nommé :file:`rapport.pdf` et le placer à la racine du dossier de TP ``02-dicos-text-parsing``.


Problème 1a
===========

Dans le fichier ``main.py``, développer une fonction ``to_words(text : str) -->
list`` qui prend une chaine de caractères ``text`` et qui retourne une liste de
tous les mots présents dans ``text``.

..  admonition:: Code de base

    ::

        def to_words(text):
            words = []

            # do some job here

            return words

..  admonition:: Indication
    :class: note

    Il faut commencer par "purger" le texte de tous les caractères de
    ponctuation qui ne doivent pas être considérés comme des mots.

    Voici une chaine de caractères contenant tous les caractères à ne pas
    prendre en compte. Il faut donc supprimer ces caractères du texte à analyser
    avant d'en ressortir les mots.

    ::

        punctuation = ',;.:?!"\''


Problème 1b
===========

Dans le fichier ``main.py``, développer et tester une fonction
``max_word_len(sentence) --> (index, size)``
qui retourne l'indice ainsi que la
taille du plus long mot trouvé dans la phrase
``sentence``.

..  admonition:: Code de base

    ::

        def max_word_len(words):
            # do some job here

            return (index, size)

Problème 2
==========

#.  Étudier l'annexe 2 `Trappe, règles et astuces
    <http://www.tigerjython.ch/franz/index.php?inhalt_links=navigation.inc.php&inhalt_mitte=anhang/tricks.inc.php>`_
    de TigerJython si ce n'est pas déjà fait.

#.  Dans le fichier ``main.py``, développer une fonction
    ``make_unique(elements) --> unique_elements`` qui
    retourne **une véritable copie** de la liste ``elements`` dont tous les doublons
    ont été supprimés.

Problème 3
==========

Dans le fichier ``main.py``, développer une fonction
``swap_key_values(dictionary) --> swapped_dict`` qui
inverse le rôle des clés et des valeurs du dictionnaire ``dictionary`` fourni en
argument.

..  admonition:: Exemple d’utilisation

    ..  code-block:: python

        >>> dico1 = {'computer' : 'ordinateur', 'keyboard' : 'clavier'}
        >>> swap_key_values(dico1)
        {ordinateur : 'computer', 'clavier' : 'keyboard'}


..  attention::

    Attention aux problèmes qui vont se poser avec certains dictionnaires.
    Réfléchir aux conditions que doit remplir le dictionnaire fourni en argument
    pour ne pas poser de problèmes.

    Traiter les cas problématiques à l'aide d'un mécanisme de gestion
    d'exception afin que le programme ne se plante jamais.

Problème 4
==========

Dans le fichier ``freqs.py``, développer une procédure
``char_freq(text) --> None`` qui affiche
l’histogramme des fréquences d’apparition des mots composant le texte entré par
ordre décroissant de fréquences.

..  admonition:: Exemple d'utilisation

    ..  code-block:: python

        >>> histogramme_freq("le corbeau et le renard")
        Histogramme des frequences d'apparition des mots du texte entre:

        Mots              Frequences    Histogramme
        ===========================================
        le                2             **
        corbeau           1             *
        et                1             *
        renard            1             *


Problème 5
==========

Dans le fichier ``freqs.py``, développer une fonction
``tj_char_freq(text) --> None`` qui reprend la fonction
de l'exercice précédent et affiche un joli histogramme à l'aide de
``GPanel`` dans TigerJython.

Problème 6
==========

Dans ce problème, vous allez dresser quelques statistiques concernant un texte
d'envergure qui contient un grand nombre de mots. Il s'agit de la Bible, version
Segond révisé que vous trouverez dans le fichier
:download:`files/bible_f_col.txt`. Chaque ligne de ce fichier est un verset de
la Bible au format suivant (``\t`` représente une tabulation) :

::

    <abbréviation_livre> <no_chapitre>,<no_verset>\t<verset>

Voici les premiers versets de la Genèse à titre d'exemple :

..  literalinclude:: files/first-lines.txt
    :encoding: latin1

#.  Créer un fichier ``bible_stats.py`` qui contiendra votre programme
#.  Importer le module ``freqs`` créé dans le problème précédent


..  note::

    Importer en intégralité le contenu du fichier dans la mémoire n'est pas très
    efficace car le fichier est très grand. Voici comment lire un fichier texte
    ligne à ligne et le traiter immédiatement :

    ..  code-block:: python

        with open(filename, 'r', encoding='latin1') as fd:
            for line in fd:
                process_line(line)

    où ``process_line()`` est une fonction qui effectue un certain traitement sur la
    ligne ``line``.

    Dans le code précédent, l'objet ``fd`` retourné par le gestionaire de
    contexte ``with`` est un objet permettant de manipuler appeler un *file
    descriptor*.

    L'utilisation d'un gestionnaire de contexte ``with`` est la façon
    "Pythonesque" correcte de lire un fichier. Il n'est pas nécessaire de le
    ferme explicitement avec ``fd.close()`` car c'est le gestionnaire de
    contexte qui s'en charge. C'est d'ailleurs là tout son intérêt.

..  attention::

    Le fichier :file:`bible_f_col.txt` est encodé avec l'encodage `latin1`.
    Pour l'ouvrir sans encombre, il faut donc faire la chose suivante sous Python
    3

    ::

        with open(filename, 'r', encoding='latin1') as fd:
            # la suite ici
            do_something()

    Cela ne fonctionne pas dans Python 2.7 (et donc pas non plus dans
    TigerJython) car la fonction ``open`` standard ne prend pas en charge
    l'argument ``encoding``. Pour s'en sortir, il faut utiliser la fonction
    ``open`` du module ``codecs`` en ajoutant la ligne suivante au début du
    fichier :

    ::

        from codecs import open

Consignes à réaliser
--------------------

Développer plusieurs fonctions permettant de répondre aux questions ci-dessous.
Vous les nommerez selon votre inspiration mais faites en sorte qu'une fonction
ne fasse toujours qu'une chose bien définie. Essayez de favoriser la
réutilisation du code.

Préparation
+++++++++++

#.  Construire une liste ``refs`` contenant toutes les références des versets bibliques triées dans l'ordre d'apparition dans le texte.
#.  Construire un dictionnaire ``verses`` contenant tous les versets de sorte que les clés du dictionnaire soient les références présentes dans la liste ``refs`` et que les valeurs soient la liste de mots contenus dans le verset en question. Voici ce que cela donnerait en se limitant au premier verset :

    ::

        verses = {
          'Gn 1,1' : ['Au', 'commencement', 'Dieu', 'créa', 'le', 'ciel', 'et', 'la', 'terre']
        }

Statistique sur le texte
++++++++++++++++++++++++

Pour chaque question, développer une fonction sans paramètre et nommée
``question_NN`` où ``NN`` est le numéro de la question. On aura donc

::

    def question_01():
        return content

    def question_02():
        return genesis_verse_count

    def question_03():
        return ref_of_max_verse_len_in_genesis

    etc ...u

#.  Retourner (``str``) le contenu du verset ayant pour référence ``Mt 11,28``.
#.  Retourner (``int``) le nombre de versets présents dans le livre de la Genèse (Abbréviation ``Gn``)
#.  Retourner (``str``) la référence du verset de la Genèse comptant le plus de mots.
#.  Retourner (``int``) le nombre de mots présents dans le livre de la Genèse en entier.
#.  Retourner (``int``) le nombre de mots présents dans la Bible tout entière
#.  Retourner (``int``) le nombre d'occurrences du mot ``"alliance"`` dans l'ensemble de la Bible.
#.  Retourner (``tuple(str, int)``) le plus long mot présent dans la Bible ainsi que sa longueur.

Diagramme des fréquences
++++++++++++++++++++++++

Copiez le programme TigerJython réalisé dans la question précédente dans un fichier ``bible_freqs.py`` et dessiner le diagramme de fréquences de longueur de mots pour l'ensemble de la Bible.

Timing
++++++

Vos fonctions risquent dans un premier temps d'être assez lentes si vous ne
réfléchissez pas bien à la manière de procéder. Définir une fonction
``benchmark()`` qui affiche le temps d'exécution de chaque réponse. Attention,

::

    def benchmark():
        print("temps pour la question 1", timeit(question_01, n=1))
        print("temps pour la question 2", timeit(question_02, n=1))
        # etc ...
..  tip::

    le temps d'exécution de chacune des réponses en utilisant la fonction
    ``timit`` définie dans le précédent TP. Comme l'exécution des fonctions est
    dans ce cas conséquente, on n'exécute chaque fonction qu'une seule fois
    (``n=1``).
