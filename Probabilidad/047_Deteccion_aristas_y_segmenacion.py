import cv2
import numpy as np
import matplotlib.pyplot as plt

# -------- Cargar imagen en escala de grises --------
# Asegúrate de que la ruta de la imagen sea correcta
ruta_imagen = 'Probabilidad/Imagenes/ladrillo.jpg'
imagen = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)

# Verificar si la imagen se cargó correctamente
if imagen is None:
    print(f"Error: No se pudo cargar la imagen en la ruta '{ruta_imagen}'. Verifica la ruta.")
    exit()

# -------- Aplicar filtro de Canny para detectar bordes --------
# Parámetros: umbral bajo y umbral alto
umbral_bajo = 100
umbral_alto = 200
bordes = cv2.Canny(imagen, umbral_bajo, umbral_alto)

# -------- Segmentación por Umbral (Threshold) --------
# Si el valor del píxel es mayor que 127, se vuelve blanco (255); si no, negro (0)
umbral_segmentacion = 127
_, segmentada = cv2.threshold(imagen, umbral_segmentacion, 255, cv2.THRESH_BINARY)

# -------- Mostrar resultados --------
plt.figure(figsize=(15, 5))

# Imagen original
plt.subplot(1, 3, 1)
plt.imshow(imagen, cmap='gray')
plt.title('Imagen original')
plt.axis('off')

# Bordes detectados con Canny
plt.subplot(1, 3, 2)
plt.imshow(bordes, cmap='gray')
plt.title(f'Bordes (Canny)\nUmbral bajo: {umbral_bajo}, Umbral alto: {umbral_alto}')
plt.axis('off')

# Imagen segmentada
plt.subplot(1, 3, 3)
plt.imshow(segmentada, cmap='gray')
plt.title(f'Segmentación (Umbral)\nUmbral: {umbral_segmentacion}')
plt.axis('off')

plt.tight_layout()
plt.show()

# -------- Información adicional --------
print("Procesamiento completado.")
print(f"Parámetros de Canny: Umbral bajo = {umbral_bajo}, Umbral alto = {umbral_alto}")
print(f"Parámetro de segmentación: Umbral = {umbral_segmentacion}")
