import cv2 
import math
import numpy as np

class VectorMatrix:
    def from_gradient(gray):
            fieldx = cv2.Scharr(gray, cv2.CV_32F, 1, 0) / 15.36
            fieldy = cv2.Scharr(gray, cv2.CV_32F, 0, 1) / 15.36

            return VectorMatrix(fieldx, fieldy) 