### LIBRERÍAS
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

import numpy as np

lados = 10

# Lista de vértices

vertex = [ [0.,-2.],
           [1.,1.],
           [-1.,1.],#Primer triángulo
          
           [0.,2.],
           [1.,-1.],
           [-1.,-1.]#segundo triángulo
         ]

# Lista de índices
index = [0, 1, 2, 3, 4 ,5 ,6]#orden consecutivo

def init():
    """
    Función que inicializa la ventana
    """
    # Establecemos el color de fondo
    glClearColor(0.5, 0.5, 0.5, 0.0)
    
    # El tipo de proyección
    glMatrixMode(GL_PROJECTION)
    
    # El recorte que vamos a mostrar en la pantalla
    gluOrtho2D(-2.0, 2.0, -2.0, 2.0)
    


def dibu():
    global vertex
    glClear(GL_COLOR_BUFFER_BIT)
    
    
    glColor3f(0.0, 0.0, 0.0)
    
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(2, GL_FLOAT, 0, vertex)
    
    #Usamos GL_Triangles, para tratarlos como 2 triángulos diferentes cada 3 puntos
    glDrawElements(GL_TRIANGLES, len(vertex), GL_UNSIGNED_BYTE, index)
    glDisableClientState(GL_VERTEX_ARRAY)

    
    glFlush()

glutInit(sys.argv) # Inicializamos GLUT

glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

glutInitWindowPosition(1000,500) # Posición de la ventana
glutInitWindowSize(500, 500)# Indica el tamaño de la ventana

glutCreateWindow("Lineas")# Creamos la ventana

init()# Inicializamos aquí a la ventana

glutDisplayFunc(dibu)

glutMainLoop()
