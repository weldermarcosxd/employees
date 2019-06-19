import sys
import resources
from PyQt5 import uic, QtWidgets


class App(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.win = uic.loadUi("views/login.ui")
        self.win.pushButton.clicked.connect(self.login)
        self.win.show()

    def login(self):
        self.win.close()
        self.win = uic.loadUi("views/employees.ui")
        self.win.actionExit.triggered.connect(self.logout)
        self.win.pushButtonExit.clicked.connect(self.logout)
        self.win.show()

    def logout(self):
        self.win.close()
        self.win = uic.loadUi("views/login.ui")
        self.win.pushButton.clicked.connect(self.login)
        self.win.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
