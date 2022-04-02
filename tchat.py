from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QInputDialog
from fenetre import Ui_MainWindow
from client import Client
import threading, time

class tchat(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        nickname = input("Nickname?")
        self.user = Client(nickname, "127.0.0.1", 9305)
        self.user.connect()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_clic)

    def on_clic(self):
        message = self.user.nickname + ": CHAT " + self.textEdit.toPlainText()        
        self.user.client.send(message.encode())
        self.textEdit.clear()

    def send_msg(self):
        while True:
            time.sleep(0.5)
            self.textBrowser.append("User2 : ouais ouais ouais")
        
    def receive(self):
        while True:
            try:
                message = self.user.client.recv(1024).decode('ascii')
                if message == "nickname?":
                    self.user.client.send(self.user.nickname.encode('utf-8'))
                else:
                    self.textBrowser.append(message)
            except:
                print("an error has occured!")
                self.user.client.close()
                break

    def mp(self):
        while True:
            time.sleep(5)
            msg = QMessageBox()
            msg.setWindowTitle("Private message")
            msg.setText("User 2 wants to have a private chat with you.")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.exec()

    def closeEvent(self, *args, **kwargs):
        for t in threading.enumerate():
            if t != threading.main_thread(): t.join()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = tchat()
    #threadMsg = threading.Thread(target = win.send_msg).start()
    #threadMp = threading.Thread(target = win.mp).start()
    threadRec = threading.Thread(target = win.receive).start()
    threadLis = threading.Thread(target = win.refresh_list).start()
    win.show()
    sys.exit(app.exec())    
    