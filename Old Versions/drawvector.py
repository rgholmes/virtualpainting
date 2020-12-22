import numpy as np
import cv2
import random
import scipy
from scipy.interpolate import UnivariateSpline

img = cv2.imread('images/output.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def spline_to_lookup_table(spline_breaks: list, break_values: list):
    spl = UnivariateSpline(spline_breaks, break_values)
    return spl(range(256))

x = [0, 128, 180, 255]
y = [0, 192, 200, 255]
myLUT = spline_to_lookup_table(x,y)
img_curved = cv2.LUT(img, myLUT).astype(np.uint8)




def drawline(image, radius, hieght, width):

    #grid = []
    point0 = []
    point1 = []

    #for i in range(circles):
    #x_0 = random.randint(0, width - 1) 
    #y_0 = random.randint(0, hieght - 1)

    #x_0 = random.randint(0, 400) 
    #y_0 = random.randint(0, 400)

    #x_1 = random.randint(0, 400) 
    #y_1 = random.randint(0, 400)

    #if x_0 > x_1:
     #   x_0, x_1 = x_1, x_0
     #   print('switched')
    
    #cv2.circle(img, (x_0, y_0), 10, (255,0,0), 0)

    #cv2.circle(img, (x_1, y_1), 5, (255,0,0), 0)

    x_0 = 100
    y_0 = 150

    x_1 = 50
    y_1 = 170


    cv2.circle(img, (x_0, img.shape[0]-y_0), 10, (255,0,0), 0)
    cv2.circle(img, (x_1, img.shape[0]-y_1), 5, (255,0,0), 0)


    point0.append((x_0,y_0))
    point1.append((x_1,y_1))

    #x_axis = abs(x_1 - x_0)
    #y_axis = abs(y_1 - y_0)

    #in opencv the x value is the same but the y value is flipped
    m = (y_1-y_0)/(x_1-x_0)

    x_mid = int((x_1 - x_0)/2)
    y_mid = int((y_1 - y_0)/2)
    #x_axis = abs(x_1 - x_mid)
    #y_axis = abs(y_1 - y_mid)

    x_axis = abs(x_1 - x_0)
    y_axis = abs(y_1 - y_0)

    print('slope = ' + str(m))
    print('Point 0 = ' + str(point0[0]))
    print('Point 1 = ' + str(point1[0]))

    if x_axis > y_axis:
        if x_0 <= x_1:
            for i in range(x_axis):
                j = int(y_0 - m*i)
                img[img.shape[0] - j, x_0 + i] = 255
        else:
            for i in range(-x_axis, 0):
                j = int(y_0 - m*i)
                img[img.shape[0] - y_axis - j, x_1 - i] = 255
    #elif x_axis < y_axis:

    


    #if abs(m) < 1:
    #    print('x axis')
    #    for i in range(x_axis):
    #        j = int(m*i+y_0)
    #        #opencv so hieght width (y,x)
    #        img[j, x_mid + i] = 255
    #    print(1)
    #elif m >= 1:
    #    for j in range(y_axis):
    #        i = int((j)/m + x_0)
    #        img[j + y_0, i] = 255
    #    print(2)
    #else:
    #    for j in range(y_axis):
    #        i = int((j)/m - x_0)
    #        img[j + y_0, i + j] = 255
    #    print(3)

    #grid.append((x,y))

    #color = img[x,y]

    #for i in range(x-radius, x+radius):
    #    for j in range(y-radius, y+radius):
    #
    #        point = int((x-i)** 2 + (y-j)**2)
    #        
    #        if point == (radius**2):
    #            img[i,j] = 255
            

    #cv2.circle(img, grid[0], radius, (255,0,0), 0)



    return(image)
white = [0, 0, 0]
blue = 255

img_canvas = np.zeros((40, 40), np.uint8)
#create a blank canvas with BGR values
img_canvas[:] = white


def createfunction(image):
    x1 = 3
    y1 = 2
    x2 = 9
    y2 = 6
    x3 = 5
    y3 = 3

    #img[y1, x1] = blue
    img[y2, x2] = blue

    #https://math.stackexchange.com/questions/680646/get-polynomial-function-from-3-points

    a = (x1*(y3-y2)+x2*(y1-y3)+x3*(y2-y1))/((x1-x2)*(x1-x3)*(x2-x3))

    b = (y2-y1)/(x2-x1)-a*(x1-x2)

    c = y1 - a*x1**2 - b*x1

    print(a, b, c)

    param = abs(x1-x2)

    for x in range(0, 39):
        y = int(a*x**2 + b*x + c) 
        img[y, x] = 255
    
    return image

#img_drawn = drawline(img, radius=9, hieght=img.shape[0], width=img.shape[1])
img_drawn = createfunction(img_canvas)
cv2.imwrite('images/vector_output.jpg', img_drawn)