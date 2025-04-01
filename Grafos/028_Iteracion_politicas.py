import numpy as np

# Parámetros del algoritmo
gamma = 0.9  # Factor de descuento: qué tan importante es el futuro en comparación con el presente
theta = 0.0001  # Criterio de convergencia: diferencia mínima aceptable entre iteraciones

# Definimos la cuadrícula 3x3 (los estados)
grid_size = 3  # Tamaño de la cuadrícula
states = [(i, j) for i in range(grid_size) for j in range(grid_size)]  # Lista de todos los estados posibles

# Definimos las recompensas del entorno
rewards = np.full((grid_size, grid_size), -1)  # Todos los movimientos tienen un costo de -1
rewards[2, 2] = 10  # La meta tiene una recompensa de +10
rewards[1, 1] = -10  # Un obstáculo tiene una penalización de -10

# Acciones posibles y sus movimientos correspondientes (dx, dy)
actions = {
    "Arriba": (-1, 0),    # Moverse hacia arriba
    "Abajo": (1, 0),      # Moverse hacia abajo
    "Izquierda": (0, -1), # Moverse hacia la izquierda
    "Derecha": (0, 1)     # Moverse hacia la derecha
}

# Inicializamos los valores de los estados en 0
values = np.zeros((grid_size, grid_size))  # Matriz de valores para cada estado

# Inicializamos una política aleatoria (todas las celdas eligen "Abajo" por defecto)
policy = {state: "Abajo" for state in states}  # Diccionario que almacena la acción para cada estado

# Función para obtener los movimientos válidos desde un estado
def get_valid_moves(state):
    """
    Devuelve una lista de movimientos válidos desde un estado dado.
    Cada movimiento incluye el nuevo estado y la acción correspondiente.
    """
    i, j = state
    valid_moves = []
    
    for action, (di, dj) in actions.items():
        new_i, new_j = i + di, j + dj
        # Verificamos que el nuevo estado esté dentro de los límites de la cuadrícula
        if 0 <= new_i < grid_size and 0 <= new_j < grid_size:
            valid_moves.append(((new_i, new_j), action))
    
    return valid_moves

# Etapa 1: Evaluación de la Política
def policy_evaluation():
    """
    Evalúa la política actual calculando los valores de los estados
    hasta que los valores converjan (diferencia mínima entre iteraciones).
    """
    global values
    while True:
        delta = 0  # Diferencia máxima entre valores de iteraciones consecutivas
        new_values = values.copy()  # Copia de los valores actuales para actualizarlos
        
        for state in states:
            i, j = state
            
            # Si el estado es la meta, no actualizamos su valor
            if state == (2, 2):
                continue  
            
            # Obtenemos la acción según la política actual
            action = policy[state]
            (di, dj) = actions[action]  # Movimiento correspondiente a la acción
            new_i, new_j = i + di, j + dj
            
            # Verificamos que el nuevo estado esté dentro de los límites
            if 0 <= new_i < grid_size and 0 <= new_j < grid_size:
                reward = rewards[new_i, new_j]  # Recompensa del nuevo estado
                # Actualizamos el valor del estado actual usando la ecuación de Bellman
                new_values[i, j] = reward + gamma * values[new_i, new_j]
            
            # Calculamos la diferencia máxima entre los valores antiguos y nuevos
            delta = max(delta, abs(values[i, j] - new_values[i, j]))
        
        # Actualizamos los valores
        values = new_values
        
        # Si la diferencia máxima es menor que el umbral, terminamos
        if delta < theta:
            break

# Etapa 2: Mejora de la Política
def policy_improvement():
    """
    Mejora la política actual seleccionando la mejor acción para cada estado
    basada en los valores actuales de los estados.
    """
    global policy
    policy_stable = True  # Indicador de si la política ha cambiado
    
    for state in states:
        i, j = state
        
        # Si el estado es la meta, no cambiamos su política
        if state == (2, 2):
            continue  
        
        best_action = None  # Mejor acción encontrada
        best_value = float("-inf")  # Mejor valor encontrado (inicialmente -infinito)
        
        # Evaluamos todas las acciones posibles desde el estado actual
        for (new_state, action) in get_valid_moves(state):
            ni, nj = new_state
            reward = rewards[ni, nj]  # Recompensa del nuevo estado
            value = reward + gamma * values[ni, nj]  # Valor esperado de la acción
            
            # Si encontramos una acción con mejor valor, la seleccionamos
            if value > best_value:
                best_value = value
                best_action = action
        
        # Si la mejor acción encontrada es diferente a la actual, actualizamos la política
        if policy[state] != best_action:
            policy[state] = best_action
            policy_stable = False  # La política ha cambiado
    
    return policy_stable  # Devolvemos si la política es estable

# Algoritmo de Iteración de Políticas
def policy_iteration():
    """
    Ejecuta el algoritmo de iteración de políticas:
    1. Evalúa la política actual.
    2. Mejora la política.
    3. Repite hasta que la política sea estable.
    """
    iteration = 0
    while True:
        print(f"\nIteración {iteration}: Evaluando Política...")
        policy_evaluation()  # Etapa 1: Evaluación de la política
        
        print(f"\nIteración {iteration}: Mejorando Política...")
        stable = policy_improvement()  # Etapa 2: Mejora de la política
        
        # Mostramos los valores actuales de los estados
        print("Valores de la Política:")
        print(values)
        
        # Si la política no cambia, hemos encontrado la política óptima
        if stable:
            print("\n¡Política Óptima Encontrada!")
            break
        
        iteration += 1  # Incrementamos el contador de iteraciones

# Ejecutamos la iteración de políticas
policy_iteration()

# Mostramos la política final
print("\nPolítica Óptima:")
for i in range(grid_size):
    row = ""
    for j in range(grid_size):
        # Mostramos la acción óptima para cada estado
        row += f"{policy[(i, j)]:^10} "
    print(row)
