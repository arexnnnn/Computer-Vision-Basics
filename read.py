import cv2 as cv

# Reading an image

# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat', img)
# cv.waitKey(0)

# Reading Videos

capture = cv.VideoCapture('Videos/dog.mp4') # capture is an instance variable of VideoCapture class.
while True:
    isTrue, frame = capture.read() # read the video frame by frame and return if the frames are readable or not.
    cv.imshow('Video', frame)
    if cv.waitKey(20) and 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()