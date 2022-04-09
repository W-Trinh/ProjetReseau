from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QInputDialog, QPushButton, QDialog, QDialogButtonBox
from PyQt5.QtGui import QTextCursor
from fenetrev2 import Ui_TchatDNC
from client import Client
from conndialog import ConnDialog

import threading, time

class Tchat(QMainWindow, Ui_TchatDNC):

    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        connexion = ConnDialog()
        if connexion.exec_() == QDialog.Accepted:
            val = connexion.getVal()
        self.user = Client(val["nickname"], val["address"], val["port"])
        self.user.connect()
        self.setupUi(self)
        self.setWindowTitle("DNC Chat")
        self.msgArea.returnPressed.connect(self.chat)
        self.butChat.clicked.connect(self.chat)
        self.butState.clicked.connect(self.change_state)
        self.butHelp.clicked.connect(lambda: self.use_command("HELP"))
        self.butEdit.clicked.connect(self.new_nickname)
        self.butList.clicked.connect(lambda: self.use_command("LIST"))
        self.threadRec = threading.Thread(target = self.receive)
        self.threadRec.start()

    def new_nickname(self):
        newNick, ok = QInputDialog.getText(self,"New nickname","Please enter your new nickname :")
        if ok:
            self.use_command("EDIT", newNick)

    def chat(self):
        msg = self.msgArea.text().strip()
        if( len(msg) != 0):
            self.use_command("CHAT", msg)
            self.msgArea.clear()


    def change_state(self):
        if(self.butState.text()=="Online"):
            self.butState.setText("AFK")
            self.use_command("ABS")
            self.butEdit.setEnabled(False)
        else:
            self.butState.setText("Online")
            self.butEdit.setEnabled(True)
            self.use_command("BACK")

    def receive(self):
        while True:
            self.chatbox.moveCursor(QTextCursor.End)
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

    def use_command(self, command, args = None):
        message = self.user.nickname + ": " + command + " "
        if args != None:
            message += args
        self.user.client.send(message.encode())

    def closeEvent(self , event):
        self.use_command("QUIT")
        for thread in threading.enumerate():
            thread.join()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = Tchat()
    win.show()
    sys.exit(app.exec())    
    
