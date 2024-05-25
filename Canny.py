
# Controlar el canny
# de cualquier imagen
# con Trackbars

import cv2

def nada():
	pass

# Leer imagen

url = "Paisaje.jpg"
img = cv2.imread(url)
img = cv2.resize(img, (400, 300))

cv2.namedWindow("canny")
cv2.createTrackbar("bajo", "canny", 0, 255, nada)
cv2.createTrackbar("alto", "canny", 0, 255, nada)

switch = "0 : 0FF \n 1 : ON"
cv2.createTrackbar(switch, "canny", 0, 1, nada)

while True:

	bajo = cv2.getTrackbarPos("bajo", "canny")
	alto = cv2.getTrackbarPos("alto", "canny")
	s = cv2.getTrackbarPos(switch, "canny")

	if s == 0:
		borde = img
	else:
		borde = cv2.Canny(img, bajo, alto)

	# Mostrar imagen 

	cv2.imshow("Imagen original", img)
	cv2.imshow("Imagen canny", borde)

	c = cv2.waitKey(1) & 0XFF

	if c == 27:
		break

cv2.destroyAllWindows()