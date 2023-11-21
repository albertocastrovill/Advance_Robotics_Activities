import cv2
import numpy as np

# Definir el rango del color verde en HSV
lower_green = np.array([50, 100, 100])
upper_green = np.array([70, 255, 255])

# Iniciar la captura de video desde la primera cámara
cap = cv2.VideoCapture(3)

# Loop para leer cuadros desde la cámara
while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_frame, lower_green, upper_green)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Encuentra contornos en la máscara
    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Encuentra el contorno más grande (suponiendo que es el objetivo)
        c = max(contours, key=cv2.contourArea)

        # Calcular el centroide
        M = cv2.moments(c)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            # Calcular el ángulo de orientación del contorno
            # (usando el código de tu función original para calcular el ángulo)
            # ...

            # Dibujar el contorno y el centroide en el cuadro
            frame = cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            # Aquí también podrías dibujar la orientación del triángulo usando líneas.

    # Mostrar el cuadro procesado
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Cuando todo está hecho, liberar la captura
cap.release()
cv2.destroyAllWindows()