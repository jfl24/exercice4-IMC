
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
