import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# -------------------------------
# 1. Generamos datos sintéticos
# -------------------------------

# Creamos un conjunto de datos sintéticos con 300 muestras, 3 centros y una desviación estándar de 1.0.
# Estos datos se usarán para probar el algoritmo K-Means.
X, y_real = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)

# -------------------------------
# 2. Definimos el algoritmo K-means
# -------------------------------

def k_means(X, k, max_iter=100, tol=1e-4):
    """
    Implementación del algoritmo K-Means.
    
    Parámetros:
    - X: ndarray, datos de entrada (matriz de características).
    - k: int, número de grupos (clusters) a formar.
    - max_iter: int, número máximo de iteraciones permitidas.
    - tol: float, tolerancia para determinar la convergencia (cambio mínimo en los centroides).
    
    Retorna:
    - grupos: ndarray, índice del grupo asignado a cada punto.
    - centroides: ndarray, posiciones finales de los centroides.
    """
    # Número de muestras (filas) en los datos de entrada
    n_muestras = X.shape[0]
    
    # Validación: el número de grupos no puede ser mayor que el número de muestras
    if k > n_muestras:
        raise ValueError("El número de grupos k no puede ser mayor que el número de muestras.")

    # Inicialización aleatoria de los centroides
    # Seleccionamos aleatoriamente k puntos de los datos como los centroides iniciales
    np.random.seed(42)  # Fijamos la semilla para reproducibilidad
    indices_aleatorios = np.random.choice(n_muestras, k, replace=False)
    centroides = X[indices_aleatorios]

    # Iteramos hasta el número máximo de iteraciones o hasta que se alcance la convergencia
    for i in range(max_iter):
        # Paso 1: Asignar cada punto al centroide más cercano
        # Calculamos la distancia euclidiana entre cada punto y cada centroide
        distancias = np.linalg.norm(X[:, np.newaxis] - centroides, axis=2)
        # Asignamos cada punto al índice del centroide más cercano
        grupos = np.argmin(distancias, axis=1)

        # Paso 2: Recalcular los centroides
        # Calculamos la nueva posición de cada centroide como la media de los puntos asignados a él
        nuevos_centroides = np.array([
            X[grupos == j].mean(axis=0) if np.any(grupos == j) else centroides[j]
            for j in range(k)
        ])

        # Verificar convergencia
        # Si el cambio en los centroides es menor que la tolerancia, terminamos el algoritmo
        if np.linalg.norm(centroides - nuevos_centroides) < tol:
            print(f"Convergencia alcanzada en la iteración {i + 1}")
            break

        # Actualizamos los centroides para la siguiente iteración
        centroides = nuevos_centroides

    # Retornamos los grupos asignados y las posiciones finales de los centroides
    return grupos, centroides

# -------------------------------
# 3. Ejecutamos K-means
# -------------------------------

# Definimos el número de grupos (clusters) que queremos encontrar
k = 3  # Número de grupos
# Ejecutamos el algoritmo K-Means con los datos generados
grupos_encontrados, centroides_finales = k_means(X, k)

# -------------------------------
# 4. Mostramos los resultados
# -------------------------------

# Creamos una figura para visualizar los resultados
plt.figure(figsize=(8, 6))

# Dibujamos los puntos de datos, coloreados según el grupo al que pertenecen
plt.scatter(X[:, 0], X[:, 1], c=grupos_encontrados, cmap='viridis', marker='o', label='Datos agrupados')

# Dibujamos los centroides finales en rojo con un marcador más grande
plt.scatter(centroides_finales[:, 0], centroides_finales[:, 1], c='red', marker='X', s=200, label='Centroides')

# Agregamos título y etiquetas a los ejes
plt.title('Resultado del Algoritmo K-Means (Agrupamiento No Supervisado)')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')

# Mostramos la leyenda y una cuadrícula para facilitar la lectura
plt.legend()
plt.grid(True)

# Mostramos la gráfica
plt.show()
