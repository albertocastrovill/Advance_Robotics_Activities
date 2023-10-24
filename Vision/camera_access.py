#Importar librerías para abrir la cámara
import cv2

#Abrir la cámara
cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("No se pudo abrir la cámara")
    exit()

frameNumber = 0

#Leer la cámara
while True:
    ret, frame = cam.read()
    if not ret:
        print("No se pudo abrir la cámara")
        break

    cv2.imshow('Camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    #Tomar foto cuando oprima la tecla 's'
    if cv2.waitKey(5) & 0xFF == ord('s'):
        frameNumber += 1
        #guardar la imagen en carpeta fotos
        cv2.imwrite(f'fotos/frame{frameNumber}.jpg', frame)
        print(f'frame{frameNumber}.jpg saved')

#Cerrar la cámara
cam.release()

#Cerrar todas las ventanas
cv2.destroyAllWindows()

