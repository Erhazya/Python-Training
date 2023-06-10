import json
import os
import logging

# Configuration du module logging pour afficher les messages de niveau DEBUG
logging.basicConfig(level=logging.DEBUG)


def get_movies():
    """
    Récupère la liste des films à partir du fichier JSON et retourne une liste d'objets Movie correspondants.

    Returns:
        list[Movie]: Une liste d'objets Movie représentant les films.
    """
    with open(Movie.DIR_DATA, "r") as f:
        content = json.load(f)

    movies = [Movie(movie_title) for movie_title in content]

    return movies


class Movie:
    DIR_DATA = os.path.join(os.path.dirname(__file__), 'data', 'movie.json')

    # Si le fichier de données n'existe pas, crée un fichier JSON vide
    if not os.path.exists(DIR_DATA):
        with open(DIR_DATA, "w") as f:
            json.dump([], f)

    def __init__(self, movie_name: str):
        self.movie_name = movie_name.title()

    def __str__(self) -> str:
        return self.movie_name

    def _get_movies(self):
        """
        Récupère la liste des films à partir du fichier JSON.

        Returns:
            list: La liste des films.
        """
        try:
            with open(self.DIR_DATA, "r") as f:
                return json.load(f)
        except json.decoder.JSONDecodeError:
            pass

    def _write_movies(self, content=None):
        """
        Écrit la liste des films dans le fichier JSON.

        Args:
            content (list): La liste des films.
        """
        if content is None:
            content = []
        with open(self.DIR_DATA, "w") as f:
            json.dump(content, f, indent=4, ensure_ascii=False)

    def add_movies(self):
        """
        Ajoute le film à la liste des films.

        Si le film est déjà dans la liste, affiche un avertissement.
        """
        contenu = self._get_movies()

        if self.movie_name not in contenu:
            contenu.append(self.movie_name)
            self._write_movies(contenu)
            return True
        else:
            logging.warning("Le film est déjà dans la liste")
            return False

    def remove_from_movies(self):
        """
        Supprime le film de la liste des films.

        Si le film n'est pas dans la liste, affiche un avertissement.
        """
        content = self._get_movies()

        if self.movie_name in content:
            content.remove(self.movie_name)
        else:
            logging.warning("Le film n'est pas dans la liste")

        self._write_movies(content)


if __name__ == "__main__":
    pass
