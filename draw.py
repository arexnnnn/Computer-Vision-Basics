# Drawing various shapes on our image

import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') # Args = height,width,no of color channels.
cv.imshow('Blank',blank)                     # uint8 = datatype of an image

# Paint the image a certain color

blank[200:250, 250:300] = 255,0,0
cv.imshow('Blue', blank)

# Draw a rectangle

cv.rectangle(blank, (0,0), (150,150), (0,0,255), thickness=2)
cv.imshow('Rectangle', blank)

cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,255), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

# Draw a circle

cv.circle(blank, (blank.shape[1], blank.shape[0]), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank)

# Draw a line

cv.line(blank, (100,200), (400,500), (0,255,0), thickness=3)
cv.imshow('Line', blank)

# Write text

cv.putText(blank, 'Orewa Kaizoku', (100,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)