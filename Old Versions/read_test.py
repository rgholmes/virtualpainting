import cv2 as cv
import sys
import numpy as np

img = cv.imread('images/starwars1.jpg')

#def dodge(image, mask):
#    return cv.divide(image, 255 - mask, scale=256)

gray_image = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
inv_gray = 255 - gray_image
blurred_image = cv.GaussianBlur(inv_gray, (21, 21), 0, 0)
gray_sketch = cv.divide(gray_image, 255 - blurred_image, scale = 256)

def convert_to_pencil_sketch(image):
    gray_image = cv.cvtcolor(image, cv.COLOR_RGB2GRAY)
    blurred_image = cv.GaussianBlur(gray_image, (21, 21), 0, 0)
    gray_sketch = cv.divide(gray_image, blurred_image, scale = 256)
    return cv.cvtColor(gray_sketch, cv.COLOR_Gray2RGB)

cv.imshow('image', gray_sketch)
cv.waitKey(0)