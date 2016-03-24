'''
Created on Jan 5, 2015

@author: edwingsantos
'''

if __name__ == '__main__':
    pass

from PIL import Image
from pylab import *

im = array(Image.open('empire.jpg').convert('L'))

figure() 

gray()

contour(im, origin='image')
axis('equal')
axis('off')

figure()

hist(im.flatten(),128)
show()