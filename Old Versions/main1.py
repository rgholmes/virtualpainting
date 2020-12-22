import numpy as np
import cv2
import random
import color
import vectormatrix
from color import vibrancy, createcanvas
from vectormatrix import creategrid, creategradient

img = cv2.imread('images/starwars1.jpg')
#img2 = img.reshape((-1, 3))
#img2 = np.float32(img2)

#img_ref = vibrancy(img)

def applybrush(image):
    radius = 2

    for i in range(0, (len(grid)-1)):

        conversion = grid[i]
        h = conversion[1]
        l = conversion[0]
        color = img[conversion[1], conversion[0]]
        color = (int(color[0]), int(color[1]), int(color[2]))

        gradval = img_grad[h,l]
        #print(gradval)

        tempgrid = []

    
        target = img_grad[h,l]
        closest = 0
        opt_h = 0
        opt_l = 0
     
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:
                    k = h+1 - 1
                    m = l+j - 1
                    new = abs(img_grad[k,m] - target)
                    old = abs(closest - target)
                    if new < old:
                        opt_h = h+i - 1
                        opt_l = l+j - 1
                        closest = img_grad[h+i-1,l+j-1]

        tempgrid.append((opt_l, opt_h))
        #print(tempgrid)
        cv2.circle(img_canvas, grid[i], radius, tuple(color), -1)
  
        cv2.circle(img_canvas, tempgrid[0], radius, tuple(color), -1)


    return(image)

#img_mean = kmeans(img2, k=10, attempts=10)
img_grad = creategradient(img)

grid = creategrid(img.shape[0], img.shape[1], circles=150000)

img_canvas = createcanvas(img)

img_final = applybrush(img_canvas)

print(img_final.shape[0], img_final.shape[1])

cv2.imwrite('images/output.jpg', img_final)
