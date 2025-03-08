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
