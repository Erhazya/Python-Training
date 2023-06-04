# https://www.docstring.fr/glossaire/json/?utm_source=udemy&utm_campaign=json-glossary


import json  # Importation du module json pour travailler avec des données JSON

chemin = "./FichierTest/info.json"  # Chemin du fichier JSON à créer

with open(chemin, "w") as f:  # Ouvre le fichier en mode écriture et l'assigne à la variable 'f'
    json.dump(list(range(20)), f, indent=4)  # Écrit une liste de nombres de 0 à 19 dans le fichier JSON avec une indentation de 4 espaces

# La méthode dump() du module json permet d'écrire des données JSON dans un fichier.
# Dans ce cas, la liste range(20) contenant les nombres de 0 à 19 est écrite dans le fichier avec une indentation de 4 espaces.

with open(chemin, "r") as f:  # Ouvre le fichier en mode lecture et l'assigne à la variable 'f'
    liste = json.load(f)  # Charge les données JSON à partir du fichier et les assigne à la variable 'liste'
    print(liste)  # Affiche la liste chargée à partir du fichier
    print(type(liste))  # Affiche le type de données de la liste (en général, une liste en Python)

# La méthode load() du module json permet de charger des données JSON à partir d'un fichier.
# Dans ce cas, les données JSON du fichier sont chargées dans la variable 'liste'.
# La fonction print() est utilisée pour afficher le contenu de la liste ainsi que son type.




with open(chemin, "r") as f:  # Ouvre le fichier en mode lecture et l'assigne à la variable 'f'
    donnees = json.load(f)  # Charge les données JSON à partir du fichier et les assigne à la variable 'donnees'

donnees.append(222)  # Ajoute la valeur 222 à la liste 'donnees'
donnees.append(444)  # Ajoute la valeur 444 à la liste 'donnees'

with open(chemin, "w") as f:  # Ouvre le fichier en mode écriture et l'assigne à la variable 'f'
    json.dump(donnees, f, indent=4 , ensure_ascii=False)  # Écrit les données de la liste 'donnees' dans le fichier JSON avec une indentation de 4 espaces

# L'argument 'ensure_ascii=False' est utilisé pour assurer que les caractères non-ASCII sont correctement gérés et conservés dans le fichier JSON.
# Par défaut, ensure_ascii est True, ce qui signifie que les caractères non-ASCII sont échappés en utilisant la notation \uXXXX.
# En fixant ensure_ascii à False, les caractères non-ASCII sont directement écrits dans le fichier JSON sans être échappés.
# Les données JSON sont d'abord chargées à partir du fichier dans la variable 'donnees'.
# Ensuite, les valeurs 222 et 444 sont ajoutées à la liste 'donnees' à l'aide de la méthode append().
# Enfin, les données mises à jour de la liste 'donnees' sont réécrites dans le fichier en remplaçant le contenu existant.










