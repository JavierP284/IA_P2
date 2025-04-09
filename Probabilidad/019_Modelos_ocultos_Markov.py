import numpy as np

# -------------------------------
# DEFINICIÓN DEL MODELO HMM
# -------------------------------

# Estados ocultos del clima
# Estos son los estados que queremos inferir (no son directamente observables)
estados = ["Soleado", "Lluvioso"]

# Observaciones visibles
# Estas son las observaciones que podemos medir directamente
observaciones = ["Paraguas", "NoParaguas"]

# Distribución inicial de probabilidad del estado
# Probabilidad inicial de que el clima sea Soleado o Lluvioso
prob_inicial = np.array([0.6, 0.4])  # P(Soleado), P(Lluvioso)

# Matriz de transición: P(estado_t | estado_t-1)
# Probabilidad de pasar de un estado a otro en el siguiente paso de tiempo
transicion = np.array([
    [0.7, 0.3],  # Soleado → [Soleado, Lluvioso]
    [0.4, 0.6]   # Lluvioso → [Soleado, Lluvioso]
])

# Matriz de emisión: P(observación | estado)
# Probabilidad de observar algo dado un estado oculto
emision = np.array([
    [0.1, 0.9],  # Soleado → [Paraguas, NoParaguas]
    [0.8, 0.2]   # Lluvioso → [Paraguas, NoParaguas]
])

# Observaciones reales que recibimos
# Estas son las observaciones que queremos usar para inferir los estados ocultos
observaciones_dadas = ["Paraguas", "Paraguas", "NoParaguas"]

# Convertimos observaciones a índices (0 o 1)
# Esto facilita el acceso a las matrices de emisión
obs_idx = [observaciones.index(o) for o in observaciones_dadas]

def validar_matrices(prob_inicial, transicion, emision):
    """
    Valida que las matrices de probabilidad sean correctas.
    - La distribución inicial debe sumar 1.
    - Cada fila de las matrices de transición y emisión debe sumar 1.
    """
    assert np.isclose(np.sum(prob_inicial), 1), "La distribución inicial no suma 1."
    assert all(np.isclose(np.sum(row), 1) for row in transicion), "Las filas de la matriz de transición no suman 1."
    assert all(np.isclose(np.sum(row), 1) for row in emision), "Las filas de la matriz de emisión no suman 1."

def filtrado_HMM(obs_idx, prob_inicial, transicion, emision):
    """
    Algoritmo de filtrado hacia adelante para calcular las probabilidades
    de los estados ocultos en cada paso de tiempo.
    """
    T = len(obs_idx)  # Número de observaciones
    N = len(estados)  # Número de estados ocultos
    alpha = np.zeros((T, N))  # Matriz para almacenar las probabilidades filtradas

    # Paso 1: inicialización con el primer valor
    # Calculamos la probabilidad inicial considerando la primera observación
    alpha[0] = prob_inicial * emision[:, obs_idx[0]]
    alpha[0] /= np.sum(alpha[0])  # Normalizamos para que las probabilidades sumen 1

    # Paso 2: recursión hacia adelante
    # Calculamos las probabilidades para cada paso de tiempo
    for t in range(1, T):
        for j in range(N):
            # Calculamos la probabilidad de llegar al estado j en el tiempo t
            alpha[t, j] = emision[j, obs_idx[t]] * np.sum(alpha[t-1] * transicion[:, j])
        alpha[t] /= np.sum(alpha[t])  # Normalizamos las probabilidades

    return alpha

def viterbi_HMM(obs_idx, prob_inicial, transicion, emision):
    """
    Algoritmo de Viterbi para encontrar la secuencia más probable de estados ocultos.
    """
    T = len(obs_idx)  # Número de observaciones
    N = len(estados)  # Número de estados ocultos
    delta = np.zeros((T, N))  # Matriz para almacenar las probabilidades más altas
    psi = np.zeros((T, N), dtype=int)  # Matriz para almacenar las rutas óptimas

    # Inicialización
    # Calculamos la probabilidad inicial considerando la primera observación
    delta[0] = prob_inicial * emision[:, obs_idx[0]]

    # Recursión
    # Calculamos las probabilidades más altas para cada paso de tiempo
    for t in range(1, T):
        for j in range(N):
            # Calculamos la probabilidad de la mejor ruta hacia el estado j
            trans_p = delta[t-1] * transicion[:, j]
            psi[t, j] = np.argmax(trans_p)  # Guardamos el índice del mejor estado previo
            delta[t, j] = np.max(trans_p) * emision[j, obs_idx[t]]

    # Reconstrucción del camino óptimo
    # Retrocedemos para encontrar la secuencia más probable de estados
    camino = np.zeros(T, dtype=int)
    camino[T-1] = np.argmax(delta[T-1])  # Último estado más probable
    for t in reversed(range(1, T)):
        camino[t-1] = psi[t, camino[t]]  # Seguimos la ruta óptima hacia atrás

    # Convertir índices a nombres de estados
    estados_probables = [estados[i] for i in camino]
    return estados_probables

# Validamos las matrices
# Esto asegura que las matrices de probabilidad estén correctamente definidas
validar_matrices(prob_inicial, transicion, emision)

# Aplicamos el filtrado
# Calculamos las probabilidades de los estados ocultos en cada paso de tiempo
alpha = filtrado_HMM(obs_idx, prob_inicial, transicion, emision)

# Mostramos las probabilidades filtradas
print("PROBABILIDADES FILTRADAS (estado oculto en cada paso):")
for t in range(len(obs_idx)):
    print(f"Tiempo {t+1}: P(Soleado) = {alpha[t][0]:.4f}, P(Lluvioso) = {alpha[t][1]:.4f}")

# Aplicamos Viterbi
# Calculamos la secuencia más probable de estados ocultos
mejor_camino = viterbi_HMM(obs_idx, prob_inicial, transicion, emision)

# Mostramos la secuencia más probable de estados ocultos
print("\nSECUENCIA MÁS PROBABLE DE ESTADOS OCULTOS (Viterbi):")
print(" → ".join(mejor_camino))
