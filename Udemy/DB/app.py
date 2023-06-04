import sqlite3

# Établir la connexion à la base de données SQLite
conn = sqlite3.connect("database.db")

# Créer un objet curseur pour exécuter des commandes SQL
c = conn.cursor()

# Créer la table "employees" si elle n'existe pas déjà
c.execute("""
CREATE TABLE IF NOT EXISTS employees(
    prenom TEXT,
    nom TEXT,
    salaire INT
)
""")

# Dictionnaire avec les valeurs à insérer ou à mettre à jour
d = {"salaire": 4000, "prenom": "Mirabelle", "nom": "Bert"}

# Insérer ou mettre à jour une ligne dans la table "employees" avec les valeurs du dictionnaire
#c.execute("INSERT INTO employees VALUES (:prenom, :nom, :salaire)", d)

c.execute("""UPDATE employees SET salaire=:salaire WHERE prenom=:prenom and nom=:nom""", d)

# Sélectionner toutes les lignes de la table "employees"
c.execute("SELECT * FROM employees")
# Récupérer la première ligne de résultat
info = c.fetchone()
print(info)
# Récupérer la deuxième ligne de résultat
info = c.fetchone()
print(info)
# Récupérer la troisième ligne de résultat
info = c.fetchone()
print(info)

# Supprimer une ligne de la table "employees" où le prénom est "Paul"
c.execute("DELETE FROM employees WHERE prenom='Paul'")

# Valider les modifications dans la base de données
conn.commit()

# Fermer la connexion à la base de données
conn.close()
