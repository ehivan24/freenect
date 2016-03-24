'''
Created on Jan 5, 2015

@author: edwingsantos
'''

if __name__ == '__main__':
    pass

from PIL import Image
from pylab import *

im = array(Image.open('empire.jpg'))
imshow(im)
print('Click 3 points')
x = ginput(3)
print ('u clicked' , x)
show() 