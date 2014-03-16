import wx


def create(parent):
    panel=IdentityManagementPanel(parent=parent)
    return panel
	
class IdentityManagementPanel(wx.Panel):
    def __init__(self, parent):
            wx.Panel.__init__(self, parent, -1)
            button=wx.Button(self,-1,"IdentityManagement")



if __name__ == '__main__':
    app=wx.PySimpleApp()
    frame=wx.Frame(parent=None,id=-1)
    panel=IdentityManagementPanel(parent=frame)
    frame.Show()
    app.MainLoop()
