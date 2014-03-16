import wx


def create(parent):
    panel=CesiumPanel(parent=parent)
    return panel
	
class CesiumPanel(wx.Panel):
    def __init__(self, parent):
            wx.Panel.__init__(self, parent, -1)
            button=wx.Button(self,-1,"Cesium")



if __name__ == '__main__':
    app=wx.PySimpleApp()
    frame=wx.Frame(parent=None,id=-1)
    panel=CesiumPanel(parent=frame)
    frame.Show()
    app.MainLoop()

