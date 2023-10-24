import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

# Open the csv file for reading
asphaltData = pd.read_csv('ASPHALT01_UDEMPLBLD01F28MOD.csv', header=None)
earthData = pd.read_csv('EARTH01_UDEMSCFLDF20MOD.csv', header=None)
grassData = pd.read_csv('GRASS01_UDEMSMBRDF22MOD.csv', header=None)

# Histogram for Data 
plt.figure(figsize=(8,6))

hist1, bins1, _ = plt.hist(asphaltData[1], bins=15, density=True, alpha=0.7, color='gray', label='Asphalt')
hist2, bins2, _ = plt.hist(earthData[1], bins=15, density=True, alpha=0.7, color='green', label='Earth')
hist3, bins3, _ = plt.hist(grassData[1], bins=15, density=True, alpha=0.7, color='blue', label='Grass')

# Fit a normal distribution to each dataset
params1 = norm.fit(asphaltData[1])
params2 = norm.fit(earthData[1])
params3 = norm.fit(grassData[1])

x = np.linspace(min(np.min(asphaltData[1]), np.min(earthData[1]), np.min(grassData[1])),
                max(np.max(asphaltData[1]), np.max(earthData[1]), np.max(grassData[1])))

plt.plot(x, norm.pdf(x,params1[0],params1[1]), 'r-', label='PDF of Asphalt')
plt.plot(x, norm.pdf(x,params2[0],params2[1]), 'g-', label='PDF of Earth')
plt.plot(x, norm.pdf(x,params3[0],params3[1]), 'b-', label='PDF of Grass')

plt.xlabel('Intensity')
plt.ylabel('Probability Density')
plt.legend()
plt.show()

# Abrir el archivo csv para leer
newData = pd.read_csv('dataSetF12.csv')

newData = newData['intensity'].values

"""
#Método 1: Usando for loops = lento

# Clasificar cada punto en el nuevo conjunto de datos
asphalt_count = 0
earth_count = 0
grass_count = 0

for point in newData:
    p_asphalt = norm.pdf(point, loc=params1[0], scale=params1[1])
    p_earth = norm.pdf(point, loc=params2[0], scale=params2[1])
    p_grass = norm.pdf(point, loc=params3[0], scale=params3[1])
    
    if p_asphalt > p_earth and p_asphalt > p_grass:
        asphalt_count += 1
    elif p_earth > p_asphalt and p_earth > p_grass:
        earth_count += 1
    else:
        grass_count += 1

total_points = len(newData)
print(f"Cantidad de Puntos Analizados: {total_points}")
print(f"Porcentaje de Asfalto: {(asphalt_count / total_points) * 100:.2f}%")
print(f"Porcentaje de Tierra: {(earth_count / total_points) * 100:.2f}%")
print(f"Porcentaje de Pasto: {(grass_count / total_points) * 100:.2f}%")
"""

# Método 2: Usando máscaras = rápido

# Calcula las densidades de probabilidad
p_asphalt = norm.pdf(newData, loc=params1[0], scale=params1[1])
p_earth = norm.pdf(newData, loc=params2[0], scale=params2[1])
p_grass = norm.pdf(newData, loc=params3[0], scale=params3[1])

# Clasificar datos usando las densidades de probabilidad
asphalt_mask = (p_asphalt > p_earth) & (p_asphalt > p_grass)
earth_mask = (p_earth > p_asphalt) & (p_earth > p_grass)

# Contar los puntos clasificados
asphalt_count = np.sum(asphalt_mask)
earth_count = np.sum(earth_mask)
grass_count = len(newData) - asphalt_count - earth_count

# Imprimir resultados
total_points = len(newData)
print(f"Cantidad de Puntos Analizados: {total_points}")
print(f"Porcentaje de Asfalto: {(asphalt_count / total_points) * 100:.2f}%")
print(f"Porcentaje de Tierra: {(earth_count / total_points) * 100:.2f}%")
print(f"Porcentaje de Pasto: {(grass_count / total_points) * 100:.2f}%")

# Determina el terreno observado en base a los conteos
if asphalt_count > earth_count and asphalt_count > grass_count:
    terreno_observado = "Asfalto"
elif earth_count > asphalt_count and earth_count > grass_count:
    terreno_observado = "Tierra"
else:
    terreno_observado = "Pasto"

print(f"Terreno Observado en el Dataset es mayormente {terreno_observado}")





