import numpy as np
import matplotlib.pyplot as plt

# ---------- Parámetros del SOM ----------
# Configuración del mapa SOM
filas = 10         # Número de filas del mapa (dimensión vertical)
columnas = 10      # Número de columnas del mapa (dimensión horizontal)
dim_entrada = 3    # Dimensión de los vectores de entrada (en este caso, RGB)

# Parámetros de entrenamiento
epocas = 100       # Número de épocas de entrenamiento
tasa_inicial = 0.5 # Tasa de aprendizaje inicial (se reducirá con el tiempo)
radio_inicial = max(filas, columnas) / 2  # Radio inicial del vecindario (máximo)

# ---------- Datos de entrada ----------
# Generamos datos aleatorios para simular vectores RGB
np.random.seed(0)  # Fijamos la semilla para reproducibilidad
entradas = np.random.rand(500, dim_entrada)  # 500 muestras de 3 valores (R, G, B)

# ---------- Inicialización de los pesos ----------
# Inicializamos los pesos de las neuronas del mapa con valores aleatorios
# Cada neurona tiene un vector de pesos de la misma dimensión que los datos de entrada
pesos = np.random.rand(filas, columnas, dim_entrada)

# ---------- Función de distancia euclidiana ----------
# Calcula la distancia entre dos vectores
def distancia(a, b):
    return np.linalg.norm(a - b)

# ---------- Función de vecindario (gaussiana) ----------
# Calcula la influencia de una neurona en función de su distancia al BMU
def vecindad(distancia, radio):
    return np.exp(-distancia**2 / (2 * (radio**2)))

# ---------- Visualización del progreso ----------
# Muestra el estado actual del mapa SOM
def visualizar_mapa(pesos, epoca, filas, columnas):
    plt.figure(figsize=(6, 6))
    for i in range(filas):
        for j in range(columnas):
            # Cada neurona se representa como un punto coloreado según sus pesos RGB
            plt.scatter(j, filas - 1 - i, color=pesos[i][j], s=200)
    plt.title(f"Mapa SOM - Época {epoca+1}")
    plt.axis("off")  # Ocultamos los ejes para una visualización más limpia
    plt.show()

# ---------- Entrenamiento SOM ----------
# Entrenamos el mapa SOM durante un número de épocas
for epoca in range(epocas):
    # Reducimos la tasa de aprendizaje y el radio del vecindario con el tiempo
    tasa = tasa_inicial * (1 - epoca / epocas)  # Tasa decreciente
    radio = radio_inicial * (1 - epoca / epocas)  # Radio decreciente

    # Iteramos sobre cada entrada
    for entrada in entradas:
        # 1. Buscar la neurona ganadora (BMU - Best Matching Unit)
        bmu_pos = (0, 0)  # Posición inicial de la BMU
        min_dist = float('inf')  # Distancia mínima inicial (infinita)

        # Recorremos todas las neuronas del mapa
        for i in range(filas):
            for j in range(columnas):
                # Calculamos la distancia entre la entrada y los pesos de la neurona
                d = distancia(entrada, pesos[i][j])
                if d < min_dist:  # Si encontramos una distancia menor
                    min_dist = d  # Actualizamos la distancia mínima
                    bmu_pos = (i, j)  # Guardamos la posición de la BMU

        # 2. Actualizar pesos de las neuronas en el vecindario
        for i in range(filas):
            for j in range(columnas):
                # Calculamos la distancia de la neurona actual a la BMU
                dist_vecinal = distancia(np.array([i, j]), np.array(bmu_pos))
                if dist_vecinal <= radio:  # Si está dentro del radio del vecindario
                    # Calculamos la influencia de la neurona
                    influencia = vecindad(dist_vecinal, radio)
                    # Actualizamos los pesos de la neurona
                    pesos[i][j] += tasa * influencia * (entrada - pesos[i][j])

    # Mostrar progreso cada 10 épocas
    if epoca % 10 == 0 or epoca == epocas - 1:
        print(f"Época {epoca+1}/{epocas}")
        visualizar_mapa(pesos, epoca, filas, columnas)

# ---------- Visualización del Mapa SOM final ----------
# Mostramos el estado final del mapa SOM después del entrenamiento
visualizar_mapa(pesos, epocas - 1, filas, columnas)
