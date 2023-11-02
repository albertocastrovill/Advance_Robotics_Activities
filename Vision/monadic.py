import cv2
import numpy as np
import matplotlib.pyplot as plt

originalImage = cv2.imread('imgs/CRGS.jpeg')
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
imageHistogram = cv2.calcHist([grayImage], [0], None, [256], [0, 256])

plt.figure()
plt.subplot(1,3,1)
colorImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)
plt.imshow(colorImage)
plt.title("Color Image")
plt.subplot(1,3,2)
#plt.imshow(originalImage)
plt.imshow(grayImage, cmap='gray')
plt.title("Gray Image")
plt.subplot(1,3,3)
plt.hist(grayImage.ravel(), 256, [0, 256])
plt.xlim([0, 256])
plt.tight_layout()
plt.title("Histogram")

binarization = True
if binarization:
    #define the threshold value
    #thresholdValue = 128
    upperThresholdValue = 180
    lowerThresholdValue = 150
    #apply the thresholding
    ret, binaryImage = cv2.threshold(grayImage, lowerThresholdValue, upperThresholdValue, cv2.THRESH_BINARY)
    #display the binary image
    plt.figure(2)
    plt.imshow(binaryImage, cmap='gray')
    plt.title("Binary Image")
    saveImage = False
    if saveImage:
        fileName = "imgs/binaryImage.png"
        cv2.imwrite(fileName, binaryImage)
        print(f"Image saved as {fileName}")

    invertedBinaryImage = True
    

plt.axis('off')
plt.show()