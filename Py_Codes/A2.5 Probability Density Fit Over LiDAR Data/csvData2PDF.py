import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

# Open the csv file for reading
asphaltData = pd.read_csv('ASPHALT01_UDEMPLBLD01F28MOD.csv', header=None)
earthData = pd.read_csv('EARTH01_UDEMPLBLD01F28MOD.csv', header=None)
grassData = pd.read_csv('GRASS01_UDEMPLBLD01F28MOD.csv', header=None)

#print(asphaltData[1])

# Create histograms
plt.figure(figsize=(8,6))

# Histogram for Data 1
hist1, bins1, _ = plt.hist(asphaltData[1], bins=15, density=True, alpha=0.7, color='gray', label='Asphalt')
hist2, bins2, _ = plt.hist(earthData[1], bins=15, density=True, alpha=0.7, color='green', label='Earth')
hist3, bins3, _ = plt.hist(grassData[1], bins=15, density=True, alpha=0.7, color='blue', label='Grass')

# Fit a normal distribution to Data 1
params1 = norm.fit(asphaltData[1])
params2 = norm.fit(earthData[1])
params3 = norm.fit(grassData[1])

methodOne = False
if methodOne:
    pdf1 = norm.pdf(bins1, loc=params1[0], scale=params1[1])
    # Overlay the PDF curve for Data 1 on the histogram
    plt.plot(bins1, pdf1, 'r-', linewidth=2, label='PDF of Asphalt')
else:
    x = np.linspace(np.min(asphaltData[1]), np.max(asphaltData[1]))
    # Overlay the PDF curve for Data 1 on the histogram
    plt.plot(x, norm.pdf(x,params1[0],params1[1]),)
plt.xlabel('Intensity')
plt.ylabel('Probability Density')
plt.show()

