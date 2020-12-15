import numpy as np
import cv2
import random
import color
import vectormatrix
from color import vibrancy
from vectormatrix import creategrid, creategradient

img = cv2.imread('images/starwars3.jpg')
#img2 = img.reshape((-1, 3))
#img2 = np.float32(img2)

img_ref = vibrancy(img)

img_canvas = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
#create a blank canvas with BGR values
img_canvas[:] = (31, 46, 100)

def applybrush(image):

    for i in range(0, (len(grid)-1)):

        conversion = grid[i]
        h = conversion[1]
        l = conversion[0]
        color = img_ref[h, l]
        color = (int(color[0]), int(color[1]), int(color[2]))

        radval = int(img_grad[h,l])

        if radval < mean:
            if radval < (mean - std):
                radius = 9
            else:
                radius = 6
        elif radval > mean:
            if radval < (mean + std):
                radius = 4
            else:
                radius = 3
        else:
            radius = 6

        cv2.circle(img_canvas, grid[i], radius, tuple(color), -1)

    return(image)

#img_mean = kmeans(img2, k=10, attempts=10)
img_grad = creategradient(img)
mean, std = cv2.meanStdDev(img_grad)
print(mean)
print(std)

grid = creategrid(img.shape[0], img.shape[1], circles=90000)
img_final = applybrush(img_canvas)

cv2.imwrite('images/output.jpg', img_grad)
