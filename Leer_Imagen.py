
import cv2

# Leer la imagen

url = "Python.png"
img = cv2.imread(url)

# Redimensionar tamaño

img = cv2.resize(img, (500, 500))

# Mostrar imagen

cv2.imshow("Imagen", img)

# Cerrar interfaz

cv2.waitKey(0)