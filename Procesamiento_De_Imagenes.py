
import cv2
import numpy as np

# Leer imagen

url = "Utileria_2.png"
img = cv2.imread(url)

kernel = np.ones((5, 5), np.uint8)
print(f"Kernel: \n{kernel}")

# Distintos estilos de imagen

img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gris, (5, 5), 1) 
img_canny = cv2.Canny(img, 200, 200) 

img_dilatacion = cv2.dilate(img_canny, kernel, iterations = 1)
img_erosion = cv2.erode(img_dilatacion, kernel, iterations = 1) 

# Mostrar imagen

cv2.imshow("Imagen original", img)
cv2.imshow("Imagen gris", img_gris)
cv2.imshow("Imagen blur", img_blur)
cv2.imshow("Imagen canny", img_canny)
cv2.imshow("Imagen dilatada", img_dilatacion)
cv2.imshow("Imagen erosion", img_erosion)
cv2.waitKey(0)