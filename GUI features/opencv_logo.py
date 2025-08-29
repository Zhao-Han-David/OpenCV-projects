import cv2 as cv
import numpy as np

img = np.ones((900,900,3), np.uint8) * 255

pt1=(450,200)
pt2=(200,600)
pt3=(700,600)
pt4=(950,200)
pt5=(575,400)

pts = np.array([pt1, pt2, pt3], np.int32)
pts = pts.reshape((-1,1,2))

pts2 = np.array([pt5, pt3, pt4], np.int32)
pts2 = pts2.reshape((-1,1,2))

cv.circle(img, (450,200), 150, (0,0,255), 100, cv.LINE_AA)
cv.circle(img, (200,600), 150, (0,255,0), 100, cv.LINE_AA)
#cv.polylines(img, [pts], isClosed=True, color=(255,255,255), thickness=1)
cv.fillPoly(img, [pts], color=(255,255,255))

cv.circle(img, (700,600), 150, (255,0,0), 100, cv.LINE_AA)

cv.fillPoly(img, [pts2], color=(255,255,255))

cv.imshow("OpenCV logo", img)
cv.waitKey(0)
cv.destroyAllWindows()