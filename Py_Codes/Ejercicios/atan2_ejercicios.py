import numpy as np
import math

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

def seg_triangulo_rec2(p1,p2):
    x = p2[0] - p1[0]
    y = p2[1] - p1[1]

    yx= y/x
    res = np.rad2deg(math.atan(yx))
    return res

pA = np.array([2.1,1.5])
pB = np.array([3.2, 0.4])
point = seg_triangulo_rec(pA,pB)
print(point)

"""
p1 = np.array([0,0])
p2 = np.array([2.1, 1.5])
point1 = seg_triangulo_rec(p1,p2)
point1_a = seg_triangulo_rec2(p1,p2)
print("PUNTO A")
print(point1_a)
print(point1)

p1 = np.array([0,0])
p2 = np.array([-1, 0.9])
point2 = seg_triangulo_rec(p1,p2)
point2_a = seg_triangulo_rec2(p1,p2)
print("PUNTO B")
print(point2_a)
print(point2)


p1 = np.array([0,0])
p2 = np.array([-1, -0.9])
point3 = seg_triangulo_rec(p1,p2)
point3_a = seg_triangulo_rec2(p1,p2)
print("PUNTO C")
print(point3_a)
print(point3)


p1 = np.array([0,0])
p2 = np.array([2.1, -1.5])
point4 = seg_triangulo_rec(p1,p2)
point4_a = seg_triangulo_rec2(p1,p2)
print("PUNTO D")
print(point4_a)
print(point4)
"""

def angles(points):
    waypoints = []
    for i in range(len(points)-1):
        p1 = points[i]
        p2 = points[i+1]
        #print(p1,p2)
        point = seg_triangulo_rec(p1,p2)
        if point < 0:
            point = 360 + point
        waypoints.append(point)
    return waypoints

def distance(points):
    waypoints = []
    for i in range(len(points)-1):
        p1 = points[i]
        p2 = points[i+1]
        #print(p1,p2)
        point = np.linalg.norm(p2-p1)
        waypoints.append(point)
    return waypoints



points = np.array([[0,0],[2.0,1.5],[3.0,0.5],[2.8,2],[-1,2],[-0.5,1.0]])

angles = angles(points)
print("ANGLES WAYPOINTS") 
print(angles)

distance = distance(points)
print("DISTANCE WAYPOINTS")
print(distance)

