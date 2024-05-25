
from StackImages import *

# Leer imagen

url = "Figuras.jpg"
img = cv2.imread(url)

# Escala de grises

img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Difuminacion

img_blur = cv2.GaussianBlur(img_gris, (7, 7), 1)

# Canny

img_canny = cv2.Canny(img_blur, 50, 50)

img_stack = stack_images(
	0.7, ([img, img_gris, img_blur], [img_canny, img, img]))

# Redireccionar tamaño

img_stack = cv2.resize(img_stack, (900, 600))

# Mostrar imagen

cv2.imshow("Figuras", img)
cv2.imshow("Figuras en escala de grises", img_gris)
cv2.imshow("Figuras difuminadas", img_blur)
cv2.imshow("Figuras Canny", img_canny)
cv2.imshow("Figuras Stack", img_stack)

# Cerrar interfaz

cv2.waitKey(0)