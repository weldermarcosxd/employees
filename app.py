import sys
import resources
from PyQt5 import uic, QtWidgets
from controllers.employeesController import EmployeesController

from controllers.loginController import LoginController


class App(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.login()

    def employees(self):
        employeesController = EmployeesController()
        self.win = employeesController.win
        self.emiss = employeesController
        self.emiss.change_window.connect(self.changeWindow)
        self.win.show()

    def login(self):
        loginController = LoginController()
        self.win = loginController.win
        self.emiss = loginController
        self.emiss.change_window.connect(self.changeWindow)
        self.win.show()

    def changeWindow(self, method_name):
        self.win.close()
        method_to_call = getattr(self, method_name)
        method_to_call()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
