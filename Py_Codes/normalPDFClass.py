import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#Generar datos de prueba
np.random.seed(0)
dataSet1 = np.random.normal(loc=5, scale=5, size=1000)
dataSet2 = np.random.normal(loc=10, scale=3, size=1000)

# Definir tamaño de imagen
plt.figure(figsize=(8, 6))

#Generar un histograma de los datos
histDAtaSet1, bins, _ = plt.hist(dataSet1, bins=20, density=True, alpha=0.7, label="dataSet1", color="blue")
histDAtaSet2, bins, _ = plt.hist(dataSet2, bins=20, density=True, alpha=0.5, label="dataSet2", color="orange")


#Ajustar una curva de densidad de probabilidad a los datos
paramsDataset1 = norm.fit(dataSet1)
pdf1 = norm.pdf(bins, loc=paramsDataset1[0], scale=paramsDataset1[1])
plt.plot(bins, pdf1, color="red", label="pdf1", linewidth=2)

paramsDataset2 = norm.fit(dataSet2)
pdf2 = norm.pdf(bins, loc=paramsDataset2[0], scale=paramsDataset2[1])
plt.plot(bins, pdf2, color="green", label="pdf2", linewidth=2)


#Desplegar la curva de densidad de probabilidad
plt.xlabel("Variable")
plt.ylabel("Probability density")
plt.title("Histograma de los datos")
plt.legend()
plt.show()


