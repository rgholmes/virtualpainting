import numpy as np
import cv2
import random

img = cv2.imread('images/starwars3.jpg')

def createcanvas(image):
    img_canvas = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
    #create a blank canvas with BGR values
    img_canvas[:] = (31, 46, 100)
    return img_canvas

def findcolor(image, color_pallete, r, g, b):

    m1 = np.array([r],[g],[b])
    m2 = np.array([,,],[[,,])





    return(tuple(color))

def vibrancy(image):

    b = image[:,:,0]
    g = image[:,:,1]
    r = image[:,:,2]
    alpha = 2 # Contrast control (1.0-3.0)
    beta = 0 # Brightness control (0-100)

    b = cv2.convertScaleAbs(b, alpha=alpha, beta=beta)
    g = cv2.convertScaleAbs(g, alpha=1, beta=beta)
    r = cv2.convertScaleAbs(r, alpha=1.5, beta=beta)
    img_bgr = cv2.merge((b,g,r))

    return(img_bgr)

def kmeans(image, k, attempts):
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

    ret, label, center=cv2.kmeans(img2, k, None, criteria, attempts, cv2.KMEANS_RANDOM_CENTERS)
    #converts into integers
    center = np.uint8(center) 
    res = center[label.flatten()]

    #reshape into original image
    res2 = res.reshape((img.shape))

    return(res2)

#img_vib = vibrancy(img)
    
#cv2.imwrite('images/color_blue.jpg', img_vib)
