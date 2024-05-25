
import cv2

def detectar_figuras(img):

    # Convertir la imagen a escala de grises

    img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Aplicar umbral para obtener una imagen binaria

    _, img_umbral = cv2.threshold(img_gris, 127, 255, cv2.THRESH_BINARY)
    
    # Encontrar contornos en la imagen binarizada

    contornos, _ = cv2.findContours(img_umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Iterar sobre los contornos encontrados

    for contorno in contornos:
        area = cv2.contourArea(contorno)
        print(f"Area: {area}")

        if area > 200:  # Filtrar contornos pequeños por ruido

            # Encontrar aproximación poligonal de los contornos

            perimetro = cv2.arcLength(contorno, True)
            print(f"Perimetro: {perimetro}")

            aproximado = cv2.approxPolyDP(contorno, 0.02 * perimetro, True)
            objecto_esquina = len(aproximado)
            print(f"Lados: {objecto_esquina}")
  
            # Obtener las coordenadas del rectángulo delimitador

            x, y, w, h = cv2.boundingRect(aproximado)
            
            # Dibujar un rectángulo alrededor de la figura detectada

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Determinar el tipo de objeto según el número de lados

            if objecto_esquina == 3:
                tipo_objecto = "Triangulo"

            elif objecto_esquina == 4:
                tipo_objecto = "Cuadrado"

            else:
                tipo_objecto = "Otro"

            # Mostrar información del contorno como texto

            texto = tipo_objecto
            cv2.putText(img, texto, (x, y - 10), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    
    # Mostrar la imagen con los rectángulos dibujados

    cv2.imshow("Deteccion de Figuras", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Cargar la imagen

url = "Utileria_1.png"
img = cv2.imread(url)
img = cv2.resize(img, (500, 500))

detectar_figuras(img)