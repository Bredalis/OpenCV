
import cv2
import numpy as np

# Colores

bordes = (0, 0, 255)
color_texto = (0, 0, 0)

# Leer imagen

url = "Colores.jpg"
img = cv2.imread(url)
img = cv2.resize(img, (500, 400))

img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img_gris, kernel, iterations = 2)
dilatacion = cv2.dilate(erosion, kernel, iterations = 3)

# Suavizar imagen

gauss = cv2.GaussianBlur(dilatacion, (5, 5), 0)

img_canny = cv2.Canny(gauss, 100, 50)

# Contornos

contornos, _ = cv2.findContours(img_canny, cv2.RETR_EXTERNAL, 
	cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contornos, -1, bordes, 2)

# Conteo de objectos

texto = f"Numero de objectos encontrados: {len(contornos)}"
cv2.putText(img, texto, (10, 390), cv2.FONT_ITALIC, 0.7, color_texto, 2)
print(texto)

# Mostrar imagen

cv2.imshow("Imagen original", img)
cv2.imshow("Imagen gris", img_gris)
cv2.imshow("Imagen con objectos cortados", erosion)
cv2.imshow("Imagen Canny", img_canny)

# Cerrar interfaz

cv2.waitKey(0)
cv2.destroyAllWindows()