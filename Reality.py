'''
Created on Jan 5, 2015

@author: edwingsantos
'''

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame
import pygame.image
from pygame.locals import * 
import math
import pickle
from numpy import *

width,height = 1000,747

def drawBackGround(inimage):
    """ """ 
    bg_image = pygame.image.load(inimage).convert()
    bg_data = pygame.image.tostring(bg_image, "RGBX", 1)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glEnable(GL_TEXTURE_2D)
    glTexImage2D(GL_TEXTURE_2D,0,GL_RGBA,width,height,0,GL_RGBA,GL_UNSIGNED_BYTE,bg_data)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    
    glBegin(GL_QUADS)
    glTexCoord2f(0.0,0.0); glVertex3f(-1.0,-1.0,-1.0) 
    glTexCoord2f(1.0,0.0); glVertex3f( 1.0,-1.0,-1.0) 
    glTexCoord2f(1.0,1.0); glVertex3f( 1.0, 1.0,-1.0)
    glTexCoord2f(0.0,1.0); glVertex3f(-1.0, 1.0,-1.0) 
     
    glEnd()
    
    glDeleteTextures(1)
    
def set_projection_from_camera(K):
    """ Set view from a camera calibration matrix. """
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()
    fx = K[0,0]
    fy = K[1,1]
    fovy = 2*arctan(0.5*height/fy)*180/pi 
    aspect = (width*fy)/(height*fx)
    # define the near and far clipping planes
    near = 0.1 
    far = 100.0
    # set perspective
    gluPerspective(fovy,aspect,near,far) 
    glViewport(0,0,width,height)

def set_modelview_from_camera(Rt):
    """ Set the model view matrix from camera pose. """
    glMatrixMode(GL_MODELVIEW) 
    glLoadIdentity()
# rotate teapot 90 deg around x-axis so that z-axis is up
    Rx = array([[1,0,0],[0,0,-1],[0,1,0]])
# set rotation to best approximation
    R = Rt[:,:3]
    U,S,V = linalg.svd(R)
    R = dot(U,V)
    R[0,:] = -R[0,:] # change sign of x-axis
# set translation
    t = Rt[:,3]
# setup 4*4 model view matrix
    M = eye(4)
    M[:3,:3] = dot(R,Rx) 
    M[:3,3] = t
# transpose and flatten to get column order
    M = M.T
    m = M.flatten()
# replace model view with the new matrix
    glLoadMatrixf(m)
    
    
def draw_teapot(size):
    """ Draw a red teapot at the origin. """
    glEnable(GL_LIGHTING) 
    glEnable(GL_LIGHT0) 
    glEnable(GL_DEPTH_TEST)    
    glClear(GL_DEPTH_BUFFER_BIT)
    glMaterialfv(GL_FRONT,GL_AMBIENT,[0,0,0,0]) 
    glMaterialfv(GL_FRONT,GL_DIFFUSE,[0.5,0.0,0.0,0.0]) 
    glMaterialfv(GL_FRONT,GL_SPECULAR,[0.7,0.6,0.6,0.0]) 
    glMaterialf(GL_FRONT,GL_SHININESS,0.25*128.0) 
    glutSolidTeapot(size)

    