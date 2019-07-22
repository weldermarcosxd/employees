import sys
from PyQt5 import uic, QtWidgets, QtCore, QtSql
from dao.usersDao import UsersDao


class LoginController(QtWidgets.QWidget):

    change_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.win = uic.loadUi("views/login.ui")
        self.win.pushButton.clicked.connect(self.logins)
        self.win.lineEdit.setText("weldermarcosxd")
        self.dao = UsersDao()
        self.win.show()

    def logins(self):
        credentials = {}
        credentials['username'] = self.win.lineEdit.text()
        credentials['password'] = self.win.lineEdit_2.text()

        if(self.dao.login(credentials)):
            self.change_window.emit('employees')
        else:
            msg = QtWidgets.QMessageBox()
            msg.setText(" Invalid username or password")
            msg.setWindowTitle("Login Failed")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = LoginController()
    sys.exit(app.exec_())
