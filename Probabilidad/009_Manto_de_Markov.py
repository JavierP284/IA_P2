# Creamos un diccionario que representa la red bayesiana (grafo dirigido)
# Cada nodo tiene una lista de sus padres
red_bayesiana = {
    "A": [],          # A no tiene padres
    "C": [],          # C no tiene padres
    "B": ["A", "C"],  # B tiene como padres a A y C
    "D": ["B"],       # D es hijo de B
    "E": ["B"],       # E es hijo de B
    "F": ["D", "E"]   # F tiene como padres a D y E
}

# Función para obtener el Manto de Markov de un nodo
def manto_markov(nodo, red):
    """
    Calcula el Manto de Markov de un nodo en una red bayesiana.
    El Manto de Markov incluye:
    - Los padres del nodo
    - Los hijos del nodo
    - Los co-padres (otros padres de los hijos del nodo)
    """
    padres = set(red[nodo])  # Padres del nodo

    hijos = set()            # Hijos del nodo
    co_padres = set()        # Otros padres de los hijos (co-padres)

    # Buscar hijos (nodos que tienen como padre al nodo actual)
    for posible_hijo, padres_posibles in red.items():
        if nodo in padres_posibles:
            hijos.add(posible_hijo)

            # Buscar co-padres (otros padres del hijo)
            for padre in padres_posibles:
                if padre != nodo:
                    co_padres.add(padre)

    # El manto de Markov es la unión de padres, hijos y co-padres
    return padres.union(hijos).union(co_padres)

# Probar la función con varios nodos
nodos = ["A", "B", "C", "D", "E", "F"]
for nodo in nodos:
    manto = manto_markov(nodo, red_bayesiana)
    print(f"Manto de Markov del nodo {nodo}: {manto}")
