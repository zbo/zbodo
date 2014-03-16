import SqliteDataAccess
import StatusManager

def StatusManagerTest(self):
        manager1 = StatusManager.StatusManager()
        manager2 = StatusManager.StatusManager()
        print manager1
        print manager2

def DynamicLoad(self):
        self.messageTextBox.AppendText("test button pressed\r\n")
        clientModule=__import__('Tools.bobtest',fromlist=["*"])
        self.ShowMessage("load module"+str(clientModule))
        clientModule.test()

def SqliteTests(self):
        sqlHelper=SqliteDataAccess.SqliteDataAccessHelper()
        sqlHelper.OpenDataBase("MyDB.s3db")

        data=sqlHelper.RetriveDataByQuery('select * from config')
        print data
        sqlHelper.OperateDataByQuery("INSERT INTO config(MoudleName,ClassName,MenuName) VALUES ('TestClinet','TestClinetClass','Test Client');")
        data=sqlHelper.RetriveDataByQuery('select * from config')
        print data
        sqlHelper.OperateDataByQuery("Update config Set MoudleName = 'TestClinet2',MenuName ='Test Client2'  Where ClassName = 'TestClinetClass';")
        data=sqlHelper.RetriveDataByQuery('select * from config')
        print data
        sqlHelper.OperateDataByQuery("delete from config Where ClassName = 'TestClinetClass';")
        data=sqlHelper.RetriveDataByQuery('select * from config')
        print data
        sqlHelper.CommitChange()
        sqlHelper.CloseDataBase()
        import uuid
        print uuid.uuid4()
        pass
def InsertData(self):
        sql='''INSERT INTO config
            (MoudleName,ClassName,MenuName,GroupName) VALUES
            ('OutBoundQueue','OutBoundQueueClass','Out Bound Queue','Admin');'''
        sqlHelper=SqliteDataAccess.SqliteDataAccessHelper()
        sqlHelper.OpenDataBase("MyDB.s3db")
        sqlHelper.OperateDataByQuery(sql)
        sqlHelper.CommitChange()
        sqlHelper.CloseDataBase()



def SetFocusByName(self,name):
      pageCount=self.book.GetPageCount()
      for i in range(0,pageCount):
          pageName=self.book.GetPageText(i)
          if pageName==name:
              page= self.book.GetPage(i)
              page.SetFocus()
              break
      pass

