import numpy as np
import math

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


def angles(points,initial_angle):
    waypoints = []
    for i in range(len(points)-1):
        p1 = points[i]
        p2 = points[i+1]
        #print(p1,p2)
        point = seg_triangulo_rec(p1,p2)
        if point < 0:
            point = 360 + point - initial_angle
        else:
            point = point

        initial_angle = point
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

initial_angle = 0

points = np.array([[0,0],[2.0,1.5],[3.0,0.5],[2.8,2],[-1,2],[-0.5,1.0]])

angles = angles(points, initial_angle)
print("ANGLES WAYPOINTS") 
print(angles)

distance = distance(points)
print("DISTANCE WAYPOINTS")
print(distance)