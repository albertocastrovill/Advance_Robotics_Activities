import numpy as np
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt

#Define the size and standard deviation of the Gaussian kernel
kernel_size = 5
std_dev = 1.0

#Generate the Gaussian kernel
gaussian_kernel = np.fromfunction(
    lambda x,y: (1/(2*np.pi*std_dev**2))*
    np.exp((-(x-(kernel_size-1)/2)**2-(y-(kernel_size-1)/2)**2)/(2*std_dev**2)), 
    (kernel_size, kernel_size))

#Normalize the kernel
gaussian_kernel = gaussian_kernel/np.sum(gaussian_kernel)

#Display the kernel
print("Gaussian Kernel:")
print(gaussian_kernel)

#Optionally, you can also visualize the kernel using Matplotlib
plt.imshow(gaussian_kernel, cmap='viridis', interpolation='none')
plt.title("Gaussian Kernel")
plt.colorbar()
plt.show()
