# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fenetre.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TchatDNC(object):
    def setupUi(self, TchatDNC):
        TchatDNC.setObjectName("TchatDNC")
        TchatDNC.resize(991, 651)
        self.centralwidget = QtWidgets.QWidget(TchatDNC)
        self.centralwidget.setObjectName("centralwidget")
        self.chatbox = QtWidgets.QTextBrowser(self.centralwidget)
        self.chatbox.setGeometry(QtCore.QRect(10, 10, 781, 501))
        self.chatbox.setObjectName("Chatbox")
        self.msgArea = QtWidgets.QLineEdit(self.centralwidget)
        self.msgArea.setGeometry(QtCore.QRect(10, 570, 640, 50))
        self.msgArea.setObjectName("msgArea")
        self.butChat = QtWidgets.QPushButton(self.centralwidget)
        self.butChat.setGeometry(QtCore.QRect(660, 570, 125, 50))
        self.butChat.setObjectName("butChat")
        self.butState = QtWidgets.QPushButton(self.centralwidget)
        self.butState.setGeometry(QtCore.QRect(10, 520, 100, 40))
        self.butState.setObjectName("butState")
        self.butHelp = QtWidgets.QPushButton(self.centralwidget)
        self.butHelp.setGeometry(QtCore.QRect(130, 520, 110, 40))
        self.butHelp.setObjectName("butHelp")
        self.butEdit = QtWidgets.QPushButton(self.centralwidget)
        self.butEdit.setGeometry(QtCore.QRect(260, 520, 120, 40))
        self.butEdit.setObjectName("butEdit")
        self.listUser = QtWidgets.QListWidget(self.centralwidget)
        self.listUser.setGeometry(QtCore.QRect(800, 10, 181, 611))
        self.listUser.setObjectName("listUser")
        self.sendTo = QtWidgets.QComboBox((self.centralwidget))
        self.sendTo.setGeometry(QtCore.QRect(660,520,125,40))
        self.sendTo.setObjectName("sendTo")
        self.sendTo.addItem("Everyone")
        TchatDNC.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TchatDNC)
        self.statusbar.setObjectName("statusbar")
        TchatDNC.setStatusBar(self.statusbar)

        self.retranslateUi(TchatDNC)
        QtCore.QMetaObject.connectSlotsByName(TchatDNC)

    def retranslateUi(self, TchatDNC):
        _translate = QtCore.QCoreApplication.translate
        TchatDNC.setWindowTitle(_translate("TchatDNC", "MainWindow"))
        self.butChat.setText(_translate("TchatDNC", "Send"))
        self.butState.setText(_translate("TchatDNC", "Online"))
        self.butHelp.setText(_translate("TchatDNC", "Command list"))
        self.butEdit.setText(_translate("TchatDNC", "Change nickname"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TchatDNC = QtWidgets.QMainWindow()
    ui = Ui_TchatDNC()
    ui.setupUi(TchatDNC)
    TchatDNC.show()
    sys.exit(app.exec_())
