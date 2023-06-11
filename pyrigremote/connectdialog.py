
from PySide6.QtWidgets import *
from PySide6.QtSerialPort import *

class ConnectDialog(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Connect to serial port")
        
        self.layout = QVBoxLayout()

        self.gridLayout = QGridLayout()

        # Serial port combo box
        serialPortInfos = QSerialPortInfo.availablePorts()
        self.portCombo = QComboBox()
        for portInfo in serialPortInfos:
            self.portCombo.addItem(portInfo.portName())

        self.gridLayout.addWidget(QLabel("Serial port:"), 0,0)
        self.gridLayout.addWidget(self.portCombo, 0,1)

        # Baud rate combo box
        self.rateCombo = QComboBox()
        self.rateCombo.addItems(["1200", "2400", "4800", "9600", "19200", "38400", "57600", "115200"])

        self.gridLayout.addWidget(QLabel("Baud rate:"), 1,0)
        self.gridLayout.addWidget(self.rateCombo, 1,1)

        # Dialog button box
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        
        # add everything to the layout
        self.layout.addLayout(self.gridLayout)
        self.layout.addWidget(self.buttonBox)

        self.setLayout(self.layout)
