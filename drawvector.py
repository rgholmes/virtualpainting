import numpy as np
import cv2
import random

img = cv2.imread('images/output.jpg')

def drawline(image, length, hieght, width):

    grid = []

    #for i in range(circles):
    x = random.randint(0, width - 1) 
    y = random.randint(0, hieght - 1)
    grid.append((x,y))



    return(image)
    
img_drawn = drawline(img, length=200, hieght=img.shape[0], width=img.shape[1])

cv2.imwrite('images/vector_output.jpg', img)