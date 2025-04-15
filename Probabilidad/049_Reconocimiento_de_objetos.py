import cv2

# ----------------------------- Cargar clasificadores Haar -----------------------------
clasificador_rostro = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
clasificador_ojos = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Verificar si los clasificadores se cargaron correctamente
if clasificador_rostro.empty() or clasificador_ojos.empty():
    print("Error al cargar los clasificadores Haar.")
    exit()

# ----------------------------- Cargar imagen -----------------------------
imagen = cv2.imread('Probabilidad/Imagenes/persona.jpg')

# Verificar si la imagen se cargó correctamente
if imagen is None:
    print("Error al cargar la imagen. Verifica la ruta.")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# ----------------------------- Detectar rostros -----------------------------
rostros = clasificador_rostro.detectMultiScale(gris, scaleFactor=1.3, minNeighbors=5)

# Dibujar rectángulos alrededor del rostro
for (x, y, w, h) in rostros:
    cv2.rectangle(imagen, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Rectángulo azul en el rostro
    roi_gris = gris[y:y+h, x:x+w]
    roi_color = imagen[y:y+h, x:x+w]
    
    # Detectar ojos dentro de cada rostro
    ojos = clasificador_ojos.detectMultiScale(roi_gris)
    for (ox, oy, ow, oh) in ojos:
        cv2.rectangle(roi_color, (ox, oy), (ox+ow, oy+oh), (0, 255, 0), 2)  # Rectángulo verde en cada ojo

# ----------------------------- Mostrar resultados -----------------------------
cv2.imshow('Reconocimiento de Objetos (Rostros y Ojos)', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
