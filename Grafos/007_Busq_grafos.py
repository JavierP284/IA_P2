from collections import deque

# Función de Búsqueda en Amplitud (BFS)
def bfs(grafo, nodo_inicial, objetivo):
    # Inicializamos la cola de búsqueda y el conjunto de nodos visitados
    cola = deque([nodo_inicial])  # Usamos una cola para explorar por niveles
    visitados = set()  # Conjunto de nodos que hemos visitado
    visitados.add(nodo_inicial)  # Marcamos el nodo inicial como visitado
    padres = {nodo_inicial: None}  # Diccionario para rastrear los nodos padres

    # Bucle de búsqueda
    while cola:
        nodo_actual = cola.popleft()  # Extraemos el primer nodo de la cola
        
        # Si encontramos el objetivo, reconstruimos el camino
        if nodo_actual == objetivo:
            return reconstruir_camino(padres, nodo_inicial, objetivo)

        # Exploramos los vecinos del nodo actual
        for vecino in grafo.get(nodo_actual, []):
            if vecino not in visitados:
                visitados.add(vecino)  # Marcamos el vecino como visitado
                cola.append(vecino)  # Añadimos el vecino a la cola para explorarlo
                padres[vecino] = nodo_actual  # Guardamos el nodo actual como su padre

    return None  # Si no se encuentra el objetivo, devolvemos None

# Función para reconstruir el camino desde el nodo inicial hasta el objetivo
def reconstruir_camino(padres, nodo_inicial, nodo_objetivo):
    camino = []
    nodo = nodo_objetivo
    while nodo is not None:
        camino.append(nodo)
        nodo = padres.get(nodo)
    
    # Invertimos el camino para que sea desde el nodo inicial hasta el objetivo
    camino.reverse()
    return camino

# Ejemplo de grafo representado como un diccionario de adyacencia
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Usamos la función de Búsqueda en Amplitud (BFS)
nodo_inicial = 'A'
nodo_objetivo = 'F'
camino = bfs(grafo, nodo_inicial, nodo_objetivo)

if camino:
    print(f"El camino más corto de {nodo_inicial} a {nodo_objetivo} es: {camino}")
else:
    print(f"No se encontró un camino entre {nodo_inicial} y {nodo_objetivo}.")
