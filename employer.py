
# Demander à l'utilisateur d'entrer les noms et les salaires dans une liste
liste_personnes = []
while True:
    nom = input("Entrez un nom (ou 'fin' pour terminer) : ")
    if nom == 'fin':
        break
    salaire = int(input("Entrez le salaire correspondant : "))
    liste_personnes.append([nom, salaire])

# Vérifier si la liste est vide
if len(liste_personnes) == 0:
    print("La liste est vide.")
else:
    # Demander à l'utilisateur de saisir un nom existant dans la liste
    nom_recherche = input("Entrez un nom à rechercher : ")
    
    # Rechercher le nom dans la liste
    personne_trouvee = None
    for personne in liste_personnes:
        if personne[0] == nom_recherche:
            personne_trouvee = personne
            break
    
    # Vérifier si le nom a été trouvé
    if personne_trouvee is not None:
        nom = personne_trouvee[0]
        salaire = personne_trouvee[1]
        
        print("Nom :", nom)
        print("Salaire :", salaire)
    else:
        print("Le nom n'existe pas dans la liste.")
    
    # Calculer la personne avec le salaire le plus bas et le salaire le plus élevé
    salaires = [personne[1] for personne in liste_personnes]
    salaire_min = min(salaires)
    salaire_max = max(salaires)
    
    # Trouver les personnes avec le salaire le plus bas et le salaire le plus élevé
    personnes_salaire_min = [personne[0] for personne in liste_personnes if personne[1] == salaire_min]
    personnes_salaire_max = [personne[0] for personne in liste_personnes if personne[1] == salaire_max]
    
    print("Personne(s) avec le salaire le plus bas :", personnes_salaire_min)
    print("Personne(s) avec le salaire le plus élevé :", personnes_salaire_max)