# Basic functions

import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

# GreyScaling
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv. GaussianBlur(img, (7,7) , cv.BORDER_DEFAULT) # intensity of blur
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175) # passing the image and 2 threshold values
cv.imshow('Canny Edges', canny)

# Dilating
dilated = cv.dilate(canny, (7,7), iterations=3)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv. imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropped
cropped = img[100:200, 300:350]
cv.imshow('Cropped', cropped)

cv.waitKey(0)