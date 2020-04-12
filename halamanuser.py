from PyQt5 import QtCore, QtGui, QtWidgets
from usertoantrecontroller import User_Look
from homepageusercontroller import User_Controller
import sys


class User_Window(object):
    def __init__(self, username):
        self.username = username
        self.homepageusercontroller = User_Controller(self.username)
        self.name = self.homepageusercontroller.getName()
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.MainWindow.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(335, 441)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 60, 161, 51))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 191, 71))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 290, 151, 81))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 10, 101, 61))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 170, 121, 81))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 335, 26))
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
        self.label.setText(_translate("MainWindow", self.name))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Nomor Antrean Tersedia</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "AMBIL"))
        self.label_3.setText(_translate("MainWindow", "Selamat Datang"))
        self.label_4.setText(_translate("MainWindow", str(self.showAntreanTersedia())))
        self.pushButton.clicked.connect(lambda: self.pushGetAntre(MainWindow))

    def showAntreanTersedia(self):
        return self.homepageusercontroller.showNomor_Tersedia()
##        hasil = self.homepageusercontroller.showNomor_Tersedia()
##        return hasil['antrean'])

    def pushGetAntre(self, MainWindow):
        hasil = self.homepageusercontroller.getNomor()
        self.popupDapat()
        

    def popupDapat(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Selamat!")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Silahkan Menunggu Giliran Anda!")
        msg.exec_()
        
        


    
##if __name__ == "__main__":
##    import sys
##    app = QtWidgets.QApplication(sys.argv)
##    MainWindow = QtWidgets.QMainWindow()
##    ui = User_Window("budi123")
##    ui.setupUi(MainWindow)
##    MainWindow.show()
##    sys.exit(app.exec_())


##from PyQt5 import QtCore, QtGui, QtWidgets
##from usertoantrecontroller import User_Look
##from homepageusercontroller import User_Controller
##import sys
##
##
##class User_Window(object):
##    def __init__(self, username):
##        self.username = username
##        self.homepageusercontroller = User_Controller(self.username)
##        selfname = self.homepageusercontroller.getName()
##        self.MainWindow = QtWidgets.QMainWindow()
##        self.setupUi(self.MainWindow)
##        self.MainWindow.show()
##        
##    def setupUi(self, MainWindow):
##        MainWindow.setObjectName("MainWindow")
##        MainWindow.resize(335, 441)
##        self.centralwidget = QtWidgets.QWidget(MainWindow)
##        self.centralwidget.setObjectName("centralwidget")
##        self.label = QtWidgets.QLabel(self.centralwidget)
##        self.label.setGeometry(QtCore.QRect(90, 60, 161, 51))
##        self.label.setAlignment(QtCore.Qt.AlignCenter)
##        self.label.setObjectName("label")
##        self.label_2 = QtWidgets.QLabel(self.centralwidget)
##        self.label_2.setGeometry(QtCore.QRect(30, 130, 191, 71))
##        self.label_2.setObjectName("label_2")
##        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
##        self.pushButton.setGeometry(QtCore.QRect(80, 260, 151, 81))
##        self.pushButton.setObjectName("pushButton")
##        self.label_3 = QtWidgets.QLabel(self.centralwidget)
##        self.label_3.setGeometry(QtCore.QRect(120, 10, 101, 61))
##        self.label_3.setObjectName("label_3")
##        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
##        self.textBrowser.setGeometry(QtCore.QRect(190, 140, 81, 61))
##        self.textBrowser.setObjectName("textBrowser")
##        MainWindow.setCentralWidget(self.centralwidget)
##        self.menubar = QtWidgets.QMenuBar(MainWindow)
##        self.menubar.setGeometry(QtCore.QRect(0, 0, 335, 26))
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
##        self.label.setText(_translate("MainWindow", "User"))
##        self.label_2.setText(_translate("MainWindow", "Nomor Antrean Tersedia"))
##        self.pushButton.setText(_translate("MainWindow", "AMBIL"))
##        self.label_3.setText(_translate("MainWindow", "Selamat Datang"))
##        self.textBrowser.append(self.homepageusercontroller.showNomor_Tersedia())
##
##    def showAntreanTersedia(self, MainWindow):
##        return self.homepageusercontroller.showNomor_Tersedia()
##        
##        
##        
##
##
##if __name__ == "__main__":
##    import sys
##    app = QtWidgets.QApplication(sys.argv)
##    MainWindow = QtWidgets.QMainWindow()
##    ui = User_Window("budi123")
##    ui.setupUi(MainWindow)
##    MainWindow.show()
##    sys.exit(app.exec_())
####
