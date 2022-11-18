import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QLabel, QGridLayout
from PyQt5.QtCore import QCoreApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)

        lab = QLabel("Saisir votre nom")
        text = QLineEdit("")
        ok = QPushButton("Ok")
        quit = QPushButton("Quitter")

# Ajouter les composants au grid ayout

        grid.addWidget(lab, 0, 0)
        grid.addWidget(text, 0, 1)
        grid.addWidget(ok, 1, 0)
        grid.addWidget(quit, 1, 1)

        ok.clicked.connect(self._actionOk)
        quit.clicked.connect(self._actionQuitter)

        self.setWindowTitle("Une première fenêtre")

    def _actionOk(self):
        self.text()

    def _actionQuitter(self):
        QCoreApplication.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()