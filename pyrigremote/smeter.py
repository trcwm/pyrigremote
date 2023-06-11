# Copyright 2023 - 2023, Niels Moseley and the pyrigremote contributors
# SPDX-License-Identifier: GPL-3.0-only

from PySide6.QtCore import Qt
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class SMeter(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setMinimumHeight(24)
        self.value = 128

    def setValue(self, v : int):
        self.value = min(max(v, 0), 255)
        self.update()

    def paintEvent(self, paintEvent : QPaintEvent):
        painter = QPainter(self)

        rrect = self.rect()
        rrect.adjust(0,0,-1,-1)

        x = (self.width()-2)/255.0 * float(self.value)

        pal = QPalette()
        bkcolor = pal.window().color()

        painter.setPen(QColor("black"))
        painter.setBrush(bkcolor)
        painter.drawRect(rrect)

        rrect.adjust(1,1,0,0)
        rrect.setRight(x)
        painter.fillRect(rrect, QColor("lightgreen"))
