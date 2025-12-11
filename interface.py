def demander_infos():
    poids = float(input("Entrez votre poid en kg : "))
    taille = float(input("Entrez votre taille en metre : "))
    return poids, taille

def afficher_resultat(imc, categorie):
    print("\n=== Résultat IMC ===")
    print(f"Votre IMC : {imc}")
    print(f"Vous etes dans la categorie {categorie}")