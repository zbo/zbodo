import wx


def create(parent):
    panel=ServiceConfigPanel(parent=parent)
    return panel
	
class ServiceConfigPanel(wx.Panel):
    def __init__(self, parent):
            wx.Panel.__init__(self, parent, -1)
            button=wx.Button(self,-1,"ServiceConfig")



if __name__ == '__main__':
    app=wx.PySimpleApp()
    frame=wx.Frame(parent=None,id=-1)
    panel=ServiceConfigPanel(parent=frame)
    frame.Show()
    app.MainLoop()