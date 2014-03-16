import wx
import wx.grid
import wx.html
import wx.aui
import Configuration
import LoginDialog
import SqliteDataAccess
import cStringIO

ID_GridContent = wx.NewId()
ID_TextContent = wx.NewId()
ID_TreeContent = wx.NewId()
ID_HTMLContent = wx.NewId()
ID_SizeReportContent = wx.NewId()
ID_CreatePerspective = wx.NewId()

ID_TransparentHint = wx.NewId()
ID_VenetianBlindsHint = wx.NewId()
ID_RectangleHint = wx.NewId()
ID_NoHint = wx.NewId()
ID_HintFade = wx.NewId()
ID_AllowFloating = wx.NewId()
ID_NoVenetianFade = wx.NewId()
ID_TransparentDrag = wx.NewId()
ID_AllowActivePane = wx.NewId()

ID_About = wx.NewId()
ID_Welcome = wx.NewId()
ID_Perspective = wx.NewId()
ID_LOGIN=wx.NewId()

ID_TestButton=wx.NewId()

#----------------------------------------------------------------------
def GeCiscoIcon():
    icon=wx.Icon('cisco.ico',wx.BITMAP_TYPE_ICO)
    return icon
class ClientUIMeta:
    ClientData=None
    MenuID=None
    TreeNodeId=None


