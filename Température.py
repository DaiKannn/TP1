import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QLabel, QGridLayout, QComboBox, QMessageBox
from PyQt5.QtCore import QCoreApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)

        temp = QLabel("Température")
        unite = QLabel("°C")
        self.__text = QLineEdit("")
        conv = QPushButton("Convertir")
        choix = QComboBox()
        choix.addItem("°C->K")
        choix.addItem("K->°C")
        aide = QPushButton("?")
        conv2 = QLabel("Conversion")
        self.__text2 = QLineEdit("")
        unite2 = QLabel("K")

# Ajouter les composants au grid ayout

        grid.addWidget(temp, 0, 0)
        grid.addWidget(unite,0,2)
        grid.addWidget(self.__text, 0, 1)
        grid.addWidget(conv, 1, 1)
        grid.addWidget(choix, 1,2)
        grid.addWidget(conv2,2,0)
        grid.addWidget(self.__text2, 2, 1)
        grid.addWidget(unite2,2,2)
        grid.addWidget(aide, 3, 3)

        conv.clicked.connect(self._actionConv)
        # choix.currentTextChanged().connect(self._actionChoix)
        aide.clicked.connect(self._actionAide)

        self.setWindowTitle("Une première fenêtre")

    def _actionConv(self):
        self.__text2.setText(f" {int(self.__text.text())+273.15}")

    def _actionAide(self):
        msgBox = QMessageBox()
        msgBox.setText("Permet de convertir un nombre soit de Kelvin vers Celius, soit de Celcius vers Kelvin.")
        msgBox.setWindowTitle("Aide")
        marche = msgBox.exec()

    # def _actionChoix(self):










if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()