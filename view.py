from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QTextEdit, QMenuBar, QMenu,
    QLabel
)
from PyQt6.QtGui import QAction

from disk_widget import CipherDiskWidget


class CaesarCipherView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Шифр Цезаря")

        # Меню
        self.menuBar = QMenuBar()
        self.fileMenu = QMenu("Файл")
        self.optionsMenu = QMenu("Опции")

        self.loadAction = QAction("Открыть")
        self.saveAction = QAction("Сохранить")
        self.exitAction = QAction("Выход")
        self.fileMenu.addAction(self.loadAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)

        self.settingsAction = QAction("Настройки шифра")
        self.colorAction = QAction("Цвет фона")
        self.optionsMenu.addAction(self.settingsAction)
        self.optionsMenu.addAction(self.colorAction)

        self.menuBar.addMenu(self.fileMenu)
        self.menuBar.addMenu(self.optionsMenu)

        # Основные элементы
        self.inputText = QTextEdit()
        self.outputText = QTextEdit()
        self.outputText.setReadOnly(True)
        self.encryptButton = QPushButton("Зашифровать")
        self.decryptButton = QPushButton("Дешифровать")

        self.cipherDisk = CipherDiskWidget()  # 👈 Добавляем круг

        # Макеты
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.encryptButton)
        buttonLayout.addWidget(self.decryptButton)

        layout = QVBoxLayout()
        layout.setMenuBar(self.menuBar)
        layout.addWidget(self.inputText)
        layout.addWidget(self.outputText)
        layout.addLayout(buttonLayout)
        layout.addWidget(self.cipherDisk)

        self.setLayout(layout)