class AtomClientMainFrame(wx.Frame):
    menuConfigMappingList=[]
    configList=[]
    configGroupList={}
    tree=None
    messageTextBox=None
    def BuildToolBar(self):
        tb2 = wx.ToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize,
                         wx.TB_FLAT | wx.TB_NODIVIDER)
        tb2.SetToolBitmapSize(wx.Size(16, 16))
        tb2_bmp1 = wx.ArtProvider_GetBitmap(wx.ART_QUESTION, wx.ART_OTHER, wx.Size(16, 16))
        tb2.AddLabelTool(-1, "A", tb2_bmp1)
        tb2.AddLabelTool(-1, "B", tb2_bmp1)
        tb2.AddSeparator()
        tb2.AddLabelTool(-1, "C", tb2_bmp1)
        tb2.Realize()
        tb3 = wx.ToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize,
                         wx.TB_FLAT | wx.TB_NODIVIDER)
        tb3.SetToolBitmapSize(wx.Size(16, 16))
        tb3_bmp1 = wx.ArtProvider_GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, wx.Size(16, 16))
        tb3.AddLabelTool(-1, "A", tb3_bmp1)
        tb3.AddLabelTool(-1, "B", tb3_bmp1)
        tb3.AddLabelTool(-1, "C", tb3_bmp1)
        tb3.Realize()
        tb4 = wx.ToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize,
                         wx.TB_FLAT | wx.TB_NODIVIDER | wx.TB_HORZ_TEXT)
        tb4.SetToolBitmapSize(wx.Size(16, 16))
        tb4_bmp1 = wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16, 16))
        tb4.AddSeparator()
        tb4.AddLabelTool(-1, "D", tb4_bmp1)
        tb4.Realize()
        return tb2, tb3, tb4

    def BuildMenuStatusBar(self):
        self.mb = wx.MenuBar()
        self.file_menu = wx.Menu()
        self.file_menu.Append(wx.ID_EXIT, "Exit")

        self.login_menu=wx.Menu()
        self.login_menu.Append(ID_LOGIN,"Login")

        self.perspectives_menu = wx.Menu()
        self.perspectives_menu.Append(ID_Perspective, "Default Startup")
        self.tools_menu = wx.Menu()

        self.help_menu = wx.Menu()
        self.help_menu.Append(ID_About, "About...")
        self.help_menu.Append(ID_Welcome, "Welcome Page")
        self.mb.Append(self.file_menu, "File")
        self.mb.Append(self.login_menu,"Login")
        self.mb.Append(self.perspectives_menu, "Perspectives")
        self.mb.Append(self.tools_menu, "Tools")
        self.mb.Append(self.help_menu, "Help")
        self.SetMenuBar(self.mb)
        self.statusbar = self.CreateStatusBar(2, wx.ST_SIZEGRIP)
        self.statusbar.SetStatusWidths([-2, -3])
        self.statusbar.SetStatusText("Ready", 0)
        self.statusbar.SetStatusText("Welcome to Atom client!", 1)
        # min size for the frame itself isn't completely done.
        # see the end up FrameManager::Update() for the test
        # code. For now, just hard code a frame minimum size
        self.SetMinSize(wx.Size(400, 300))

    def __init__(self, parent, id=-1, title="Atom Client Demo", pos=wx.DefaultPosition,
                 size=(1200, 800), style=wx.DEFAULT_FRAME_STYLE |
                                            wx.SUNKEN_BORDER |
                                            wx.CLIP_CHILDREN):

        wx.Frame.__init__(self, parent, id, title, pos, size, style)

        # tell FrameManager to manage this frame
        self._mgr = wx.aui.AuiManager()
        self._mgr.SetManagedWindow(self)

        self._perspectives = []
        self.n = 0
        self.x = 0

        self.SetIcon(GeCiscoIcon())

        # create menu
        self.BuildMenuStatusBar()

        # create some toolbars

        tb2, tb3, tb4 = self.BuildToolBar()

        #load layout from config
        self.BuildLayoutByConfig()

        # add a bunch of panes
        self._mgr.AddPane(self.CreateTreeCtrl(), wx.aui.AuiPaneInfo().
                          Name("All Clients").Caption("All Clients").
                          Left().Layer(1).Position(1).CloseButton(True).MaximizeButton(True))

        self._mgr.AddPane(self.CreateTextCtrl(), wx.aui.AuiPaneInfo().
                          Name("Message").Caption("Message").
                          Bottom().Layer(1).Position(1).CloseButton(True).MaximizeButton(True))

        # create some center panes

        self._mgr.AddPane(self.CreateCenterTabs(), wx.aui.AuiPaneInfo().Name("CenterTab").
                          CenterPane().Hide())



        # add the toolbars to the manager

        self._mgr.AddPane(tb2, wx.aui.AuiPaneInfo().
                          Name("tb2").Caption("Toolbar 2").
                          ToolbarPane().Top().Row(1).
                          LeftDockable(False).RightDockable(False))

        self._mgr.AddPane(tb3, wx.aui.AuiPaneInfo().
                          Name("tb3").Caption("Toolbar 3").
                          ToolbarPane().Top().Row(1).Position(1).
                          LeftDockable(False).RightDockable(False))

        self._mgr.AddPane(tb4, wx.aui.AuiPaneInfo().
                          Name("tb4").Caption("Sample Bookmark Toolbar").
                          ToolbarPane().Top().Row(1).Position(2).
                          LeftDockable(False).RightDockable(False))

        self._mgr.AddPane(wx.Button(self, ID_TestButton, "Test Button"),
                          wx.aui.AuiPaneInfo().Name("").
                          ToolbarPane().Top().Row(1).Position(3).
                          LeftDockable(False).RightDockable(False))

        # make some default perspectives

        all_panes = self._mgr.GetAllPanes()
        for ii in xrange(len(all_panes)):
            if not all_panes[ii].IsToolbar():
                all_panes[ii].Hide()

        self._mgr.GetPane("All Clients").Show().Left().Layer(0).Row(0).Position(0)
        self._mgr.GetPane("Message").Show().Bottom().Layer(0).Row(0).Position(0)
        self._mgr.GetPane("CenterTab").Show()

        perspective_default = self._mgr.SavePerspective()
        self._perspectives.append(perspective_default)


        
        # "commit" all changes made to FrameManager
        self._mgr.Update()

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        # Show How To Use The Closing Panes Event

        self.Bind(wx.EVT_MENU, self.OnExit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.OnLogin, id=ID_LOGIN)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=ID_About)
        self.Bind(wx.EVT_MENU, self.OnWelcome, id=ID_Welcome)

        self.Bind(wx.EVT_MENU, self.OnRestorePerspective, id=ID_Perspective)
        self.Bind(wx.EVT_BUTTON, self.OnTestButton, id=ID_TestButton)

    def OnMenuClientChange(self,event):
        self.ShowMessage("change the client to ...")
        for meta in self.menuConfigMappingList:
            if meta.MenuID==event.GetId():
                moduleName= meta.ClientData.ModuleName
                if self.SetFocusToExistingTab(moduleName)==-1:
                    self.LoadClientPage(moduleName)
        self._mgr.Update()

    def  BuildMenuByConfigList(self,configList):
        for config in configList:
            # add menu
            menuItem=wx.MenuItem(self.tools_menu,-1, config.MenuName)
            self.tools_menu.AppendItem(menuItem)
            self.Bind(wx.EVT_MENU, self.OnMenuClientChange, menuItem)
            # add meta to list
            clientMeta=ClientUIMeta()
            clientMeta.ClientData=config
            clientMeta.MenuID=menuItem.Id
            self.menuConfigMappingList.append(clientMeta)

    def BuildLayoutByConfig(self):
        configReader = Configuration.ConfigReader()
        self.configList = configReader.ReadConfig()
        self.BuildMenuByConfigList(self.configList)


    def OnTestButton(self,event):
        import SomeTestCode;
        #SomeTestCode.InsertData(self)
        #SomeTestCode.StatusManagerTest(self)
        #SomeTestCode.SetFocusByName(self,"ODMQD")
        #SomeTestCode.SqliteTests(self);
        SomeTestCode.DynamicLoad(self);
        pass

    def OnClose(self, event):
        self._mgr.UnInit()
        del self._mgr
        self.Destroy()


    def OnExit(self, event):
        self.Close()

    def OnWelcome(self, event):
        page = self.CreateWelcomePage()
        self.book.AddPage(page, "Welcome To Atom Client")

    def OnAbout(self, event):

        msg = "Atom Client Demo\n" + \
              "An draft simple ideas about the atom client \n" + \
              "(c) Copyright 2012, Cisco Corporation"
        dlg = wx.MessageDialog(self, msg, "About Atom Client Demo",
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def OnLogin(self, event):
           dlg=LoginDialog.LoginDialog(self)
           dlg.ShowModal()
           dlg.Destroy()
    def GetDockArt(self):
        return self._mgr.GetArtProvider()

    def DoUpdate(self):
        self._mgr.Update()

    def OnEraseBackground(self, event):
        event.Skip()


    def OnSize(self, event):
        event.Skip()


    def OnRestorePerspective(self, event):
        self._mgr.LoadPerspective(self._perspectives[0])


    def GetStartPosition(self):
        self.x = self.x + 20
        x = self.x
        pt = self.ClientToScreen(wx.Point(0, 0))
        return wx.Point(pt.x + x, pt.y + x)


    def CreateTextCtrl(self):
        text = "Begin Atom Client Work\r\n"
        self.messageTextBox= wx.TextCtrl(self,-1, text, wx.Point(0, 0), wx.Size(150, 90),
                           wx.NO_BORDER | wx.TE_MULTILINE)
        return self.messageTextBox


    def CreateTreeCtrl(self):
        self.BuildGroupedListFromConfig()
        self.tree = wx.TreeCtrl(self, -1, wx.Point(0, 0), wx.Size(200, 250),
                           wx.TR_DEFAULT_STYLE | wx.NO_BORDER)
        root = self.tree.AddRoot("All")
        keys=self.configGroupList.keys()
        for i in range(len(keys)):
            key=keys[len(keys)-1-i]
            roottemp=self.tree.AppendItem(root, key, 0)
            for j in range(len(self.configGroupList[key])):
                self.tree.AppendItem(roottemp, self.configGroupList[key][j].MenuName, 0)
            if len(self.configGroupList[key])<5:
                self.tree.Expand(roottemp)
        self.tree.Expand(root)
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnTreeSelChanged, self.tree)
        return self.tree

    def ShowMessage(self,message):
        self.messageTextBox.AppendText(message+"\r\n")
        pass;

    def FindModuleNameByMenuName(self,text):
        for config in self.configList:
            if config.MenuName==text:
                return config.ModuleName
        return None

    def LoadClientPage(self, moduleName):
        clientModule = __import__("Tools."+moduleName,fromlist=["*"])
        panel = clientModule.create(self)
        panel.Hide()
        self.book.AddPage(panel, moduleName)
        panel.SetFocus()

    def OnTreeSelChanged(self,event):
        item = event.GetItem()
        text=self.tree.GetItemText(item)
        self.ShowMessage(text+" is selected")
        moduleName = self.FindModuleNameByMenuName(text)
        if moduleName!=None:
            # load module and add panel to main center
            if self.SetFocusToExistingTab(moduleName)==-1:
                self.LoadClientPage(moduleName)

    def CreateCenterTabs(self):
        self.book = wx.aui.AuiNotebook(self)
        page = self.CreateWelcomePage()
        self.book.AddPage(page, "Welcome To Atom Client")
        return self.book

    def CreateWelcomePage(self):
            ctrl = wx.html.HtmlWindow(self, -1, wx.DefaultPosition, wx.Size(400, 300))
            if "gtk2" in wx.PlatformInfo:
                ctrl.SetStandardFonts()
            ctrl.SetPage(self.GetIntroText())
            return ctrl

    def GetIntroText(self):
        return overview

    def SetFocusToExistingTab(self, name):
          pageCount=self.book.GetPageCount()
          for i in range(0,pageCount):
             pageName=self.book.GetPageText(i)
             if pageName==name:
                 page= self.book.GetPage(i)
                 page.SetFocus()
                 return i
          return -1

    def BuildGroupedListFromConfig(self):
         for item in self.configList:

             if self.configGroupList.has_key(item.GroupName)==False:
                 listNew=[]
                 listNew.append(item)
                 self.configGroupList[item.GroupName]=listNew
             else:
                 self.configGroupList[item.GroupName].append(item)

overview="<b>HTML Content</b><br/><h1>hello atom</h1>"

if __name__=='__main__':
    app=wx.PySimpleApp()
    mainFrame=AtomClientMainFrame(parent=None,id=-1)
    mainFrame.Show()
    app.MainLoop()