import faker
import logging
from pathlib import Path
from datetime import date, time , datetime



def get_time():

    return str(datetime.now())
    

# Récupère le répertoire de base du fichier actuel
BASE_DIR = Path(__file__).resolve().parent

# Configure le module de logging pour écrire les messages dans le fichier "user.log" dans le répertoire de base
logging.basicConfig(filename=BASE_DIR / "user.log", level=logging.DEBUG)


# Crée une instance de la classe Faker avec la localisation "fr_FR"
fake = faker.Faker(locale="fr_FR")

def get_user(nb_user: int = 1):
    """
    Génère une liste de noms d'utilisateurs.

    Args:
        nb_user (int): Le nombre d'utilisateurs à générer. Par défaut, un seul utilisateur est généré.

    Returns:
        list[str]: Une liste contenant les noms d'utilisateurs générés.
    """
    liste_user = []

    for _ in range(nb_user):

        logging.info(get_time() +" Genere user " + str(_+1))

        # Génère un prénom aléatoire
        first_name = fake.first_name()
        # Génère un nom de famille aléatoire
        last_name = fake.last_name()
        # Ajoute le prénom et le nom de famille à la liste des utilisateurs
        logging.info("Add user")
        liste_user.append(first_name + " " + last_name)
    
    # Retourne la liste des utilisateurs
    return liste_user, logging.info("Return user")


if __name__ == "__main__":
    # Appelle la fonction get_user avec un argument de 5 pour générer 5 utilisateurs et les affiche
    print(get_user(5))
