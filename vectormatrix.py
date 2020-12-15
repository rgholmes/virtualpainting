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

    alpha = 3 # Contrast control (1.0-3.0)
    beta = 20 # Brightness control (0-100)

    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_lap = cv2.Laplacian(img_gray, cv2.CV_16S, ksize=3)
    img_lap = cv2.convertScaleAbs(img_lap, alpha=alpha, beta=beta)
    img_blur = cv2.GaussianBlur(img_lap, (13, 13), 0, 0)
    img_blur = cv2.GaussianBlur(img_blur, (13, 13), 0, 0)
    return(img_blur)

