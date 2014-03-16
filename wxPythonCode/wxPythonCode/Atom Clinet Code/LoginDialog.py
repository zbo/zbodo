import wx

class LoginDialog(wx.Dialog):
    def __init__(self, parent, id = -1):
            wx.Dialog.__init__(self, parent, id, u'Login', size = (400, 200))
            vSizer=wx.BoxSizer(wx.VERTICAL)
            vSizer.AddSpacer(30)

            userNameSizer=wx.BoxSizer(wx.HORIZONTAL)
            userNameSizer.AddSpacer(30)
            lblUserName = wx.StaticText(self, -1, "User Name:",size=wx.Size(60, 20))
            txbUserName = wx.TextCtrl(self, -1, "User Name")
            userNameSizer.Add(item=lblUserName, proportion=0, flag=wx.EXPAND|wx.ALL, border=3)
            userNameSizer.Add(item=txbUserName, proportion=1, flag=wx.EXPAND|wx.ALL, border=3)
            userNameSizer.AddSpacer(30)
            vSizer.Add(item=userNameSizer, proportion=0, flag=wx.EXPAND|wx.ALL, border=0)

            passWordSizer=wx.BoxSizer(wx.HORIZONTAL)
            passWordSizer.AddSpacer(30)
            lblUserName = wx.StaticText(self, -1, "Password:",size=wx.Size(60, 20))
            txbUserName = wx.TextCtrl(self, -1, "Password")
            passWordSizer.Add(item=lblUserName, proportion=0, flag=wx.EXPAND|wx.ALL, border=3)
            passWordSizer.Add(item=txbUserName, proportion=1, flag=wx.EXPAND|wx.ALL, border=3)
            passWordSizer.AddSpacer(30)
            vSizer.Add(item=passWordSizer, proportion=0, flag=wx.EXPAND|wx.ALL, border=0)

            vSizer.AddSpacer(30)
            loginSizer=wx.BoxSizer(wx.HORIZONTAL)
            loginSizer.AddSpacer(30)
            ckbAsAdmin=wx.CheckBox(self,-1,"Login as admin")
            btnLogin=wx.Button(self,-1,"Login")
            loginSizer.AddSpacer(30)
            loginSizer.AddSpacer(30)
            loginSizer.Add(item=ckbAsAdmin,proportion=0, flag=wx.EXPAND|wx.ALL, border=3)
            loginSizer.AddSpacer(30)
            loginSizer.AddSpacer(30)
            loginSizer.Add(item=btnLogin,proportion=0, flag=wx.EXPAND|wx.ALL, border=3)
            vSizer.Add(item=loginSizer, proportion=0, flag=wx.EXPAND|wx.ALL, border=0)

            self.SetSizer(vSizer)