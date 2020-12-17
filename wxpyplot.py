#@date: 2020/9/29
#@author: Shohei Watanabe
#@brief: This is WX-GraphPlotFrame library(with matplotlib)
#        It can be used like wx.Panel simply.


import wx

#user append
import numpy as np
import matplotlib
matplotlib.interactive(True)
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from matplotlib.figure import Figure

UPDATE_TIME = 100 #milliseconds
INTERNAL_TIMER_ID = -1


#reference: https://gist.github.com/ikapper/765932799dd5dd36230b0d5205735bd3
#customize Panel Class
class Wxplot(wx.Panel):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr):
        super().__init__(parent, id, pos, size, style, name)
        self.parent = parent
        self.lastplot = None
        self.figure = Figure(None)
        self.figure.set_facecolor((240/255, 240/255, 240/255))
        self.subplot = self.figure.add_subplot(111)

        #canvas
        self.canvas = FigureCanvasWxAgg(self, -1, self.figure)
        self.canvas.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.Layout()

        self.timer = wx.Timer(self, INTERNAL_TIMER_ID)
        self.Bind(wx.EVT_TIMER, self.update_graph, self.timer)
        self.timer.Start(UPDATE_TIME)

        #data
        self.x = np.linspace(0, 1, 10)
        self.y = np.zeros(10)
        self.color = "blue"
        self.title = None
        self.xlabel = None
        self.ylabel = None

    def update_graph(self, event):
        if self.lastplot:
            self.lastplot[0].remove()

        if self.title is not None:
            self.subplot.set_title(self.title)
        if self.xlabel is not None:
            self.subplot.set_xlabel(self.xlabel)
        if self.ylabel is not None:
            self.subplot.set(self.ylabel)

        self.lastplot = self.subplot.plot(self.x, self.y, color=self.color)
        self.canvas.draw()


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, size=(500,500))
    panel = Wxplot(frame)
    frame.Show()
    app.MainLoop()

