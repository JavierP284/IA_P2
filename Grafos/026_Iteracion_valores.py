import numpy as np

# Parámetros del algoritmo
gamma = 0.9  # Factor de descuento (qué tan importante es el futuro)
theta = 0.0001  # Criterio de convergencia (pequeña diferencia entre iteraciones)

# Definimos la cuadrícula 3x3 (los estados)
grid_size = 3
states = [(i, j) for i in range(grid_size) for j in range(grid_size)]

# Definimos las recompensas del entorno
rewards = np.full((grid_size, grid_size), -1)  # Todos los movimientos cuestan -1
rewards[2, 2] = 10  # Meta con recompensa +10
rewards[1, 1] = -10  # Obstáculo con penalización -10

# Acciones posibles: (dx, dy)
actions = {
    "Arriba": (-1, 0),
    "Abajo": (1, 0),
    "Izquierda": (0, -1),
    "Derecha": (0, 1)
}

# Inicializamos los valores de los estados en 0
values = np.zeros((grid_size, grid_size))

# Función para obtener estados vecinos válidos
def get_valid_moves(state):
    i, j = state
    valid_moves = []
    
    for action, (di, dj) in actions.items():
        new_i, new_j = i + di, j + dj
        if 0 <= new_i < grid_size and 0 <= new_j < grid_size:  # Verificamos límites
            valid_moves.append(((new_i, new_j), action))
    
    return valid_moves

# Algoritmo de Iteración de Valores
def value_iteration():
    iteration = 0  # Contador de iteraciones

    while True:
        delta = 0  # Máxima diferencia entre iteraciones
        new_values = values.copy()  # Copia para actualizar los valores
        
        for state in states:
            i, j = state
            
            if state == (2, 2):  # Si es la meta, no cambiamos su valor
                continue  
            
            max_value = float("-inf")  # Iniciamos con un valor muy bajo
            
            # Evaluamos cada acción posible desde el estado actual
            for (new_state, action) in get_valid_moves(state):
                ni, nj = new_state
                reward = rewards[ni, nj]  # Recompensa del nuevo estado
                value = reward + gamma * values[ni, nj]  # Fórmula de Iteración de Valores
                
                if value > max_value:
                    max_value = value  # Guardamos el mejor valor encontrado
            
            # Actualizamos el valor del estado
            new_values[i, j] = max_value
            
            # Calculamos el cambio más grande en esta iteración
            delta = max(delta, abs(values[i, j] - new_values[i, j]))
        
        values[:] = new_values  # Actualizamos los valores
        iteration += 1
        
        print(f"Iteración {iteration}:")
        print(values)
        print("\n")

        # Si el cambio es menor que theta, terminamos
        if delta < theta:
            break

# Ejecutamos la iteración de valores
value_iteration()
