import heapq

# Función de Búsqueda Voraz Primero el Mejor
def busqueda_voraz(grafo, inicio, objetivo, heuristica):
    # Si el nodo inicial ya es el objetivo, retornamos inmediatamente
    if inicio == objetivo:
        return [inicio]

    # Inicializamos la lista de nodos por explorar (cola de prioridad)
    open_list = []
    heapq.heappush(open_list, (heuristica[inicio], inicio))  # (heurística, nodo)

    # Diccionario para rastrear el camino
    came_from = {}

    # Conjunto para rastrear los nodos explorados
    explorados = set()

    # Conjunto para evitar agregar múltiples veces el mismo nodo a la cola de prioridad
    en_cola = {inicio}

    while open_list:
        # Extraemos el nodo con la heurística más baja
        _, current_node = heapq.heappop(open_list)
        en_cola.remove(current_node)  # Quitamos el nodo de la lista de pendientes

        # Si hemos alcanzado el objetivo, reconstruimos el camino
        if current_node == objetivo:
            return reconstruir_camino(came_from, current_node)

        # Marcamos el nodo como explorado
        explorados.add(current_node)

        # Exploramos los vecinos del nodo actual
        for vecino in grafo[current_node]:
            # Solo exploramos si el vecino no ha sido explorado ni está en la cola
            if vecino not in explorados and vecino not in en_cola:
                came_from[vecino] = current_node  # Guardamos el camino
                heapq.heappush(open_list, (heuristica[vecino], vecino))
                en_cola.add(vecino)  # Marcamos que este nodo está en la cola

    return None  # Si no se encuentra el objetivo, devolvemos None

# Función para reconstruir el camino desde el objetivo hasta el inicio
def reconstruir_camino(came_from, current_node):
    camino = []
    while current_node in came_from:
        camino.append(current_node)
        current_node = came_from[current_node]
    camino.append(current_node)  # Agregamos el nodo inicial
    return camino[::-1]  # Invertimos el camino para obtenerlo desde el inicio

# Grafo representado como un diccionario de adyacencia
# El grafo es un diccionario donde las claves son los nodos y los valores son listas de nodos vecinos
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Heurísticas para cada nodo (estimación del costo restante hasta el objetivo)
# En un problema real, las heurísticas deben estar basadas en el dominio del problema
heuristica = {
    'A': 6,  # Heurística de A (estimación de costo hasta el objetivo)
    'B': 2,  # Heurística de B
    'C': 3,  # Heurística de C
    'D': 1,  # Heurística de D
    'E': 4,  # Heurística de E
    'F': 0   # Heurística de F (objetivo, por lo que su heurística es 0)
}

# Usamos la Búsqueda Voraz Primero el Mejor para encontrar el camino de A a F
nodo_inicial = 'A'
nodo_objetivo = 'F'
camino = busqueda_voraz(grafo, nodo_inicial, nodo_objetivo, heuristica)

if camino:
    print(f"El camino encontrado de {nodo_inicial} a {nodo_objetivo} es: {camino}")
else:
    print(f"No se encontró un camino entre {nodo_inicial} y {nodo_objetivo}.")
