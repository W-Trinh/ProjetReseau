from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QInputDialog, QPushButton, QDialog, QDialogButtonBox

from fenetrev2 import Ui_TchatDNF
from client import Client
from conndialog import ConnDialog

import threading, time

class Tchat(QMainWindow, Ui_TchatDNF):

    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        connexion = ConnDialog()
        if connexion.exec_() == QDialog.Accepted:
            val = connexion.getVal()
        self.user = Client(val["nickname"], val["address"], 9310)
        self.user.connect()
        self.setupUi(self)
        self.setWindowTitle("DNF Chat")
        self.butChat.clicked.connect(self.chat)
        self.butState.clicked.connect(self.change_state)
        self.butHelp.clicked.connect(self.get_command)
        self.butEdit.clicked.connect(self.new_nickname)

    def new_nickname(self):
        newNick, ok = QInputDialog.getText(self,"New nickname","Please enter your new nickname :")
        if ok:
            message = self.user.nickname + ": EDIT " + newNick        
            self.user.client.send(message.encode())

    def chat(self):
        message = self.user.nickname + ": CHAT " + self.msgArea.toPlainText()        
        self.user.client.send(message.encode())
        self.msgArea.clear()

    def change_state(self):
        if(self.butState.text()=="Online"):
            self.butState.setText("AFK")
        else:
            self.butState.setText("Online")

    def get_command(self):
        message = self.user.nickname + ": HELP"
        self.user.client.send(message.encode())

    def receive(self):
        while True:
            try:
                message = self.user.client.recv(1024).decode('ascii')
                if message == "nickname?":
                    self.user.client.send(self.user.nickname.encode('utf-8'))
                else:
                    self.chatbox.append(message)
            except:
                print("an error has occured!")
                self.user.client.close()
                break

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = Tchat()
    #threadMsg = threading.Thread(target = win.send_msg).start()
    #threadMp = threading.Thread(target = win.mp).start()
    threadRec = threading.Thread(target = win.receive).start()
    win.show()
    sys.exit(app.exec())    
    