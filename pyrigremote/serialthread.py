# Copyright 2023 - 2023, Niels Moseley and the pyrigremote contributors
# SPDX-License-Identifier: GPL-3.0-only

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtSerialPort import *
from queue import *

class SerialThread(QThread):
    
    dataReady = Signal()

    def __init__(self, portname, baudrate):
        QThread.__init__(self)
        self.portname = portname
        self.baudrate = baudrate
        self.txQueue  = Queue()
        self.rxQueue  = Queue()
        
        print("Opening {:s} at {:d} baud".format(self.portname, self.baudrate))
        self.port = QSerialPort()
        self.port.setPortName(self.portname)
        self.port.setBaudRate(self.baudrate)
        result = self.port.open(QIODevice.ReadWrite)
        
        if not result:
            print("port open error")
        else:   
            print("port open ok")

    def run(self):
        print("Running...")
        self.running = True 

        while self.running:
            if self.port.waitForReadyRead(1):
                buffer = self.port.readAll()
                self.rxQueue.put(buffer.data())
                self.dataReady.emit()

            if not self.txQueue.empty():
                txdata = str(self.txQueue.get())
                self.port.write(toBytes(txdata))

            self.msleep(100)

    def strToBytes(self, s : str):
        return s.encode('latin-1')

    def bytesToStr(self, buf) -> str:
        return buf if type(buf) is str else "".join([chr(buf) for b in buf])

    def send(self, data : str):
        self.txQueue.put(data)

    def hasData(self) -> bool:
        return not self.rxQueue.empty()

    def getData(self):
        return self.rxQueue.get()
