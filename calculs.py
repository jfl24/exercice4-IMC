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





