import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while (1):

    _,frame = cap.read()

    hsv1 = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    hsv2 = hsv1.copy()
    hsv3 = hsv1.copy()
    hsv4 = hsv1.copy()
    lower_blue = np.array([100, 100,100])
    upper_blue = np.array([140,255,255])

    lower_green = np.array([50,100,100])
    upper_green = np.array([70,255,255])

    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 100, 100])
    upper_red2 = np.array([179, 255, 255])

    mask_blue = cv.inRange(hsv1, lower_blue, upper_blue)
    mask_green = cv.inRange(hsv2, lower_green, upper_green)
    mask_red1 = cv.inRange(hsv3, lower_red1, upper_red1)
    mask_red2 = cv.inRange(hsv3, lower_red2, upper_red2)
    mask_red = mask_red1 | mask_red2

    blue = cv.bitwise_and(frame, frame, mask=mask_blue)
    green = cv.bitwise_and(frame, frame, mask=mask_green)
    red = cv.bitwise_and(frame, frame, mask=mask_red)

    #final = blue + green + red
    final = cv.add(cv.add(blue, green), red)


    cv.imshow('frame',frame)
    cv.imshow('mask_blue', mask_blue)
    cv.imshow('mask_green', mask_green)
    cv.imshow('mask_red', mask_red)
    cv.imshow('final result', final)
    k = cv.waitKey(5) & 0xFF 
    if k == 27: break

cap.release()
cv.destroyAllWindows()