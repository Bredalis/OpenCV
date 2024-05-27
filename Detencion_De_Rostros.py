
import  cv2

color = (255, 0, 0)
grosor = 2

clasificador = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
captura_video = cv2.VideoCapture(0)

while True:

	resultado, ventana = captura_video.read()
	ventana_gris = cv2.cvtColor(ventana, cv2.COLOR_BGR2GRAY)

	caras = clasificador.detectMultiScale(ventana_gris)

	# Detectar los rostros

	for (x, y, ancho, alto) in caras:
		cv2.rectangle(ventana, (x, y), (x + ancho, y + alto), color, grosor)

	cv2.imshow("Video", ventana)

	if cv2.waitKey(1) == ord("q"):
		break

cv2.destroyAllWindows()
captura_video.release()