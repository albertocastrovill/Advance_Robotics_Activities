import cv2
import numpy as np
import math

def calc_angle(p1, p2):
    x = p2[0] - p1[0]
    y = p2[1] - p1[1]
    res = np.rad2deg(np.arctan2(y, x))
    return res

def process_frame(frame):
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
    angle_deg = None

    if contours:
        # Encuentra el contorno más grande (suponiendo que es el objetivo)
        c = max(contours, key=cv2.contourArea)

        # Aproximar el contorno a un polígono
        epsilon = 0.01 * cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, epsilon, True)

        if len(approx) >= 3:  # Asegurarse de que es un triángulo
            # Calcular el centroide
            M = cv2.moments(c)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                centroid = (cx, cy)

                # Encontrar la punta del triángulo (el punto más alejado del centroide)
                tip = max(approx, key=lambda p: cv2.norm((cx, cy) - p[0]))[0]
                tip = (tip[0], tip[1])

                # Calcular el ángulo de orientación con respecto al eje horizontal
                angle_deg = calc_angle(centroid, tip)
                
                if angle_deg < 0:
                    angle_deg = abs(angle_deg)
                else:
                    angle_deg = 360 - angle_deg

                # Dibujar el contorno, el centroide y la punta del triángulo
                cv2.drawContours(frame, [approx], -1, (0, 255, 0), 2)
                cv2.circle(frame, centroid, 7, (255, 255, 255), -1)
                cv2.line(frame, centroid, tuple(tip), (255, 0, 0), 5)

                # Mostrar el ángulo de orientación
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, f"Angle: {angle_deg:.2f} degrees", (cx + 10, cy + 10), font, 0.5, (255, 0, 0), 2)

    # Devolver el ángulo y el cuadro procesado
    return angle_deg, frame, mask

# Ejemplo de uso de la función con captura de video en tiempo real
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    angle, processed_frame, mask = process_frame(frame)
    
    # Si se detectó un ángulo, mostrarlo
    if angle is not None:
        print(f"Angle: {angle:.2f} degrees")

    # Mostrar el cuadro procesado y la máscara
    cv2.imshow('Processed Frame', processed_frame)
    cv2.imshow('Mask', mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

