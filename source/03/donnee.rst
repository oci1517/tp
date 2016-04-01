
Calculatrice graphique
======================

Développer un programme dans TigerJython capable de dessiner le graphe de fonctions mathématiques

Spécifications
--------------

.. admonition:: Saisie de la fonction à tracer
   :class: note
   
   * Lorsque l'utilisateur appuye sur la touche :kbd:`Enter`, le programme ouvre une boîte de dialogue
     comportant un message approprié et 
     permettant de saisir sous forme de chaine de caractères une expression *Python*
     représentant la fonction :math:`f(x) = \ldots` à tracer.
     
   * La chaine ainsi reçue sera transformée en une fonction Python ``f(x : float) --> float``
     à l'aide de la fonction ``pythonify(expr) --> function`` pour être ensuite tracée
     
     ..  code-block:: python
     
         def pythonify(expr):
            return eval('lambda x: ' + expr)
            
    
     
.. admonition:: Traçage de la fonction
   :class: note
   
   * La fonction saisie sera automatiquement tracée dans un repère cartésien gradué et avec
     une grille visible.
   
   * La fonction saisie sera affichée avec une couleur X11 aléatoire différente 
     des fonctions déjà présentes dans le repère.
   
   
.. admonition:: Domaine de visualisation, zoom et repère
   :class: note
   
   * Les fonctions seront tracées dans un repère cartésien
   
   * Le domaine de visualisation par défaut sera :math:`x \in [-5; 5]` et :math:`y \in [-5; 5]`
   
   * La combinaison de touches :kbd:`Maj + haut` va zoomer sur l'axe des :math:`Oy` (diminuer l'intervalle de dessin) de 10%
   * La combinaison de touches :kbd:`Maj + bas` va dézoomer sur l'axe des :math:`Oy` (augmenter l'intervalle de dessin) de 10%
   
   * La combinaison de touches :kbd:`Ctrl + haut` va zoomer sur l'axe des :math:`Ox` (diminuer l'intervalle de dessin) de 10%
   * La combinaison de touches :kbd:`Ctrl + bas` va dézoomer sur l'axe des :math:`Ox` (augmenter l'intervalle de dessin) de 10%
   
.. tip::

   Effectuer un zoom revient à tout effacer et redessiner les fonctions dans le repère avec
   un domaine de visualisation différent.
     
.. tip::

   On peut tester si les touches Majuscule ou Ctrl sont enfoncées en même temps 
   qu'une autre touche avec la fonction ``getModifiers()``. Le programme suivant
   permet de se faire la main ...
   
   .. code-block:: python

      from gpanel import *
      makeGPanel(0, 10, 0, 10)
      
      text(1, 5, "Press any key.")
      while True:
          key = getKeyCodeWait()
          mod = getModifiers()
          print key, mod
          

.. admonition:: Gestion des fonctions affichées
   :class: note
   
   *  Maintenir à jour une liste contenant toutes les fonctions à afficher
   *  Une pression de la touche :kbd:`backspace` efface la dernière fonction saisie
      et la supprime de la liste
   *  Une pression de la touche :kbd:`delete` efface la première fonction saisie
      encore présente et la supprime de la liste
          
Étapes
------

.. todo:: à revoir

#. Créer un dépôt privé ``oci-tp-module-2`` dans voter compte bitbucket et le partager
   avec ``donnerc`` et avec votre coéquipier.
   
#. Définir une fonction ``draw_axis(xmin, xmax, ymin, ymax)`` qui se charge de dessiner
   un repère cartésien répondant aux spécifications ou retoucher la fonction ``setup``
   dans (`plot.py sur bitbucket`_)
   
#. Créer un gestionnaire d'événements pour le clavier et ouvrir une boîte de dialogue
   appropriée pour demander l'expression de la fonction à tracer. Attention à gérer
   correctement les saisies invalides des utilisateurs. 
   
      *  Saisie vide
      *  Pas une expression Python valide



#. Réutiliser le module ``plot.py`` (`plot.py sur bitbucket`_)
   développé en cours en l'adaptant aux besoins spécifiques de notre application. Charger le module
   ``plot`` pour pouvoir utiliser les fonctions du module.
   
   
#. Planifier les prochaines étapes vous-mêmessage

#. Supprimer les bouts de codes inutiles

#. Rajouter des commentaires pour éclairer les passages acrobatiques
   

   
   
.. _plot.py sur bitbucket: https://bitbucket.org/donnerc/tj_exos/src/4f6600e4f288bc19df8c68d3bddcfdd666f3561e/chapitre_03/section_04_functions_return/plot.py?at=master&fileviewer=file-view-default