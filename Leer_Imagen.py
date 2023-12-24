
import cv2

# Leer la imagen
img = cv2.imread("C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Icon/Imagenes/Python.png")

# Redimensionar tamaño
img = cv2.resize(img, (500, 500))

# Mostrar imagen
cv2.imshow("Imagen", img)

# Cerrar interfaz
cv2.waitKey(0)