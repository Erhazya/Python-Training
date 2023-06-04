from PySide6 import QtWidgets
import currency_converter

# Définition de la classe App qui hérite de QtWidgets.QWidget
class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Convertisseur de devises")
        self.devise = currency_converter.CurrencyConverter()
        self.setFixedSize(800, 100)
        self.setup_ui()
        self.set_default_values()
        self.setup_connections()
        self.setup_css()

    def setup_ui(self):
        """
        Configure l'interface utilisateur de l'application.
        """
        self.layout = QtWidgets.QHBoxLayout(self)
        self.cbb_deviseFrom = QtWidgets.QComboBox()
        self.spn_montant = QtWidgets.QDoubleSpinBox()
        self.cbb_deviseTo = QtWidgets.QComboBox()
        self.spn_montantconverti = QtWidgets.QDoubleSpinBox()
        self.btn_inverser = QtWidgets.QPushButton("Inverser la devise")

        # Ajoute les widgets au layout horizontal
        self.layout.addWidget(self.cbb_deviseFrom)
        self.layout.addWidget(self.spn_montant)
        self.layout.addWidget(self.cbb_deviseTo)
        self.layout.addWidget(self.spn_montantconverti)
        self.layout.addWidget(self.btn_inverser)

    def set_default_values(self):
        """
        Définit les valeurs par défaut pour les widgets de l'application.
        """
        # Ajoute les devises disponibles à la ComboBox cbb_deviseFrom
        self.cbb_deviseFrom.addItems(sorted(self.devise.currencies))
        # Définit la devise par défaut à "EUR"
        self.cbb_deviseFrom.setCurrentText("EUR")

        # Ajoute les devises disponibles à la ComboBox cbb_deviseTo
        self.cbb_deviseTo.addItems(sorted(self.devise.currencies))
        # Définit la devise par défaut à "USD"
        self.cbb_deviseTo.setCurrentText("USD")

        # Définit les limites de la plage de valeurs pour les SpinBox spn_montant et spn_montantconverti
        self.spn_montant.setRange(1, 1000000)
        self.spn_montantconverti.setRange(1, 1000000)

        # Définit les valeurs par défaut pour les SpinBox spn_montant et spn_montantconverti
        self.spn_montant.setValue(100)
        self.spn_montantconverti.setValue(100)

    def setup_connections(self):
        """
        Configure les connexions des signaux et des slots pour les widgets de l'application.
        """
        self.cbb_deviseFrom.activated.connect(self.compute)
        self.cbb_deviseTo.activated.connect(self.compute)
        self.spn_montant.valueChanged.connect(self.compute)
        self.btn_inverser.clicked.connect(self.inverser_devise)

    def compute(self):
        """
        Effectue le calcul de conversion de devise en fonction des valeurs sélectionnées et mises à jour les résultats.
        """
        montant = self.spn_montant.value()
        devise_from = self.cbb_deviseFrom.currentText()
        devise_to = self.cbb_deviseTo.currentText()

        try:
            resultat = self.devise.convert(montant, devise_from, devise_to)
        except currency_converter.currency_converter.RateNotFoundError:
            pass
        else:
            self.spn_montantconverti.setValue(resultat)

    def inverser_devise(self):
        """
        Inverse les devises sélectionnées et effectue le calcul de conversion.
        """
        devise_from = self.cbb_deviseFrom.currentText()
        devise_to = self.cbb_deviseTo.currentText()

        self.cbb_deviseFrom.setCurrentText(devise_to)
        self.cbb_deviseTo.setCurrentText(devise_from)
        self.compute()

    def setup_css(self):
        """
        Configure les styles CSS pour l'application.
        """
        self.setStyleSheet("""
            background-color: black;
            color: white;
            border: none;
        """)
        
        self.btn_inverser.setStyleSheet("background-color: red")

app = QtWidgets.QApplication([])

# Crée une instance de la classe App
win = App()
win.show()

# Exécute l'application
app.exec()
