from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QSpinBox, QComboBox, QPushButton
)
from PyQt6.QtGui import QColor

class CipherSettingsDialog(QDialog):
    def __init__(self, current_shift=3, current_direction='вправо', background_color: QColor = None):
        super().__init__()
        self.setWindowTitle("Настройки шифра")
        self.setModal(True)

        # Применяем цвет фона, если задан
        if background_color:
            self.setStyleSheet(f"background-color: {background_color.name()};")

        self.shiftBox = QSpinBox()
        self.shiftBox.setRange(1, 25)
        self.shiftBox.setValue(current_shift)

        self.directionBox = QComboBox()
        self.directionBox.addItems(["вправо", "влево"])
        self.directionBox.setCurrentText(current_direction)

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Отмена")
        okButton.clicked.connect(self.accept)
        cancelButton.clicked.connect(self.reject)

        layout = QVBoxLayout()
        shiftLayout = QHBoxLayout()
        shiftLayout.addWidget(QLabel("Сдвиг:"))
        shiftLayout.addWidget(self.shiftBox)

        dirLayout = QHBoxLayout()
        dirLayout.addWidget(QLabel("Направление:"))
        dirLayout.addWidget(self.directionBox)

        btnLayout = QHBoxLayout()
        btnLayout.addWidget(okButton)
        btnLayout.addWidget(cancelButton)

        layout.addLayout(shiftLayout)
        layout.addLayout(dirLayout)
        layout.addLayout(btnLayout)
        self.setLayout(layout)

    def get_settings(self):
        return self.shiftBox.value(), self.directionBox.currentText()
