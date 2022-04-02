from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLineEdit, QLabel

class ConnDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Connexion")

        QBtn = QDialogButtonBox.Cancel | QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()

        self.labNick = QLabel("Nickname :")
        self.labAdr = QLabel("Address :")
        self.labPort = QLabel("Port :")

        self.txtNick = QLineEdit()
        self.txtAdr = QLineEdit("127.0.0.1")
        self.txtPort = QLineEdit()

        self.layout.addWidget(self.labNick)
        self.layout.addWidget(self.txtNick)

        self.layout.addWidget(self.labAdr)
        self.layout.addWidget(self.txtAdr)

        self.layout.addWidget(self.labPort)
        self.layout.addWidget(self.txtPort)

        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def getVal(self):
        val = {"nickname" : self.txtNick.text(), "address" : self.txtAdr.text(), "port" :self.txtPort.text()}
        return val