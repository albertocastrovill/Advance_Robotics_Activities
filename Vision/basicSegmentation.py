import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import imutils

#Load the grayscale image
originalImage = cv2.imread('img_triangle/triangle1.jpg')
grayScaleImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

#Threshold the image to obtain a binary image
thresholdValue = 50
_, binaryImage = cv2.threshold(grayScaleImage, thresholdValue, 255, cv2.THRESH_BINARY)

#Find the contours in the binary image
contours, hierarchy = cv2.findContours(binaryImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print("Number of contours found = {}".format(len(contours)))

#Check if there is at least one contour
if contours:
    # Take the first contour (assuming it's the only one)
    contour = contours[len(contours)-1]

    # Calculate moments for the region
    moments = cv2.moments(contour)

    # Calculate the centroid of the region
    cx = int(moments['m10'] / moments['m00'])
    cy = int(moments['m01'] / moments['m00'])

    # Calculate the area of the region
    area = cv2.contourArea(contour)

    # Calculate the central moments
    mu20 = moments['mu20'] / moments['m00']
    mu02 = moments['mu02'] / moments['m00']
    mu11 = moments['mu11'] / moments['m00']

    # Compute the inertia matrix J
    J = np.array([[mu20, mu11], [mu11, mu02]])

    # Calculate eigenvalues of the inertia matrix
    eigenvalues, eigenvectors = np.linalg.eig(J)

    # Determine the major eigenvector (corresponding to the larger eigenvalue)
    majorEigenvector = eigenvectors[:, np.argmax(eigenvalues)]

    # Compute the orientation angle using atan2
    orientationAngle = math.atan2(majorEigenvector[1], majorEigenvector[0])

    # Convert the angle to degrees
    orientationAngleDeg = math.degrees(orientationAngle)
    # Print the properties of the single region
    print("Region:")
    print(f"Centroid: ({cx}, {cy})")
    print(f"Area: {area}")
    print(f"Central Moments:")
    print(f"  mu20: {mu20}")
    print(f"  mu02: {mu02}")
    print(f"  mu11: {mu11}")
    print("Eigenvalues of Inertia Matrix J:", eigenvalues)
    print("Eigenvectors of Inertia Matrix J:")
    print("  Eigenvector 1:", eigenvectors[:, 0])
    print("  Eigenvector 2:", eigenvectors[:, 1])
    print("Orientation Angle:", orientationAngleDeg)
    #print(f"Moments: {moments}")

    # Draw the contour and centroid on the original image
    newColorImage = cv2.cvtColor(binaryImage, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(newColorImage, [contour], 0, (0, 255, 0), 2)
    cv2.circle(newColorImage, (cx, cy), 5, (0, 255, 0), -1)  # -1 fills the circle
    """
    # OPTIONAL Draw the ellipse
    # Fit an ellipse to the contour
    ellipse = cv2.fitEllipse(contour)
    cv2.ellipse(newColorImage, ellipse, (0, 0, 255), 2)
    # Extract major and minor axes from the ellipse parameters
    center, axes, angle = ellipse
    major_axis = int(max(axes) / 2)
    minor_axis = int(min(axes) / 2)
    # Calculate endpoints for major and minor axes
    major_axis_endpoint_x = int(center[0] - major_axis * math.cos(math.radians(orientationAngleDeg)))
    major_axis_endpoint_y = int(center[1] - major_axis * math.sin(math.radians(orientationAngleDeg)))

    minor_axis_endpoint_x = int(center[0] + minor_axis * math.sin(math.radians(orientationAngleDeg)))
    minor_axis_endpoint_y = int(center[1] - minor_axis * math.cos(math.radians(orientationAngleDeg)))
    # Draw major and minor axes
    cv2.line(newColorImage, (int(center[0]), int(center[1])), (major_axis_endpoint_x, major_axis_endpoint_y), (255, 0, 0), 2)
    cv2.line(newColorImage, (int(center[0]), int(center[1])), (minor_axis_endpoint_x, minor_axis_endpoint_y), (255, 0, 0), 2)
    """
    # Display the original image with contour and centroid
    resizedNewColorImage =imutils.resize(newColorImage, width=800)
    cv2.imshow('Image with Contour and Centroid', resizedNewColorImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No contours found.")

