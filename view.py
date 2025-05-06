from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QTextEdit, QFileDialog, QColorDialog, QMenuBar, QMenu,
    QLabel
)
from PyQt6.QtGui import QAction

class CaesarCipherView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Шифр Цезаря")

        # Текстовые поля
        self.inputText = QTextEdit()
        self.outputText = QTextEdit()
        self.outputText.setReadOnly(True)

        # Кнопки
        self.encryptButton = QPushButton("Зашифровать")
        self.decryptButton = QPushButton("Дешифровать")

        # Меню
        self.menuBar = QMenuBar(self)
        self.fileMenu = QMenu("Файл", self)
        self.optionsMenu = QMenu("Опции", self)

        self.loadAction = QAction("Открыть файл", self)
        self.saveAction = QAction("Сохранить в файл", self)
        self.exitAction = QAction("Выход", self)
        self.fileMenu.addActions([self.loadAction, self.saveAction, self.exitAction])

        self.settingsAction = QAction("Настройки шифра", self)
        self.colorAction = QAction("Цвет фона", self)
        self.optionsMenu.addActions([self.settingsAction, self.colorAction])

        self.menuBar.addMenu(self.fileMenu)
        self.menuBar.addMenu(self.optionsMenu)

        # Основной макет
        layout = QVBoxLayout(self)
        layout.setMenuBar(self.menuBar)
        layout.addWidget(QLabel("Обычный текст:"))
        layout.addWidget(self.inputText)
        layout.addWidget(QLabel("Результат:"))
        layout.addWidget(self.outputText)

        buttonsLayout = QHBoxLayout()
        buttonsLayout.addWidget(self.encryptButton)
        buttonsLayout.addWidget(self.decryptButton)
        layout.addLayout(buttonsLayout)
