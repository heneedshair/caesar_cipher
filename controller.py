from PyQt6.QtWidgets import QFileDialog, QColorDialog, QMessageBox
from model import CaesarCipherModel
from view import CaesarCipherView
from settings_dialog import CipherSettingsDialog

class CaesarCipherController:
    def __init__(self, view: CaesarCipherView, model: CaesarCipherModel):
        self.view = view
        self.model = model
        self.background_color = None
        self._connect_signals()
        self.view.cipherDisk.set_shift(self.model.shift)

    def _connect_signals(self):
        self.view.encryptButton.clicked.connect(self.encrypt)
        self.view.decryptButton.clicked.connect(self.decrypt)
        self.view.loadAction.triggered.connect(self.load_file)
        self.view.saveAction.triggered.connect(self.save_file)
        self.view.exitAction.triggered.connect(self.view.close)
        self.view.colorAction.triggered.connect(self.change_background_color)
        self.view.settingsAction.triggered.connect(self.open_settings_dialog)

    def _validate_input(self, text: str) -> bool:
        if not text.strip():
            QMessageBox.warning(self.view, "Ошибка", "Поле ввода не должно быть пустым.")
            return False
        return True

    def encrypt(self):
        text = self.view.inputText.toPlainText()
        if not self._validate_input(text):
            return
        result = self.model.encrypt(text)
        self.view.outputText.setText(result)

    def decrypt(self):
        text = self.view.inputText.toPlainText()
        if not self._validate_input(text):
            return
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
            self.background_color = color
            self.view.setStyleSheet(f"background-color: {color.name()};")

    def open_settings_dialog(self):
        dialog = CipherSettingsDialog(
            current_shift=self.model.shift,
            current_direction=self.model.direction,
            background_color=self.background_color
        )
        if self.background_color:
            dialog.setStyleSheet(f"background-color: {self.background_color.name()};")
        if dialog.exec():
            shift, direction = dialog.get_settings()
            self.model.set_parameters(shift, direction)
            self.view.cipherDisk.set_shift(shift)
