from collections import deque

def generar_grafo(laberinto):
    """
    Convierte un laberinto en un grafo donde los nodos representan posiciones accesibles.
    """
    filas, columnas = len(laberinto), len(laberinto[0])
    grafo = {}

    # Direcciones posibles (arriba, abajo, izquierda, derecha)
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(filas):
        for j in range(columnas):
            if laberinto[i][j] == 1:  # Si es un camino, se agrega al grafo
                vecinos = []
                for di, dj in direcciones:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < filas and 0 <= nj < columnas and laberinto[ni][nj] == 1:
                        vecinos.append((ni, nj))  # Conexión válida
                grafo[(i, j)] = vecinos  # Guardamos el nodo y sus vecinos

    return grafo

def bfs_caminos(grafo, inicio, objetivo):
    """
    Algoritmo de búsqueda en anchura (BFS) para encontrar el camino más corto.
    """
    cola = deque([(inicio, [inicio])])  # Cola con el nodo y el camino tomado
    visitados = set()

    while cola:
        nodo, camino = cola.popleft()

        if nodo == objetivo:  # Si llegamos al destino, retornamos el camino encontrado
            return camino

        if nodo not in visitados:
            visitados.add(nodo)
            for vecino in grafo.get(nodo, []):
                if vecino not in visitados:
                    cola.append((vecino, camino + [vecino]))

    return None  # No hay camino

# Representación del laberinto (1 = camino, 0 = pared)
laberinto = [
    [1, 1, 0, 1, 1],
    [0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

# Definir entrada y salida
inicio = (0, 0)
objetivo = (4, 4)

# Aplicar acondicionamiento del corte: convertir laberinto en grafo eliminando conexiones inválidas
grafo = generar_grafo(laberinto)

# Encontrar el camino más corto después del corte
camino = bfs_caminos(grafo, inicio, objetivo)

# Mostrar resultados
if camino:
    print("Camino encontrado:", camino)
else:
    print("No hay camino posible")
