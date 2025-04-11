import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# -------------------------------
# 1. Generamos datos sintéticos
# -------------------------------

X, y_real = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)

# -------------------------------
# 2. Definimos el algoritmo K-means
# -------------------------------

def k_means(X, k, max_iter=100, tol=1e-4):
    """
    Implementación del algoritmo K-Means.
    
    Parámetros:
    - X: ndarray, datos de entrada.
    - k: int, número de grupos.
    - max_iter: int, número máximo de iteraciones.
    - tol: float, tolerancia para la convergencia.
    
    Retorna:
    - grupos: ndarray, índice del grupo asignado a cada punto.
    - centroides: ndarray, posiciones finales de los centroides.
    """
    n_muestras = X.shape[0]
    if k > n_muestras:
        raise ValueError("El número de grupos k no puede ser mayor que el número de muestras.")

    # Inicialización aleatoria de los centroides
    np.random.seed(42)  # Para reproducibilidad
    indices_aleatorios = np.random.choice(n_muestras, k, replace=False)
    centroides = X[indices_aleatorios]

    for i in range(max_iter):
        # Paso 1: Asignar cada punto al centroide más cercano
        distancias = np.linalg.norm(X[:, np.newaxis] - centroides, axis=2)
        grupos = np.argmin(distancias, axis=1)

        # Paso 2: Recalcular los centroides
        nuevos_centroides = np.array([
            X[grupos == j].mean(axis=0) if np.any(grupos == j) else centroides[j]
            for j in range(k)
        ])

        # Verificar convergencia
        if np.linalg.norm(centroides - nuevos_centroides) < tol:
            print(f"Convergencia alcanzada en la iteración {i + 1}")
            break

        centroides = nuevos_centroides

    return grupos, centroides

# -------------------------------
# 3. Ejecutamos K-means
# -------------------------------

k = 3  # Número de grupos
grupos_encontrados, centroides_finales = k_means(X, k)

# -------------------------------
# 4. Mostramos los resultados
# -------------------------------

plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=grupos_encontrados, cmap='viridis', marker='o', label='Datos agrupados')
plt.scatter(centroides_finales[:, 0], centroides_finales[:, 1], c='red', marker='X', s=200, label='Centroides')
plt.title('Resultado del Algoritmo K-Means (Agrupamiento No Supervisado)')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.legend()
plt.grid(True)
plt.show()
