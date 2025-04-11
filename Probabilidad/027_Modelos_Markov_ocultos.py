import numpy as np

# ----------------------------
# Modelo de Markov Oculto (HMM)
# ----------------------------

# Estados ocultos (no observables)
# Estos representan los estados internos del sistema que no podemos observar directamente.
estados = ['Soleado', 'Lluvioso']

# Observaciones posibles
# Estas son las acciones o eventos que podemos observar.
observaciones = ['Camina', 'Compra', 'Limpia']

# Probabilidades iniciales para cada estado (día 1)
# Representan la probabilidad de que el sistema comience en un estado específico.
prob_inicial = {'Soleado': 0.6, 'Lluvioso': 0.4}

# Matriz de transición entre estados
# Define la probabilidad de pasar de un estado a otro en el siguiente paso.
prob_transicion = {
    'Soleado': {'Soleado': 0.7, 'Lluvioso': 0.3},
    'Lluvioso': {'Soleado': 0.4, 'Lluvioso': 0.6}
}

# Probabilidades de emisión: lo que se observa dado un estado
# Define la probabilidad de observar un evento específico dado un estado oculto.
prob_emision = {
    'Soleado': {'Camina': 0.6, 'Compra': 0.3, 'Limpia': 0.1},
    'Lluvioso': {'Camina': 0.1, 'Compra': 0.4, 'Limpia': 0.5}
}

# Secuencia de observaciones que queremos analizar
# Esta es la secuencia de eventos observados que queremos explicar usando el modelo.
secuencia_obs = ['Camina', 'Compra', 'Limpia']

# ----------------------------
# Algoritmo de Viterbi
# ----------------------------

def viterbi(estados, observaciones, prob_inicial, prob_transicion, prob_emision, secuencia_obs):
    """
    Implementación del algoritmo de Viterbi para encontrar la secuencia más probable de estados.

    Parámetros:
    - estados: lista de estados ocultos.
    - observaciones: lista de observaciones posibles.
    - prob_inicial: dict, probabilidades iniciales de cada estado.
    - prob_transicion: dict, matriz de transición entre estados.
    - prob_emision: dict, matriz de emisión (probabilidades de observación dado un estado).
    - secuencia_obs: lista de observaciones.

    Retorna:
    - camino_optimo: lista con la secuencia más probable de estados.
    - probabilidad_max: probabilidad de la secuencia más probable.
    """
    # Inicializamos la tabla de probabilidades y los caminos
    # `V` almacena las probabilidades máximas de llegar a cada estado en cada paso.
    # `camino` almacena los caminos más probables para llegar a cada estado.
    V = [{}]  # Tabla de probabilidades
    camino = {}  # Guarda los caminos más probables

    # Paso de inicialización
    # Calculamos las probabilidades iniciales para cada estado en el primer paso.
    for estado in estados:
        # Probabilidad de comenzar en `estado` y observar la primera observación.
        V[0][estado] = prob_inicial[estado] * prob_emision[estado][secuencia_obs[0]]
        # El camino inicial para cada estado es simplemente ese estado.
        camino[estado] = [estado]

    # Paso de recursión
    # Calculamos las probabilidades para los pasos siguientes (t > 0).
    for t in range(1, len(secuencia_obs)):
        V.append({})  # Agregamos una nueva fila para el tiempo t.
        nuevo_camino = {}  # Almacenará los nuevos caminos más probables.

        for estado_actual in estados:
            # Calculamos la probabilidad máxima para llegar al estado actual desde cualquier estado anterior.
            (prob_max, estado_prev) = max(
                [(V[t - 1][estado_anterior] *  # Probabilidad de llegar al estado anterior
                  prob_transicion[estado_anterior][estado_actual] *  # Probabilidad de transición al estado actual
                  prob_emision[estado_actual][secuencia_obs[t]],  # Probabilidad de observar la observación actual
                  estado_anterior)  # Guardamos el estado anterior
                 for estado_anterior in estados]
            )

            # Guardamos la probabilidad máxima para el estado actual en el tiempo t.
            V[t][estado_actual] = prob_max
            # Actualizamos el camino más probable para llegar al estado actual.
            nuevo_camino[estado_actual] = camino[estado_prev] + [estado_actual]

        # Actualizamos los caminos con los nuevos caminos calculados.
        camino = nuevo_camino

    # Paso final: elegimos el mejor camino al final de la secuencia
    # Buscamos el estado final con la probabilidad máxima.
    n = len(secuencia_obs) - 1  # Último tiempo
    (probabilidad_max, estado_final) = max((V[n][estado], estado) for estado in estados)

    # Retornamos el camino más probable y su probabilidad.
    return camino[estado_final], probabilidad_max

# ----------------------------
# Ejecución del algoritmo
# ----------------------------

# Ejecutamos el algoritmo de Viterbi
camino_optimo, probabilidad_max = viterbi(estados, observaciones, prob_inicial, prob_transicion, prob_emision, secuencia_obs)

# ----------------------------
# Mostramos resultados
# ----------------------------
print("Secuencia observada:", secuencia_obs)
print("Secuencia más probable de estados:", camino_optimo)
print("Probabilidad de esa secuencia:", probabilidad_max)
