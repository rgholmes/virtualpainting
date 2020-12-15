import cv2
import numpy as np
import vector
import math
from vector import VectorMatrix


img = cv2.imread('images/starwars1.jpg')

def cartoonize(rgb_image, *, num_pyr_downs=2, num_bilaterals=2):

    downsampled_img = rgb_image
    for _ in range(num_pyr_downs):
        downsampled_img = cv2.pyrDown(downsampled_img)

    for _ in range(num_bilaterals):
        filterd_small_img = cv2.bilateralFilter(downsampled_img, 31, 9, 7)

    filtered_normal_img = filterd_small_img

    for _ in range(num_pyr_downs):
        filtered_normal_img = cv2.pyrUp(filtered_normal_img)
    
    if filtered_normal_img.shape != rgb_image.shape:
        filtered_normal_img = cv2.resize(filtered_normal_img, rgb_image.shape[:2])
    
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img_blur = cv2.medianBlur(img_gray, 9)
    img_blur = cv2.GaussianBlur(img_gray, (15, 15), 0, 0)

    gray_edges = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
    #gray_edges = cv2.Canny(img_blur, 50, 100)
    rgb_edges = cv2.cvtColor(gray_edges, cv2.COLOR_GRAY2RGB)
    cv2.imshow('Image3', gray_edges)
    return cv2.bitwise_and(filtered_normal_img, rgb_edges)

#gx = cv2.Scharr(img_gray, cv2.CV_32F, 1, 0, 1) 
#gy = cv2.Scharr(img_gray, cv2.CV_32F, 0, 1, 1) 

#modimg = cv2.add(gx, gy)
#modimg = cv2.addWeighted(gx, 0.5, gy, 0.5, 0)

mod_img = cartoonize(img)

#k-size must be odd
#mg_gau = cv2.GaussianBlur(modimg, (5, 5), 0, 0)
#img_gau_inv = 255 - (img_gau * 255)

#edges = cv2.Canny(img, 50, 100)
#laplacian64 = cv2.Laplacian(img_gray, cv2.CV_64F)
#laplacian = np.uint8(np.absolute(laplacian64))

#img_cvt = cv2.cvtColor(img_gau_inv, cv2.COLOR_GRAY2RGB)
#cv2.imshow('gx', gx)
#cv2.imshow('gy', gy)
#cv2.imshow('Image2', img_cvt)
#cv2.imshow('Image2', img_gau)
cv2.imshow('Image', mod_img)

cv2.waitKey(0)