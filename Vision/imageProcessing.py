import cv2
import numpy as np
from matplotlib import pyplot as plt

#Read a color image and convert it to grayscale
originalImage = cv2.imread('imgs/CRGS.jpeg', cv2.IMREAD_GRAYSCALE)

gaussianSmooth = True

if gaussianSmooth:
    #Define kernel size and sigma value for Gaussian smoothing
    kernelSize = 199
    sigma = 5

    #Create 2D Gaussian kernel
    gaussianKernel = cv2.getGaussianKernel(kernelSize, sigma)
    #Compute the output of two vectors
    gaussianKernel = np.outer(gaussianKernel, gaussianKernel)

    #Use OpenCV functions to perform convolution
    gaussianImage = cv2.filter2D(originalImage, -1, gaussianKernel)

    #plot the results
    plt.subplot(1,2,1)
    plt.imshow(originalImage, cmap='gray')
    plt.title("Original Image")
    plt.subplot(1,2,2)
    plt.imshow(gaussianImage, cmap='gray')
    plt.title("Gaussian Smoothed Image")
    plt.show()

