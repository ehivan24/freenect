'''
Created on Jan 5, 2015

@author: edwingsantos
'''

if __name__ == '__main__':
    pass

"""
from mpl_toolkits.mplot3d import axes3d
from PIL import Image
from pylab import *


fig = figure()
ax = fig.gca(projection="3d")

X,Y,Z = axes3d.get_test_data(0.25)
ax.plot(X.flatten(),Y.flatten(),Z.flatten(),'o') 
show()

"""

import cv2

clicked = False
def onMouse(event,x,y,flags, param):
    global clicked
    if event == cv2.cv.CV_EVENT_MOUSEMOVE:
        clicked = True

cameraCap = cv2.VideoCapture(0)
cv2.namedWindow('Video')
cv2.setMouseCallback('Video', onMouse)

print 'Showing camera feed. Click window or press any key to stop.'
success, frame = cameraCap.read()
while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow('Video', frame)
    success, frame = cameraCap.read()
cv2.destroyWindow('Video')

        
        


