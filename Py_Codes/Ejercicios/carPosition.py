import math
import numpy as np

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

r = d/2 #cm
w1 = 8 * math.pi
w2 = 8 * math.pi
l = 11 #cm
sensores = np.array([[(r*w1)/2 + (r*w2)/2],[0],[(r*w1)/(2*l) + (-r*w2)/(2*l)]])

XG = XGk2 + (t*R*sensores)

print(XG)


