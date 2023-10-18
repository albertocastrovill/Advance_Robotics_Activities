import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

# Leer los datos del archivo csvo
data = pd.read_csv("data.csv", header=None)

# Definir tamaño de imagen
plt.figure(figsize=(8, 6))

#Generar un histograma de los datos
histData, bins, _ = plt.hist(data, bins=20, density=True, alpha=0.7, label="data", color="blue")

#Ajustar una curva de densidad de probabilidad a los datos
params = norm.fit(data)

methodOne = True
if methodOne:
    # Método 1: Usando la función de densidad de probabilidad
    pdf = norm.pdf(bins, loc=params[0], scale=params[1])
    plt.plot(bins, pdf, color="red", label="pdf", linewidth=2)
else:
    # Método 2: Usando la función de distribución acumulada
    #cdf = norm.cdf(bins, loc=params[0], scale=params[1])
    #plt.plot(bins, cdf, color="red", label="cdf", linewidth=2)
    x = np.linspace(np.min(data[1]), np.max(data[1]), 100)
    

#Desplegar la curva de densidad de probabilidad
plt.xlabel("Variable")
plt.ylabel("Probability density")
plt.title("Histograma de los datos")
plt.legend()
plt.show()
