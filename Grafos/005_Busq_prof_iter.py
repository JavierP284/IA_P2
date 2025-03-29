#Funcion de Búsqueda en Profundidad Iterativa
def busqueda_profundidad_iterativa(grafo, nodo_inicial, objetivo):
    """
    Implementación del algoritmo de Búsqueda en Profundidad Iterativa.
    Retorna un camino desde el nodo de inicio hasta el nodo objetivo si existe,
    o None si no se encuentra un camino.
    """
    for profundidad_maxima in range(len(grafo)):
        print(f"Buscando hasta profundidad {profundidad_maxima}")
        visitados = set() # Conjunto para almacenar los nodos visitados y evitar ciclos
        pila = [(nodo_inicial, 0)] # Pila para almacenar los nodos a explorar y su profundidad

        while pila:
            nodo, profundidad = pila.pop() # Extraer el nodo y su profundidad de la pila
            if nodo == objetivo: # Si se encuentra el nodo objetivo, se retorna el camino
                return True
            
            #si no se ha visitado el nodo y no se ha alcanzado la profundidad máxima
            if nodo not in visitados and profundidad <= profundidad_maxima:
                visitados.add(nodo)

                # Agregar los nodos adyacentes a la pila con la profundidad incrementada
                for vecino in grafo.get(nodo, []):
                    pila.append((vecino, profundidad + 1))
        # Si no se encuentra el objetivo en esta profundidad, se incrementa la profundidad máxima

    return None # Si no se encuentra el objetivo, retorna None

# Ejemplo de grafo representado como un diccionario de adyacencia
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Usamos la función de Búsqueda en Profundidad Iterativa
nodo_inicial = 'A'
objetivo = 'F'
resultado = busqueda_profundidad_iterativa(grafo, nodo_inicial, objetivo)

if resultado:
    print(f"El objetivo {objetivo} fue encontrado.")
else:
    print(f"El objetivo {objetivo} no fue encontrado.")