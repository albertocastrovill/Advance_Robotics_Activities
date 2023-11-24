import pandas as pd
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.ndimage import uniform_filter1d, convolve1d

# Cargando el archivo CSV con los datos LiDAR
lidar_data_path = 'JDC02_TRCF2.csv'
lidar_data = pd.read_csv(lidar_data_path)

# Creando una gráfica 3D tipo scatter plot de los datos LiDAR
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Asignando los ejes
ax.scatter(lidar_data['Points:0'], lidar_data['Points:1'], lidar_data['Points:2'], c='blue', marker='.')

# Etiquetas y título
ax.set_xlabel('X Coordinates')
ax.set_ylabel('Y Coordinates')
ax.set_zlabel('Z Coordinates')
ax.set_title('3D Scatter Plot of LiDAR Data')

# Mostrar la gráfica
plt.show()

# Filtrando los datos para obtener aquellos cuya distancia sea igual o menor a 10 metros
central_region_data = lidar_data[lidar_data['distance_m'] <= 10]

# Creando una gráfica 3D tipo scatter plot para el nuevo conjunto de datos
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Asignando los ejes para la región central
ax.scatter(central_region_data['Points:0'], central_region_data['Points:1'], central_region_data['Points:2'], c='red', marker='.')

# Etiquetas y título
ax.set_xlabel('X Coordinates')
ax.set_ylabel('Y Coordinates')
ax.set_zlabel('Z Coordinates')
ax.set_title('3D Scatter Plot of LiDAR Data (Central Region)')

# Mostrar la gráfica
plt.show()

# Selección de datos donde laser_id es 5
laser_5_data = central_region_data[central_region_data['laser_id'] == 5]

# Ordenar los datos por 'azimuth' para aplicar filtros de manera coherente
laser_5_data_sorted = laser_5_data.sort_values(by='azimuth')

# Aplicar un filtro promediador de 1x3 a la columna de distancia
filtered_distance = uniform_filter1d(laser_5_data_sorted['distance_m'], size=3)

# Definir un kernel para el filtro de gradiente simétrico de 1x7
gradient_kernel = [-1, -2, -1, 0, 1, 2, 1]

# Aplicar el filtro de gradiente
gradient_filtered_distance = convolve1d(filtered_distance, gradient_kernel)

# Preparar datos para gráficas
azimuth = laser_5_data_sorted['azimuth']
original_distance = laser_5_data_sorted['distance_m']

# Convertir a arrays de NumPy antes de graficar
azimuth_np = azimuth.to_numpy()
original_distance_np = original_distance.to_numpy()

"""
# Crear una sola gráfica 2D que combine las tres visualizaciones
fig, ax = plt.subplots(figsize=(12, 8))

# Gráfica 1: Azimuth vs Distancia Original
ax.plot(azimuth_np, original_distance_np, label='Original Distance', color='blue')

# Gráfica 2: Azimuth vs Filtro Promedio
ax.plot(azimuth_np, filtered_distance, label='Filtered Average', color='orange')

# Gráfica 3: Azimuth vs Filtro Gradiente
ax.plot(azimuth_np, gradient_filtered_distance, label='Gradient Filtered', color='green')

# Configuración de la gráfica
ax.set_title('Azimuth vs Distance Analysis')
ax.set_xlabel('Azimuth')
ax.set_ylabel('Distance (m)')
ax.legend()

# Mostrar la gráfica
plt.tight_layout()
plt.show()
"""


# Crear gráficas 2D
fig, axs = plt.subplots(3, 1, figsize=(12, 18))

# Gráfica 1: Azimuth vs Distancia Original
axs[0].plot(azimuth_np, original_distance_np, label='Original Distance')
axs[0].set_title('Azimuth vs Original Distance')
axs[0].set_xlabel('Azimuth')
axs[0].set_ylabel('Distance (m)')
axs[0].legend()

# Gráfica 2: Azimuth vs Filtro Promedio
axs[1].plot(azimuth_np, filtered_distance, label='Filtered Average', color='orange')
axs[1].set_title('Azimuth vs Filtered Average Distance')
axs[1].set_xlabel('Azimuth')
axs[1].set_ylabel('Filtered Distance (m)')
axs[1].legend()

# Gráfica 3: Azimuth vs Filtro Gradiente
axs[2].plot(azimuth_np, gradient_filtered_distance, label='Gradient Filtered', color='green')
axs[2].set_title('Azimuth vs Gradient Filtered Distance')
axs[2].set_xlabel('Azimuth')
axs[2].set_ylabel('Gradient Filtered Distance (m)')
axs[2].legend()

# Mostrar las gráficas
plt.tight_layout()
plt.show()

