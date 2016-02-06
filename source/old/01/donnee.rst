
Exponentiation rapide
#####################

Informations
============

*  Délai : mardi 16 février
*  Durée estimée par groupes : 8 heures (4 heures par étudiant)
*  À rendre : dépôt bitbucket du travail pratique

Composition des groupes
-----------------------

* Équipe 1 : Quentin et Aleandro
* Équipe 2 : Samuel et Lucien
* Équipe 3 : Maxime et Bruno


Préparation
===========

.. todo:: 

   Retoucher les instructions de préparation

* Créer un workspace public de type *Python* dans votre compte https://c9.io
* Cloner le dépôt ... qui présente la structure ... 

.. tip::

   Les fichiers pour ce problème se trouvent dans le dossier ``01``
   
   ::
   
      ├── 01
      │   ├── a_list.txt
      │   ├── generate.py
      │   ├── n_list.txt
      │   └── power.py

Le programme :file:`compute.py` charge deux listes de nombres à partir des 
fichiers :file:`a_list.txt` et :file:`n_list.txt`


.. code-block:: python

   # liste de bases
   a_list = [...]
   # listes d'exposants
   n_list = [...]
   

.. admonition:: Consignes
   :class: warning

   *  Développer la fonction ``job()`` pour qu'elle crée une liste ``result``
      dont les éléments sont de la forme

      :: 

         power(a_list[i], n_list[i]) > 1000

   *  Votre fonction ``job()`` doit passer les tests définis dans le fichier :file:`test.py`. Pour passer les tests, la fonction doit notamment s'exécuter en moins de ... secondes 
      
   *  Développer une fonction ``count`` qui compte le nombre d'éléments de ``results`` qui sont compris entre 0.2 et 0.4.


