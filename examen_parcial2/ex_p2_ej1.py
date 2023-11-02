import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Leer datos y graficar
data = pd.read_csv('baseballDataset.csv')
plt.scatter(data['Angulo'], data['Distancia'], color='blue', label='Datos')
plt.xlabel('Ángulo de Bateo')
plt.ylabel('Distancia Horizontal Recorrida')
plt.title('Distancia vs. Ángulo de Bateo')

# Modelo matemático (Polinomial)
z = np.polyfit(data['Angulo'], data['Distancia'], 2)
p = np.poly1d(z)
angulos = np.linspace(0, 65, 5000)
p_ang = p(angulos)
plt.plot(angulos, p_ang, 'r-', label='Ajuste polinomial')
plt.legend()

# Efectividad del modelo
y_pred = p(data['Angulo'])
y_actual = data['Distancia']
R2 = 1 - (np.sum((y_actual - y_pred)**2) / ((len(y_actual) - 1) * np.var(y_actual, ddof=1)))
print(f'Coeficiente de determinación R^2: {R2:.3f}')

# Sugerencia del Asistente de Bateo
distancia_objetivo = 140  # cambiar la distancia objetivo
sugerencias = []

# Como es una ecuación cuadrática, lo más probable es que haya dos ángulos con los cuales llegarías a la misma distancia objetivo
# Por lo tanto será necesario cacular los diferentes ángulos de esta ecuación que dan como resultado la distancia objetivo.

for ang in angulos:
    dist = p(ang)
    if abs(dist - distancia_objetivo) < 0.07:  # usando un margen de error de 0.07 para que no haya problemas con la precisión de los números
        sugerencias.append(ang)

print(f"Sugerencias de ángulo para una distancia de {distancia_objetivo}: {sugerencias}")


plt.show()
