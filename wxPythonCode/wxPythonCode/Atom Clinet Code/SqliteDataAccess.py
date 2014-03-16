__author__ = 'bobzh'
import sqlite3

class SqliteDataAccessHelper:
    conn=None
    def OpenDataBase(self,dbName):
        self.conn=sqlite3.connect(dbName)

    def CloseDataBase(self):
        self.conn.close()

    def RetriveDataByQuery(self,query):
        cur=self.conn.cursor()
        cur.execute(query)
        data=cur.fetchall()
        return data

    def OperateDataByQuery(self, query):
        cur=self.conn.cursor()
        cur.execute(query)

    def CommitChange(self):
        self.conn.commit()