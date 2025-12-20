def calculer_imc(poids, taille):
    imc = poids / (taille * taille)
    return imc

def interpreter_imc(imc):
    if imc >= 40.0:
        categorie = "Obésité, classe 3"
    elif imc >= 35.0:
        categorie = "Obésité, classe 2"
    elif imc >= 30.0:
        categorie = "Obésité, classe 1"
    elif imc >= 25.0:
        categorie = "Excès de poids / Surpoids"
    elif imc >= 18.5:
        categorie = "Poids normal"
    else:
        categorie = "Poids insuffisant"
    return categorie




def demander_infos():
    poids = float(input("Entrez votre poid en kg : "))
    taille = float(input("Entrez votre taille en metre : "))
    return poids, taille

def afficher_resultat(imc, categorie):
    print("\n=== Résultat IMC ===")
    print(f"Votre IMC : {imc}")
    print(f"Vous etes dans la categorie {categorie}")




import os

FICHIER_HISTORIQUE = "historique_imc.txt"

def sauvegarder_calcul(nom, imc):
    with open(FICHIER_HISTORIQUE, "a") as f:
        f.write(f"{nom} : {imc:.2f}\n")

def afficher_historique():
    if not os.path.exists(FICHIER_HISTORIQUE):
        print("Aucun calcul enregistré.")
        return

    print("=== Historique des calculs IMC ===")
    with open(FICHIER_HISTORIQUE, "r") as f:
        for ligne in f:
            print(ligne.strip())
