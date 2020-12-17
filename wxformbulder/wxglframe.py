
import wx
import glfw
from OpenGL.GL import *

from numpy.random import rand

def rand_inrange(min, max):
    return (max - min)*rand() + min



class MyGL():
    def __init__(self, size=(640, 480), showflag=True):
        if not glfw.init():
            raise Exception("RuntimeError: glfw.init() failed")

        glfw.window_hint(glfw.VISIBLE, showflag) #set window invisible
        self.window = glfw.create_window(640, 480, "test", None, None)

        if not self.window:
            glfw.terminate()
            raise Exception("WindowError: glfw.create_window() failed")

        glfw.make_context_current(self.window)


    def WindowRoutie(self):
        while not glfw.window_should_close(self.window):
            glClearColor(0.0, 0.0, 0.0, 0.0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.MyDraw()
            glfw.swap_buffers(self.window)
            glfw.poll_events()
        
        glfw.destroy_window(self.window)
        glfw.terminate()
        


    def MyDraw(self):
        glBegin(GL_POLYGON)
        for i in range(3):
            glColor3f(rand_inrange(0, 1), rand_inrange(0, 1), rand_inrange(0, 1))
            glVertex2f(rand_inrange(-0.5, 0.5), rand_inrange(-0.5, 0.5))
        glEnd()





if __name__ == "__main__":
    mygl = MyGL()
    mygl.WindowRoutie()

    
    