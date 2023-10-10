import numpy as np
import pandas as pd

x = np.array([3,4,5,6,7])
y = np.array([2.5,3.2,3.8,6.5,12])

data = dict()
data['x'] = x
data['y'] = y
data['x2'] = np.power(x,2)
data['x3'] = np.power(x,3)
data['x4'] = np.power(x,4)
data['xy'] = x*y
data['x2y'] = data['x2'] * y

x = data['x']
y = data['y']
x2 = data['x2'] 
x3 = data['x3']
x4 = data['x4']
xy = data['xy']
x2y = data['x2y']

table = pd.DataFrame(data)

# Se calculan las sumas de las columnas y se hace un append a la ultima fila de la tabla
sums = {
    'x': sum(x),
    'y': sum(y),
    'x2': sum(data['x2']),
    'x3': sum(data['x3']),
    'x4': sum(data['x4']),
    'xy': sum(data['xy']),
    'x2y': sum(data['x2y'])
}

table = table._append(sums, ignore_index=True)

print(table)


# Se crea la matriz de coeficientes
A = np.array([x4,x3,x2],[x3,x2,x],[x2,x,len(x)])
B = np.array([x2y,xy,y])
Ax = B

# Se resuelve el sistema de ecuaciones
coeffs = np.linalg.solve(A,B)
print(coeffs)