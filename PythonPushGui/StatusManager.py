import PushServer
import Queue

class StatusManager(object):
    instance = None
    clientId=""
    connected=False
    stream=None
    pushServer=None
    pushContentQueue=Queue.Queue(0)
    @staticmethod
    def new():
        if not StatusManager.instance:
            StatusManager.log = StatusManager()
        return StatusManager.instance
    
    def SetClientId(self,clientIdInput):
        self.clientId=clientIdInput

    def GetClientId(self):
        return self.clientId

    def PushToClient(self,str):
        PushServer.WebPUSH().Push(str)

    def GetNextPush(self):
        if self.pushContentQueue.qsize()>0:
            content=self.pushContentQueue.get()
            return content
