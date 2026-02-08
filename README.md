# Calcul de l’enveloppe convexe — Algorithme de Graham

Ce programme est l’un de mes **premiers projets d’algorithmique géométrique**, écrit **au lycée**.  
Il met en œuvre **l’algorithme de Graham Scan**, un classique pour calculer **l’enveloppe convexe** d’un nuage de points.  
L’objectif : relier les points extérieurs d’un ensemble pour former la plus petite “coquille” les englobant tous.

---

## Description du projet

Le script :
- génère un **nuage de points aléatoires en 2D** ;
- identifie le **point le plus bas** (qui sera sur l’enveloppe) ;
- **calcule les angles** de tous les autres points par rapport à ce point de référence ;
- trie les points selon ces angles pour former une **première approximation du contour** ;
- puis **supprime les virages à droite** pour ne garder que les points formant **l’enveloppe convexe finale**.

Le tout est accompagné d’un **affichage visuel dynamique** (via `matplotlib`), permettant de suivre l’évolution de la construction pas à pas.

---

## 🧩 Technologies utilisées

- **Python 3**
- **Matplotlib** — pour afficher les points et les segments
- **NumPy** — pour manipuler efficacement les coordonnées
- **math** — pour les calculs d’angles et d’orientations
- **random** — pour générer le nuage de points

---

## Principe de l’algorithme de Graham

1. Trouver le **point le plus bas** du nuage (s’il y en a plusieurs, choisir celui le plus à gauche).  
2. Calculer l’**angle polaire** de chaque autre point par rapport à ce point de référence.  
3. **Trier les points** par angle croissant.  
4. Parcourir la liste triée et **supprimer tout point qui ferait tourner le contour “vers la droite”**.  
5. Les points restants forment **l’enveloppe convexe**.

 Complexité en temps :  
> O(n) + O(n × log n) + O(n) = **O(n × log n)**

---

##  Points faibles (liés à l’époque de création)

Comme il s’agit d’un projet de collège :
- L’algorithme est **fonctionnel mais peu structuré**.
- Il n’y a **aucune gestion d’erreurs** ni de modularisation.
- Le **code est monolithique**, sans classes ni fonctions réutilisables.
- Les visuels sont affichés à chaque itération, ce qui **ralentit beaucoup** l’exécution.
- La gestion des angles et des doublons pourrait être simplifiée avec des bibliothèques modernes.

---

##  Pistes d’amélioration

Aujourd’hui, je pourrais améliorer le projet en :
- Découpant le code en fonctions et classes claires (`Point`, `GrahamScan`, etc.)
- Ajoutant une option pour **désactiver l’affichage interactif** (plus rapide sur grands ensembles).
- Permettant de **charger un nuage de points depuis un fichier**.
- Comparant la performance avec d’autres algorithmes (Jarvis, QuickHull…).
- Nettoyant le code pour suivre les standards PEP8.
- Ajoutant un **affichage final coloré** distinguant l’enveloppe et les points internes.

---

##  Conclusion

Ce projet m’a permis de découvrir :
- la **géométrie algorithmique** (angles, orientation, enveloppes convexes),
- la **visualisation de données**,
- et surtout la satisfaction de **voir un algorithme “prendre vie”** à travers un graphe animé.

Même s’il est rudimentaire, ce code marque une étape importante dans ma progression en programmation.

---

👨‍💻 *Projet d’apprentissage — réalisé au collège pour explorer la géométrie computationnelle et la visualisation algorithmique.*
