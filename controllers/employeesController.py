import sys
from PyQt5 import uic, QtWidgets, QtCore


class EmployeesController(QtWidgets.QWidget):

    change_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.win = uic.loadUi("views/employees.ui")
        self.win.pushButtonExit.clicked.connect(self.logout)
        self.win.actionExit.triggered.connect(self.logout)
        self.win.show()

    def logout(self):
        self.change_window.emit('login')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = EmployeesController()
    sys.exit(app.exec_())
