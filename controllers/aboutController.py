import sys
from PyQt5 import uic, QtWidgets, QtCore


class AboutController(QtWidgets.QWidget):

    change_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        uic.loadUi("views/about.ui", self)
        self.show()

    def back(self):
        self.change_window.emit('employees')

    def closeEvent(self, event):
        self.back()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = AboutController()
    sys.exit(app.exec_())
