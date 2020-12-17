# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

#user append
import wxpyplot
import numpy as np



###########################################################################
## Class MyFrame4
###########################################################################

class MyFrame4 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1080,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.plotarea = wxpyplot.Wxplot( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer3.Add( self.plotarea, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"size", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer11.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_spinCtrl5 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 20, 1 )
		bSizer11.Add( self.m_spinCtrl5, 0, wx.ALL, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer12.Add( ( 0, 0), 2, wx.EXPAND, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Amp", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer12.Add( self.m_staticText11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Phase[rad]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer12.Add( self.m_staticText12, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Freq[rad/s]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		bSizer12.Add( self.m_staticText13, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer11.Add( bSizer12, 0, wx.ALIGN_CENTER|wx.EXPAND, 5 )

		self.m_grid3 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid3.CreateGrid( 1, 3 )
		self.m_grid3.EnableEditing( True )
		self.m_grid3.EnableGridLines( True )
		self.m_grid3.EnableDragGridSize( False )
		self.m_grid3.SetMargins( 0, 0 )

		# Columns
		self.m_grid3.EnableDragColMove( False )
		self.m_grid3.EnableDragColSize( True )
		self.m_grid3.SetColLabelSize( 30 )
		self.m_grid3.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid3.EnableDragRowSize( True )
		self.m_grid3.SetRowLabelSize( 80 )
		self.m_grid3.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid3.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer11.Add( self.m_grid3, 1, wx.ALIGN_CENTER|wx.ALL, 5 )


		gSizer3.Add( bSizer11, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		self.ctrltimer = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.evt_ctrltimer, self.ctrltimer)
		self.ctrltimer.Start(100)

		self.plotarea.x = np.linspace(0, 2*np.pi, 10000)
		self.plotarea.y = np.zeros(10000)
		self.size = [1,1]

	def __del__( self ):
		pass

	def evt_ctrltimer(self, event):
		self.size[0] = self.size[1]
		self.size[1] = self.m_spinCtrl5.Value
		if self.size[1] - self.size[0] > 0:
			self.m_grid3.AppendRows(self.size[1] - self.size[0])
		elif self.size[1] - self.size[0] < 0:
			self.m_grid3.DeleteRows(pos=self.size[0]-1, numRows=self.size[0] - self.size[1])
		
		y = np.zeros(10000)
		for i in range(self.size[1]):
			try:
				amp = float(self.m_grid3.GetCellValue(i, 0))	
			except ValueError:
				amp = 0.0
			try:
				phase = float(self.m_grid3.GetCellValue(i, 1))
			except ValueError:
				phase = 0.0
			try:
				w = float(self.m_grid3.GetCellValue(i, 2))
			except ValueError:
				w = 0.0			
			y += amp*np.cos(w*self.plotarea.x + phase)
		self.plotarea.y = y
		

if __name__ == "__main__":
	app = wx.App()
	frame = MyFrame4(None)
	app.SetTopWindow(frame)
	frame.Show()
	app.MainLoop()
