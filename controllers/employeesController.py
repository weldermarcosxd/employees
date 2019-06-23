import sys
from PyQt5 import uic, QtWidgets, QtCore


class EmployeesController(QtWidgets.QWidget):

    change_window = QtCore.pyqtSignal(str)
    callRpt = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.win = uic.loadUi("views/employees.ui")
        self.win.pushButtonExit.clicked.connect(self.logout)
        self.win.actionExit.triggered.connect(self.logout)
        self.win.pushButtonInfo.clicked.connect(self.about)
        self.win.actionAbout.triggered.connect(self.about)
        self.win.actionRelEmployee.triggered.connect(self.reportEmp)
        self.win.actionRelDepartment.triggered.connect(self.reportDept)
        self.win.show()

    def logout(self):
        self.change_window.emit('login')

    def about(self):
        self.change_window.emit('about')

    def reportEmp(self):
        self.callRpt.emit('employeesRpt')

    def reportDept(self):
        self.callRpt.emit('departmentRpt')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = EmployeesController()
    sys.exit(app.exec_())
