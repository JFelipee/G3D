from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

glutInit(sys.argv)
def torus():
    glutWireTorus(0.25, 0.6, 10, 10)
    glFlush()

glutCreateWindow("Mi primera ventana")
glutDisplayFunc(torus)
glutMainLoop
