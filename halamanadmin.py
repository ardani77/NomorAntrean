from PyQt5 import QtCore, QtGui, QtWidgets
from halamanadmin2 import LihatUser_Window
from halamanadmin4 import EditAntrean_Window


class Admin_Window(object):
    def __init__(self, username):
        self.username = username
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.MainWindow.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(340, 476)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 10, 121, 101))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 130, 141, 101))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 260, 141, 101))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 340, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Antrean"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Administrator</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Nomor Antrean"))
        self.pushButton_2.setText(_translate("MainWindow", "Melihat User"))
        self.pushButton.clicked.connect(lambda: self.pushAntre(MainWindow))
        self.pushButton_2.clicked.connect(lambda: self.pushUser(MainWindow))
        
    def pushAntre(self, MainWindow):
        self.halamanadmin4 = EditAntrean_Window(self.username)
        MainWindow.close()

    def pushUser(self, MainWindow):
        self.halamanadmin2 = LihatUser_Window(self.username)
        MainWindow.close()

    
        


##if __name__ == "__main__":
##    import sys
##    app = QtWidgets.QApplication(sys.argv)
##    MainWindow = QtWidgets.QMainWindow()
##    ui = Admin_Window("ardani123")
##    ui.setupUi(MainWindow)
##    MainWindow.show()
##    sys.exit(app.exec_())

##from PyQt5 import QtCore, QtGui, QtWidgets
##from halamanadmin2 import Lihatuser_Window
##from halamanadmin4 import EditAntrean_Window
##
##
##
##class Admin_Window(object):
##    def __init__(self, username):
##        self.username = username
##        self.MainWindow = QtWidgets.QMainWindow()
##        self.setupUi(self.MainWindow)
##        self.MainWindow.show()
##        
##    def setupUi(self, MainWindow):
##        MainWindow.setObjectName("MainWindow")
##        MainWindow.resize(340, 476)
##        self.centralwidget = QtWidgets.QWidget(MainWindow)
##        self.centralwidget.setObjectName("centralwidget")
##        self.label = QtWidgets.QLabel(self.centralwidget)
##        self.label.setGeometry(QtCore.QRect(120, 10, 121, 101))
##        self.label.setObjectName("label")
##        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
##        self.pushButton.setGeometry(QtCore.QRect(90, 110, 141, 101))
##        self.pushButton.setObjectName("pushButton")
##        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
##        self.pushButton_2.setGeometry(QtCore.QRect(90, 240, 141, 91))
##        self.pushButton_2.setObjectName("pushButton_2")
##        MainWindow.setCentralWidget(self.centralwidget)
##        self.menubar = QtWidgets.QMenuBar(MainWindow)
##        self.menubar.setGeometry(QtCore.QRect(0, 0, 340, 26))
##        self.menubar.setObjectName("menubar")
##        MainWindow.setMenuBar(self.menubar)
##        self.statusbar = QtWidgets.QStatusBar(MainWindow)
##        self.statusbar.setObjectName("statusbar")
##        MainWindow.setStatusBar(self.statusbar)
##
##        self.retranslateUi(MainWindow)
##        QtCore.QMetaObject.connectSlotsByName(MainWindow)
##
##    def retranslateUi(self, MainWindow):
##        _translate = QtCore.QCoreApplication.translate
##        MainWindow.setWindowTitle(_translate("MainWindow", "Antrean"))
##        self.label.setText(_translate("MainWindow", "Administrator"))
##        self.pushButton.setText(_translate("MainWindow", "Nomor Antrean"))
##        self.pushButton_2.setText(_translate("MainWindow", "Melihat User"))
##        self.pushButton.clicked.connect(lambda: self.pushEditAntrean(MainWindow))
##        self.pushButton_2.clicked.connect(lambda: self.pushLihatUser(MainWindow))
##
##    def pushEditAntrean(self, MainWindow):
##        self.halamanadmin4 = EditAntrean_Window(username)
####        MainWindow.close()
##
##    def pushLihatUser(self,MainWindow):
##        self.halamanadmin2 = LihatUser_Window(username)
####        MainWindow.close()
##        
##        
##
##
##if __name__ == "__main__":
##    import sys
##    app = QtWidgets.QApplication(sys.argv)
##    MainWindow = QtWidgets.QMainWindow()
##    ui = Admin_Window("ardani123")
##    ui.setupUi(MainWindow)
##    MainWindow.show()
##    sys.exit(app.exec_())

