import cv2
import numpy as np

# Leer la imagen en escala de grises
# Se carga la imagen 'filtro.jpeg' en modo de escala de grises.
image = cv2.imread('filtro.jpeg', cv2.IMREAD_GRAYSCALE)

# Verificar si la imagen se cargó correctamente
# Si la imagen no se encuentra o no se puede cargar, se muestra un mensaje de error y se detiene el programa.
if image is None:
    print("Error: No se pudo cargar la imagen. Verifica la ruta del archivo.")
    exit()

# Contaminar la imagen con ruido gaussiano
# Se define el ruido gaussiano con una media (mean) y una varianza (var).
mean = 0  # Media del ruido
var = 100  # Varianza del ruido
sigma = var ** 0.5  # Desviación estándar del ruido
# Se genera una matriz de ruido gaussiano con las mismas dimensiones que la imagen.
gaussian_noise = np.random.normal(mean, sigma, image.shape).reshape(image.shape)
# Se suma el ruido gaussiano a la imagen original.
noisy_gaussian = image + gaussian_noise
# Se asegura que los valores de los píxeles estén en el rango válido [0, 255].
noisy_gaussian = np.clip(noisy_gaussian, 0, 255).astype(np.uint8)

# Contaminar la imagen con ruido sal y pimienta
# Se define la proporción de sal y pimienta y la cantidad total de ruido.
s_vs_p = 0.5  # Proporción de sal frente a pimienta
amount = 0.04  # Cantidad de ruido
# Se crea una copia de la imagen original para añadir el ruido.
noisy_sp = np.copy(image)

# Sal
# Se calcula el número de píxeles que serán afectados por el ruido de tipo "sal".
num_salt = np.ceil(amount * image.size * s_vs_p)
# Se generan coordenadas aleatorias para los píxeles que serán afectados.
coords = [np.random.randint(0, i, int(num_salt)) for i in image.shape]
# Se asigna el valor máximo (255) a los píxeles seleccionados para simular "sal".
noisy_sp[tuple(coords)] = 255

# Pimienta
# Se calcula el número de píxeles que serán afectados por el ruido de tipo "pimienta".
num_pepper = np.ceil(amount * image.size * (1. - s_vs_p))
# Se generan coordenadas aleatorias para los píxeles que serán afectados.
coords = [np.random.randint(0, i, int(num_pepper)) for i in image.shape]
# Se asigna el valor mínimo (0) a los píxeles seleccionados para simular "pimienta".
noisy_sp[tuple(coords)] = 0

# Aplicar filtros a la imagen con ruido gaussiano
# Se aplican diferentes filtros para reducir el ruido gaussiano:
filtered_gaussian_gaussian = cv2.GaussianBlur(noisy_gaussian, (5, 5), 0)  # Filtro gaussiano
filtered_gaussian_mean = cv2.blur(noisy_gaussian, (5, 5))  # Filtro de media
filtered_gaussian_median = cv2.medianBlur(noisy_gaussian, 5)  # Filtro de mediana
filtered_gaussian_min = cv2.erode(noisy_gaussian, np.ones((5, 5), np.uint8))  # Filtro mínimo
filtered_gaussian_max = cv2.dilate(noisy_gaussian, np.ones((5, 5), np.uint8))  # Filtro máximo

# Aplicar filtros a la imagen con ruido sal y pimienta
# Se aplican los mismos filtros para reducir el ruido sal y pimienta:
filtered_sp_gaussian = cv2.GaussianBlur(noisy_sp, (5, 5), 0)  # Filtro gaussiano
filtered_sp_mean = cv2.blur(noisy_sp, (5, 5))  # Filtro de media
filtered_sp_median = cv2.medianBlur(noisy_sp, 5)  # Filtro de mediana
filtered_sp_min = cv2.erode(noisy_sp, np.ones((5, 5), np.uint8))  # Filtro mínimo
filtered_sp_max = cv2.dilate(noisy_sp, np.ones((5, 5), np.uint8))  # Filtro máximo

# Mostrar las imágenes resultantes usando cv2
# Se muestran la imagen original, las imágenes con ruido y las imágenes filtradas.
cv2.imshow('Original', image)
cv2.imshow('Ruido Gaussiano', noisy_gaussian)
cv2.imshow('Ruido Sal y Pimienta', noisy_sp)

cv2.imshow('Gaussiano (Gaussiano)', filtered_gaussian_gaussian)
cv2.imshow('Media (Gaussiano)', filtered_gaussian_mean)
cv2.imshow('Mediana (Gaussiano)', filtered_gaussian_median)
cv2.imshow('Minimo (Gaussiano)', filtered_gaussian_min)
cv2.imshow('Maximo (Gaussiano)', filtered_gaussian_max)

cv2.imshow('Gaussiano (Sal y Pimienta)', filtered_sp_gaussian)
cv2.imshow('Media (Sal y Pimienta)', filtered_sp_mean)
cv2.imshow('Mediana (Sal y Pimienta)', filtered_sp_median)
cv2.imshow('Minimo (Sal y Pimienta)', filtered_sp_min)
cv2.imshow('Maximo (Sal y Pimienta)', filtered_sp_max)

# Esperar a que el usuario presione una tecla y cerrar las ventanas
# cv2.waitKey(0) espera indefinidamente hasta que se presione una tecla.
cv2.waitKey(0)
cv2.destroyAllWindows()  # Cierra todas las ventanas abiertas por OpenCV.