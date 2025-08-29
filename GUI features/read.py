import cv2 as cv

#Reading Images

# img = cv.imread('Photos/large.jpeg')

# cv.imshow('Cat', img)

# cv.waitKey(0)


# Reading Videos

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()   