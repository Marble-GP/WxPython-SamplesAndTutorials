# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

from time import time
###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer1.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer1.Add( ( 0, 100), 0, wx.EXPAND, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"00:00.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer1.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CHAR_HOOK, self.evt_Keyboard )
		self.Bind( wx.EVT_RIGHT_DOWN, self.evt_TimerReset )
		self.Bind( wx.EVT_LEFT_DOWN, self.evt_TimerToggle )

		#set Timer event
		self.timer = wx.Timer(self)
		self.Bind( wx.EVT_TIMER, self.evt_Timer, source=self.timer)


		self.timerflag = False
		self.counter = 0
		self.timercount = 0
		self.basetime = time()
		self.hour = 0
		self.minute = 0#0~59
		self.second = 0 #0~59
		self.subsec = 0 #0~99

	def __del__( self ):
		pass
	


	# Virtual event handlers, overide them in your derived class
	def evt_Keyboard( self, event ):
		key = event.GetKeyCode()
		print(key)
		if key == 315:#up-arrow-key
			print("countup")
			self.counter += 1
		elif key == 317:#bottom-arrow-key
			print("countdown")
			self.counter -= 1
		
		elif key == 27:#esc-key
			self.counter = 0
		self.m_staticText1.SetLabel(str(self.counter))

	def evt_TimerReset( self, event ):
		self.hour = 0
		self.minute = 0
		self.second = 0
		self.subsec = 0
		self.m_staticText2.SetLabel("00:00.00")

	def evt_TimerToggle( self, event ):
		self.timerflag = not self.timerflag
		if self.timerflag:
			print("timer start")
			self.timer.Start(10)
			while(self.basetime == 0.0):
				self.basetime = time()
		else:
			print("timer stop")
			self.timer.Stop()
			self.timercount = 0

	def evt_Timer( self, event ):
		self.timercount += 1
		#more Accurate Time Gets from OS
		systime = time()
		self.basetime = self.subsec
		self.subsec = int(((systime - self.basetime) - int(systime - self.basetime))*100)
		if self.subsec < self.basetime:
			self.second += 1
		if self.second >= 60:
			self.second -= 60
			self.minute += 1
		if self.minute >= 60:
			self.minute -= 60
			self.hour += 1
		
		label=  str(self.minute).zfill(2) + ':' + str(self.second).zfill(2) + "." + str(self.subsec).zfill(2)
		if self.hour:#hour != 0
			label = str(self.hour)+":"+label
		
		self.m_staticText2.SetLabel(label)






if __name__ == "__main__":
	app = wx.App()
	frame = MyFrame1(None)
	app.SetTopWindow(frame)
	frame.Show()
	app.MainLoop()
