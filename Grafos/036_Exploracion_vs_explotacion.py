import numpy as np
import random

# Definir acciones y sus recompensas estimadas
acciones = ["A", "B", "C", "D"]
q_values = {a: 0 for a in acciones}  # Valores iniciales de recompensa Q

# Parámetros de exploración-explotación
epsilon = 0.2  # Probabilidad de exploración
alpha = 0.1  # Tasa de aprendizaje
gamma = 0.9  # Factor de descuento

def elegir_accion():
    """
    Selecciona una acción usando la estrategia ε-greedy:
    - Con probabilidad epsilon, elige una acción aleatoria (explora).
    - De lo contrario, elige la acción con el mayor valor Q (explota).
    """
    if random.uniform(0, 1) < epsilon:
        return random.choice(acciones)  # Exploración (elige una acción aleatoria)
    else:
        return max(q_values, key=q_values.get)  # Explotación (elige la mejor acción conocida)

def actualizar_Q(accion, recompensa):
    """
    Actualiza el valor Q de la acción usando la fórmula:
    Q(a) = Q(a) + α * (recompensa - Q(a))
    """
    q_values[accion] += alpha * (recompensa - q_values[accion])

# Simulación de episodios
for episodio in range(10):  # Simular 10 iteraciones
    accion = elegir_accion()  # Elegir acción con exploración/explotación
    recompensa = random.randint(-10, 10)  # Simular una recompensa aleatoria
    actualizar_Q(accion, recompensa)  # Actualizar la tabla Q
    print(f"Episodio {episodio + 1}: Acción = {accion}, Recompensa = {recompensa}, Q-Values = {q_values}")

# Mostrar la mejor acción después del entrenamiento
mejor_accion = max(q_values, key=q_values.get)
print(f"\nMejor acción después del entrenamiento: {mejor_accion}")
