# Copyright 2023 - 2023, Niels Moseley and the pyrigremote contributors
# SPDX-License-Identifier: GPL-3.0-only

from digitwidget import *

class FreqDisplay(QWidget):

    frequencyChanged = Signal(int)

    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.frequency = 7000000
        self.numberOfDigits = 9
        self.createWidget()

    def setFrequency(self, frequency : int):
        self.frequency = frequency
        updateDigits()
        updateTransparency()

    def getFrequency(self) -> int:
        return self.frequency

    def createWidget(self):
        self.setContentsMargins(QMargins(0,0,0,0))
        self.mainLayout = QHBoxLayout()
        self.mainLayout.setContentsMargins(QMargins(0,0,0,0))
        self.mainLayout.setSpacing(0)

        self.digits = []
        for idx in range(0, self.numberOfDigits):
            self.digits.append(DigitWidget())

            self.digits[idx].setID(self.numberOfDigits - idx - 1)
            self.digits[idx].digitUp.connect(self.onDigitUp)
            self.digits[idx].digitDown.connect(self.onDigitDown)

            if ((idx+1) % 3) == 0:
                self.digits[idx].setDigitMargins(QMargins(10,0,10,-10))
            else:
                self.digits[idx].setDigitMargins(QMargins(10,0,0,-10))

            self.mainLayout.addWidget(self.digits[idx])

        self.updateDigits()
        self.updateTransparency()
        self.setLayout(self.mainLayout)

    def updateTransparency(self):
        transparent = True
        for d in self.digits:
            if not (d.getValue() == 0):
                transparent = False;

            d.setTransparent(transparent)

    def updateDigits(self):
        freq = self.frequency
        digitValues = []
        for idx in range(0, self.numberOfDigits):
            digitValues.append(freq % 10)
            freq = freq // 10

        idx = 0
        for digit in reversed(self.digits):
            digit.setValue(digitValues[idx])
            idx = idx + 1

    def onDigitUp(self, id : int):
        digitPower = pow(10, id)

        self.frequency = self.frequency + digitPower
        self.updateDigits()

        self.updateTransparency()
        self.frequencyChanged.emit(self.frequency)
        return

    def onDigitDown(self, id : int):
        digitPower = pow(10, id)

        self.frequency = max(self.frequency - digitPower, 0)
        self.updateDigits()

        self.updateTransparency()
        self.frequencyChanged.emit(self.frequency)
        return
