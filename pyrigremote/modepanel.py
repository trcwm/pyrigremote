# Copyright 2023 - 2023, Niels Moseley and the pyrigremote contributors
# SPDX-License-Identifier: GPL-3.0-only

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class ModePanel(QWidget):

    muteToggled  = Signal(bool)
    stuffChanged = Signal((int,))

    def __init__(self, parent=None):
        super().__init__(parent)

        self.createWidget()

    def createWidget(self):
        self.mainLayout = QVBoxLayout()

        box = QGroupBox("Setup")
        boxLayout = QGridLayout()
        box.setLayout(boxLayout)

        ## MODE
        self.modeCombo = QComboBox()
        self.modeCombo.addItems(["CW", "LSB", "USB", "AM", "NBFM"])
        self.modeCombo.activated.connect(self.stuffChanged)
        boxLayout.addWidget(QLabel("Mode:"), 1, 0)
        boxLayout.addWidget(self.modeCombo, 1, 1)
        
        ## AGC
        self.agcCombo = QComboBox()
        self.agcCombo.addItems(["OFF", "SLOW", "FAST"])
        self.agcCombo.activated.connect(self.stuffChanged)
        boxLayout.addWidget(QLabel("AGC:"), 2, 0)
        boxLayout.addWidget(self.agcCombo, 2, 1)

        ## VOLUME
        boxLayout.addWidget(QLabel("Volume:"), 3, 0)

        self.volume = QSlider()
        self.volume.setOrientation(Qt.Orientation.Horizontal)
        self.volume.valueChanged.connect(self.stuffChanged)

        boxLayout.addWidget(self.volume, 3, 1)

        self.muteButton = QPushButton("Mute")
        self.muteButton.setCheckable(True)
        self.muteButton.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.muteButton.toggled.connect(self.muteToggled)
        boxLayout.addWidget(self.muteButton, 3, 2)
        
        self.mainLayout.addWidget(box)
        self.setLayout(self.mainLayout)

    def getVolume(self) -> int:
        return self.volume.value()

    def setVolume(self, volume : int):
        self.volume.setValue(volume)

    def getMode(self) -> str:
        return self.modeCombo.currentText()

    def getAGC(self) -> str:
        return self.agcCombo.currentText()

