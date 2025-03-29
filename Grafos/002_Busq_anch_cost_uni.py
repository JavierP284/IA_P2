import heapq  # Se importa heapq para usar una cola de prioridad

def busqueda_costo_uniforme(grafo, inicio, meta):
    """
    Implementa el algoritmo de Búsqueda en Anchura de Costo Uniforme (UCS).
    Retorna el camino más corto desde el nodo de inicio hasta el objetivo.
    """

    # Crear la cola de prioridad
    cola_prioridad = [(0, inicio, [])]  # (Costo acumulado, Nodo actual, Camino recorrido)

    visitado = set()  # Conjunto para guardar los nodos ya visitados y evitar ciclos

    while cola_prioridad:
        costo, nodo, camino = heapq.heappop(cola_prioridad)  # Se extrae el nodo de menor costo

        if nodo in visitado:  # Se ignora el nodo si ya se visitó
            continue

        camino = camino + [nodo]  # Se actualiza el camino recorrido
        visitado.add(nodo)  # Se marca el nodo como visitado

        if nodo == meta:  # Si se llega al objetivo, se retorna el resultado
            return costo, camino
        
        # Explorar nodos adyacentes
        for vecino, costo_arista in grafo.get(nodo, {}).items():
            if vecino not in visitado:
                heapq.heappush(cola_prioridad, (costo + costo_arista, vecino, camino))
    
    return float('inf'), []  # Si no se encuentra un camino, retorna infinito y una lista vacía

# Definimos un grafo ponderado con costos en las aristas
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 1},
    'F': {'C': 3, 'E': 1}
}

# Nodo inicial y nodo objetivo
start_node = 'A'
goal_node = 'F'

# Ejecutamos el algoritmo UCS
costo, camino = busqueda_costo_uniforme(grafo, start_node, goal_node)

# Mostramos el resultado
print(f"Costo mínimo: {costo}")
print(f"Camino más corto: {' -> '.join(camino)}")
