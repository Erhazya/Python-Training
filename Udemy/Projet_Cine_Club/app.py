from movie import get_movies
from PySide6 import QtWidgets
from PySide6 import QtCore

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setFixedSize(500, 400)
        self.setup_ui()
        self.set_default_movie()



        
        """ self.set_default_values()
        self.setup_connections()
        self.setup_css()"""


    def setup_ui(self):
        """
        Configure l'interface utilisateur de l'application.
        """
        self.layout = QtWidgets.QVBoxLayout(self)



        self.spn_movieBox = QtWidgets.QLineEdit()
        self.btn_button_add_movie = QtWidgets.QPushButton("Ajoutez un film")
        self.wlist_movie_show = QtWidgets.QListWidget()
        self.btn_button_remove_movie = QtWidgets.QPushButton("Supprimer un Film")

        
        # Ajoute les widgets au layout horizontal
        self.layout.addWidget(self.spn_movieBox)
        self.layout.addWidget(self.btn_button_add_movie)
        self.layout.addWidget(self.wlist_movie_show)
        self.layout.addWidget(self.btn_button_remove_movie)


    def set_default_movie(self):

        movies = get_movies()
    
        for movie in movies :
            lw_item = QtWidgets.QListWidgetItem(movie.movie_name)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.wlist_movie_show.addItem(lw_item)


    
   




app = QtWidgets.QApplication([])

# Crée une instance de la classe App
win = App()
win.show()

# Exécute l'application
app.exec()
