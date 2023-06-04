from dataclasses import dataclass

# Définition de la classe Voiture
class Voiture:
    def __init__(self, marque, vitesse):
        """
        Initialise une instance de la classe Voiture.

        Args:
            marque (str): La marque de la voiture.
            vitesse (int): La vitesse de la voiture.
        """
        self.marque = marque
        self.vitesse = vitesse

    @classmethod
    def porsche(cls):
        """
        Méthode de classe qui crée une instance de la classe Voiture avec la marque "Porsche" et une vitesse de 200.

        Returns:
            Voiture: Une instance de la classe Voiture avec la marque "Porsche" et une vitesse de 200.
        """
        return cls(marque="Porsche", vitesse=200)

# Crée une instance de la classe Voiture avec la marque "Lambo" et une vitesse de 250
voiture = Voiture("Lambo", 250)

# Utilise la méthode de classe porsche pour créer une instance de la classe Voiture avec la marque "Porsche" et une vitesse de 200
voiture2 = Voiture.porsche()

# Affiche la marque et la vitesse de la voiture
print(voiture.marque)
print(voiture.vitesse)
print(voiture2.marque)
print(voiture2.vitesse)

# Décorateur dataclass pour définir la classe User
@dataclass
class User:
    first_name: str
    last_name: str

    def __post_init__(self):
        """
        Méthode appelée après l'initialisation de l'instance de la classe User.
        """
        # print("Creation finie")

# Crée une instance de la classe User avec les attributs first_name="Patrick" et last_name="Lambert"
user = User(first_name="Patrick", last_name="Lambert")

# Crée une autre instance de la classe User avec les attributs first_name="Jean" et last_name="Lambert"
user2 = User(first_name="Jean", last_name="Lambert")
