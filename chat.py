from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 501, 261))
        font = QtGui.QFont()
        font.setFamily("Minecraft 1.1")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: rgb(134, 134, 134);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 260, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Minecraft 1.1")
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(100, 100, 100);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 300, 501, 101))
        font = QtGui.QFont()
        font.setFamily("Minecraft 1.1")
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 56, 56);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(400, 260, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Minecraft 1.1")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Friend_chat  desine by Vol4ok"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Minecraft 1.1\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "You Messege"))
        self.pushButton.setText(_translate("MainWindow", "SEND"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Nick:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
