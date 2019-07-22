import sys
from PyQt5 import uic, QtWidgets, QtCore, QtSql


class EmployeesListController(QtWidgets.QWidget):

    change_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        uic.loadUi("views/employeeList.ui", self)
        self.loadEmployees()
        self.lineEdit.returnPressed.connect(self.filter)
        self.tableView.doubleClicked.connect(self.select)
        self.show()

    def loadEmployees(self):
        model = QtSql.QSqlTableModel(self)
        query = QtSql.QSqlQuery(
            '''select emp_no as 'Number', concat(first_name, ' ', last_name) as 'Name', gender as 'Gender',
            birth_date as 'Birth Date', hire_date as 'Hire Date' from employees''')
        model.setQuery(query)
        # model.setTable("employees")
        model.select()
        self.tableView.setModel(model)

    def filter(self):
        model = QtSql.QSqlTableModel(self)
        filter = self.lineEdit.text()

        if filter == '':
            self.loadEmployees()
            return

        str = '''select emp_no as 'Number', concat(first_name, ' ', last_name) as 'Name', gender as 'Gender',
            birth_date as 'Birth Date', hire_date as 'Hire Date' from employees
            where first_name like '%{}%' or last_name like '%{}%' or emp_no = '{}' 
            order by first_name'''.format(filter, filter, filter)
        query = QtSql.QSqlQuery(str)
        model.setQuery(query)
        model.select()
        self.tableView.setModel(model)

    def select(self, index):
        model = self.tableView.model()
        modelIndex = model.index(index.row(), 0)
        print(int(model.data(modelIndex)))

    def back(self):
        self.change_window.emit('employees')

    def closeEvent(self, event):
        self.back()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = EmployeesListController()
    sys.exit(app.exec_())
