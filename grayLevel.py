'''
Created on Jan 5, 2015

@author: edwingsantos
'''

if __name__ == '__main__':
    pass

from scipy import ndimage
from PIL import Image
from pylab import *

im = array(Image.open('empire.jpg').convert('L'))
im1 = array(Image.open('empire.jpg'))
H = array([[1.4,0.05,-100],[0.05,1.5,-100],[0,0,1]])
im2 = ndimage.affine_transform(im, H[:2,:2],(H[0,2],H[1,2]))
figure()

gray()
imshow(im2)
#imshow(im1)
show()