# Copyright 2023 - 2023, Niels Moseley and the pyrigremote contributors
# SPDX-License-Identifier: GPL-3.0-only

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import resources

class DigitWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setValue(0)
        
        self.transparent = False
        self.digitSize  = self.digitImage.size()
        self.setDigitMargins(QMargins(0,0,0,0))

    def setTransparent(self, transparent : bool):
        if not(self.transparent == transparent):
            self.transparent = transparent
            self.update()

    def setDigitMargins(self, margins : QMargins):
        self.digitMargins = margins
        widgetSize = self.digitSize.grownBy(margins)        
        self.setFixedSize(widgetSize)
        
    def setValue(self, value : int):
        resourceNames = [
            ":/images/0.png",
            ":/images/1.png",
            ":/images/2.png",
            ":/images/3.png",
            ":/images/4.png",
            ":/images/5.png",
            ":/images/6.png",
            ":/images/7.png",
            ":/images/8.png",
            ":/images/9.png"
        ]

        self.digitValue = max(0, min(value, 9))
        self.digitImage = QPixmap(resourceNames[self.digitValue])
        self.update()

    def paintEvent(self, paintEvent):
        painter = QPainter(self)

        painter.fillRect(self.rect(), QColor(255,255,255))

        if self.transparent:
            painter.setOpacity(0.35)
            painter.drawPixmap(QPoint(self.digitMargins.left(), self.digitMargins.top()), self.digitImage)
            painter.setOpacity(1.0)
        else:
            painter.drawPixmap(QPoint(self.digitMargins.left(), self.digitMargins.top()), self.digitImage)

