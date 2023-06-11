# Copyright 2023 - 2023, Niels Moseley and the pyrigremote contributors
# SPDX-License-Identifier: GPL-3.0-only

from PySide6.QtCore import Qt
from PySide6.QtWidgets import *

class ToolBar(QToolBar):
    def __init__(self, parent):
        super(ToolBar, self).__init__(parent)

        self.connectButton = QPushButton('Connect')
        self.refreshButton = QPushButton('Refresh')
        
        self.addWidget(self.connectButton)
        self.addWidget(self.refreshButton)

