# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fenetre.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TchatDNF(object):
    def setupUi(self, TchatDNF):
        TchatDNF.setObjectName("TchatDNF")
        TchatDNF.resize(795, 651)
        self.centralwidget = QtWidgets.QWidget(TchatDNF)
        self.centralwidget.setObjectName("centralwidget")
        self.chatbox = QtWidgets.QTextBrowser(self.centralwidget)
        self.chatbox.setGeometry(QtCore.QRect(10, 10, 781, 501))
        self.chatbox.setObjectName("Chatbox")
        self.msgArea = QtWidgets.QTextEdit(self.centralwidget)
        self.msgArea.setGeometry(QtCore.QRect(10, 570, 641, 51))
        self.msgArea.setObjectName("msgArea")
        self.butChat = QtWidgets.QPushButton(self.centralwidget)
        self.butChat.setGeometry(QtCore.QRect(660, 570, 131, 51))
        self.butChat.setObjectName("butChat")
        self.butList = QtWidgets.QPushButton(self.centralwidget)
        self.butList.setGeometry(QtCore.QRect(660, 520, 131, 36))
        self.butList.setObjectName("butList")
        self.butState = QtWidgets.QPushButton(self.centralwidget)
        self.butState.setGeometry(QtCore.QRect(10, 520, 96, 36))
        self.butState.setObjectName("butState")
        self.butHelp = QtWidgets.QPushButton(self.centralwidget)
        self.butHelp.setGeometry(QtCore.QRect(120, 520, 121, 36))
        self.butHelp.setObjectName("butHelp")
        self.butEdit = QtWidgets.QPushButton(self.centralwidget)
        self.butEdit.setGeometry(QtCore.QRect(250, 520, 131, 36))
        self.butEdit.setObjectName("butEdit")
        TchatDNF.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TchatDNF)
        self.statusbar.setObjectName("statusbar")
        TchatDNF.setStatusBar(self.statusbar)

        self.retranslateUi(TchatDNF)
        QtCore.QMetaObject.connectSlotsByName(TchatDNF)

    def retranslateUi(self, TchatDNF):
        _translate = QtCore.QCoreApplication.translate
        TchatDNF.setWindowTitle(_translate("TchatDNF", "MainWindow"))
        self.butChat.setText(_translate("TchatDNF", "Send"))
        self.butList.setText(_translate("TchatDNF", "Users list"))
        self.butState.setText(_translate("TchatDNF", "Online"))
        self.butHelp.setText(_translate("TchatDNF", "Command list"))
        self.butEdit.setText(_translate("TchatDNF", "Change nickname"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TchatDNF = QtWidgets.QMainWindow()
    ui = Ui_TchatDNF()
    ui.setupUi(TchatDNF)
    TchatDNF.show()
    sys.exit(app.exec_())
