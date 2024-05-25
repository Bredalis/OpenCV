
# Librerias

import cv2
import imutils
import winsound

captura_video = cv2.VideoCapture(0)

while True:

	_, camara = captura_video.read()
	_, camara_2 = captura_video.read()

	diferencia = cv2.absdiff(camara, camara_2)
	camara_gris = cv2.cvtColor(diferencia, cv2.COLOR_BGR2GRAY)
	camara_blur = cv2.GaussianBlur(camara_gris, (5, 5), 0)

	_, limite = cv2.threshold(camara_blur, 20, 255, cv2.THRESH_BINARY)
	camara_dilatada = cv2.dilate(limite, None, iterations = 3)

	# Contornos

	contornos, _ = cv2.findContours(camara_dilatada, cv2.RETR_TREE, 
		cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(camara, contornos, -1, (0, 0, 255), 2)

	for contorno in contornos:
		if cv2.contourArea(contorno) < 5000:
			continue

		# Coordenadas

		x, y, w, h = cv2.boundingRect(contorno)

		cv2.rectangle(camara, (x, y), (x + w, y + h), (0, 0, 255), 2)

		# Sonido cuando detecte movimiento

		winsound.PlaySound("Campana.mp3", 
			winsound.SND_ASYNC)

	# Mostrar ventana

	cv2.imshow("Detector de movimiento", camara_gris)

	if cv2.waitKey(10) == ord("q"):
		break

cv2.destroyAllWindows()