# --------------------------------------------------------
# Planificación de Orden Parcial: Hacer un sándwich
# --------------------------------------------------------

# Lista de acciones
# Cada acción tiene:
# - "pre": un conjunto de precondiciones que deben cumplirse antes de ejecutar la acción.
# - "post": un conjunto de efectos que ocurren después de ejecutar la acción.
acciones = {
    "sacar_pan": {
        "pre": set(),  # No requiere precondiciones
        "post": {"pan_fuera"}  # El pan estará fuera
    },
    "untar_mantequilla": {
        "pre": {"pan_fuera"},  # Requiere que el pan esté fuera
        "post": {"pan_untado"}  # El pan estará untado con mantequilla
    },
    "poner_jamon": {
        "pre": {"pan_untado"},  # Requiere que el pan esté untado
        "post": {"pan_con_jamon"}  # El pan tendrá jamón
    },
    "tapar_sandwich": {
        "pre": {"pan_con_jamon"},  # Requiere que el pan tenga jamón
        "post": {"sandwich_listo"}  # El sándwich estará listo
    }
}

# --------------------------------------------------------
# Función: obtener dependencias de orden entre acciones
def obtener_orden_parcial(acciones):
    """
    Genera las dependencias de orden parcial entre las acciones.

    Args:
        acciones (dict): Diccionario con las acciones, sus precondiciones y efectos.

    Returns:
        list: Lista de pares (a_i, a_j) donde a_i debe preceder a a_j.
    """
    dependencias = []  # Lista para almacenar las dependencias entre acciones

    # Iteramos sobre todas las combinaciones de acciones (a_i, a_j)
    for a_i, datos_i in acciones.items():
        for a_j, datos_j in acciones.items():
            # Si las postcondiciones de a_i son necesarias como precondiciones de a_j
            if a_i != a_j and datos_i["post"] & datos_j["pre"]:
                dependencias.append((a_i, a_j))  # a_i debe ejecutarse antes de a_j

    return dependencias

# --------------------------------------------------------
# Función: detectar ciclos en las dependencias
def detectar_ciclos(dependencias):
    """
    Detecta si hay ciclos en las dependencias.

    Args:
        dependencias (list): Lista de pares (a_i, a_j) que representan las dependencias.

    Returns:
        bool: True si hay ciclos, False en caso contrario.
    """
    from collections import defaultdict, deque

    # Construir un grafo dirigido a partir de las dependencias
    grafo = defaultdict(list)  # Diccionario para almacenar los nodos y sus vecinos
    grados_entrada = defaultdict(int)  # Contador de grados de entrada para cada nodo

    # Llenar el grafo y calcular los grados de entrada
    for antes, despues in dependencias:
        grafo[antes].append(despues)  # Agregar una arista dirigida de 'antes' a 'despues'
        grados_entrada[despues] += 1  # Incrementar el grado de entrada de 'despues'

    # Algoritmo de Kahn para detección de ciclos
    # Inicializamos una cola con los nodos que tienen grado de entrada 0
    cola = deque([nodo for nodo in grafo if grados_entrada[nodo] == 0])
    visitados = 0  # Contador de nodos visitados

    while cola:
        nodo = cola.popleft()  # Sacamos un nodo de la cola
        visitados += 1  # Marcamos el nodo como visitado
        for vecino in grafo[nodo]:  # Iteramos sobre los vecinos del nodo
            grados_entrada[vecino] -= 1  # Reducimos el grado de entrada del vecino
            if grados_entrada[vecino] == 0:  # Si el grado de entrada es 0, lo agregamos a la cola
                cola.append(vecino)

    # Si no visitamos todos los nodos, hay un ciclo
    return visitados != len(grafo)

# --------------------------------------------------------
# Ejecución del ejemplo
print("Analizando planificación de orden parcial...\n")

# Obtener pares de orden parcial
orden_parcial = obtener_orden_parcial(acciones)

# Mostrar dependencias mínimas
print("Dependencias entre acciones (orden mínimo requerido):")
for antes, despues in orden_parcial:
    print(f" - '{antes}' debe ir antes que '{despues}'")

# Verificar si hay ciclos
if detectar_ciclos(orden_parcial):
    print("\nError: Se detectaron ciclos en las dependencias. La planificación no es válida.")
else:
    print("\nNo se detectaron ciclos. La planificación es válida.")

# --------------------------------------------------------
# Opcional: Representar como grafo
try:
    import networkx as nx
    import matplotlib.pyplot as plt

    # Crear un grafo dirigido con las dependencias
    grafo = nx.DiGraph()
    grafo.add_edges_from(orden_parcial)  # Agregar las aristas al grafo

    # Dibujar el grafo
    plt.figure(figsize=(8, 6))
    nx.draw_networkx(grafo, with_labels=True, node_color='lightblue', font_weight='bold')
    plt.title("Grafo de dependencias de orden parcial")
    plt.show()
except ImportError:
    print("\nNota: Instala 'networkx' y 'matplotlib' para visualizar el grafo.")
