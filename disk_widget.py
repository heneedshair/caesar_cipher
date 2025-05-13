from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QFont
from PyQt6.QtCore import QPointF
import math

class CipherDiskWidget(QWidget):
    def __init__(self, shift=0):
        super().__init__()
        self.setMinimumSize(300, 300)
        self.shift = shift

    def set_shift(self, shift):
        self.shift = shift % 26
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setRenderHint(QPainter.RenderHint.Antialiasing)

        center = QPointF(self.width() / 2, self.height() / 2)
        outer_radius = min(self.width(), self.height()) // 2 - 20
        inner_radius = outer_radius - 40

        font = QFont('Arial', 12)
        qp.setFont(font)

        # Внешний круг (A-Z)
        for i in range(26):
            angle_deg = i * 360 / 26
            angle_rad = math.radians(angle_deg)
            x = center.x() + outer_radius * math.cos(angle_rad)
            y = center.y() + outer_radius * math.sin(angle_rad)
            qp.drawText(int(x - 8), int(y + 5), chr(65 + i))  # A-Z

        # Внутренний круг (со сдвигом)
        for i in range(26):
            angle_deg = i * 360 / 26
            angle_rad = math.radians(angle_deg)
            shifted = (i + self.shift) % 26
            x = center.x() + inner_radius * math.cos(angle_rad)
            y = center.y() + inner_radius * math.sin(angle_rad)
            qp.drawText(int(x - 8), int(y + 5), chr(65 + shifted))  # A-Z со сдвигом
