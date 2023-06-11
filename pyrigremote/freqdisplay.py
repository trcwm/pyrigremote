# Copyright 2023 - 2023, Niels Moseley and the pyrigremote contributors
# SPDX-License-Identifier: GPL-3.0-only

from digitwidget import *

class FreqDisplay(QWidget):

    frequencyChanged = Signal(int)

    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.numberOfDigits = 9
        self.createWidget()

    def getFrequency(self) -> int:
        freq = int(0)

        # digits are ordered from high to low
        for d in self.digits:
            freq = freq * 10
            freq = freq + d.getValue()

        return freq

    def createWidget(self):
        self.setContentsMargins(QMargins(0,0,0,0))
        self.mainLayout = QHBoxLayout()
        self.mainLayout.setContentsMargins(QMargins(0,0,0,0))
        self.mainLayout.setSpacing(0)

        self.digits = []
        for idx in range(0, self.numberOfDigits):
            self.digits.append(DigitWidget())

            self.digits[idx].setID(self.numberOfDigits - idx - 1)
            self.digits[idx].digitChanged.connect(self.onDigitChanged)
            if ((idx+1) % 3) == 0:
                self.digits[idx].setDigitMargins(QMargins(10,0,10,-10))
            else:
                self.digits[idx].setDigitMargins(QMargins(10,0,0,-10))

            self.mainLayout.addWidget(self.digits[idx])

        self.setLayout(self.mainLayout)


    def onDigitChanged(self, id : int):
        self.frequencyChanged.emit(0)
        return
