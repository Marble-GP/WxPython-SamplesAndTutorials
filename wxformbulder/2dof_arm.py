# -*- coding: utf-8 -*-
import wx
import wx.xrc

from wxgraphicframe import GLFrame
from OpenGL.GL import *
import numpy as np
###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1080,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( 1080, 720 )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = GLFrame( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 640,480 ), wx.TAB_TRAVERSAL )
		self.m_panel1.SetProperty(self.MyDrawFunc)


		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		bSizer2.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer2.Add( self.m_textCtrl1, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"1st Angle and Length", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer4.Add( self.m_staticText4, 0, wx.ALL, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_spinCtrlDouble7 = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -90, 90, 0, 1 )
		self.m_spinCtrlDouble7.SetDigits( 0 )
		bSizer7.Add( self.m_spinCtrlDouble7, 0, wx.ALL, 5 )

		self.m_spinCtrlDouble8 = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0.1, 0.8, 0.5, 0.05 )
		self.m_spinCtrlDouble8.SetDigits( 0 )
		bSizer7.Add( self.m_spinCtrlDouble8, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer7, 0, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 50), 0, wx.EXPAND, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"2nd Angle and Length", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer4.Add( self.m_staticText5, 0, wx.ALL, 5 )

		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_spinCtrlDouble71 = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -90, 90, 0, 1 )
		self.m_spinCtrlDouble71.SetDigits( 0 )
		bSizer71.Add( self.m_spinCtrlDouble71, 0, wx.ALL, 5 )

		self.m_spinCtrlDouble81 = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0.1, 0.8, 0.5, 0.05 )
		self.m_spinCtrlDouble81.SetDigits( 0 )
		bSizer71.Add( self.m_spinCtrlDouble81, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer71, 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 50), 0, wx.EXPAND, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Manupurating X and Y of the arm tip", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer4.Add( self.m_staticText6, 0, wx.ALL, 5 )

		bSizer72 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_spinCtrlDouble72 = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -1, 1, 1, 0.01 )
		self.m_spinCtrlDouble72.SetDigits( 0 )
		bSizer72.Add( self.m_spinCtrlDouble72, 0, wx.ALL, 5 )

		self.m_spinCtrlDouble82 = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -1, 1, 0, 0.01 )
		self.m_spinCtrlDouble82.SetDigits( 0 )
		bSizer72.Add( self.m_spinCtrlDouble82, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer72, 1, wx.EXPAND, 5 )

		bSizer73 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer73.Add( self.m_button5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_toggleBtn1 = wx.ToggleButton( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer73.Add( self.m_toggleBtn1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer4.Add( bSizer73, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CHAR_HOOK, self.evt_KeyInput )
		self.m_button5.Bind( wx.EVT_BUTTON, self.evt_Reset )
		self.m_toggleBtn1.Bind( wx.EVT_TOGGLEBUTTON, self.evt_StartToggle )

		self.timer = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.evt_timerctrl, source=self.timer)
		self.timer.Start(100)

		self.m_spinCtrlDouble72.Bind(wx.EVT_SPINCTRLDOUBLE, self.evt_EditOtherVal)
		self.m_spinCtrlDouble82.Bind(wx.EVT_SPINCTRLDOUBLE, self.evt_EditOtherVal)

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def evt_KeyInput( self, event ):
		event.Skip()

	def evt_Reset( self, event ):
		self.m_spinCtrlDouble8.SetValue(0.5)
		self.m_spinCtrlDouble81.SetValue(0.5)
		self.m_spinCtrlDouble7.SetValue(0)
		self.m_spinCtrlDouble71.SetValue(0)
		self.m_spinCtrlDouble72.SetValue(1)
		self.m_spinCtrlDouble82.SetValue(0)
		self.m_toggleBtn1.SetValue(False)
		self.m_textCtrl1.SetValue('')

	def evt_StartToggle( self, event ):
		event.Skip()

	def MyDrawFunc(self):
		L = [self.m_spinCtrlDouble8.Value, self.m_spinCtrlDouble81.Value]
		TH = [self.m_spinCtrlDouble7.Value/180*np.pi, self.m_spinCtrlDouble71.Value/180*np.pi]

		x0 = -0.8
		y0 = 0.0
		x = x0
		y = y0

		#Draw White Wall
		glColor3f(1.0, 1.0, 1.0)
		glBegin(GL_POLYGON)
		glVertex2f(-1, -1)
		glVertex2f(-1, 1)
		glVertex2f(x0, 1)
		glVertex2f(x0, -1)
		glEnd()

		for i in range(2):
			Lx = L[i]*np.cos(TH[i])
			Ly = L[i]*np.sin(TH[i])

			glColor3f(0, 1, 1)
			glBegin(GL_LINES)
			glVertex2f(x,y)
			glVertex2f(x+Lx,y+Ly)

			glEnd()

			glColor3f(1.0, 1.0, 0.0)
			DrawCircle(x, y, 0.025)

			x += Lx
			y += Ly

	def evt_timerctrl(self, event):
		if self.m_toggleBtn1.Value:
			self.m_panel1.Start()

			L = [self.m_spinCtrlDouble8.Value, self.m_spinCtrlDouble81.Value]
			TH = [self.m_spinCtrlDouble7.Value/180*np.pi, self.m_spinCtrlDouble71.Value/180*np.pi]
			x = L[0]*np.cos(TH[0])+L[1]*np.cos(TH[1])
			y = L[0]*np.sin(TH[0])+L[1]*np.sin(TH[1])
			msg = "x:{}  y:{}  theta[0]:{}  theta[1]:{}\n".format(x, y, TH[0]*180/np.pi, TH[1]*180/np.pi)
			base = self.m_textCtrl1.Value
			if len(msg) + len(msg) > 0xFFFF:
				val = msg + base[len(msg):]
			else:
				val = msg + base
			self.m_textCtrl1.SetValue(val)
				
		else:
			self.m_panel1.Stop()

	#Inv-Kinematics solution of 2-DoF arm model
	def evt_EditOtherVal(self, event):
		x = self.m_spinCtrlDouble72.Value
		y = self.m_spinCtrlDouble82.Value
		L1 = self.m_spinCtrlDouble8.Value
		L2 = self.m_spinCtrlDouble81.Value
		theta = np.zeros(2)
		
		theta[0] = -np.arccos((x**2 + y**2 + L1**2 - L2**2)/(2*L1*np.sqrt(x**2 + y**2))) + np.arctan(y/x)
		theta[1] = np.arctan((y-L1*np.sin(theta[0]))/(x-L1*np.cos(theta[0])))-theta[0]

		self.m_spinCtrlDouble7.SetValue(theta[0]*180/np.pi)
		self.m_spinCtrlDouble71.SetValue(theta[1]*180/np.pi)



def DrawCircle(x0, y0, r):
	glBegin(GL_POLYGON)
	for i in range(36):
		th = i*10/180*np.pi
		glVertex2f(x0+r*np.cos(th), y0+r*np.sin(th))
	glEnd()




if __name__ == "__main__":
	app = wx.App()
	frame = MyFrame1(None)
	app.SetTopWindow(frame)
	frame.Show()
	app.MainLoop()