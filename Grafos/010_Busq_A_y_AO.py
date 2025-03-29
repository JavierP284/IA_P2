import heapq

### --- Algoritmo A* (A Estrella) --- ###

def busqueda_A_estrella(grafo, costos, inicio, objetivo, heuristica):
    """
    Implementación de A* para encontrar el camino más corto en un grafo.
    """
    # Lista de nodos abiertos (prioridad por f(n) = g(n) + h(n))
    open_list = []
    heapq.heappush(open_list, (heuristica[inicio], inicio, 0))  # (f(n), nodo, g(n))

    # Diccionario para rastrear de dónde viene cada nodo
    came_from = {}

    # Costos acumulados desde el nodo inicial
    g_score = {nodo: float('inf') for nodo in grafo}
    g_score[inicio] = 0

    while open_list:
        # Extraemos el nodo con menor f(n) de la lista abierta
        _, current_node, g_actual = heapq.heappop(open_list)

        # Si llegamos al objetivo, reconstruimos el camino
        if current_node == objetivo:
            return reconstruir_camino(came_from, current_node)

        # Recorremos los vecinos del nodo actual
        for vecino in grafo[current_node]:
            # Calculamos el nuevo costo g(n) para el vecino
            nuevo_g = g_actual + costos.get((current_node, vecino), float('inf'))
            if nuevo_g < g_score[vecino]:  # Si encontramos un mejor camino
                came_from[vecino] = current_node  # Actualizamos el predecesor
                g_score[vecino] = nuevo_g  # Actualizamos g(n)
                f_nuevo = nuevo_g + heuristica[vecino]  # Calculamos f(n)
                heapq.heappush(open_list, (f_nuevo, vecino, nuevo_g))  # Añadimos a la lista abierta

    return None  # No hay solución si salimos del bucle

def reconstruir_camino(came_from, nodo):
    """
    Reconstruye el camino óptimo encontrado por A*.
    """
    camino = []
    while nodo in came_from:  # Seguimos el rastro de predecesores
        camino.append(nodo)
        nodo = came_from[nodo]
    camino.append(nodo)  # Añadimos el nodo inicial
    return camino[::-1]  # Invertimos el camino para obtener el orden correcto

### --- Algoritmo AO* --- ###

class Nodo:
    """
    Representa un nodo en el grafo AND-OR para el algoritmo AO*.
    """
    def __init__(self, nombre, es_meta=False):
        self.nombre = nombre  # Nombre del nodo
        self.es_meta = es_meta  # Indica si es un nodo meta
        self.hijos = []  # Lista de (nodos hijos, costo)
        self.mejor_camino = None  # Guarda el camino óptimo
        self.costo = float('inf') if not es_meta else 0  # Costos iniciales (0 si es meta)

    def agregar_hijo(self, hijos, costo):
        """
        Agrega una conexión desde este nodo a sus hijos con un costo asociado.
        """
        self.hijos.append((hijos, costo))

def ao_star(nodo, heuristica):
    """
    Implementación del algoritmo AO* para grafos AND-OR con correcta actualización de costos.
    """
    if nodo.es_meta:  # Si el nodo es meta, su costo es 0
        return nodo.costo

    mejor_costo = float('inf')  # Inicializamos el mejor costo como infinito
    mejor_opcion = None  # Para guardar la mejor opción de hijos

    # Recorremos todas las conexiones del nodo actual
    for hijos, costo in nodo.hijos:
        # Calculamos el costo total de esta opción (costo + suma de costos de los hijos)
        total = costo + sum(ao_star(hijo, heuristica) for hijo in hijos)
        if total < mejor_costo:  # Si encontramos un mejor costo
            mejor_costo = total
            mejor_opcion = hijos

    # Actualizamos el nodo con la mejor opción encontrada
    if mejor_opcion:
        nodo.mejor_camino = mejor_opcion  # Guardamos el mejor camino
        nodo.costo = mejor_costo  # Actualizamos el costo del nodo
        heuristica[nodo.nombre] = mejor_costo  # Actualizamos la heurística del nodo

    return nodo.costo  # Retornamos el costo del nodo

def reconstruir_camino_AO(nodo):
    """
    Reconstruye el camino óptimo en un grafo AND-OR después de AO*.
    """
    if nodo.mejor_camino is None:  # Si no hay mejor camino, devolvemos solo este nodo
        return [nodo.nombre]

    camino = [nodo.nombre]  # Añadimos el nodo actual al camino
    for hijo in nodo.mejor_camino:  # Recorremos los hijos del mejor camino
        camino.extend(reconstruir_camino_AO(hijo))  # Añadimos los caminos de los hijos

    return camino

### --- Pruebas de los Algoritmos --- ###

# Grafo para A*
grafo_a_estrella = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Costos de A*
costos_a_estrella = {
    ('A', 'B'): 1, ('A', 'C'): 4,
    ('B', 'D'): 1, ('B', 'E'): 2,
    ('C', 'F'): 3, ('E', 'F'): 2
}

# Heurística de A*
heuristica_a_estrella = {'A': 6, 'B': 2, 'C': 3, 'D': 1, 'E': 4, 'F': 0}

# Ejecutamos A*
print("Ejecutando A*...")
camino_a_estrella = busqueda_A_estrella(grafo_a_estrella, costos_a_estrella, 'A', 'F', heuristica_a_estrella)
print(f"Camino óptimo con A*: {camino_a_estrella}\n")


# Grafo AND-OR para AO*
print("Ejecutando AO*...")
A = Nodo('A')
B = Nodo('B')
C = Nodo('C')
D = Nodo('D', es_meta=True)  # Meta
E = Nodo('E', es_meta=True)  # Meta

# Definimos conexiones en AO* (AND implica que ambos deben cumplirse)
A.agregar_hijo([B], 3)   # Camino A → B con costo 3
B.agregar_hijo([D], 2)   # Camino B → D con costo 2
A.agregar_hijo([C], 4)   # Camino A → C con costo 4
C.agregar_hijo([E], 1)   # Camino C → E con costo 1

# Heurística inicial para AO*
heuristica_ao = {'A': 6, 'B': 2, 'C': 3, 'D': 0, 'E': 0}

# Ejecutamos AO*
ao_star(A, heuristica_ao)

# Obtenemos el camino óptimo en AO*
camino_ao = reconstruir_camino_AO(A)
print(f"Camino óptimo con AO*: {camino_ao}")
