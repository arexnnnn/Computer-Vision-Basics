# In this particular section we're gonna apply certain transformations such as-
# Translation
# Rotation
# Resize
# Flip
# Crop


import numpy as np
import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('Park',img)

def translate(img,x,y):
    transMatrix = np.float32([[0,1,x],[1,0,y]])
    dimensions = (img.shape[0], img.shape[1])
    return cv.warpAffine(img, transMatrix, dimensions)

# +x --> right
# -x --> left
# +y --> down
# -y --> up

translated = translate(img,100,200)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotationPoint=None):
    (height,width) = img.shape[:2]
    if rotationPoint is None:
        rotationPoint = (width//2, height//2)

    rotationMatrix = cv.getRotationMatrix2D(rotationPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotationMatrix, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(img, -90)
cv.imshow('Rotated Rotated', rotated_rotated)

# Resizing
resized = cv. resize (img, (500,500), interpolation=cv. INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img,1)
cv.imshow('Flip', flip)

# Cropping
cropped = img[200:300, 300:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)
