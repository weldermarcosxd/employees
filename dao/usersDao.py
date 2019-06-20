from PyQt5 import QtSql
from dao.dao import Dao


class UsersDao(object):

    def __init__(self):
        dao = Dao()
        self.db = dao.openDb()

    def login(self, credentials):
        username = credentials['username']
        password = credentials['password']

        self.db.open()
        query = QtSql.QSqlQuery(self.db)
        query.prepare(
            'SELECT name, pass FROM users WHERE name=:username and pass = :password')
        query.bindValue(':username', username)
        query.bindValue(':password', password)
        executed = query.exec()
        self.db.close()

        if executed and query.first():
            return True
        else:
            return False


if __name__ == "__main__":
    login = LoginDao()
    res = login.openDb()
    print(res.open())
