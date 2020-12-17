#@date 2020/9/29
#@author Shohei Watanabe
#@brief This is WX-GraphicsFrame library (with three sample classes and a sample program(how to use these classes)).
#       It can be used like wx.Panel simply.
import wx
import cv2
from numpy import zeros, frombuffer, reshape, int8

import glfw
from OpenGL.GL import *

#@brief: This is base class, used for inheritance.
class GraphicBaseFrame(wx.Panel):
        def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr):
            super().__init__(parent, id, pos, size, style, name)

            self.parent = parent

            self.size = size
            self.fps = 30

            self.parent.SetSize(self.size)

            self.frame = zeros((self.size[0], self.size[1], 3))
            self.bmp = wx.Bitmap.FromBuffer(self.size[0], self.size[1], self.frame)

            self.frametimer = wx.Timer(self)
            self.Bind(wx.EVT_PAINT, self.OnPaint)
            self.Bind(wx.EVT_TIMER, self.FrameUpdate, source=self.frametimer)
            self.Bind(wx.EVT_ERASE_BACKGROUND, self.evt_Background)#to avoid flickering

            self._debug = False

        def evt_Background(self, event):
            pass
        
        def Start(self):
            self.frametimer.Start(1000.0/self.fps)

        def Stop(self):
            self.frametimer.Stop()

        def OnPaint(self, evt):
            if self._debug:
                print("onPaint")
            dc = wx.BufferedPaintDC(self)
            dc.DrawBitmap(self.bmp, 0, 0)
        

#@Brief: This is the most simple example of usage of GraphicBaseFrame class (draw black background)
class BlackFrame(GraphicBaseFrame):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr):
        super().__init__(parent, id, pos, size, style, name)
        self.Bind(wx.EVT_TIMER, self.FrameUpdate, source=self.frametimer)
        self.fps = 1

    def FrameUpdate(self,event):
        print("Frame update")
        self.bmp = wx.Bitmap.FromBuffer(self.size[0], self.size[1], zeros((self.size[0], self.size[1], 3)))
        self.Refresh()


#@Brief: This is a example of usage of GraphicBaseFrame class (getting camera frame)
class CVCamFrame(GraphicBaseFrame):
        def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr):
            super().__init__(parent, id, pos, size, style, name)
            self.Bind(wx.EVT_TIMER, self.FrameUpdate, source=self.frametimer)
            
            
        def SetProperty(self, ch=0, fps=30):
            self.channel = ch
            self.fps = fps
            self.capture = cv2.VideoCapture(self.channel)
            self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.size[0])
            self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.size[1])
            self.parent.SetSize(self.size)

        def FrameUpdate(self, event):
            ret, frame = self.capture.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.frame = cv2.putText(frame, "ch{}  {}fps".format(self.channel, self.fps), (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), thickness=2)
                self.bmp.CopyFromBuffer(frame)
                self.Refresh()



#@Brief: This is a example of usage of GraphicBaseFrame class (getting Image form contents directly)
class CVImageFrame(GraphicBaseFrame):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr):
        super().__init__(parent, id, pos, size, style, name)
        import os, re
        self.Bind(wx.EVT_TIMER, self.FrameUpdate, source=self.frametimer)
        
        self.Graphiclist = []
        self.path = "contents"
        self.index = 0
        self.fps = 5

        for Graphic in os.listdir(self.path):
            root, ext = os.path.splitext(Graphic)
            if ext in {".png", ".jpg", ".gif"}:
                self.Graphiclist.append(Graphic)


        if len(self.Graphiclist) == 0:
            raise Exception("GraphicNotFoundError")


    def FrameUpdate(self, event):
        fname = self.path+"/"+self.Graphiclist[self.index]
        Graphic = cv2.imread(fname)
        Graphic = cv2.cvtColor(Graphic, cv2.COLOR_BGR2RGB)
        self.size = (Graphic.shape[1], Graphic.shape[0])
        self.parent.SetSize(self.size)
        self.bmp = wx.Bitmap.FromBuffer(self.size[0], self.size[1], Graphic)
        self.Refresh()

#@Brief: This is a example of usage of GraphicBaseFrame class (Draw CG graphics with openGL)
class GLFrame(GraphicBaseFrame):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr):
        super().__init__(parent, id, pos, size, style, name)

        if not glfw.init():
            raise Exception("RuntimeError: glfw.init() failed")

        glfw.window_hint(glfw.VISIBLE, False) #set window invisible
        self.window = glfw.create_window(size[0], size[1], "invisible window", None, None)
        if not self.window:
            glfw.terminate()
            raise Exception("WindowError: glfw.create_window() failed")

        glfw.make_context_current(self.window)

        self.Bind(wx.EVT_TIMER, self.FrameUpdate, source=self.frametimer)

    def SetProperty(self, DrawFunc, fps=30, bgcolor=(0, 0, 0, 0)):
        self.DrawFunction = DrawFunc
        self.fps = fps
        self.bgcolor = bgcolor

    def FrameUpdate(self, event):
        if not glfw.window_should_close(self.window):
            glClearColor(self.bgcolor[0], self.bgcolor[1], self.bgcolor[2], self.bgcolor[3])
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.DrawFunction()
            glfw.swap_buffers(self.window)
            glfw.poll_events()

            glReadBuffer(GL_BACK)
            self.buffer = glReadPixels(0, 0, self.size[0], self.size[1], GL_RGB, type=GL_UNSIGNED_BYTE)
            self.bmp = wx.Bitmap.FromBuffer(self.size[0], self.size[1], self.buffer)
            self.Refresh()
        else:
            glfw.destroy_window(self.window)
            glfw.terminate()



#******** This is sample code ********
from numpy.random import rand

def _rand_inrange(min, max):
    return (max - min)*rand() + min

def _SampleDraw():
    glBegin(GL_POLYGON)
    for i in range(3):
        glColor3f(_rand_inrange(0, 1), _rand_inrange(0, 1), _rand_inrange(0, 1))
        glVertex2f(_rand_inrange(-1, 1), _rand_inrange(-1, 1))
    glEnd()    

if __name__ == "__main__":
    app = wx.App()
    frame1 = wx.Frame(None)
    frame2 = wx.Frame(None)
    frame3 = wx.Frame(None)
    #cvimframe = CVImageFrame(frame1, size=(640,480))
    cvcamframe = CVCamFrame(frame2, size=(640,480))
    glframe = GLFrame(frame3, size=(640,480))

    cvcamframe.SetProperty()
    glframe.SetProperty(_SampleDraw, bgcolor=(1.0, 1.0, 1.0, 0.0))

    #cvimframe.Start()
    cvcamframe.Start()
    glframe.Start()

    frame1.Show()
    frame2.Show()
    frame3.Show()

    app.MainLoop()