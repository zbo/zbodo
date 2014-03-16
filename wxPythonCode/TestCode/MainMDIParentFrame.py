#Boa:MDIParent:MainMDIParentFrame

import wx

def create(parent):
    return MainMDIParentFrame(parent)

[wxID_MAINMDIPARENTFRAME] = [wx.NewId() for _init_ctrls in range(1)]

[wxID_MAINMDIPARENTFRAMEMENU1ITEMS0, wxID_MAINMDIPARENTFRAMEMENU1ITEMS1, 
] = [wx.NewId() for _init_coll_menu1_Items in range(2)]

class MainMDIParentFrame(wx.MDIParentFrame):
    def _init_coll_MainmenuBar_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.menu1, title='File')

    def _init_coll_menu1_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_MAINMDIPARENTFRAMEMENU1ITEMS0,
              kind=wx.ITEM_NORMAL, text='File')
        parent.Append(help='', id=wxID_MAINMDIPARENTFRAMEMENU1ITEMS1,
              kind=wx.ITEM_NORMAL, text='Copy')

    def _init_utils(self):
        # generated method, don't edit
        self.MainmenuBar = wx.MenuBar()

        self.menu1 = wx.Menu()

        self._init_coll_MainmenuBar_Menus(self.MainmenuBar)
        self._init_coll_menu1_Items(self.menu1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.MDIParentFrame.__init__(self, id=wxID_MAINMDIPARENTFRAME,
              name='MainMDIParentFrame', parent=prnt, pos=wx.Point(553, 423),
              size=wx.Size(400, 250),
              style=wx.DEFAULT_FRAME_STYLE | wx.VSCROLL | wx.HSCROLL,
              title='Main')
        self._init_utils()
        self.SetClientSize(wx.Size(384, 212))
        self.SetToolTipString('Main')
        self.SetMenuBar(self.MainmenuBar)

    def __init__(self, parent):
        self._init_ctrls(parent)
