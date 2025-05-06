from PyQt6.QtWidgets import QFileDialog, QColorDialog, QMessageBox
from model import CaesarCipherModel
from view import CaesarCipherView
from PyQt6.QtGui import QColor

class CaesarCipherController:
    def __init__(self, view: CaesarCipherView, model: CaesarCipherModel):
        self.view = view
        self.model = model
        self._connect_signals()

    def _connect_signals(self):
        self.view.encryptButton.clicked.connect(self.encrypt)
        self.view.decryptButton.clicked.connect(self.decrypt)
        self.view.loadAction.triggered.connect(self.load_file)
        self.view.saveAction.triggered.connect(self.save_file)
        self.view.exitAction.triggered.connect(self.view.close)
        self.view.colorAction.triggered.connect(self.change_background_color)

    def _validate_input(self, text: str) -> bool:
        if not text.strip():
            QMessageBox.warning(self.view, "Ошибка", "Поле ввода не должно быть пустым.")
            return False
        return True

    def encrypt(self):
        text = self.view.inputText.toPlainText()
        if not self._validate_input(text):
            return
        self.model.set_parameters(self.view.shiftBox.value(), self.view.directionBox.currentText())
        result = self.model.encrypt(text)
        self.view.outputText.setText(result)

    def decrypt(self):
        text = self.view.inputText.toPlainText()
        if not self._validate_input(text):
            return
        self.model.set_parameters(self.view.shiftBox.value(), self.view.directionBox.currentText())
        result = self.model.decrypt(text)
        self.view.outputText.setText(result)

    def load_file(self):
        path, _ = QFileDialog.getOpenFileName(self.view, "Открыть файл", "", "Text Files (*.txt)")
        if path:
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    self.view.inputText.setText(f.read())
            except Exception as e:
                QMessageBox.critical(self.view, "Ошибка", f"Не удалось открыть файл:\n{e}")

    def save_file(self):
        path, _ = QFileDialog.getSaveFileName(self.view, "Сохранить файл", "", "Text Files (*.txt)")
        if path:
            try:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(self.view.outputText.toPlainText())
            except Exception as e:
                QMessageBox.critical(self.view, "Ошибка", f"Не удалось сохранить файл:\n{e}")

    def change_background_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.view.setStyleSheet(f"background-color: {color.name()};")
