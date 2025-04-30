# -----------------------------------------------------
# Ejemplo de GraphPlan básico: Preparar café
# -----------------------------------------------------

# Hechos iniciales: Representan el estado inicial del mundo.
# En este caso, tenemos agua fría y café sin preparar.
estado_inicial = {"agua_fria", "cafe_sin_preparar"}

# Objetivo final: Representa el estado deseado que queremos alcanzar.
# Aquí, el objetivo es tener el café listo.
objetivo = {"cafe_listo"}

# Acciones: Cada acción tiene un nombre, precondiciones y efectos.
# Las precondiciones son los hechos que deben cumplirse para ejecutar la acción.
# Los efectos son los hechos que se añaden al estado después de ejecutar la acción.
acciones = [
    {
        "nombre": "calentar_agua",
        "precondiciones": {"agua_fria"},  # Necesitamos agua fría para calentarla.
        "efectos": {"agua_caliente"}      # El resultado es agua caliente.
    },
    {
        "nombre": "poner_cafe",
        "precondiciones": {"cafe_sin_preparar"},  # Necesitamos café sin preparar.
        "efectos": {"cafe_en_taza"}              # El resultado es café en la taza.
    },
    {
        "nombre": "verter_agua",
        "precondiciones": {"agua_caliente", "cafe_en_taza"},  # Necesitamos agua caliente y café en la taza.
        "efectos": {"cafe_listo"}                             # El resultado es café listo.
    }
]

# -----------------------------------------------------
# Construcción del Grafo de Planificación
def construir_grafo(estado_inicial, acciones, objetivo, max_niveles=5):
    """
    Construye un grafo de planificación para alcanzar un objetivo dado.
    
    Args:
        estado_inicial (set): Conjunto de hechos iniciales.
        acciones (list): Lista de acciones con precondiciones y efectos.
        objetivo (set): Conjunto de hechos que se desean alcanzar.
        max_niveles (int): Número máximo de niveles a construir.

    Returns:
        list: Lista de niveles del grafo, cada uno con hechos y acciones aplicadas.
    """
    niveles = []  # Lista para almacenar los niveles del grafo.
    estado_actual = estado_inicial.copy()  # Copia del estado inicial para no modificar el original.

    # Construcción del grafo nivel por nivel.
    for nivel in range(max_niveles):
        print(f"\n*Nivel {nivel} del grafo:")
        acciones_disponibles = []  # Lista para almacenar las acciones que se pueden ejecutar en este nivel.

        # Recorremos todas las acciones para verificar cuáles se pueden ejecutar.
        for accion in acciones:
            # Si las precondiciones de la acción están en el estado actual, la acción es ejecutable.
            if accion["precondiciones"].issubset(estado_actual):
                acciones_disponibles.append(accion["nombre"])  # Añadimos la acción a la lista de ejecutables.
                estado_actual |= accion["efectos"]  # Actualizamos el estado actual con los efectos de la acción.
                print(f"  Acción '{accion['nombre']}' se puede ejecutar.")

        # Añadimos el estado actual y las acciones ejecutadas al nivel del grafo.
        niveles.append((estado_actual.copy(), acciones_disponibles))

        # Si el objetivo está contenido en el estado actual, hemos alcanzado el objetivo.
        if objetivo.issubset(estado_actual):
            print("\nObjetivo alcanzado en el nivel", nivel)
            return niveles

    # Si no alcanzamos el objetivo después de construir todos los niveles, mostramos un mensaje.
    print("\nNo se pudo alcanzar el objetivo en los niveles dados.")
    return niveles

# -----------------------------------------------------
# Mostrar el grafo de planificación construido
def mostrar_grafo(niveles):
    """
    Muestra los niveles del grafo de planificación.

    Args:
        niveles (list): Lista de niveles del grafo.
    """
    for i, (estados, acciones) in enumerate(niveles):
        print(f"\n*Nivel {i}:")
        print(f"  Hechos: {sorted(estados)}")  # Mostramos los hechos en el nivel actual.
        print(f"  Acciones aplicadas: {acciones}")  # Mostramos las acciones ejecutadas en este nivel.

# -----------------------------------------------------
# Validar datos de entrada
def validar_datos(estado_inicial, acciones, objetivo):
    """
    Valida que los datos de entrada sean consistentes.

    Args:
        estado_inicial (set): Conjunto de hechos iniciales.
        acciones (list): Lista de acciones con precondiciones y efectos.
        objetivo (set): Conjunto de hechos que se desean alcanzar.

    Raises:
        ValueError: Si los datos de entrada no son válidos.
    """
    hechos_definidos = estado_inicial.copy()  # Copiamos los hechos iniciales.

    # Recorremos las acciones para añadir sus precondiciones y efectos a los hechos definidos.
    for accion in acciones:
        hechos_definidos |= accion["precondiciones"] | accion["efectos"]

    # Si el objetivo contiene hechos que no están definidos, lanzamos un error.
    if not objetivo.issubset(hechos_definidos):
        raise ValueError("El objetivo contiene hechos no definidos en las acciones o el estado inicial.")

# -----------------------------------------------------
# Ejecutar GraphPlan
try:
    # Validamos los datos de entrada antes de construir el grafo.
    validar_datos(estado_inicial, acciones, objetivo)

    # Construimos el grafo de planificación.
    grafo = construir_grafo(estado_inicial, acciones, objetivo)

    # Mostramos el grafo construido.
    mostrar_grafo(grafo)
except ValueError as e:
    # Si hay un error en los datos de entrada, lo mostramos.
    print(f"Error en los datos de entrada: {e}")
