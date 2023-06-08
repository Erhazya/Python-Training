from pathlib import Path

fichier01 = Path("././FichierTest/readme.txt")

fichier02 = Path("././FichierTest/readm.txt")

fichier03 = Path("C:/Users\Se7en\Documents\GitHub\Python-Training\FichierTest/fichier_invalide.abc")

try:
    with open(fichier01, "r") as f:
        contenu = f.read()
        print(contenu)
except:
    print("Erreur dans le chargement du fichier")

try:
    with open(fichier02, "r") as f:
        contenu = f.read()
        print(contenu)
except FileNotFoundError as e:
    print(e.filename)
    print("Fichier introuvable")

try:
    with open(fichier03, "r") as f:
        contenu = f.read()
        print(contenu)
except UnicodeDecodeError:
    print("Impossible d'ouvvrir le fichier")
