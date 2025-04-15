# Importamos las librerías necesarias
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargamos la imagen en escala de grises
imagen = cv2.imread('Probabilidad/Imagenes/carretera.jpg', cv2.IMREAD_GRAYSCALE)

# Verificamos si la imagen se cargó correctamente
if imagen is None:
    raise ValueError("No se pudo cargar la imagen. Asegúrate de que 'carretera.jpg' esté en el mismo directorio.")

# Aplicamos un filtro de bordes usando el detector de Canny
bordes = cv2.Canny(imagen, 50, 150, apertureSize=3)

# Usamos la transformada de Hough para detectar líneas en la imagen
lineas = cv2.HoughLines(bordes, 1, np.pi / 180, 150)

# Convertimos la imagen original en color para dibujar líneas con color
imagen_color = cv2.cvtColor(imagen, cv2.COLOR_GRAY2BGR)

# Dibujamos las líneas detectadas en la imagen
if lineas is not None:
    for i, linea in enumerate(lineas):
        rho, theta = linea[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho

        # Calculamos los puntos extremos de la línea para dibujarla
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        # Dibujamos la línea en color rojo
        cv2.line(imagen_color, (x1, y1), (x2, y2), (0, 0, 255), 2)

        # Etiquetamos cada línea con un número
        cv2.putText(imagen_color, f'Línea {i+1}', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

# Mostramos el resultado usando matplotlib
plt.figure(figsize=(10, 8))
plt.imshow(cv2.cvtColor(imagen_color, cv2.COLOR_BGR2RGB))
plt.title('Líneas detectadas y etiquetadas')
plt.axis('off')
plt.show()
