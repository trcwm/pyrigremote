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
from serialthread import *

class MainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
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

        self.serialThread = None

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

    @Slot()
    def onConnect(self):
        connectDialog = ConnectDialog(self)
        if (connectDialog.exec()):
            if not (self.serialThread == None):
                self.serialThread.running = False
                self.serialThread.wait(500)

            self.serialThread = SerialThread(connectDialog.getPortName(), connectDialog.getBaudRate())
            self.serialThread.setParent(self)
            self.serialThread.start()
            self.serialThread.dataReady.connect(self.onSerialDataReady)
        else:
            print("Fail!")

    @Slot()
    def onFrequency1Changed(self, int):
        print("VFO1: ", self.fdisplay1.getFrequency())

    @Slot()
    def onFrequency2Changed(self, int):
        print("VFO2: ", self.fdisplay2.getFrequency())

    @Slot()
    def onModeChanged(self):
        vol  = self.modePanel.getVolume()
        mode = self.modePanel.getMode() 
        agc  = self.modePanel.getAGC()

        print(vol, mode, agc)

    @Slot()
    def onMuteChanged(self, state : bool):
        if state:
            print("MUTE")
        else:
            print("mute")

    @Slot()
    def onSerialDataReady(self):
        data = self.serialThread.getData()
        print(str(data))

    def closeEvent(self, event):
        self.serialThread.running = False
        self.serialThread.wait()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

if (__name__ == "__main__"):
    main()
