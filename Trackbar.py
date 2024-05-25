
import cv2
import numpy as np

def nada():
	pass

# Crear imagen

img = np.zeros((300, 600, 3), np.uint8)
cv2.namedWindow("Imagen")

cv2.createTrackbar("Rojo", "Imagen", 0, 255, nada)
cv2.createTrackbar("Verde", "Imagen", 0, 255, nada)
cv2.createTrackbar("Azul", "Imagen", 0, 255, nada)

switch = "0 : 0FF \n 1 : 0N"

cv2.createTrackbar(switch, "Imagen", 0, 1, nada)

while True:

	# Trackbar de distintos colores

	rojo = cv2.getTrackbarPos("Rojo", "Imagen")
	verde = cv2.getTrackbarPos("Verde", "Imagen")
	azul = cv2.getTrackbarPos("Azul", "Imagen")
	s = cv2.getTrackbarPos(switch, "Imagen")

	if s == 0:
		pass
	else:
		img[:] = [rojo, verde, azul]

	cv2.imshow("Paleta de colores", img)
	c = cv2.waitKey(1) & 0xFF

	# Cerrar ventana
	if c == 27:
		break

print(f"Colores RGB: {rojo}, {verde}, {azul}")

cv2.destroyAllWindows()