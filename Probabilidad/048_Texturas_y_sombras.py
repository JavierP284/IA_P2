import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import local_binary_pattern

# Función para cargar una imagen en escala de grises
def cargar_imagen(ruta):
    """
    Carga una imagen desde la ruta especificada y la convierte a escala de grises.
    Si no se encuentra la imagen, lanza una excepción.

    """
    imagen = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
    if imagen is None:
        raise FileNotFoundError(f"No se pudo cargar la imagen en la ruta: {ruta}")
    return imagen

# Función para detectar texturas usando Local Binary Pattern (LBP)
def detectar_textura(imagen, puntos, radio):
    """
    Aplica el método Local Binary Pattern (LBP) para detectar texturas en la imagen.
    
    Parámetros:
        imagen (np.ndarray): Imagen en escala de grises.
        puntos (int): Número de puntos circulares para el cálculo de LBP.
        radio (int): Radio del círculo para el cálculo de LBP.
    
    Retorna:
        np.ndarray: Imagen procesada con LBP.
    """
    return local_binary_pattern(imagen, puntos, radio, method='uniform')

# Función para detectar sombras en la imagen
def detectar_sombras(imagen, umbral):
    """
    Detecta sombras en la imagen aplicando un umbral binario inverso.
    
    Parámetros:
        imagen (np.ndarray): Imagen en escala de grises.
        umbral (int): Valor del umbral para la detección de sombras.
    
    Retorna:
        np.ndarray: Imagen binaria con las sombras detectadas.
    """
    _, sombras = cv2.threshold(imagen, umbral, 255, cv2.THRESH_BINARY_INV)
    return sombras

# Función para mostrar los resultados de la detección
def mostrar_resultados(imagen, lbp, sombras):
    """
    Muestra la imagen original, la textura detectada (LBP) y las sombras detectadas.
    
    Parámetros:
        imagen (np.ndarray): Imagen original en escala de grises.
        lbp (np.ndarray): Imagen procesada con LBP.
        sombras (np.ndarray): Imagen binaria con las sombras detectadas.
    """
    plt.figure(figsize=(12, 4))

    # Mostrar la imagen original
    plt.subplot(1, 3, 1)
    plt.imshow(imagen, cmap='gray')
    plt.title('Imagen original')
    plt.axis('off')

    # Mostrar la textura detectada (LBP)
    plt.subplot(1, 3, 2)
    plt.imshow(lbp, cmap='gray')
    plt.title('Textura (LBP)')
    plt.axis('off')

    # Mostrar las sombras detectadas
    plt.subplot(1, 3, 3)
    plt.imshow(sombras, cmap='gray')
    plt.title('Sombras detectadas')
    plt.axis('off')

    # Ajustar el diseño y mostrar la figura
    plt.tight_layout()
    plt.show()

# Función para guardar los resultados en archivos
def guardar_resultados(lbp, sombras, ruta_lbp, ruta_sombras):
    """
    Guarda las imágenes procesadas (LBP y sombras) en archivos.
    
    Parámetros:
        lbp (np.ndarray): Imagen procesada con LBP.
        sombras (np.ndarray): Imagen binaria con las sombras detectadas.
        ruta_lbp (str): Ruta para guardar la imagen LBP.
        ruta_sombras (str): Ruta para guardar la imagen de sombras.
    """
    cv2.imwrite(ruta_lbp, lbp.astype(np.uint8))  # Convertir LBP a uint8 antes de guardar
    cv2.imwrite(ruta_sombras, sombras)

# --------- Parámetros configurables ---------
# Ruta de la imagen de entrada
ruta_imagen = 'Probabilidad/Imagenes/ladrillo.jpg'

# Parámetros para el cálculo de LBP
puntos = 24  # Número de puntos circulares para LBP
radio = 3    # Radio del círculo para LBP

# Umbral para la detección de sombras
umbral_sombras = 70

# --------- Ejecución del algoritmo ---------
try:
    # Cargar la imagen desde la ruta especificada
    imagen = cargar_imagen(ruta_imagen)

    # Detectar texturas usando LBP
    lbp = detectar_textura(imagen, puntos, radio)

    # Detectar sombras aplicando un umbral
    sombras = detectar_sombras(imagen, umbral_sombras)

    # Mostrar los resultados en una ventana gráfica
    mostrar_resultados(imagen, lbp, sombras)

    # Guardar los resultados en archivos
    guardar_resultados(lbp, sombras, 'lbp_resultado.jpg', 'sombras_resultado.jpg')
    print("Resultados guardados: lbp_resultado.jpg, sombras_resultado.jpg")

except FileNotFoundError as e:
    # Manejo de errores si la imagen no se encuentra
    print(e)
