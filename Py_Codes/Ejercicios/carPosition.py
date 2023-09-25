import math
import numpy as np
import random
#from mpmath import cot

encoder = 20
numPulsos = 80

RPS = 4 
VelAngular = 8* math.pi
RapLineal = 0.955
d = 7.6
C = math.pi * d

xg = 0
yg = 0
tg = 0

XGk1 = np.array([[xg], [yg], [tg]])

XGk2 = np.array([[xg], [yg], [tg]])

t = 2 #seg

R = np.array([[np.cos(0), -np.sin(0), 0],[np.sin(0), np.cos(0), 0],[0, 0, 1]])

# Porcentaje de rango (5%)
porcentaje_rango = 5

# Calcula el rango mínimo y máximo
rango_minimo = d - (d * porcentaje_rango / 100)
rango_maximo = d + (d * porcentaje_rango / 100)

# Genera un valor aleatorio dentro del rango
dl = random.uniform(rango_minimo, rango_maximo)
dr = random.uniform(rango_minimo, rango_maximo)
#print(f"Valor diametro left : {dl}")
#print(f"Valor diametro right : {dr}")

r1 = dl/2 #cm
r2 = dr/2  #cm
w1 = 8 * math.pi
w2 = 8 * math.pi
l = 11 #cm

sensores = np.array([[(r1*w1)/2 + (r2*w2)/2],[0],[(r1*w1)/(2*l) + (-r2*w2)/(2*l)]])

XG = XGk2 + (t*R*sensores)

print(XG)


## Segunda parte

L = 0
R1 = 0
W = 0

#eq3 = math.tan(L / R1 + (W/2))
#eq5 = math.tan(L / R1 - (W/2))

def cot (angulo):
    return 1/math.tan(angulo)


Delta = math.tan((cot(10) + cot(10)) / 2)
deg = math.degrees(Delta)
print(deg)

