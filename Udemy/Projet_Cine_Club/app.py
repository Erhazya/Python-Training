from movie import get_movies
from PySide6 import QtWidgets
from movie import Movie


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setFixedSize(500, 400)
        self.setup_ui()
        self.set_default_movie()
        self.setup_connections()

    def setup_ui(self):
        """
        Configure l'interface utilisateur de l'application.
        """
        self.layout = QtWidgets.QVBoxLayout(self)

        self.spn_movieBox = QtWidgets.QLineEdit()
        self.btn_button_add_movie = QtWidgets.QPushButton("Ajoutez un film")
        self.wlist_movie_show = QtWidgets.QListWidget()
        self.wlist_movie_show.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_button_remove_movie = QtWidgets.QPushButton("Supprimer un film")

        # Ajoute les widgets au layout vertical
        self.layout.addWidget(self.spn_movieBox)
        self.layout.addWidget(self.btn_button_add_movie)
        self.layout.addWidget(self.wlist_movie_show)
        self.layout.addWidget(self.btn_button_remove_movie)

    def set_default_movie(self):
        """
        Définit les films par défaut dans la liste de films.
        """

        movies = get_movies()

        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.movie_name)
            lw_item.movie = movie
            self.wlist_movie_show.addItem(lw_item)

    def setup_connections(self):
        """
        Configure les connexions des signaux et des slots pour les widgets de l'application.
        """
        self.btn_button_add_movie.clicked.connect(self.add_movies)
        self.btn_button_remove_movie.clicked.connect(self.remove_movies)
        self.spn_movieBox.returnPressed.connect(self.add_movies)

    def add_movies(self):
        """
        Ajoute un film à la liste de films.
        """
        movie = self.spn_movieBox.text()
        if not movie:
            return False

        movie = Movie(movie_name=movie)

        result = movie.add_movies()

        if result is True:
            lw_item = QtWidgets.QListWidgetItem(movie.movie_name)
            lw_item.movie = movie
            self.wlist_movie_show.addItem(lw_item)

        self.spn_movieBox.setText("")

    def remove_movies(self):
        """
        Supprime les films sélectionnés de la liste de films.
        """
        for selected_item in self.wlist_movie_show.selectedItems():
            movie = selected_item.movie
            movie.remove_movies()

            self.wlist_movie_show.takeItem(self.wlist_movie_show.row(selected_item))


app = QtWidgets.QApplication([])

# Crée une instance de la classe App
win = App()
win.show()

# Exécute l'application
app.exec()
