from collections import deque

# Función de Búsqueda Bidireccional
def busqueda_bidireccional(grafo, nodo_inicial, nodo_objetivo):
    # Inicializamos las colas de búsqueda para ambos extremos
    cola_inicial = deque([nodo_inicial])
    cola_objetivo = deque([nodo_objetivo])
    
    # Conjuntos para llevar registro de los nodos visitados desde ambos extremos
    visitados_inicial = {nodo_inicial}
    visitados_objetivo = {nodo_objetivo}
    
    # Diccionarios para almacenar los caminos desde los nodos iniciales y objetivos
    padres_inicial = {nodo_inicial: None}
    padres_objetivo = {nodo_objetivo: None}

    # Bucle que realiza la búsqueda desde ambos extremos
    while cola_inicial and cola_objetivo:
        # Expansión de la búsqueda desde el nodo inicial
        if cola_inicial:
            nodo_actual = cola_inicial.popleft()
            # Explorar los vecinos del nodo actual
            for vecino in grafo.get(nodo_actual, []):
                if vecino not in visitados_inicial:
                    visitados_inicial.add(vecino)
                    cola_inicial.append(vecino)
                    padres_inicial[vecino] = nodo_actual
                    
                    # Si encontramos un nodo en la cola del objetivo, terminamos
                    if vecino in visitados_objetivo:
                        return reconstruir_camino(padres_inicial, padres_objetivo, nodo_inicial, nodo_objetivo, vecino)
        
        # Expansión de la búsqueda desde el nodo objetivo
        if cola_objetivo:
            nodo_actual = cola_objetivo.popleft()
            # Explorar los vecinos del nodo actual
            for vecino in grafo.get(nodo_actual, []):
                if vecino not in visitados_objetivo:
                    visitados_objetivo.add(vecino)
                    cola_objetivo.append(vecino)
                    padres_objetivo[vecino] = nodo_actual
                    
                    # Si encontramos un nodo en la cola del inicial, terminamos
                    if vecino in visitados_inicial:
                        return reconstruir_camino(padres_inicial, padres_objetivo, nodo_inicial, nodo_objetivo, vecino)

    return None  # Si no encontramos ningún camino

# Función para reconstruir el camino desde los nodos inicial y objetivo
def reconstruir_camino(padres_inicial, padres_objetivo, nodo_inicial, nodo_objetivo, nodo_comun):
    # Reconstruir el camino desde el nodo inicial hacia el nodo común
    camino_inicial = []
    nodo = nodo_comun
    while nodo is not None:
        camino_inicial.append(nodo)
        nodo = padres_inicial.get(nodo)
    camino_inicial.reverse()  # Invertir el camino para que sea desde el inicio

    # Reconstruir el camino desde el nodo objetivo hacia el nodo común
    camino_objetivo = []
    nodo = nodo_comun
    while nodo is not None:
        camino_objetivo.append(nodo)
        nodo = padres_objetivo.get(nodo)
    
    # El camino completo es la concatenación del camino inicial y el camino objetivo
    return camino_inicial + camino_objetivo[1:]

# Ejemplo de grafo representado como un diccionario de adyacencia
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Usamos la función de Búsqueda Bidireccional
nodo_inicial = 'A'
nodo_objetivo = 'F'
camino = busqueda_bidireccional(grafo, nodo_inicial, nodo_objetivo)

if camino:
    print(f"El camino más corto de {nodo_inicial} a {nodo_objetivo} es: {camino}")
else:
    print(f"No se encontró un camino entre {nodo_inicial} y {nodo_objetivo}.")
