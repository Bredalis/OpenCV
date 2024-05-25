
import cv2
import numpy as np

# Leer imagen

url = "Genero.png"
img = cv2.imread(url)

# Medida del logo

ancho, alto = 128, 128

puntos = np.float32([[14, 14], [107, 11], [12, 208], [106, 215]])
puntos_2 = np.float32([[0, 0], [ancho, 0], [0, alto], [ancho, alto]])

# Creacion de la matriz

matriz = cv2.getPerspectiveTransform(puntos, puntos_2)
img_2 = cv2.warpPerspective(img, matriz, (ancho, alto))

# Mostrar la imagen

cv2.imshow("Imagen Original", img)
cv2.imshow("Imagen Modificada", img_2)

# Cerrar interfaz

cv2.waitKey(0) 