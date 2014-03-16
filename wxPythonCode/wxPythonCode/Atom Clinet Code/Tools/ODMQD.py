import  wx

def create(parent):
    panel=ODMQDPanel(parent=parent)
    return panel

class ODMQDPanel(wx.Panel):

    def BoxSizerLayout(self):
        vSizer=wx.BoxSizer(wx.VERTICAL)
        vSizer.AddSpacer(50)
        testFileSizer=wx.BoxSizer(wx.HORIZONTAL)
        lblTestFile = wx.StaticText(self, -1, "Test File:",size=wx.Size(60, 20))
        txbTestFile = wx.TextCtrl(self, -1, "Test File")
        btnBrowseTestFile = wx.Button(self, -1, 'Browse ...')
        testFileSizer.AddSpacer(30)
        testFileSizer.Add(item=lblTestFile, proportion=0, flag=wx.EXPAND|wx.ALL, border=3)
        testFileSizer.Add(item=txbTestFile, proportion=1, flag=wx.EXPAND|wx.ALL, border=3)
        testFileSizer.Add(item=btnBrowseTestFile, proportion=0, flag=wx.EXPAND|wx.ALL, border=3)
        testFileSizer.AddSpacer(30)
        vSizer.Add(item=testFileSizer, proportion=0, flag=wx.EXPAND|wx.ALL, border=0)
        vSizer.AddSpacer(30)

        repairFileSizer=wx.BoxSizer(wx.HORIZONTAL)
        lblRepairFile = wx.StaticText(self, -1, "Repair File:",size=wx.Size(60, 20))
        txbRepairFile = wx.TextCtrl(self, -1, "Repair File")
        btnBrowseRepairFile = wx.Button(self, -1, 'Browse ...')
        repairFileSizer.AddSpacer(30)
        repairFileSizer.Add(item=lblRepairFile, proportion=0, flag=wx.EXPAND|wx.ALL, border=3)
        repairFileSizer.Add(item=txbRepairFile, proportion=1, flag=wx.EXPAND|wx.ALL, border=3)
        repairFileSizer.Add(item=btnBrowseRepairFile, proportion=0, flag=wx.EXPAND|wx.ALL, border=3)
        repairFileSizer.AddSpacer(30)
        vSizer.Add(item=repairFileSizer, proportion=0, flag=wx.EXPAND|wx.ALL, border=0)

        checkBoxSizer=wx.BoxSizer(wx.HORIZONTAL)
        ckbReSend=wx.CheckBox(self,-1,"Re-Send")
        checkBoxSizer.AddSpacer(30)
        checkBoxSizer.Add(item=ckbReSend, proportion=1, flag=wx.EXPAND|wx.ALL, border=3)
        checkBoxSizer.AddSpacer(30)
        vSizer.Add(item=checkBoxSizer, proportion=0, flag=wx.EXPAND|wx.ALL, border=0)

        submitSizer=wx.BoxSizer(wx.HORIZONTAL)
        btnCancel=wx.Button(self, -1, 'Cancel')
        lblSpacer = wx.StaticText(self, -1, "",size=wx.Size(20, 20))
        btnSubmit=wx.Button(self,-1,"Submit")
        submitSizer.Add(item=lblSpacer, proportion=1, flag= wx.ALIGN_RIGHT, border=3)
        submitSizer.Add(item=btnCancel, proportion=0, flag=wx.EXPAND, border=3)
        #submitSizer.AddSpacer(30)
        submitSizer.AddSpacer(30)
        submitSizer.Add(item=btnSubmit, proportion=0, flag=wx.EXPAND, border=3)
        submitSizer.AddSpacer(30)
        submitSizer.AddSpacer(30)
        vSizer.Add(item=submitSizer, proportion=0, flag=wx.EXPAND|wx.ALL, border=0)

        self.SetSizer(vSizer)
        pass

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)
        self.BoxSizerLayout()


if __name__ == '__main__':
    app=wx.PySimpleApp()
    frame=wx.Frame(parent=None,id=-1)
    panel=create(frame)
    frame.Show()
    app.MainLoop()

