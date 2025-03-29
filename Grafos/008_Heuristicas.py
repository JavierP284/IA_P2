import heapq

# Función de búsqueda A*
def a_star(grafo, inicio, objetivo, heuristica):
    # Inicializamos las estructuras de datos
    open_list = []  # Lista de nodos por explorar (con prioridad)
    heapq.heappush(open_list, (0 + heuristica[inicio], 0, inicio))  # (f(n), g(n), nodo)
    came_from = {}  # Diccionario para rastrear el camino
    g_score = {nodo: float('inf') for nodo in grafo}  # Costo real de inicio a cualquier nodo
    g_score[inicio] = 0  # El costo de llegar al nodo de inicio es 0
    f_score = {nodo: float('inf') for nodo in grafo}  # Estimación del costo total
    f_score[inicio] = heuristica[inicio]  # f(n) = g(n) + h(n)

    while open_list:
        # Extraemos el nodo con el menor f(n)
        _, _, current_node = heapq.heappop(open_list)

        # Si hemos llegado al objetivo, reconstruimos el camino
        if current_node == objetivo:
            return reconstruir_camino(came_from, current_node)

        # Exploramos los vecinos del nodo actual
        for vecino, costo in grafo[current_node].items():
            tentative_g_score = g_score[current_node] + costo  # Costo total desde inicio hasta el vecino

            # Si encontramos un camino mejor hacia el vecino, actualizamos los valores
            if tentative_g_score < g_score[vecino]:
                came_from[vecino] = current_node  # Guardamos el camino
                g_score[vecino] = tentative_g_score  # Actualizamos el costo g(n)
                f_score[vecino] = g_score[vecino] + heuristica[vecino]  # Actualizamos f(n)
                heapq.heappush(open_list, (f_score[vecino], tentative_g_score, vecino))  # Añadimos a la lista

    return None  # Si no se encuentra un camino, devolvemos None

# Función para reconstruir el camino desde el objetivo al inicio
def reconstruir_camino(came_from, current_node):
    camino = [current_node]
    while current_node in came_from:
        current_node = came_from[current_node]
        camino.append(current_node)
    camino.reverse()
    return camino

# Grafo representado como un diccionario de adyacencia
# El grafo es un diccionario donde las claves son los nodos y los valores son otros diccionarios
# que contienen los nodos vecinos y sus costos de conexión
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Heurísticas para cada nodo (estimación del costo restante hasta el objetivo)
# Estas heurísticas deben ser proporcionadas de acuerdo al problema específico
heuristica = {
    'A': 7,  # Estimación del costo de A a D
    'B': 6,  # Estimación del costo de B a D
    'C': 2,  # Estimación del costo de C a D
    'D': 0   # El objetivo (D) tiene heurística 0
}

# Usamos el algoritmo A* para encontrar el camino más corto de A a D
nodo_inicial = 'A'
nodo_objetivo = 'D'
camino = a_star(grafo, nodo_inicial, nodo_objetivo, heuristica)

if camino:
    print(f"El camino más corto de {nodo_inicial} a {nodo_objetivo} es: {camino}")
else:
    print(f"No se encontró un camino entre {nodo_inicial} y {nodo_objetivo}.")
