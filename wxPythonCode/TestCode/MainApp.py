#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import MainFrame
import MainMDIParentFrame

modules ={u'MainFrame': [1, 'Main frame of Application', u'MainFrame.py'],
 u'MainMDIParentFrame': [0, '', u'MainMDIParentFrame.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = MainMDIParentFrame.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
