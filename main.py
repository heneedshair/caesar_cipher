import sys
from PyQt6.QtWidgets import QApplication
from model import CaesarCipherModel
from view import CaesarCipherView
from controller import CaesarCipherController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = CaesarCipherView()
    model = CaesarCipherModel()
    controller = CaesarCipherController(view, model)
    view.show()
    sys.exit(app.exec())
