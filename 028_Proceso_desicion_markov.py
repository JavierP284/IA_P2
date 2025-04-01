import numpy as np

# Definir los parámetros del MDP
gamma = 0.9  # Factor de descuento (prioriza recompensas a corto/largo plazo)
theta = 0.0001  # Criterio de convergencia

# Definir los estados
estados = ['A', 'B', 'C']

# Definir las acciones posibles en cada estado
acciones = {
    'A': ['Ir_B', 'Ir_C'],
    'B': ['Ir_A', 'Ir_C'],
    'C': ['Ir_A']
}

# Definir la función de recompensa R(s, a, s')
recompensas = {
    'A': {'Ir_B': 5, 'Ir_C': 10},
    'B': {'Ir_A': -1, 'Ir_C': 2},
    'C': {'Ir_A': 0}
}

# Definir la probabilidad de transición P(s' | s, a)
transiciones = {
    'A': {'Ir_B': {'B': 1.0}, 'Ir_C': {'C': 1.0}},
    'B': {'Ir_A': {'A': 1.0}, 'Ir_C': {'C': 1.0}},
    'C': {'Ir_A': {'A': 1.0}}
}

# Inicializar valores de los estados (V)
V = {s: 0 for s in estados}  # Todos los valores comienzan en 0

# Iteración de valores
while True:
    delta = 0  # Almacena el mayor cambio en V(s)
    nuevo_V = V.copy()  # Crear una copia de los valores actuales
    
    for s in estados:
        max_valor = float('-inf')  # Inicializar con un valor muy bajo
        
        for a in acciones.get(s, []):  # Recorrer acciones disponibles en el estado s
            valor_accion = 0
            
            for s_prima, prob in transiciones[s][a].items():
                recompensa = recompensas[s][a]  # Obtener recompensa inmediata
                valor_accion += prob * (recompensa + gamma * V[s_prima])  # Fórmula de Bellman
            
            max_valor = max(max_valor, valor_accion)  # Seleccionar el mejor valor
            
        nuevo_V[s] = max_valor  # Actualizar valor óptimo del estado
        
        delta = max(delta, abs(nuevo_V[s] - V[s]))  # Actualizar cambio máximo
    
    V = nuevo_V  # Actualizar los valores de los estados
    
    if delta < theta:  # Verificar convergencia
        break

# Mostrar los valores óptimos de cada estado
print("Valores Óptimos de los Estados (V):")
for estado, valor in V.items():
    print(f"{estado}: {valor:.2f}")
