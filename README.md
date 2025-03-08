# Devoir-Python
Voici un exemple de code python que nous proposons qui permet de calculer les moyennes des étudiants avec des explications bien détaillé sur la 
realisation du projet


Voici un README.md détaillé, intégrant des précisions sur le code Python pour le projet de calcul de moyennes :

# Projet Collaboratif : Calcul de Moyenne en Python

## Description du Projet
Ce projet a pour objectif de permettre aux étudiants d'appliquer des concepts de programmation en Python ainsi que de gestion de version avec Git et GitHub. Le programme développé doit permettre de saisir les données relatives à plusieurs étudiants, calculer leurs moyennes de notes, et afficher les résultats de manière claire.

## Fonctionnalités Principales
- Saisie du nombre d'étudiants et de leurs notes respectives.
- Calcul de la moyenne pour chaque étudiant.
- Affichage formaté des résultats.

## Instructions d’Installation et d’Exécution

### Prérequis
Avant de commencer, assurez-vous d'avoir installé Python 3.x et Git. Vous pouvez télécharger Python depuis [python.org](https://www.python.org/downloads/) et Git depuis [git-scm.com](https://git-scm.com/downloads).

### Étapes pour Cloner le Repository
1. Clonez le repository depuis GitHub :
```bash
git clone https://github.com/votre_nom_utilisateur/nom_du_repository.git

1. Accédez au répertoire du projet :

cd nom_du_repository

Exécution du Programme

Pour exécuter le programme, utilisez la commande suivante :

python calcul_moyenne.py

Extrait de Code Python

Voici le code Python développé pour le projet :

# Saisie du nombre d’étudiants
n = int(input("Entrer le nombre d’étudiants : "))

# Initialisation des données
etudiants = {}

for i in range(n):
nom = input("Entrer le nom de l’étudiant : ")
n_notes = int(input(f"Entrer le nombre de notes pour {nom} : "))

notes = []
for j in range(n_notes):
note = float(input(f"Entrer la note {j + 1} : "))
notes.append(note)

etudiants[nom] = notes

# Calcul des moyennes
moyennes = {}

for nom, notes in etudiants.items():
if len(notes) > 0:
moyenne = sum(notes) / len(notes)
else:
moyenne = 0
moyennes[nom] = moyenne

# Affichage des résultats
print("\nMoyennes des étudiants :")
for nom, moyenne in moyennes.items():
print(f"{nom} : {moyenne:.2f}")

Explication du Code

1. Saisie des Données :

- n = int(input("Entrer le nombre d’étudiants : "))

- Demande à l'utilisateur de saisir le nombre d'étudiants.

- Un dictionnaire etudiants est créé pour stocker les noms des étudiants comme clés et leurs notes comme valeurs (sous forme de listes).

- Pour chaque étudiant :

- Le nom est demandé.

- Le nombre de notes est demandé puis utilisé pour une boucle qui récupère chaque note, stockée dans une liste notes.

1. Calcul des Moyennes :

- Un deuxième dictionnaire moyennes est créé pour stocker la moyenne des notes de chaque étudiant.

- Le code calcule la moyenne à l'aide de moyenne = sum(notes) / len(notes), qui somme les notes et divise par leur nombre.

- Si un étudiant n'a pas de notes, sa moyenne est définie à 0.

1. Affichage des Résultats :

- Le programme utilise une boucle pour afficher les noms des étudiants accompagnés de leurs moyennes, formatées avec deux décimales.

Gestion des Erreurs

- Assurez-vous que le nombre d'étudiants et le nombre de notes sont des valeurs valides.

- Envisagez d'ajouter des vérifications d'entrées pour éviter les erreurs dues aux saisies invalides (ex. nombres négatifs ou non numériques).

Contributeurs

- IBINDA Marc Lévi

- NDJIMBILS DIOBA Rustin Verlin

-MIKOMBO Sephora

- ONDO ABAGHE Rooly Marvin

Commandes Git Utilisées

- git init : Pour initialiser un nouveau repository local.

- git clone <https://github.com/Lumineux7/Devoir-Python> : Pour cloner le repository à partir de GitHub.

- git add <Pyton.py> : Pour ajouter des fichiers au suivi Git.

- git commit -m "message" : Pour enregistrer les modifications avec un message explicatif.

- git branch <develop-feature> : Pour créer une nouvelle branche pour le développement.

- git checkout <main> : Pour passer à une autre branche.

- git merge <develop-feature> : Pour fusionner une branche dans la branche courante.

- git push origin <main> : Pour pousser vos modifications vers le repository distant.

Contact

Pour toute question ou suggestion, n'hésitez pas à contacter les contributeurs nommés ci-dessus.

Ce modèle de README.md est conçu pour être complet et précis. Il couvre tous les aspects importants du projet, y compris des sections sur l'exécution du code, explications détaillées du code, et des informations pertinentes sur Git. Assurez-vous de personnaliser les informations du projet, comme les contributeurs et l'URL du repository.
