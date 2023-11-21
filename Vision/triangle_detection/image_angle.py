import cv2
import numpy as np
import math

# Cargar la imagen
image_path = 'img_triangle/triangle5.jpg'  
frame = cv2.imread(image_path)

# Convertir el cuadro capturado de BGR a HSV
hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Definir el rango del color verde en HSV
lower_green = np.array([50, 100, 100])
upper_green = np.array([70, 255, 255])

# Crear una máscara para detectar solo el color verde
mask = cv2.inRange(hsv_frame, lower_green, upper_green)

# Opcional: usar dilatación y erosión para eliminar pequeños puntos en la máscara
mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)

# Encuentra contornos en la máscara
contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if contours:
    # Encuentra el contorno más grande (suponiendo que es el objetivo)
    c = max(contours, key=cv2.contourArea)
        # Aproximar el contorno a un polígono
    epsilon = 0.01 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)

    # Calcular el centroide
    M = cv2.moments(c)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        centroid = (cx, cy)

        # Encontrar la punta del triángulo (el punto más alejado del centroide)
        tip = max(approx, key=lambda p: cv2.norm((cx, cy) - p[0]))[0]
        tip = (tip[0], tip[1])
        print(f"Punta: {tip}")
        cv2.circle(frame, tuple(tip), 3, (255, 0, 0), -1)

        # Calcula la matriz de covarianza y luego los eigenvectores (para la orientación)
        covar_matrix = np.array([[M['mu20'], M['mu11']], [M['mu11'], M['mu02']]])
        eigenvalues, eigenvectors = np.linalg.eig(covar_matrix)
        angle = np.arctan2(eigenvectors[1, 0], eigenvectors[0, 0])

        # Convertir el ángulo a grados
        angle_deg = np.degrees(angle)

        # Dibujar el contorno y el centroide en el cuadro
        frame = cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
        cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)

        # Dibujar la orientación del triángulo
        length = 50  # Longitud de la línea de orientación
        endpoint_x = int(cx + length * math.cos(angle))
        endpoint_y = int(cy + length * math.sin(angle))
        #cv2.line(frame, (cx, cy), (endpoint_x, endpoint_y), (255, 0, 0), 5)
        cv2.line(frame, centroid, tuple(tip), (255, 0, 0), 5)

        # Mostrar el ángulo de orientación
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, f"Angle: {angle_deg:.2f} degrees", (cx + 10, cy + 10), font, 0.5, (255, 0, 0), 2)

# Mostrar el cuadro procesado
cv2.imshow('frame', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
