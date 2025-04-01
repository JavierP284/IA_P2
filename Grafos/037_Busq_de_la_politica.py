import numpy as np
import random

# Parámetros del problema
estados = ['A', 'B', 'C', 'D']  # Conjunto de estados posibles
acciones = ['Izquierda', 'Derecha']  # Conjunto de acciones posibles

# Matriz de transición de probabilidades P(s'|s,a) (estado actual -> acción -> nuevo estado)
transiciones = {
    'A': {'Izquierda': 'A', 'Derecha': 'B'},
    'B': {'Izquierda': 'A', 'Derecha': 'C'},
    'C': {'Izquierda': 'B', 'Derecha': 'D'},
    'D': {'Izquierda': 'C', 'Derecha': 'D'}
}

# Recompensas inmediatas por tomar una acción en cada estado
recompensas = {
    'A': {'Izquierda': 0, 'Derecha': 1},
    'B': {'Izquierda': 0, 'Derecha': 2},
    'C': {'Izquierda': 0, 'Derecha': 3},
    'D': {'Izquierda': 0, 'Derecha': 0}
}

DESCUENTO = 0.9  # Factor de descuento para valorar recompensas futuras
CONVERGENCIA = 1e-6  # Umbral para determinar convergencia

def evaluar_politica(politica, V):
    """
    Evalúa una política dada y actualiza los valores de los estados según la ecuación de Bellman.
    """
    while True:
        delta = 0  # Para medir cambios en valores de estado
        for estado in estados:
            accion = politica[estado]  # Acción actual en la política
            nuevo_estado = transiciones[estado][accion]
            recompensa = recompensas[estado][accion]
            nuevo_valor = recompensa + DESCUENTO * V[nuevo_estado]
            delta = max(delta, abs(nuevo_valor - V[estado]))  # Verificar cambio significativo
            V[estado] = nuevo_valor  # Actualizar valor
        if delta < CONVERGENCIA:  # Si los valores convergen, terminamos
            break

def mejorar_politica(politica, V):
    """
    Mejora la política evaluando si hay acciones que ofrecen mayor recompensa esperada.
    """
    politica_estable = True  # Indicador de estabilidad de la política
    for estado in estados:
        # Encontrar la mejor acción para el estado actual
        mejor_accion = max(acciones, key=lambda a: recompensas[estado][a] + DESCUENTO * V[transiciones[estado][a]])
        if mejor_accion != politica[estado]:
            politica[estado] = mejor_accion
            politica_estable = False  # Se encontró una mejor política
    return politica_estable

def busqueda_politica():
    """
    Algoritmo de búsqueda de política para encontrar la mejor política en un MDP.
    """
    # Inicialización: política aleatoria y valores de estado en 0
    politica = {estado: random.choice(acciones) for estado in estados}
    V = {estado: 0 for estado in estados}
    
    while True:
        evaluar_politica(politica, V)  # Evaluamos la política actual
        if mejorar_politica(politica, V):  # Intentamos mejorar la política
            break  # Si no cambia, hemos encontrado la política óptima
    
    return politica, V

# Ejecutamos el algoritmo
politica_optima, valores_optimos = busqueda_politica()

# Mostramos la mejor política encontrada
print("Política Óptima:")
for estado, accion in politica_optima.items():
    print(f"  Estado {estado}: {accion}")

# Mostramos los valores de cada estado
print("\nValores Óptimos de los Estados:")
for estado, valor in valores_optimos.items():
    print(f"  Estado {estado}: {valor:.2f}")
