
# Filtro Blur en los rostros

import cv2

captura_video = cv2.VideoCapture(0)

# Cargar el clasificador de detección de rostros

cara_cascada = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:

    resultado, ventana = captura_video.read()
    
    # Voltear horizontalmente la imagen

    ventana = cv2.flip(ventana, 1)
    rostro = cara_cascada.detectMultiScale(ventana, 1.1, 4)

    # Iterar sobre los rostros detectados

    for x, y, w, h in rostro:

        # Crear un rectángulo alrededor del rostro detectado

        cv2.rectangle(ventana, (x, y), (x + w, y + h), (0, 255, 255), 5)
        
        # Extraer la región de interés (ROI - Region of Interest)

        roi = ventana[y: y + h, x: x + w]
        roi = cv2.GaussianBlur(roi, (25, 25), 30)
        
        # Reemplazar la región del rostro con el rostro desenfocado

        ventana[y: y + roi.shape[0], x: x + roi.shape[1]] = roi

    cv2.imshow("Video", ventana)

    c = cv2.waitKey(1)
    if c == 27:
        break

cv2.destroyAllWindows()