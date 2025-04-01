import numpy as np
import random

# Parámetros del entorno
estados = ["A", "B", "C", "D"]  # Estados posibles
acciones = ["Izquierda", "Derecha", "Arriba", "Abajo"]  # Acciones posibles

# Tabla Q inicializada en 0
Q_table = {s: {a: 0 for a in acciones} for s in estados}

# Parámetros de aprendizaje
alpha = 0.1    # Tasa de aprendizaje
gamma = 0.9    # Factor de descuento
epsilon = 0.2  # Probabilidad de exploración

def elegir_accion(estado):
    """
    Selecciona una acción usando la estrategia ε-greedy:
    - Con probabilidad epsilon, elige una acción aleatoria (explora).
    - De lo contrario, elige la acción con el mayor valor Q (explota).
    """
    if random.uniform(0, 1) < epsilon:
        return random.choice(acciones)  # Explorar
    else:
        return max(Q_table[estado], key=Q_table[estado].get)  # Explotar

# Manejo de estados no visitados en Q_table
def actualizar_Q(estado, accion, recompensa, siguiente_estado):
    """
    Actualiza la tabla Q usando la ecuación de Q-Learning:
    Q(s, a) = Q(s, a) + α * [recompensa + γ max(Q(s', a')) - Q(s, a)]
    """
    if siguiente_estado not in Q_table:
        Q_table[siguiente_estado] = {a: 0 for a in acciones}  # Inicializar si no existe
    max_Q_siguiente = max(Q_table[siguiente_estado].values())  # Mejor Q(s', a')
    Q_table[estado][accion] += alpha * (recompensa + gamma * max_Q_siguiente - Q_table[estado][accion])

# Simulación de episodios de entrenamiento
episodios = [
    [("A", "Derecha", 0, "B"), ("B", "Derecha", 0, "C"), ("C", "Abajo", 1, "D")],  # Episodio 1
    [("A", "Derecha", 0, "B"), ("B", "Izquierda", -1, "A")],  # Episodio 2 (acción negativa)
    [("C", "Abajo", 1, "D")],  # Episodio 3 (recompensa alta)
]

# Entrenamiento del agente
for episodio in episodios:
    for estado, accion, recompensa, siguiente_estado in episodio:
        # Elegir acción usando ε-greedy (opcional, si no usas acciones predefinidas)
        accion = elegir_accion(estado)
        actualizar_Q(estado, accion, recompensa, siguiente_estado)

# Mostrar la tabla Q final
print("\nTabla Q final después del entrenamiento:")
for estado in Q_table:
    print(f"Estado {estado}: {Q_table[estado]}")

# Mostrar la mejor política aprendida
print("\nPolítica aprendida:")
for estado in estados:
    mejor_accion = max(Q_table[estado], key=Q_table[estado].get)
    print(f"Estado {estado}: Mejor acción -> {mejor_accion}")
