# Why rescaling is required?

# Sometimes your camera doesn't support higher resolution more than its capacity so it needs to be rescaled
# to a moderate so that it can be easily worked on.

import cv2 as cv
def rescaleFrame(frame, scale=0.75):
    # Existing Media, Live Videos, Webcams
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height) # A tuple of width & height to get the dimensions.

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeResolution(width, height):
    # Live Video, Webcams
    capture.set(3,width)
    capture.set(4,height)

capture = cv.VideoCapture('Videos/dog.mp4')

img = cv.imread('Photos/cat.jpg')
cv.imshow('Image', img)

img_resized = rescaleFrame(img)
cv.imshow('Resized Image', img_resized)

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=0.5)

    cv.imshow('Video', frame)
    cv.imshow('Resized Video', frame_resized)

    if cv.waitKey(20) and 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()