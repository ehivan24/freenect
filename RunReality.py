'''
Created on Jan 5, 2015

@author: edwingsantos
'''

if __name__ == '__main__':
    pass
from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
import pygame, pygame.image 
from pygame.locals import * 
import pickle
import Reality as R

width,height = 800,640

def setup():
    """ Setup window and pygame environment. """
    pygame.init() 
    pygame.display.set_mode((width,height),OPENGL | DOUBLEBUF) 
    pygame.display.set_caption('OpenGL AR demo')
    
with open('ar_camera.pkl','r') as f: 
    K = pickle.load(f)
    Rt = pickle.load(f)
    
setup()
R.drawBackGround('empire.jpg')
R.set_projection_from_camera(K) 
R.set_modelview_from_camera(Rt) 
R.draw_teapot(0.02)

while True:
    event = pygame.event.poll()
    if event.type in (QUIT,KEYDOWN):
        break 
    pygame.display.flip()
        