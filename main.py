import numpy as np
import cv2
import random
import color
import vectormatrix
from matplotlib import pyplot as plt
from color import vibrancy, findcolor
from vectormatrix import creategrid, creategradient, findhighlight

img = cv2.imread('images/starwars3.jpg')
img_color = cv2.imread('images/color.png')
#img2 = img.reshape((-1, 3))
#img2 = np.float32(img2)

img_ref = vibrancy(img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


img_canvas = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
#create a blank canvas with BGR values
img_canvas[:] = (31, 46, 100)

def applybrush(image):

    for i in range(0, (len(grid)-1)):

        conversion = grid[i]
        h = conversion[1]
        l = conversion[0]

        #color = img_ref[h, l]
        color = img[h, l]
        color = (int(color[0]), int(color[1]), int(color[2]))

        alt_color = findcolor(img, img_color, r=int(color[0]), g=int(color[1]), b=int(color[2]))



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



img_range = findhighlight(img_gray, percentage=10)
#hist_plt = plt.hist(img.ravel(),256,[0,256])

#img_eq = cv2.equalizeHist(img)

#img_comb = cv2.addWeighted(img_grad, .5, img_edges, .5, 0)

grid = creategrid(img.shape[0], img.shape[1], circles=100)
img_final = applybrush(img_canvas)

#cv2.imwrite('images/gradient.jpg', img_grad)
cv2.imwrite('images/range.jpg', img_range)

#cv2.imwrite('images/histogram.jpg', hist_plt)
#cv2.imwrite('images/grayscale.jpg', img_gray)
cv2.imwrite('images/output.jpg', img_final)
