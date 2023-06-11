#!/usr/bin/python3
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
            print("OK")
        else:
            print("Fail!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

if (__name__ == "__main__"):
    main()
