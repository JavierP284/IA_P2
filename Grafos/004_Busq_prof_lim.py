def busqueda_profundidad_limitada(grafo, nodo, metta, limite, visitados=None, camino=None):
    """
    Implementación del algoritmo de Búsqueda en Profundidad Limitada.
    Retorna un camino desde el nodo de inicio hasta el nodo meta si existe,
    o None si no se encuentra un camino dentro del límite especificado.
    """
    if visitados is None:
        visitados = set()  # Conjunto para almacenar los nodos visitados y evitar ciclos
    if camino is None:
        camino = []  # Lista para guardar el camino recorrido

    visitados.add(nodo)  # Se marca el nodo actual como visitado
    camino.append(nodo)  # Se agrega el nodo actual al camino

    # Si el nodo actual es el objetivo, se retorna el camino encontrado
    if nodo == metta:
        return camino

    # Si se alcanza el límite, se retrocede (Backtracking)
    if limite <= 0:
        camino.pop()
        return None

    # Explorar los nodos adyacentes
    for vecino in grafo.get(nodo, []):
        if vecino not in visitados:  # Solo visitar nodos no explorados
            resultado = busqueda_profundidad_limitada(grafo, vecino, metta, limite - 1, visitados, camino)
            if resultado:  # Si se encontró un camino, se retorna
                return resultado

    # Si no se encuentra el objetivo en esta rama, se retrocede (Backtracking)
    camino.pop()
    return None  # Si no hay camino, retorna None

# Definimos un grafo no ponderado en forma de diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

#Nodo inicial y nodo objetivo
inicio = 'A'
objetivo = 'F'
limite_profundidad = 2 # Límite de profundidad para la búsqueda

#Se ejecuta el algoritmo DFS con límite de profundidad
resultado = busqueda_profundidad_limitada(grafo, inicio, objetivo, limite_profundidad)

#Mostrar el resultado
if resultado:
    print(f"Camino encontrado: {' -> '.join(resultado)}")
else:
    print("No se encontró un camino dentro del límite de profundidad especificado")
#Este algoritmo es útil para evitar búsquedas exhaustivas en grafos grandes o infinitos