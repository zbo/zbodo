import wx
import wx.grid
import wx.calendar
'''try add a self defined event to wxPython'''

class TestFrame(wx.Frame):
    myPanel=None
    myButton1=None
    myButton2=None
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'bob test event', size=(300, 120),pos=wx.Point(500, 500))
        self.myPanel=wx.Panel(self)
        self.myPanel.SetBackgroundColour("White")
        self.myButton1=wx.Button(parent=self.myPanel,id=-1,label="b 1",pos=(20,10),size=(100,20))
        self.myButton2=wx.Button(parent=self.myPanel,id=-1,label="b 2",pos=(20,40),size=(100,20))
        self.myButton1.Bind(wx.EVT_LEFT_DOWN,self.OnJob1,)
        self.myButton2.Bind(wx.EVT_LEFT_DOWN,self.OnJob2,)
        print 'init my frame'
    def OnJob1(self,event):
        print "do job 1"
        self.myPanel.SetBackgroundColour("Green")
        self.myButton1.Label="clicked"
        self.myButton2.Label="b 2"
        self.Refresh()
    def OnJob2(self,event):
        print "do job 2"
        self.myPanel.SetBackgroundColour("Red")
        self.myButton2.Label="clicked"
        self.myButton1.Label="b 1"
        self.Refresh()
class SubFrame(wx.Frame):
    myButtonOnSub1=None
    def __init__(self, parent,id):
        wx.Frame.__init__(self,parent,id,"sub Frame",size=(200,100),pos=wx.Point(500, 400))
        self.myPanel=wx.Panel(self)
        self.myPanel.SetBackgroundColour("White")
        self.myButtonOnSub1=wx.Button(parent=self.myPanel,id=-1,label="reset",pos=(20,10),size=(100,20))
        self.myButtonOnSub1.Bind(wx.EVT_LEFT_DOWN,self.OnJobSub1,)
    def OnJobSub1(self,event):
        print 'do job from sub frame'
        self.Parent.myPanel.SetBackgroundColour("White")
        self.Parent.myButton1.Label="b 1"
        self.Parent.myButton2.Label="b 2"
        self.Parent.Refresh()
class SimpleGrid(wx.grid.Grid):
    def __init__(self,parent,id):
        wx.grid.Grid.__init__(self,parent,wx.NewId(),pos=wx.Point(0, 0), size=wx.Size(400,300))
        self.SetColLabelSize(20)
        self.SetRowLabelSize(60)
        self.EnableEditing(False)
        self.CreateGrid(9,3)
        self.SetColLabelValue(0,"First")
        self.SetColLabelValue(1,"Last")
        self.SetColLabelValue(2,"Message")
        self.SetRowLabelValue(0,"CF")
        self.SetCellValue(0,0,"Bob")
        self.SetCellValue(0,1,"Test")
        self.SetCellValue(0,2,"Error")
class SubGridFrame(wx.Frame):
    def __init__(self, parent,id):
        wx.Frame.__init__(self,parent,id,"sub Grid Frame",size=(400,300),pos=wx.Point(700, 200))
        self.myPanel=wx.Panel(self)
        self.myPanel.SetBackgroundColour("Pink")
        self.myGrid=SimpleGrid(self.myPanel,wx.NewId())
        print self.Size
class CalendarFrame(wx.Frame):
    def __init__(self, parent,id):
        wx.Frame.__init__(self,parent,id,"calendar",size=(200,200),pos=wx.Point(800, 500))
        self.calendarCtrl1 = wx.calendar.CalendarCtrl(date=wx.DateTime.Now(),
              id=-1, name='calendarCtrl1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(179, 137),
              style=wx.calendar.CAL_SHOW_HOLIDAYS)
class TreeFrame(wx.Frame):
    def __init__(self, parent,id):
        wx.Frame.__init__(self,parent,id,"Tree",size=(200,300),pos=wx.Point(1000, 500))
        self.tree = wx.TreeCtrl(id=-1, name='treeCtrl1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(184,
              104), style=wx.TR_HAS_BUTTONS)
        root = self.tree.AddRoot('Programmer')
        os = self.tree.AppendItem(root, 'Operating Systems')
        pl = self.tree.AppendItem(root, 'Programming Languages')
        tk = self.tree.AppendItem(root, 'Toolkits')
        self.tree.ExpandAll()
        
if __name__ == '__main__':
    import sys,os
    app=wx.PySimpleApp()
    myFrame=TestFrame(parent=None,id=wx.NewId())
    mySubFrame=SubFrame(parent=myFrame,id=wx.NewId())
    mySubGridFrame=SubGridFrame(parent=myFrame,id=wx.NewId())
    myCalendarFrame=CalendarFrame(parent=myFrame,id=wx.NewId())
    myTreeFrame=TreeFrame(parent=myFrame,id=wx.NewId())
    myFrame.Show()
    mySubFrame.Show()
    mySubGridFrame.Show()
    myCalendarFrame.Show()
    myTreeFrame.Show()

    app.MainLoop()
