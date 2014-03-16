import wx
'''try add a self defined event to wxPython'''

class TestFrame(wx.Frame):
    myPanel=None
    mtButton1=None
    myButton2=None
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'bob test event', size=(300, 120))
        self.myPanel=wx.Panel(self)
        self.myPanel.SetBackgroundColour("White")
        self.myButton1=wx.Button(parent=self.myPanel,id=-1,label="b 1",pos=(20,10),size=(100,20))
        self.myButton2=wx.Button(parent=self.myPanel,id=-1,label="b 2",pos=(20,40),size=(100,20))
        self.myButton1.Bind(wx.EVT_LEFT_DOWN,self.OnJob1,)
        self.myButton2.Bind(wx.EVT_LEFT_DOWN,self.OnJob2,)
        print 'a'
    def OnJob1(self,event):
        print "do job 1"
        self.myPanel.SetBackgroundColour("White")
        self.myButton1.Label="clicked"
        self.myButton2.Label="b 2"
        self.Refresh()
    def OnJob2(self,event):
        print "do job 2"
        self.myPanel.SetBackgroundColour("Red")
        self.myButton2.Label="clicked"
        self.myButton1.Label="b 1"
        self.Refresh()
        
if __name__ == '__main__':
    import sys,os
    app=wx.PySimpleApp()
    myFrame=TestFrame(parent=None,id=wx.NewId())
    myFrame.Show()
    app.MainLoop()
