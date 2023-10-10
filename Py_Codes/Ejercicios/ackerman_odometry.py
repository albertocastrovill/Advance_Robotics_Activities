import math
import numpy as np

def compute_bicycle_odometry(encoder_pulses, pulses_per_second, wheel_radius, width, elapsed_time, xg, yg, og, delta_angle, wheel_base):
    # Convertir delta_angle a radianes 
    delta_angle_rad = math.radians(delta_angle)
    
    # Calcular la velocidad angular de las ruedas (en radianes por segundo)
    omega = (2 * math.pi * pulses_per_second) / encoder_pulses
    
    # Calcular la velocidad lineal de las ruedas (en metros por segundo)
    v = omega * wheel_radius
    
    # Calcular la velocidad del vehículo en el sistema de coordenadas global
    vx = v * math.cos(og + delta_angle_rad)
    vy = v * math.sin(og + delta_angle_rad)
    
    # Calcular la velocidad angular del vehículo
    omega_v = v * math.tan(delta_angle_rad) / wheel_base
    
    # Actualizar la pose del vehículo usando la velocidad y el tiempo transcurrido
    xg += vx * elapsed_time
    yg += vy * elapsed_time
    og += omega_v * elapsed_time
    
    # Asegurarse de que el ángulo og está en el rango [0, 2*pi]
    og = og % (2 * math.pi)

    og = math.degrees(og)
    
    # Calcular la distancia total recorrida
    total_distance = v * elapsed_time
    
    return xg, yg, og, total_distance

# Parámetros dados
encoder_pulses = 20
pulses_per_second = 80
wheel_radius = 0.036  # en metros
width = 0.22  # en metros
elapsed_time = 2  # en segundos
xg, yg, og = 0.0, 0.0, 0.0  # pose inicial
delta_angle = 0  # en grados
wheel_base = 0.22  # en metros (lb + lf)

encoder_pulses = int(input("Enter quantity of Encoder Pulses per Revolution: "))
pulses_per_second = int(input("Enter quantity of Pulses per Second: "))
wheel_radius = float(input("Enter Wheel Radius (m): "))
width = float(input("Enter Vehicle Width (W - m): "))
xg = float(input("Enter Starting X position: "))
yg = float(input("Enter Starting Y position: "))
og = float(input("Enter Starting Heading Value (degrees): "))
elapsed_time = int(input("Enter elapsed time (seconds): "))

# Calcular la odometría del modelo de bicicleta
xg, yg, og, total_distance = compute_bicycle_odometry(encoder_pulses, pulses_per_second, wheel_radius, width, elapsed_time, xg, yg, og, delta_angle, wheel_base)

# Mostrar los resultados
print(f"Pose final: Xg = {xg:.2f} m, Yg = {yg:.2f} m, Og = {og:.2f} grados")
print(f"Distancia total recorrida: {total_distance:.2f} m")
