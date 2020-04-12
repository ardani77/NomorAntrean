from loginpage import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Main:
    
    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        login = Ui_MainWindow()
        sys.exit(app.exec_())

if __name__ == "__main__":
    m = Main()
    m.run()
