import numpy as np
import matplotlib.pyplot as plt
import math

# Configuración del espacio
X_MAX, Y_MAX = 100, 100  # Dimensiones del espacio
OBS = []  # Aquí irían las coordenadas de los obstáculos

# Parámetros del carrito
MIN_STEER_ANGLE = np.radians(70)  # Ángulo mínimo de dirección en radianes
MAX_STEER_ANGLE = np.radians(110)  # Ángulo máximo de dirección en radianes
CAR_LENGTH = 2.5  # Longitud del carrito, para calcular el radio de giro

# Parámetros del RRT
NUM_NODES = 1000  # Número de nodos en el RRT
GOAL_SAMPLE_RATE = 0.1  # Probabilidad de muestreo del punto objetivo

class Node:
    def __init__(self, x, y, angle=0.0):
        self.x = x
        self.y = y
        self.angle = angle  # Orientación del carrito en radianes
        self.parent = None

def get_random_point():
    return (np.random.uniform(0, X_MAX), np.random.uniform(0, Y_MAX))

def nearest_node(node_list, random_point):
    closest_node = None
    min_dist = float('inf')
    for node in node_list:
        dist = np.hypot(node.x - random_point[0], node.y - random_point[1])
        if dist < min_dist:
            min_dist = dist
            closest_node = node
    return closest_node

def check_collision(node, obstacles):
    # Siempre devuelve False para simplificar, en la práctica esto debería ser una comprobación real
    return False

def is_goal_reached(node, goal_point, threshold=5):
    dist = np.hypot(node.x - goal_point[0], node.y - goal_point[1])
    return dist < threshold

def steer(from_node, to_point, extend_length=float('inf')):
    # Simulación de la dirección tipo Ackerman
    new_node = Node(from_node.x, from_node.y, from_node.angle)
    angle_to_goal = math.atan2(to_point[1] - from_node.y, to_point[0] - from_node.x)
    
    # Restringir el ángulo de dirección a los límites del servomotor
    if angle_to_goal - from_node.angle > 0:
        steer_angle = MIN_STEER_ANGLE
    else:
        steer_angle = -MIN_STEER_ANGLE

    # Calcular el radio de giro basado en el ángulo de las ruedas delanteras
    turn_radius = CAR_LENGTH / math.tan(steer_angle)
    
    # Calcular el arco para alcanzar el punto objetivo
    distance_to_goal = np.hypot(to_point[0] - from_node.x, to_point[1] - from_node.y)
    extend_length = min(extend_length, distance_to_goal)  # No moverse más allá del punto objetivo
    arc_angle = extend_length / turn_radius

    # Aplicar el movimiento a lo largo de un arco
    new_node.angle = from_node.angle + arc_angle
    new_node.x = from_node.x + turn_radius * (math.sin(new_node.angle) - math.sin(from_node.angle))
    new_node.y = from_node.y - turn_radius * (math.cos(new_node.angle) - math.cos(from_node.angle))
    
    new_node.parent = from_node
    return new_node

def connect_to_goal(node_list, from_node, goal_node):
    """
    Intenta conectar directamente from_node al goal_node.
    Retorna True si la conexión es exitosa, False en caso contrario.
    """
    new_node = steer(from_node, (goal_node.x, goal_node.y))
    if new_node and not check_collision(new_node, OBS):
        node_list.append(new_node)
        goal_node.parent = new_node
        node_list.append(goal_node)
        return True
    return False

# Vamos a reiniciar el proceso para asegurarnos de que no haya estados residuales
start_node = Node(0, 0)
goal_node = Node(80, 80)
node_list = [start_node]

for _ in range(NUM_NODES):
    rnd_point = get_random_point()
    if np.random.rand() < GOAL_SAMPLE_RATE:
        rnd_point = (goal_node.x, goal_node.y)
    
    nearest = nearest_node(node_list, rnd_point)
    new_node = steer(nearest, rnd_point)
    
    if new_node and not check_collision(new_node, OBS):
        node_list.append(new_node)
        
        if is_goal_reached(new_node, (goal_node.x, goal_node.y), threshold=5):
            if connect_to_goal(node_list, new_node, goal_node):
                print("Goal reached")
                break

# Dibujar el resultado
for node in node_list:
    if node.parent:
        plt.plot([node.x, node.parent.x], [node.y, node.parent.y], "-g")
plt.plot(start_node.x, start_node.y, "ob")  # Inicio en azul
plt.plot(goal_node.x, goal_node.y, "or")  # Objetivo en rojo
plt.xlim(0, X_MAX)
plt.ylim(0, Y_MAX)
plt.show()
