from PyQt5 import QtSql


class Dao(object):
    def openDb(self):
        self.db = QtSql.QSqlDatabase().database()
        if self.db.isValid():
            return self.db

        self.db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("127.0.0.1")
        self.db.setDatabaseName("employees")
        self.db.setUserName("root")
        self.db.setPassword("rock")
        return self.db

    def closeDb(self):
        if self.db is not None:
            self.db.close()


if __name__ == "__main__":
    dao = Dao()
    dao.openDb()
    dao.closeDb()
