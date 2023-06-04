# https://www.docstring.fr/blog/gerer-des-chemins-de-fichiers-avec-pathlib/


from pathlib import Path  # Importation du module pathlibµ
import shutil

print(Path.home())  # Affiche le chemin du répertoire de l'utilisateur courant

print(Path.cwd())  # Affiche le chemin du répertoire de travail actuel


p = Path("./FichierTest/fichier.txt")  # Crée un objet Path représentant le chemin "./FichierTest/fichier.txt"

p / "Documents" / "test.py"

new_path = p / "Documents" / "test.py"  # Concatène les chemins pour former un nouvel objet Path représentant le chemin "./FichierTest/fichier.txt/Documents/test.py"

new_path = p.joinpath("Documents", "main.py")  # Concatène les chemins pour former un nouvel objet Path représentant le chemin "./FichierTest/fichier.txt/Documents/main.py"

print(p)  # Affiche le chemin du fichier représenté par l'objet Path
print(p.name)  # Affiche le nom du fichier ("fichier.txt")

print(p.parent)  # Affiche le répertoire parent du fichier ("./FichierTest")

print(p.stem)  # Affiche le nom du fichier sans l'extension ("fichier")

print(p.suffix)  # Affiche l'extension du fichier (".txt")

print(p.suffixes)  # Affiche une liste de toutes les extensions du fichier ([".txt"])

print(p.parts)  # Affiche une liste des parties du chemin du fichier ([".", "FichierTest", "fichier.txt"])

print(p.exists())  # Vérifie si le fichier existe et renvoie True ou False en conséquence

print(p.is_dir())  # Vérifie si le chemin représente un répertoire et renvoie True ou False en conséquence

print(p.is_file())  # Vérifie si le chemin représente un fichier et renvoie True ou False en conséquence

new_path = p.parent / "DossierTest"  # Concatène le répertoire parent de p avec le répertoire "DossierTest" pour former un nouvel objet Path représentant le chemin du nouveau répertoire

new_path.mkdir()  # Crée le nouveau répertoire spécifié par new_path

new_path.mkdir(exist_ok=True)  # Crée le nouveau répertoire spécifié par new_path et ne lève pas d'erreur si le répertoire existe déjà

new_path.mkdir(parents=True)  # Crée le nouveau répertoire spécifié par new_path et crée également tous les répertoires parents nécessaires s'ils n'existent pas déjà

new_path.touch()  # Crée un nouveau fichier vide à l'emplacement spécifié par new_path

new_path.unlink()  # Supprime le fichier ou le répertoire spécifié par new_path

shutil.rmtree(new_path)  # Supprime récursivement le répertoire spécifié par new_path et tout son contenu

p = Path("./FichierTest/fichier.txt")

p.write_text("Bonjour")  # Écrit le texte "Bonjour" dans le fichier représenté par l'objet Path

text = p.read_text()  # Lit le contenu du fichier représenté par l'objet Path et le stocke dans la variable 'text'


for f in Path.home().iterdir():
    print(f.name)  # Affiche le nom de chaque élément dans le répertoire de l'utilisateur



png_files = p.glob("*.png")  # Utilise la méthode glob() de l'objet Path pour rechercher tous les fichiers avec l'extension ".png" dans le répertoire spécifié

png_files = p.rglob("*.png")  # Utilise la méthode rglob() de l'objet Path pour rechercher tous les fichiers avec l'extension ".png" dans le répertoire spécifié et ses sous-répertoires





# La méthode rglob() est utilisée sur un objet Path pour effectuer une recherche récursive de fichiers correspondant à un motif donné.
# La méthode glob() est utilisée sur un objet Path pour effectuer une recherche de fichiers correspondant à un motif donné.
# Utilisation de Path.home() pour obtenir le chemin du répertoire de l'utilisateur courant
# La méthode iterdir() est utilisée sur un objet Path pour obtenir un itérable des chemins des éléments (fichiers, répertoires, etc.) dans ce répertoire.
# Dans ce cas, on itère sur ces chemins à l'aide d'une boucle for et on affiche le nom de chaque élément en utilisant l'attribut name.
# L'instruction p.write_text() est utilisée pour écrire du texte dans un fichier.
# Dans ce cas, le texte "Bonjour" est écrit dans le fichier représenté par l'objet Path.
# L'instruction p.read_text() est utilisée pour lire le contenu d'un fichier comme une chaîne de caractères.
# Le contenu du fichier représenté par l'objet Path est lu et stocké dans la variable 'text'.
# L'instruction shutil.rmtree() est utilisée pour supprimer récursivement un répertoire et tous ses sous-répertoires ainsi que leurs fichiers.
# Le répertoire spécifié par new_path et tout son contenu sont supprimés.
# L'instruction new_path.touch() crée un nouveau fichier vide à l'emplacement spécifié par new_path.
# Si le fichier existe déjà, il est simplement mis à jour avec une date et une heure de modification actuelles.
# L'instruction new_path.unlink() supprime le fichier ou le répertoire spécifié par new_path.
# Pour les répertoires, ils doivent être vides pour pouvoir être supprimés.
# L'instruction new_path.mkdir() crée un nouveau répertoire à l'emplacement spécifié par new_path.
# new_path est formé en concaténant le répertoire parent de p avec le répertoire "DossierTest" à l'aide de l'opérateur / de l'objet Path.
# L'argument exist_ok=True permet de ne pas lever d'erreur si le répertoire existe déjà.
# L'argument parents=True permet de créer tous les répertoires parents nécessaires dans la hiérarchie du chemin s'ils n'existent pas déjà.
# Cela garantit que tous les répertoires parents nécessaires sont créés, le cas échéant.

# Chaque instruction utilise des méthodes ou attributs de l'objet Path pour obtenir des informations sur le chemin du fichier.
# - name renvoie le nom du fichier (incluant l'extension)
# - parent renvoie le répertoire parent du fichier
# - stem renvoie le nom du fichier sans l'extension
# - suffix renvoie l'extension du fichier
# - suffixes renvoie une liste de toutes les extensions du fichier
# - parts renvoie une liste des parties du chemin du fichier
# - exists vérifie si le fichier existe
# - is_dir vérifie si le chemin représente un répertoire
# - is_file vérifie si le chemin représente un fichier

# La méthode joinpath() est utilisée pour concaténer des chemins dans l'objet Path.
# Dans ce cas, on utilise joinpath() sur l'objet p pour concaténer les répertoires "Documents" et le fichier "main.py".
# En créant un objet Path avec le chemin "./FichierTest/fichier.txt", on peut représenter le chemin du fichier.
# En utilisant l'attribut parent de l'objet Path, on accède au répertoire parent du fichier et on l'affiche.
# La classe Path du module pathlib permet de manipuler les chemins de fichiers et de répertoires de manière portable.








