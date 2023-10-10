import numpy as np
import math

def calculate_steering_angle(L, R):
    if R == 0:
        return 0  # Avoid division by zero
    return math.atan(L/R)

def calculate_turning_radius(p1, p2):
    p1 = np.array(p1)
    p2 = np.array(p2)
    return np.linalg.norm(p2-p1)/2

def calculate_midpoint(p1, p2):
    p1 = np.array(p1)
    p2 = np.array(p2)
    return ((p1 + p2) / 2).tolist()

def ackerman_path(points, L, max_steering_angle, max_recursion_depth=10):
    if max_recursion_depth <= 0:
        return []  # Prevent infinite recursion
    
    path = []
    for i in range(len(points)-1):
        p1 = points[i]
        p2 = points[i+1]
        
        R = calculate_turning_radius(p1, p2)
        steering_angle = calculate_steering_angle(L, R)
        
        print(f"Checking path from {p1} to {p2}: R={R:.2f}, steering_angle={np.rad2deg(steering_angle):.2f}")  # Debug print
        
        if abs(steering_angle) > max_steering_angle:
            print(f"Steering angle too large, calculating midpoint...")  # Debug print
            # Point is out of reach, calculate midpoint
            midpoint = calculate_midpoint(p1, p2)
            # Recursively calculate path to midpoint and from midpoint to p2
            path += ackerman_path([p1, midpoint, p2], L, max_steering_angle, max_recursion_depth-1)
        else:
            # Point is reachable, add to path
            path.append((p1, p2, R, steering_angle))
    
    return path

# Example usage
points = [[0,0],[2.0,1.5],[3.0,0.5],[2.8,2],[-1,2],[-0.5,1.0]]
L = 2.5  # Example wheelbase
max_steering_angle = np.deg2rad(30)  # Maximum steering angle in radians

path = ackerman_path(points, L, max_steering_angle)

# Display path
for p1, p2, R, steering_angle in path:
    print(f"Move from {p1} to {p2} with turning radius {R:.2f} and steering angle {np.rad2deg(steering_angle):.2f} degrees")
