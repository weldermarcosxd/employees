import sys
import resources
from PyQt5 import uic, QtWidgets
from controllers.employeesController import EmployeesController
from controllers.loginController import LoginController
from controllers.aboutController import AboutController
from reports.employeesRpt import EmployeesRpt
from reports.departmentRpt import DepartmentRpt


class App(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.login()

    def employees(self):
        employeesController = EmployeesController()
        self.win = employeesController.win
        self.emiss = employeesController
        self.emiss.change_window.connect(self.changeWindow)
        self.emiss.callRpt.connect(self.callReport)
        self.win.show()

    def login(self):
        loginController = LoginController()
        self.win = loginController.win
        self.emiss = loginController
        self.emiss.change_window.connect(self.changeWindow)
        self.win.show()

    def about(self):
        aboutController = AboutController()
        self.win = aboutController
        self.win.change_window.connect(self.changeWindow)
        self.win.show()

    def employeesRpt(self):
        employeesRpt = EmployeesRpt()
        employeesRpt.print()

    def departmentRpt(self):
        departmentRpt = DepartmentRpt()
        departmentRpt.print()

    def changeWindow(self, method_name):
        self.win.close()
        method_to_call = getattr(self, method_name)
        method_to_call()

    def callReport(self, reportName):
        report_to_call = getattr(self, reportName)
        report_to_call()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
