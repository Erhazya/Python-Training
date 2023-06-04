from pathlib import Path  # Importation du module pathlib

chemin = Path("./FichierTest/prenoms.txt")  # Crée un objet Path représentant le chemin du fichier "prenoms.txt"

with open(chemin, "r") as f:  # Ouvre le fichier en mode lecture avec l'encodage UTF-8 et l'assigne à la variable 'f'
    lines = f.read().splitlines()  # Lit toutes les lignes du fichier et les stocke dans la liste 'lines'

prenoms = []
for line in lines:
    prenoms.extend(line.split())  # Divise chaque ligne en mots et les ajoute à la liste 'prenoms'

prenoms_final = [prenom.strip(",. ") for prenom in prenoms]  # Supprime les caractères de ponctuation et d'espacement superflu autour de chaque prénom

print(prenoms_final)
# Le fichier "prenoms.txt" est ouvert en mode lecture pour lire son contenu.
# Les lignes sont lues, divisées en mots et stockées dans la liste 'prenoms'.
# Ensuite, les prénoms sont nettoyés en supprimant les caractères de ponctuation et d'espacement superflu autour de chaque prénom.
# Les prénoms nettoyés sont triés et écrits dans le fichier, chaque prénom sur une nouvelle ligne.

# Assurez-vous que le fichier existe et que les autorisations nécessaires sont remplies pour lire et écrire dans le fichier.

