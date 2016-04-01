#################################
Dictionnaires et analyse de texte
#################################

Problème 1
==========

Développer et tester une fonction ``max_word_len(sentence) --> (index, size)``
qui retourne l'indice ainsi que la taille du plus long mot trouvé dans la phrase
``sentence``.

Problème 2
==========

Développer une fonction ``make_unique(elements) --> unique_elements`` qui
retourne **une véritable copie** de la liste ``elements`` dont tous les doublons
ont été supprimés.

Problème 3
==========

Développer une fonction ``swap_key_values(dictionary) --> swapped_dict`` qui
inverse le rôle des clés et des valeurs du dictionaire ``dictionary`` fourni en
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

Écrire une procédure ``char_freq(text) --> None`` qui affiche
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

Développer une fonction ``tj_char_freq(text) --> None`` qui reprend la fonction
de l'exercice précédent et affiche un joli histogramme à l'aide de
``GPanel`` dans TigerJython.

Problème 6
==========

Utiliser la fonction ``tj_char_freq`` développée dans l'exercice précédent pour
dresser l'histogramme des fréquences
