import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import imutils

#Load the grayscale image
originalImage = cv2.imread('imgs/CRGS.jpeg')
grayScaleImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

#Threshold the image to obtain a binary image
thresholdValue = 50
_, binaryImage = cv2.threshold(grayScaleImage, thresholdValue, 255, cv2.THRESH_BINARY)

#Find the contours in the binary image
contours, hierarchy = cv2.findContours(binaryImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print("Number of contours found = {}".format(len(contours)))

#Check if there is at least one contour

