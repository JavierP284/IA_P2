# ---------------------------------------------------
# Ejemplo de Espacio de Estados: Ordenar cubos
# ---------------------------------------------------
from collections import deque  # Importamos deque para implementar una cola eficiente

# Estado inicial (desordenado)
estado_inicial = (3, 1, 2)

# Estado objetivo (orden correcto)
estado_objetivo = (1, 2, 3)

# ---------------------------------------------------
# Validar estados inicial y objetivo
def validar_estados(estado_inicial, estado_objetivo):
    """
    Valida que el estado inicial y el estado objetivo contengan los mismos elementos.
    Si no es así, lanza una excepción.
    """
    if sorted(estado_inicial) != sorted(estado_objetivo):
        raise ValueError("El estado inicial y el estado objetivo deben contener los mismos elementos.")

# ---------------------------------------------------
# Generar nuevos estados a partir de un estado actual
def generar_sucesores(estado):
    """
    Genera todos los estados sucesores posibles intercambiando pares de elementos.
    Parámetros:
        estado (tuple): El estado actual representado como una tupla.
    Retorna:
        list: Una lista de estados sucesores generados.
    """
    sucesores = []  # Lista para almacenar los estados sucesores
    estado = list(estado)  # Convertimos la tupla en una lista para poder modificarla
    for i in range(len(estado)):  # Iteramos sobre cada elemento
        for j in range(i + 1, len(estado)):  # Iteramos sobre los elementos restantes
            nuevo = estado.copy()  # Creamos una copia del estado actual
            # Intercambiamos los elementos en las posiciones i y j
            nuevo[i], nuevo[j] = nuevo[j], nuevo[i]
            sucesores.append(tuple(nuevo))  # Convertimos la lista de nuevo a tupla y la añadimos
    return sucesores

# ---------------------------------------------------
# Búsqueda en amplitud sobre el espacio de estados
def buscar_solucion(estado_inicial, objetivo):
    """
    Realiza una búsqueda en amplitud (BFS) para encontrar el camino desde el estado inicial al objetivo.
    Parámetros:
        estado_inicial (tuple): El estado inicial del problema.
        objetivo (tuple): El estado objetivo que queremos alcanzar.
    Retorna:
        list: Una lista con los pasos para llegar al estado objetivo, o None si no se encuentra solución.
    """
    visitados = set()  # Conjunto para almacenar los estados ya visitados
    cola = deque()  # Cola para manejar los estados por explorar
    cola.append((estado_inicial, []))  # Añadimos el estado inicial junto con un camino vacío
    nodos_visitados = 0  # Contador de nodos visitados

    while cola:  # Mientras haya estados por explorar
        actual, camino = cola.popleft()  # Sacamos el primer estado de la cola
        nodos_visitados += 1  # Incrementamos el contador de nodos visitados

        # Si el estado actual ya fue visitado, lo ignoramos
        if actual in visitados:
            continue
        visitados.add(actual)  # Marcamos el estado actual como visitado

        # Si encontramos el estado objetivo, devolvemos el camino
        if actual == objetivo:
            print(f"Nodos visitados: {nodos_visitados}")
            return camino + [actual]

        # Generamos los sucesores del estado actual
        for sucesor in generar_sucesores(actual):
            # Si el sucesor no ha sido visitado, lo añadimos a la cola
            if sucesor not in visitados:
                cola.append((sucesor, camino + [actual]))
    
    # Si agotamos la cola y no encontramos solución, devolvemos None
    print(f"Nodos visitados: {nodos_visitados}")
    return None

# ---------------------------------------------------
# Ejecutar el algoritmo
try:
    # Validamos que los estados inicial y objetivo sean correctos
    validar_estados(estado_inicial, estado_objetivo)
    print("Estado inicial:", estado_inicial)
    print("Estado objetivo:", estado_objetivo)

    # Ejecutamos la búsqueda para encontrar la solución
    solucion = buscar_solucion(estado_inicial, estado_objetivo)

    # Mostramos el resultado
    if solucion:
        print("\nSolución encontrada:")
        for paso in solucion:
            print(" →", paso)  # Imprimimos cada paso del camino hacia la solución
    else:
        print("\nNo se encontró una solución.")  # Mensaje si no hay solución
except ValueError as e:
    # Capturamos y mostramos errores de validación
    print(f"Error: {e}")
