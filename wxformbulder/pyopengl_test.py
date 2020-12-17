from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
#These APIs are exactly the same as the C lang's
#GL&GLU: CG calculation library
#GLUT: CG's GUI library

#refer: http://wisdom.sakura.ne.jp/system/opengl/gl11.html

import sys

def UserDrawingRoutine():
	glClear(GL_COLOR_BUFFER_BIT)

	glBegin(GL_POLYGON)
	glColor3f(1 , 0 , 0)
	glVertex2f(-0.9 , -0.9)
	glColor3f(0 , 1 , 0)
	glVertex2f(0 , 0.9)
	glColor3f(0 , 0 , 1)
	glVertex2f(0.9 , -0.9)
	glEnd()

	glFlush()
    

def GLUT_init(title, UserRoutine, size=(640,480), bgclr=(0, 0, 0, 0)):
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_SINGLE)
    glutInitWindowSize(size[0], size[1])
    glutCreateWindow(title)
    glClearColor(bgclr[0], bgclr[1], bgclr[2], bgclr[3])
    glutDisplayFunc(UserDrawingRoutine)

    UserRoutine()
    glutMainLoop()


if __name__ == "__main__":
    GLUT_init(b"testing openGL of python wrapper", UserDrawingRoutine)