import numpy as np
import matplotlib.pyplot as plt
import math

# Configuración del espacio
X_MAX, Y_MAX = 100, 100  # Dimensiones del espacio
OBS = [(20, 50, 10), (50, 50, 15), (70, 20, 10)]  # Definición de obstáculos

# Parámetros del carrito
MIN_STEER_ANGLE = np.radians(70)  # Ángulo mínimo de dirección en radianes
MAX_STEER_ANGLE = np.radians(110)  # Ángulo máximo de dirección en radianes
CAR_LENGTH = 2.5  # Longitud del carrito

# Parámetros del RRT
NUM_NODES = 10000  # Número de nodos en el RRT
GOAL_SAMPLE_RATE = 0.1  # Probabilidad de muestreo del punto objetivo

class Node:
    def __init__(self, x, y, angle=0.0):
        self.x = x
        self.y = y
        self.angle = angle
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
    for (ox, oy, size) in obstacles:
        if ox <= node.x <= ox + size and oy <= node.y <= oy + size:
            return True
    return False

def is_goal_reached(node, goal_point, threshold=1):
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
    new_node = steer(from_node, (goal_node.x, goal_node.y))
    if new_node and not check_collision(new_node, OBS) and is_goal_reached(new_node, (goal_node.x, goal_node.y), threshold=1):
        node_list.append(new_node)
        goal_node.parent = new_node
        node_list.append(goal_node)
        return True
    return False

def draw_final_path(start_node, goal_node):
    path = []
    current_node = goal_node
    while current_node.parent is not None:
        path.append(current_node)
        current_node = current_node.parent
    path.append(start_node)
    for index in range(len(path) - 1):
        node_from = path[index]
        node_to = path[index + 1]
        plt.plot([node_from.x, node_to.x], [node_from.y, node_to.y], "-r", linewidth=line_width)

def rrt_connect_to_goal(start_node, goal_node, num_nodes, goal_sample_rate):
    node_list = [start_node]
    while True:
        rnd_point = get_random_point()
        if np.random.rand() < goal_sample_rate:
            rnd_point = (goal_node.x, goal_node.y)
        nearest = nearest_node(node_list, rnd_point)
        new_node = steer(nearest, rnd_point)
        if new_node and not check_collision(new_node, OBS):
            node_list.append(new_node)
            if is_goal_reached(new_node, (goal_node.x, goal_node.y)):
                if connect_to_goal(node_list, new_node, goal_node):
                    print("Goal reached")
                    break
    return node_list

start_node = Node(0, 0)
goal_node = Node(80, 80)
line_width = 25 / CAR_LENGTH  # Ancho de línea proporcional al ancho del carrito

# Ejecutar RRT y dibujar el resultado
node_list = rrt_connect_to_goal(start_node, goal_node, NUM_NODES, GOAL_SAMPLE_RATE)

plt.figure(figsize=(8, 6))  # Aumentar el tamaño de la figura
draw_final_path(start_node, goal_node)  # Dibujar solo la ruta final
for (ox, oy, size) in OBS:  # Dibujar los obstáculos
    plt.fill([ox, ox + size, ox + size, ox], [oy, oy, oy + size, oy + size], "k-")
plt.plot(start_node.x, start_node.y, "ob", markersize=10)  # Punto de inicio
plt.plot(goal_node.x, goal_node.y, "or", markersize=10)  # Punto objetivo
plt.xlim(0, X_MAX)  # Configurar los límites
plt.ylim(0, Y_MAX)
plt.title("RRT Path Planning: Final Path Only")
plt.grid(True, which='both', linestyle='--', linewidth=1)  # Grid más destacado
plt.minorticks_on()  # Activar minor ticks
plt.show()
