#!/usr/bin/python3
# Copyright 2023 - 2023, Niels Moseley and the pyrigremote contributors
# SPDX-License-Identifier: GPL-3.0-only

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *

# https://doc.qt.io/qtforpython-6/

from connectdialog import *

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

        self.setCentralWidget(self.mainWidget)
        self.show()

    def onConnect(self):
        connectDialog = ConnectDialog(self)
        if (connectDialog.exec()):
            print("Port name: ", connectDialog.getPortName())
            print("Baud rate: ", connectDialog.getBaudRate())
        else:
            print("Fail!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

if (__name__ == "__main__"):
    main()
