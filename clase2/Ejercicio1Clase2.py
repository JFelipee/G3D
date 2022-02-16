### LIBRERÍAS
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

import numpy as np

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
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Definir el color que tendrán los objetos que vamos a dibujar
    glColor3f(0.0, 0.0, 0.0)
    
    # Ancho de la línea
    glPointSize(5.0)
    
    ################### Puntos del eje de coordenadas X #########################
    glBegin(GL_POINTS)
    puntos=10; #puntos que tendrá los ejes
    
    #dibujamos puntos del eje x
    for x in range(-puntos, puntos):
        glVertex2f(x,0)
    glEnd()
    
    ############### Unimos puntos del eje de coordenadas X #######################
    # Ancho de la línea
    glLineWidth(1.0)
    
    # Dijamos eje x
    glBegin(GL_LINE_STRIP)
    
    #dibujamos puntos del eje x
    for x in range(-puntos, puntos):
        glVertex2f(x,0)
    glEnd()    
    
    ################### Puntos del eje de coordenadas Y #########################
    glBegin(GL_POINTS)
    
    #dibujamos puntos del eje x
    for y in range(-puntos, puntos):
        glVertex2f(0,y)
    glEnd()
        
    
    ############### Unimos puntos del eje de coordenadas Y #######################
    # Dijamos eje x
    glBegin(GL_LINE_STRIP)
    
    #dibujamos puntos del eje x
    for y in range(-puntos, puntos):
        glVertex2f(0,y)
    glEnd()    
    
    ############## Dibujamos función con los puntos existentes, es decir [-10,10] para X e Y ################
    glBegin(GL_LINE_STRIP)
    
    for k in range(-puntos,puntos):#como es una función cuadrática, se tomará el rango de puntos desde [-10,10], quedando simétrica
        glVertex2f(k, k*k)#aplicamos función f(x)=x²
    glEnd()
    
    
    glFlush()

glutInit(sys.argv) # Inicializamos GLUT

glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

glutInitWindowPosition(1000,500) # Posición de la ventana
glutInitWindowSize(700, 700)# Indica el tamaño de la ventana

glutCreateWindow("Lineas")# Creamos la ventana

init()# Inicializamos aquí a la ventana

glutDisplayFunc(dibu)

glutMainLoop()