import sys
from PyQt5 import uic, QtWidgets, QtCore, QtSql


class LoginController(QtWidgets.QWidget):

    change_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.win = uic.loadUi("views/login.ui")
        self.win.pushButton.clicked.connect(self.logins)
        self.win.show()

    def logins(self):
        credentials = {}
        credentials['username'] = self.win.lineEdit.text()
        credentials['password'] = self.win.lineEdit_2.text()

        self.load()

        if(credentials['username'] == 'weldermarcosxd'):
            self.change_window.emit('employees')
        else:
            msg = QtWidgets.QMessageBox()
            # msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText(" Invalid username or password")
            msg.setWindowTitle("Login Failed")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()

    def load(self):
        db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        db.setHostName("127.0.0.1")
        db.setDatabaseName("employees")
        db.setUserName("root")
        db.setPassword("rock")
        ok = db.open()
        if(not ok):
            print(db.lastError().text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = LoginController()
    sys.exit(app.exec_())