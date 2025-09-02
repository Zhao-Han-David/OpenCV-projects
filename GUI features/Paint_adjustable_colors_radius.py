import numpy as np
import cv2 as cv

def nothing(x):
    pass

# create trackbars for color change
drawing = True
cv.namedWindow('image')
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)
cv.createTrackbar('raza', 'image', 0,255, nothing)

# create switch for ON/OFF functionality

def paint(event, x,y, flags, param):
    global drawing, raza, r,g,b
    if(event == cv.EVENT_LBUTTONDOWN):
        drawing=True
        cv.circle(image, (x,y), raza, (b,g,r), thickness=-1)

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            cv.circle(image, (x,y), raza, (b,g,r), thickness=-1)
    
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.circle(image,(x,y),raza, (b,g,r), thickness=-1)


image = np.zeros((1800,1800,3), np.uint8)
cv.setMouseCallback('image',paint)

while(1):
    cv.imshow('image',image)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')
    raza = cv.getTrackbarPos('raza', 'image')
cv.destroyAllWindows()

