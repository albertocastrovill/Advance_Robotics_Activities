import numpy as np

p1 = np.array([2.1,1.5])
p2 = np.array([-1, 0.9])

res1 = np.rad2deg(np.arctan2(p1[1],p1[0]))
print(res1)

res2 = np.rad2deg(np.arctan2(p2[1],p2[0]))
print(res2)

def seg_triangulo_rec(p1,p2):
    x = p2[0] - p1[0]
    y = p2[1] - p1[1]

    res = np.rad2deg(np.arctan2(y,x))
    return res

pA = np.array([2.1,1.5])
pB = np.array([3.2, 0.4])
point = seg_triangulo_rec(pA,pB)
print(point)
