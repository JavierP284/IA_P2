import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# ESTADOS Y OBSERVACIONES
# -------------------------------

# Definimos los estados ocultos del modelo
estados = ["Lluvia", "NoLluvia"]

# Definimos las observaciones posibles
observaciones = ["Paraguas", "NoParaguas"]

# Matriz de transición: Probabilidad de pasar de un estado a otro
P_transicion = np.array([
    [0.7, 0.3],  # De Lluvia → [Lluvia, NoLluvia]
    [0.3, 0.7]   # De NoLluvia → [Lluvia, NoLluvia]
])

# Matriz de emisión: Probabilidad de observar algo dado un estado oculto
P_emision = np.array([
    [0.9, 0.1],  # Lluvia → [Paraguas, NoParaguas]
    [0.2, 0.8]   # NoLluvia → [Paraguas, NoParaguas]
])

# Distribución inicial: Probabilidad inicial de cada estado
estado_inicial = np.array([0.5, 0.5])  # [P(Lluvia), P(NoLluvia)]

# Observaciones dadas (lo que el agente observa en el tiempo)
observaciones_dadas = ["Paraguas", "Paraguas", "NoParaguas"]

# Convertimos las observaciones a índices para trabajar con las matrices
obs_idx = [observaciones.index(o) for o in observaciones_dadas]

# -------------------------------
# VALIDACIÓN DE ENTRADAS
# -------------------------------

# Validamos que las matrices y las observaciones sean consistentes
def validar_entradas():
    assert P_transicion.shape == (2, 2), "La matriz de transición debe ser 2x2."
    assert P_emision.shape == (2, 2), "La matriz de emisión debe ser 2x2."
    assert len(estado_inicial) == 2, "El vector de estado inicial debe tener longitud 2."
    for obs in observaciones_dadas:
        if obs not in observaciones:
            raise ValueError(f"Observación no válida: {obs}")

validar_entradas()

# -------------------------------
# FILTRADO: α (forward algorithm)
# -------------------------------

# Calcula las probabilidades de los estados ocultos dado un conjunto de observaciones
def filtrado(obs_idx):
    alphas = []  # Lista para almacenar las probabilidades en cada paso
    # Paso inicial: multiplicamos la distribución inicial por la probabilidad de emisión
    alpha = estado_inicial * P_emision[:, obs_idx[0]]
    alpha = alpha / np.sum(alpha)  # Normalización para que las probabilidades sumen 1
    alphas.append(alpha)

    # Iteramos sobre las observaciones para calcular las probabilidades en cada paso
    for t in range(1, len(obs_idx)):
        # Calculamos el nuevo alpha usando la matriz de transición y emisión
        alpha = P_emision[:, obs_idx[t]] * (P_transicion.T @ alpha)
        alpha = alpha / np.sum(alpha)  # Normalización
        alphas.append(alpha)

    return alphas

# -------------------------------
# PREDICCIÓN: siguiente paso sin observar
# -------------------------------

# Predice la probabilidad de los estados en pasos futuros sin observar nada nuevo
def prediccion(ultimo_alpha, pasos=1):
    pred = ultimo_alpha.copy()  # Iniciamos con el último alpha calculado
    for _ in range(pasos):
        # Usamos la matriz de transición para predecir el siguiente estado
        pred = P_transicion.T @ pred
    return pred

# -------------------------------
# SUAVIZADO: combinar filtrado + retroceso
# -------------------------------

# Combina información pasada (filtrado) y futura (retroceso) para estimar los estados ocultos
def suavizado(alphas):
    T = len(alphas)  # Número de pasos de tiempo
    betas = [np.ones(2)] * T  # Inicializamos betas con 1 (retroceso)
    smoothed = [None] * T  # Lista para almacenar las probabilidades suavizadas

    # Iteramos hacia atrás en el tiempo
    for t in reversed(range(T)):
        if t == T - 1:
            # En el último paso, el suavizado es igual al filtrado
            smoothed[t] = alphas[t]
        else:
            # Calculamos beta usando la matriz de transición y emisión
            beta = P_transicion @ (P_emision[:, obs_idx[t+1]] * betas[t+1])
            beta = beta / np.sum(beta)  # Normalización
            betas[t] = beta
            # Combinamos alpha y beta para obtener el suavizado
            smoothed[t] = alphas[t] * beta
            smoothed[t] = smoothed[t] / np.sum(smoothed[t])  # Normalización

    return smoothed

