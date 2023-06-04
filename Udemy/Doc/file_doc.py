chemin = "./FichierTest/fichier.txt"  # Chemin du fichier à ouvrir


#READ

with open(chemin, "r") as f:  # Ouvre le fichier en mode lecture et l'assigne à la variable 'f'
    contenu = repr(f.read())  # Lit le contenu du fichier et le représente sous forme de chaîne de caractères
    print(contenu)  # Affiche le contenu du fichier

# Le bloc 'pass' est utilisé lorsque vous n'avez pas besoin d'exécuter de code à cet endroit, mais la syntaxe Python exige une instruction. 
# Il peut être utilisé comme espace réservé ou pour indiquer une section inachevée du code.


f.seek(0)  # Déplace le curseur de lecture/écriture dans le fichier à la position de départ (offset) 0

# La méthode seek() est utilisée pour déplacer le curseur de lecture/écriture dans le fichier à une position spécifique.
# L'argument passé à seek() est l'offset (la position) vers laquelle le curseur doit être déplacé.
# Dans ce cas, seek(0) déplace le curseur au début du fichier (position 0).
# Cela signifie que les opérations de lecture/écriture ultérieures commenceront à partir du début du fichier.



# READLINES

with open(chemin, "r") as f:  # Ouvre le fichier en mode lecture et l'assigne à la variable 'f'
    contenu = f.readlines()  # Lit toutes les lignes du fichier et les stocke dans la liste 'contenu'
    print(contenu)  # Affiche le contenu du fichier (liste de lignes)

# La méthode readlines() lit toutes les lignes du fichier en conservant les caractères de fin de ligne ('\n').
# Le résultat est retourné sous forme de liste, où chaque élément de la liste correspond à une ligne du fichier.
# Chaque élément de la liste conserve les caractères de fin de ligne à la fin de la ligne, sauf pour la dernière ligne du fichier si elle ne se termine pas par un caractère de fin de ligne.






#SPLITLINES

with open(chemin, "r") as f:  # Ouvre le fichier en mode lecture et l'assigne à la variable 'f'
    contenu = f.read().splitlines()  # Lit le contenu du fichier et divise les lignes en utilisant les caractères de fin de ligne pour créer une liste de lignes
    print(contenu)  # Affiche le contenu du fichier (liste de lignes)

# La méthode read() lit tout le contenu du fichier comme une seule chaîne de caractères.
# En utilisant la méthode splitlines(), on divise cette chaîne en une liste de lignes en utilisant les caractères de fin de ligne comme séparateurs.
# La méthode splitlines() supprime les caractères de fin de ligne de chaque ligne.



#WRITE

with open(chemin, "a") as f:  # Ouvre le fichier en mode ajout (append) et l'assigne à la variable 'f'
    pass
    # f.write("Bonjour")   Écrit la chaîne de caractères "Bonjour" à la fin du fichier

# L'ouverture du fichier en mode "a" (ajout) permet d'écrire à la fin du fichier sans effacer le contenu existant.
# La méthode write() est utilisée pour écrire une chaîne de caractères dans le fichier.
# Dans ce cas, la chaîne de caractères "Bonjour" est ajoutée à la fin du fichier.
# Si le fichier n'existe pas, il sera créé.
