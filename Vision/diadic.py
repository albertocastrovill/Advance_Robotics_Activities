import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
arrayA = np.array([[1,2,3],[4,5,6],[7,8,9]])
arrayB = np.array([[1,2,3],[4,5,6],[7,8,9]])
arraySize = len(arrayA)

addResult = np.zeros_like(arrayA)

for i in range(arraySize):
    for j in range(arraySize):
        addResult[i][j] = arrayA[i][j] + arrayB[i][j]

print(addResult)
"""

#Load black  & white images
img1 = cv2.imread('imgs/spaceXlogo.jpeg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('imgs/rocket01.png', cv2.IMREAD_GRAYSCALE)

resultImage = np.zeros((600,600), dtype=np.uint8)

for i in range(600):
    for j in range(600):
        pixel1 = img1[i][j]
        pixel2 = img2[i][j]
        resultingPixel = pixel1 + pixel2
        resultImage[i][j] = np.uint8(resultingPixel)

cv2.imshow('resultImage', resultImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

        