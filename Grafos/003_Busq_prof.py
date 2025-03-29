
def busqueda_profundidad(grafo, inicio, meta, visitado=None, camino=None):
    """
    Implementación del algoritmo de Búsqueda en Profundidad (DFS).
    Retorna un camino desde el nodo de inicio hasta el nodo meta si existe.
    """
    if visitado is None:
        visitado = set()  # Conjunto para almacenar los nodos visitados y evitar ciclos
    if camino is None:
        camino = []  # Lista para guardar el camino recorrido
    
    visitado.add(inicio)  # Se marca el nodo actual como visitado
    camino.append(inicio)  # Se agrega el nodo actual al camino
    
    # Si el nodo actual es el objetivo, se retorna el camino encontrado
    if inicio == meta:
        return camino
    
    # Explorar los nodos adyacentes
    for vecino in grafo.get(inicio, []):
        if vecino not in visitado:  # Solo visitar nodos no explorados
            resultado = busqueda_profundidad(grafo, vecino, meta, visitado, camino)
            if resultado:  # Si se encontró un camino, se retorna
                return resultado
    
    # Si no se encuentra el objetivo en esta rama, se retrocede (Backtracking)
    camino.pop()
    return None  # Si no hay camino, retorna None

# Definimos un grafo no ponderado en forma de diccionario
# Las llaves representan los nodos y los valores son listas de nodos vecinos

grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Nodo inicial y nodo objetivo
inicio = 'A'
meta = 'F'

# Ejecutamos el algoritmo DFS
camino = busqueda_profundidad(grafo, inicio, meta)

# Mostramos el resultado
if camino:
    print(f"Camino encontrado: {' -> '.join(camino)}")
else:
    print("No se encontró un camino")