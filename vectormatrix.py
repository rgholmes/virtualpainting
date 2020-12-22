import numpy as np
import cv2
import random

def creategrid(hieght, width, circles):

    grid = []

    for i in range(circles):
        x = random.randint(0, width - 1) 
        y = random.randint(0, hieght - 1)
        grid.append((x,y))

    random.shuffle(grid)
    return grid

def creategradient(image):

    #alpha = 3 # Contrast control (1.0-3.0)
    #beta = 20 # Brightness control (0-100)

    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    h, w, c = image.shape
    h = h-1
    w = w-1
    #img_lap = cv2.Laplacian(img_gray, cv2.CV_16S, ksize=3)
    #img_lap = cv2.convertScaleAbs(img_lap, alpha=alpha, beta=beta)
    #img_blur = cv2.GaussianBlur(img_lap, (13, 13), 0, 0)
    #img_blur = cv2.GaussianBlur(img_blur, (13, 13), 0, 0)

    #canny-last two values are thresholds
    img_edges = cv2.Canny(image, 75, 150)

    #for i in range(0, w):
    #    for j in range(0, h):
    #        value = img_gray[j, i]
    #        if value > 150:
    #            img_edges = img_gray[j, i]
    #        else:
    #            img_edges = 255

    #return(img_blur)
    return(img_edges)

def findhighlight(image, percentage):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    img_range = cv2.inRange(image, 225, 255)
    return(img_range) 

