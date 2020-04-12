from PyQt5 import QtCore, QtGui, QtWidgets
from loginpagecontroller import LoginController
from halamanuser import User_Window
from halamanadmin import Admin_Window
import sys


class Login_Window(object):
    def __init__(self):
        MainWindow = QtWidgets.QMainWindow()
        self.setupUi(MainWindow)
        MainWindow.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 20, 361, 141))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 190, 91, 61))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 270, 111, 71))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(320, 200, 141, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 280, 141, 41))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 360, 241, 131))
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">LOGIN PAGE</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">USERNAME</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">PASSWORD</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "MASUK"))
        self.pushButton.clicked.connect(lambda: self.pushLogin(MainWindow))

    def pushLogin(self, MainWindow):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        login_controller = LoginController(username, password)
        if login_controller.checkTruth():
            if login_controller.checkRole() == "User":
                self.halamanuser = User_Window(username)
            else:
                self.halamanadmin = Admin_Window(username)
            MainWindow.close()
        else:
            self.popupWrong()

    def popupWrong(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Login gagal!")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Username atau Password Anda Salah!")
        msg.exec_()


##if __name__ == "__main__":
##    import sys
##    app = QtWidgets.QApplication(sys.argv)
##    MainWindow = QtWidgets.QMainWindow()
##    ui = Ui_MainWindow()
##    ui.setupUi(MainWindow)
##    MainWindow.show()
##    sys.exit(app.exec_())
