import random

def busqueda_online(grafo, inicio, meta):
    """
    Algoritmo de Búsqueda Online: el agente no conoce todo el grafo de antemano.
    Explora en tiempo real y toma decisiones basadas en la información descubierta.

    Args:
        grafo (dict): Representación del grafo como un diccionario de listas de adyacencia.
        inicio (str): Nodo inicial.
        meta (str): Nodo objetivo.

    Returns:
        tuple: Una tupla con el camino encontrado (o None) y un mensaje.
    """
    if inicio not in grafo or meta not in grafo:
        return None, f"Error: Nodo '{inicio}' o '{meta}' no está en el grafo."

    visitados = set()  # Conjunto para almacenar nodos visitados
    camino = []  # Lista para almacenar el camino recorrido
    actual = inicio  # Nodo inicial
    
    while actual != meta:  # Se ejecuta hasta que el nodo actual sea el nodo objetivo
        camino.append(actual)  # Se agrega el nodo actual al camino
        visitados.add(actual)  # Se marca como visitado
        
        vecinos = [n for n in grafo.get(actual, []) if n not in visitados]  # Se obtienen vecinos no visitados
        
        if not vecinos:  # Si no hay vecinos disponibles, se termina sin encontrar la meta
            return None, "No hay camino disponible"
        
        actual = random.choice(vecinos)  # Se elige un vecino al azar para continuar
    
    camino.append(meta)  # Se agrega el nodo meta al camino
    return camino, "Camino encontrado"

# Definimos un grafo de ejemplo
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Ejecutamos la búsqueda online desde A hasta F
inicio = 'A'
meta = 'F'
resultado, mensaje = busqueda_online(grafo, inicio, meta)
print(mensaje)
if resultado:
    print("Camino encontrado:", " -> ".join(resultado))
else:
    print("Camino encontrado: Ninguno")
