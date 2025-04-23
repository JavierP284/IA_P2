# ------------------------------------------
# Lógica Modal - Modelo de Kripke Mejorado
# ------------------------------------------

# Importamos las bibliotecas necesarias para la representación gráfica
import networkx as nx
import matplotlib.pyplot as plt

# Definimos los mundos posibles como nodos en el modelo de Kripke.
# Cada mundo tiene un conjunto de proposiciones (P, Q, etc.) y sus valores de verdad.
mundos = {
    "w1": {"P": True, "Q": False},  # En el mundo w1, P es verdadera y Q es falsa
    "w2": {"P": False, "Q": True}, # En el mundo w2, P es falsa y Q es verdadera
    "w3": {"P": True, "Q": True}   # En el mundo w3, tanto P como Q son verdaderas
}

# Relación de accesibilidad: define qué mundos son accesibles desde otros.
# Por ejemplo, desde el mundo w1 se puede acceder a w2 y w3.
accesibilidad = {
    "w1": ["w2", "w3"],  # Desde w1 se puede acceder a w2 y w3
    "w2": ["w1"],        # Desde w2 se puede acceder a w1
    "w3": ["w1", "w2"]   # Desde w3 se puede acceder a w1 y w2
}

# Operador modal de posibilidad: ◇P (es posible que P sea verdadera)
# Esta función verifica si existe al menos un mundo accesible desde el mundo actual
# donde la proposición `prop` es verdadera.
def es_posible(prop, mundo):
    # Validamos que el mundo exista en la relación de accesibilidad
    if mundo not in accesibilidad:
        raise ValueError(f"El mundo '{mundo}' no está definido.")
    # Validamos que la proposición exista en el mundo actual
    if prop not in mundos[mundo]:
        raise ValueError(f"La proposición '{prop}' no está definida en el mundo '{mundo}'.")
    # Recorremos los mundos accesibles desde el mundo actual
    for accesible in accesibilidad[mundo]:
        # Si la proposición es verdadera en algún mundo accesible, devolvemos True
        if mundos[accesible].get(prop, False):
            return True
    # Si no encontramos ningún mundo accesible donde la proposición sea verdadera, devolvemos False
    return False

# Operador modal de necesidad: □P (necesariamente P es verdadera)
# Esta función verifica si en todos los mundos accesibles desde el mundo actual
# la proposición `prop` es verdadera.
def es_necesario(prop, mundo):
    # Validamos que el mundo exista en la relación de accesibilidad
    if mundo not in accesibilidad:
        raise ValueError(f"El mundo '{mundo}' no está definido.")
    # Validamos que la proposición exista en el mundo actual
    if prop not in mundos[mundo]:
        raise ValueError(f"La proposición '{prop}' no está definida en el mundo '{mundo}'.")
    # Recorremos los mundos accesibles desde el mundo actual
    for accesible in accesibilidad[mundo]:
        # Si la proposición es falsa en algún mundo accesible, devolvemos False
        if not mundos[accesible].get(prop, False):
            return False
    # Si la proposición es verdadera en todos los mundos accesibles, devolvemos True
    return True

# Representación visual del modelo de Kripke
# Esta función dibuja un grafo dirigido donde los nodos representan los mundos
# y las aristas representan las relaciones de accesibilidad entre ellos.
def dibujar_modelo():
    # Creamos un grafo dirigido
    grafo = nx.DiGraph()
    # Añadimos las relaciones de accesibilidad al grafo
    for mundo, accesibles in accesibilidad.items():
        for accesible in accesibles:
            grafo.add_edge(mundo, accesible)
    # Dibujamos el grafo con etiquetas y colores
    nx.draw(grafo, with_labels=True, node_color="lightblue", font_weight="bold")
    plt.show()

# Probar en el mundo w1
# Aquí verificamos si ciertas proposiciones son posibles o necesarias en el mundo w1
print(f"En el mundo w1: ¿Es posible que P sea verdadera? {es_posible('P', 'w1')}")
print(f"En el mundo w1: ¿Es necesario que P sea verdadera? {es_necesario('P', 'w1')}")

# Dibujar el modelo de Kripke para visualizar los mundos y sus relaciones
dibujar_modelo()
