#!/usr/bin/python3
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *

# https://doc.qt.io/qtforpython-6/

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyRigRemote')

        self.mainWidget = QWidget()

        self.setCentralWidget(self.mainWidget)
        self.show()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

if (__name__ == "__main__"):
    main()
