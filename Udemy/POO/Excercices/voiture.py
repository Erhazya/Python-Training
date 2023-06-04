from dataclasses import dataclass
from typing import ClassVar

# Définition de la classe Voiture
class Voiture():
    essence: int = 100

    def afficher_reservoir(self):
        """
        Affiche le niveau d'essence restant dans la voiture.
        """
        print(f"La voiture contient encore {self.essence} Litres d'essence")

    def roule(self, km: int):
        """
        Simule un trajet en voiture sur une certaine distance.

        Args:
            km (int): La distance parcourue en kilomètres.
        """
        self.afficher_reservoir()

        if self.essence == 0:
            print("Vous n'avez plus d'essence, faites le plein !")
        elif self.essence <= 10:
            print("Vous n'avez bientôt plus d'essence !")
        else:
            consommation = (km * 5) / 100
            print(f"Vous avez parcouru {km} km")
            self.essence -= consommation

    def faire_le_plein(self):
        """
        Effectue le plein d'essence de la voiture.
        """
        print("Plein effectué ! Vous pouvez repartir")
        self.essence = 100


# Crée une instance de la classe Voiture
voiture_01 = Voiture()

# Appelle les méthodes de la voiture
voiture_01.roule(2000)
voiture_01.roule(10)
voiture_01.faire_le_plein()
voiture_01.roule(1990)
voiture_01.roule(2)
