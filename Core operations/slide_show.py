import cv2 as cv
import numpy as np
import os

folder = os.path.join("photos", "1920x1080p")
images = []
height = 300
width = 500


for filename in sorted(os.listdir(folder)):
    
    path = os.path.join(folder, filename)
    img = cv.imread(path)
    if img is not None:
        img_resized = cv.resize(img, (width, height))
        images.append(img_resized)


for i in range(len(images) - 1):
    img1 = images[i]
    img2 = images[i+1]
    for alpha in np.linspace(0, 1, num=30): 
        beta = 1 - alpha
        blended = cv.addWeighted(img1, beta, img2, alpha, 0)
        cv.imshow('slideshow', blended)
        cv.waitKey(30)  

cv.destroyAllWindows()  
