import numpy as np

# -------------------------------
# MODELO HMM: ESTADOS Y OBSERVACIONES
# -------------------------------
estados = ["Lluvia", "NoLluvia"]
observaciones = ["Paraguas", "NoParaguas"]

# Matriz de transición P(estado_t | estado_{t-1})
P_transicion = np.array([
    [0.7, 0.3],  # De Lluvia a [Lluvia, NoLluvia]
    [0.3, 0.7]   # De NoLluvia a [Lluvia, NoLluvia]
])

# Matriz de emisión P(observación | estado)
P_emision = np.array([
    [0.9, 0.1],  # Lluvia → [Paraguas, NoParaguas]
    [0.2, 0.8]   # NoLluvia → [Paraguas, NoParaguas]
])

# Distribución inicial
estado_inicial = np.array([0.5, 0.5])

# Secuencia de observaciones
observaciones_dadas = ["Paraguas", "Paraguas", "NoParaguas"]
obs_idx = [observaciones.index(o) for o in observaciones_dadas]

# -------------------------------
# ALGORITMO HACIA ADELANTE (FORWARD)
# -------------------------------
def hacia_adelante():
    """
    Calcula las probabilidades hacia adelante (alpha) para la secuencia de observaciones.
    """
    T = len(obs_idx)
    N = len(estados)
    alpha = np.zeros((T, N))

    # Inicialización
    alpha[0] = estado_inicial * P_emision[:, obs_idx[0]]
    print(f"Alpha inicial: {alpha[0]}")

    # Recursión hacia adelante
    for t in range(1, T):
        for j in range(N):
            alpha[t, j] = P_emision[j, obs_idx[t]] * np.sum(alpha[t-1] * P_transicion[:, j])
        print(f"Alpha en tiempo {t}: {alpha[t]}")

    return alpha

# -------------------------------
# ALGORITMO HACIA ATRÁS (BACKWARD)
# -------------------------------
def hacia_atras():
    """
    Calcula las probabilidades hacia atrás (beta) para la secuencia de observaciones.
    """
    T = len(obs_idx)
    N = len(estados)
    beta = np.ones((T, N))  # Iniciamos con 1s (último paso)
    print(f"Beta inicial (último paso): {beta[-1]}")

    # Recursión hacia atrás
    for t in reversed(range(T - 1)):
        for i in range(N):
            beta[t, i] = np.sum(P_transicion[i, :] * P_emision[:, obs_idx[t+1]] * beta[t+1, :])
        print(f"Beta en tiempo {t}: {beta[t]}")

    return beta

# -------------------------------
# CALCULAR SUAVIZADO: γ_t(i) = α_t(i) * β_t(i) / normalización
# -------------------------------
def suavizado_forward_backward():
    """
    Calcula las probabilidades suavizadas usando el algoritmo Forward-Backward.
    """
    alpha = hacia_adelante()
    beta = hacia_atras()
    posterior = alpha * beta

    # Normalizamos cada fila (por tiempo)
    posterior = posterior / posterior.sum(axis=1, keepdims=True)
    return posterior

# -------------------------------
# EJECUCIÓN
# -------------------------------
posterior = suavizado_forward_backward()

# Mostramos resultados
print("\nProbabilidades suavizadas en cada paso (Forward-Backward):")
for t, prob in enumerate(posterior):
    print(f"Tiempo {t+1}: P(Lluvia) = {prob[0]:.4f}, P(NoLluvia) = {prob[1]:.4f}")
