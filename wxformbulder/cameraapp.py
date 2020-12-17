# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import cv2
import wxgraphicframe
###########################################################################
## Class MyFrame5
###########################################################################

class MyFrame5 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1080,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel8 = wxgraphicframe.CVCamFrame( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 640,480 ), wx.TAB_TRAVERSAL )
		bSizer16.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer16.Add( self.m_textCtrl5, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer14.Add( bSizer16, 1, wx.EXPAND, 5 )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )


		bSizer15.Add( ( 1, 50), 0, wx.EXPAND, 5 )

		self.channel = wx.StaticText( self, wx.ID_ANY, u"Camera Ch.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.channel.Wrap( -1 )

		bSizer15.Add( self.channel, 0, wx.ALL, 5 )

		m_comboBox2Choices = []
		self.m_comboBox2 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBox2Choices, 0 )
		bSizer15.Add( self.m_comboBox2, 0, wx.ALL, 5 )


		bSizer15.Add( ( 1, 100), 0, wx.EXPAND, 5 )

		self.set_fps = wx.StaticText( self, wx.ID_ANY, u"frame rate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.set_fps.Wrap( -1 )

		bSizer15.Add( self.set_fps, 0, wx.ALL, 5 )

		self.m_slider1 = wx.Slider( self, wx.ID_ANY, 30, 1, 60, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer15.Add( self.m_slider1, 0, wx.ALL, 5 )


		bSizer15.Add( ( 1, 100), 0, wx.EXPAND, 5 )

		self.m_toggleBtn2 = wx.ToggleButton( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_toggleBtn2.SetValue( True )
		bSizer15.Add( self.m_toggleBtn2, 0, wx.ALL, 5 )


		bSizer14.Add( bSizer15, 0, wx.ALIGN_LEFT|wx.EXPAND, 5 )


		self.SetSizer( bSizer14 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_toggleBtn2.Bind( wx.EVT_TOGGLEBUTTON, self.evt_camstart )

		self.m_panel8.SetProperty(fps=self.m_slider1.Value)

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def evt_camstart( self, event ):
		if self.m_toggleBtn2.Value:
			self.m_panel8.fps = self.m_slider1.Value
			self.m_panel8.Start()
		else:
			self.m_panel8.Stop()




if __name__ == "__main__":
	app = wx.App()
	frame = MyFrame5(None)
	app.SetTopWindow(frame)
	frame.Show()
	app.MainLoop()
