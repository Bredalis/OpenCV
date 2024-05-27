
# Librerias

import cv2
import imutils
import numpy as np

captura_video = cv2.VideoCapture(0)
captura_video.set(3, 648) # Ancho
captura_video.set(4, 480) # Alto

while True:
	resultado, ventana = captura_video.read()

	# Significado de la variable (Matiz, Saturación, Valor)

	hsv = cv2.cvtColor(ventana, cv2.COLOR_BGR2HSV)

	# Colores

	amarillo_oscuro = np.array([25, 78, 128])
	amarillo_claro = np.array([30, 255, 255])	

	rojo_oscuro = np.array([0, 58, 128])
	rojo_claro = np.array([10, 255, 255])

	verde_claro = np.array([40, 70, 88])
	verde_oscuro = np.array([78, 255, 255])

	azul_claro = np.array([90, 68, 0])
	azul_oscuro = np.array([121, 255, 255])

	# Caras

	cara_1 = cv2.inRange(hsv, amarillo_claro, amarillo_oscuro)
	cara_2 = cv2.inRange(hsv, rojo_claro, rojo_oscuro)
	cara_3 = cv2.inRange(hsv, verde_claro, verde_oscuro)
	cara_4 = cv2.inRange(hsv, azul_claro, azul_oscuro)

	# Contornos

	contorno_1 = cv2.findContours(cara_1, cv2.RETR_TREE, 
		cv2.CHAIN_APPROX_SIMPLE)
	contorno_1 = imutils.grab_contours(contorno_1)

	contorno_2 = cv2.findContours(cara_2, cv2.RETR_TREE, 
		cv2.CHAIN_APPROX_SIMPLE)
	contorno_2 = imutils.grab_contours(contorno_2)

	contorno_3 = cv2.findContours(cara_3, cv2.RETR_TREE, 
		cv2.CHAIN_APPROX_SIMPLE)
	contorno_3 = imutils.grab_contours(contorno_3)

	contorno_4 = cv2.findContours(cara_4, cv2.RETR_TREE, 
		cv2.CHAIN_APPROX_SIMPLE)
	contorno_4 = imutils.grab_contours(contorno_4)

	colores = ["Amarillo", "Rojo", "Verde", "Azul"]
	contornos = [contorno_1, contorno_2, contorno_3, contorno_4]

	for i in range(len(contornos)):
		for c in contornos[i]:
			area_1 = cv2.contourArea(c)

			if area_1 > 5000:
				cv2.drawContours(ventana, [c], -1, (38, 255, 255), 3)
				m = cv2.moments(c)
				cx = int(m["m10"] / m["m00"])
				cy = int(m["m01"] / m["m00"])

				cv2.circle(ventana, (cx, cy), 7, (255, 255, 255), -1)
				cv2.putText(ventana, colores[i], (cx - 20, cy - 20), 
					cv2.FONT_ITALIC, 2, (255, 255, 255), 2)

	# Mostrar imagen

	cv2.imshow("Videos", ventana)
	c = cv2.waitKey(1) & 0xFF

	# Cerrar ventana

	if c == 27:
		break

captura_video.release()
cv2.destroyAllWindows()