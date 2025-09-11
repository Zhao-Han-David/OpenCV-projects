import cv2 as cv
import numpy as np

blue = np.uint8([[[255,0,0]]])
green = np.uint8([[[0,255,0]]])
red = np.uint8([[[0,0,255]]])

hsv_blue = cv.cvtColor(blue , cv.COLOR_BGR2HSV)
hsv_green = cv.cvtColor(green , cv.COLOR_BGR2HSV)
hsv_red = cv.cvtColor(red, cv.COLOR_BGR2HSV)

print(hsv_green)
print(hsv_blue)
print(hsv_red)