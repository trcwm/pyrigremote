#!/usr/bin/python3
# Copyright 2023 - 2023, Niels Moseley and the pyrigremote contributors
# SPDX-License-Identifier: GPL-3.0-only

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *

# https://doc.qt.io/qtforpython-6/

from connectdialog import *
from freqdisplay import *
from modepanel import *

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyRigRemote')

        self.mainWidget = QWidget()
        self.mainLayout = QGridLayout()
        self.mainWidget.setLayout(self.mainLayout)
    
        ## connect button
        self.connectButton = QPushButton("Connect")
        self.connectButton.clicked.connect(self.onConnect)
        self.mainLayout.addWidget(self.connectButton, 0,0)

        self.createVFO1()
        self.createVFO2()

        self.modePanel = ModePanel()
        self.mainLayout.addWidget(self.modePanel, 2,0, 1, 2)
        self.modePanel.stuffChanged.connect(self.onModeChanged)
        self.modePanel.muteToggled.connect(self.onMuteChanged)

        self.setCentralWidget(self.mainWidget)
        self.show()

    def createVFO1(self):
    
        vfo1box = QGroupBox("VFO 1")
        boxLayout = QVBoxLayout()
        vfo1box.setLayout(boxLayout)

        self.fdisplay1 = FreqDisplay()
        self.fdisplay1.frequencyChanged.connect(self.onFrequency1Changed)
        self.fdisplay1.setToolTip("VFO 1");

        boxLayout.addWidget(self.fdisplay1)

        self.mainLayout.addWidget(vfo1box, 1,0)
    
    def createVFO2(self):
    
        vfo2box = QGroupBox("VFO 2")
        boxLayout = QVBoxLayout()
        vfo2box.setLayout(boxLayout)

        self.fdisplay2 = FreqDisplay()
        self.fdisplay2.frequencyChanged.connect(self.onFrequency2Changed)
        self.fdisplay2.setToolTip("VFO 2");

        boxLayout.addWidget(self.fdisplay2)

        self.mainLayout.addWidget(vfo2box, 1,1)

    def onConnect(self):
        connectDialog = ConnectDialog(self)
        if (connectDialog.exec()):
            print("Port name: ", connectDialog.getPortName())
            print("Baud rate: ", connectDialog.getBaudRate())
        else:
            print("Fail!")

    def onFrequency1Changed(self, int):
        print("VFO1: ", self.fdisplay1.getFrequency())

    def onFrequency2Changed(self, int):
        print("VFO2: ", self.fdisplay2.getFrequency())

    def onModeChanged(self):
        vol  = self.modePanel.getVolume()
        mode = self.modePanel.getMode() 
        agc  = self.modePanel.getAGC()

        print(vol, mode, agc)

    def onMuteChanged(self, state : bool):
        if state:
            print("MUTE")
        else:
            print("mute")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

if (__name__ == "__main__"):
    main()