# -------------------------------
# EXPLICACIÓN: Algoritmo de Viterbi
# -------------------------------

# Encuentra la secuencia más probable de estados ocultos (decodificación)
def viterbi(obs_idx):
    T = len(obs_idx)  # Número de pasos de tiempo
    delta = np.zeros((T, 2))  # Probabilidades máximas hasta cada estado
    psi = np.zeros((T, 2), dtype=int)  # Matriz para rastrear los estados previos

    # Paso inicial: multiplicamos la distribución inicial por la probabilidad de emisión
    delta[0] = estado_inicial * P_emision[:, obs_idx[0]]

    # Iteramos sobre el tiempo para calcular delta y psi
    for t in range(1, T):
        for j in range(2):  # Para cada estado
            # Calculamos la probabilidad máxima de llegar al estado j
            trans_p = delta[t-1] * P_transicion[:, j]
            psi[t, j] = np.argmax(trans_p)  # Guardamos el estado previo más probable
            delta[t, j] = np.max(trans_p) * P_emision[j, obs_idx[t]]

    # Reconstruimos el camino más probable hacia atrás
    camino = np.zeros(T, dtype=int)
    camino[-1] = np.argmax(delta[-1])  # Último estado más probable
    for t in reversed(range(1, T)):
        camino[t-1] = psi[t, camino[t]]

    # Convertimos los índices de estados a nombres
    estados_probables = [estados[i] for i in camino]
    return estados_probables

# -------------------------------
# FUNCIONES AUXILIARES
# -------------------------------

# Imprime los resultados del filtrado en formato tabular
def imprimir_resultados_filtrado(alphas):
    print("FILTRADO:")
    print(f"{'Paso':<5} {'P(Lluvia)':<12} {'P(NoLluvia)':<12}")
    for t, a in enumerate(alphas):
        print(f"{t+1:<5} {a[0]:<12.4f} {a[1]:<12.4f}")

# Grafica las probabilidades de los estados a lo largo del tiempo
def graficar_probabilidades(alphas, titulo):
    tiempos = range(1, len(alphas) + 1)
    lluvias = [a[0] for a in alphas]
    no_lluvias = [a[1] for a in alphas]

    plt.plot(tiempos, lluvias, label="P(Lluvia)", marker='o')
    plt.plot(tiempos, no_lluvias, label="P(NoLluvia)", marker='o')
    plt.xlabel("Tiempo")
    plt.ylabel("Probabilidad")
    plt.title(titulo)
    plt.legend()
    plt.grid()
    plt.show()

# -------------------------------
# EJECUCIÓN DEL ALGORITMO
# -------------------------------

if __name__ == "__main__":
    # Filtrado
    alphas = filtrado(obs_idx)
    imprimir_resultados_filtrado(alphas)
    graficar_probabilidades(alphas, "Probabilidades de Filtrado")

    # Predicción del estado siguiente
    pred = prediccion(alphas[-1])
    print("\nPREDICCIÓN (paso siguiente):")
    print(f"P(Lluvia) = {pred[0]:.4f}, P(NoLluvia) = {pred[1]:.4f}")

    # Suavizado
    smoothed = suavizado(alphas)
    print("\nSUAVIZADO:")
    for t, s in enumerate(smoothed):
        print(f"Tiempo {t+1} → P(Lluvia) = {s[0]:.4f}, P(NoLluvia) = {s[1]:.4f}")
    graficar_probabilidades(smoothed, "Probabilidades de Suavizado")

    # Explicación (secuencia más probable de estados)
    camino = viterbi(obs_idx)
    print("\nEXPLICACIÓN (Viterbi - camino más probable):")
    print(" → ".join(camino))
