# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import json

###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		gSizer2 = wx.GridSizer( 0, 2, 5, 0 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Your name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		gSizer2.Add( self.m_staticText2, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Your favorite", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		gSizer2.Add( self.m_staticText3, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_textCtrl2, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Height [cm]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		gSizer2.Add( self.m_staticText4, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_spinCtrl1 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 65535, 175 )
		gSizer2.Add( self.m_spinCtrl1, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Weight [Kg]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		gSizer2.Add( self.m_staticText5, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_spinCtrl2 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 65535, 65 )
		gSizer2.Add( self.m_spinCtrl2, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Age", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		gSizer2.Add( self.m_staticText6, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_spinCtrl3 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 65535, 30 )
		gSizer2.Add( self.m_spinCtrl3, 0, wx.ALL, 5 )


		bSizer5.Add( gSizer2, 1, wx.EXPAND, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.evt_savejson )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def evt_savejson( self, event ):
		#event.Skip()
		dat = {} # empty dictionary
		name = self.m_textCtrl1.Value
		fav = self.m_textCtrl2.Value
		status = [self.m_spinCtrl1.Value, self.m_spinCtrl2.Value, self.m_spinCtrl3.Value]
		dat["name"] = name
		dat["favorite"] = fav
		dat["status"] = status
		with open("person_status.json", "w") as jf:
			json.dump(dat, jf)



if __name__ == "__main__":
	app = wx.App()
	frame = MyFrame3(None)
	app.SetTopWindow(frame)
	frame.Show()
	app.MainLoop()