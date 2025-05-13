from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QFont, QMouseEvent
from PyQt6.QtCore import QPointF, Qt
import math


class CipherDiskWidget(QWidget):
    def __init__(self, shift=0):
        super().__init__()
        self.setMinimumSize(300, 300)
        self._dragging = False
        self._last_angle = 0

        self.angle_offset = self.shift_to_angle(shift)

    def set_shift(self, shift):
        self.angle_offset = self.shift_to_angle(shift)
        self.update()

    def get_shift(self):
        return self.angle_to_shift(self.angle_offset)

    def shift_to_angle(self, shift: int) -> float:
        """Сдвиг в градусов"""
        return (shift % 26) * (360 / 26)

    def angle_to_shift(self, angle: float) -> int:
        """Градусы в сдвиг"""
        angle = angle % 360
        return int(round(angle / (360 / 26))) % 26

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setRenderHint(QPainter.RenderHint.Antialiasing)

        center = QPointF(self.width() / 2, self.height() / 2)
        outer_radius = min(self.width(), self.height()) // 2 - 20
        inner_radius = outer_radius - 40

        font = QFont('Arial', 12)
        qp.setFont(font)

        # Внешний круг (неподвижный)
        for i in range(26):
            angle_deg = i * 360 / 26
            angle_rad = math.radians(angle_deg)
            x = center.x() + outer_radius * math.cos(angle_rad)
            y = center.y() + outer_radius * math.sin(angle_rad)
            qp.drawText(int(x - 8), int(y + 5), chr(65 + i))

        # Внутренний круг (вращающийся)
        for i in range(26):
            angle_deg = i * 360 / 26 + self.angle_offset
            angle_rad = math.radians(angle_deg)
            x = center.x() + inner_radius * math.cos(angle_rad)
            y = center.y() + inner_radius * math.sin(angle_rad)
            qp.drawText(int(x - 8), int(y + 5), chr(65 + i))

    def mousePressEvent(self, event: QMouseEvent):
        self._dragging = True
        self._last_angle = self._calculate_angle(event.pos())

    def mouseMoveEvent(self, event: QMouseEvent):
        if not self._dragging:
            return

        current_angle = self._calculate_angle(event.pos())
        delta_angle = current_angle - self._last_angle
        self.angle_offset += delta_angle
        self._last_angle = current_angle
        self.update()

    def mouseReleaseEvent(self, event: QMouseEvent):
        self._dragging = False
        # Округляем угол до ближайшего сдвига
        self.angle_offset = self.shift_to_angle(self.get_shift())
        self.update()

    def _calculate_angle(self, pos):
        """Вычислить угол от центра до точки"""
        center = QPointF(self.width() / 2, self.height() / 2)
        dx = pos.x() - center.x()
        dy = pos.y() - center.y()
        angle = math.degrees(math.atan2(dy, dx))
        return angle
