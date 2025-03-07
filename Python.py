# Saisie du nombre d’étudiants
n = int(input("Entrer le nombre d’étudiants : "))
for i in range(n):
    nom = input("Entrer le nom de l’étudiant : ")
    n_notes = int(input(f"Entrer le nombre de notes pour {nom} : "))
    
    notes = []
    for j in range(n_notes):
        note = float(input(f"Entrer la note {j + 1} : "))
        notes.append(note)
    
    etudiants[nom] = notes
