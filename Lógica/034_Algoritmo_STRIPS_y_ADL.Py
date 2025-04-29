# -------------------------------------------------------
# Planificación STRIPS: Ejemplo mejorado en Python
# -------------------------------------------------------

# Estado inicial: Representa las condiciones actuales del entorno.
# En este caso, el robot está en la sala y la taza está vacía.
estado = {"robot_en_sala", "taza_vacia"}

# Objetivo deseado: Representa las condiciones que queremos alcanzar.
# Queremos que la taza esté llena y que el robot esté en la sala.
objetivo = {"taza_llena", "robot_en_sala"}

# Acciones disponibles: Cada acción tiene precondiciones (lo que debe cumplirse
# para ejecutarla), efectos positivos (lo que añade al estado) y efectos negativos
# (lo que elimina del estado).
acciones = {
    "mover_a_cocina": {  # Acción para mover al robot de la sala a la cocina.
        "precondiciones": {"robot_en_sala"},  # El robot debe estar en la sala.
        "añade": {"robot_en_cocina"},         # El robot estará en la cocina.
        "elimina": {"robot_en_sala"}          # El robot ya no estará en la sala.
    },
    "llenar_taza": {  # Acción para llenar la taza.
        "precondiciones": {"robot_en_cocina", "taza_vacia"},  # El robot debe estar en la cocina y la taza debe estar vacía.
        "añade": {"taza_llena"},                              # La taza estará llena.
        "elimina": {"taza_vacia"}                             # La taza ya no estará vacía.
    },
    "mover_a_sala": {  # Acción para mover al robot de la cocina a la sala.
        "precondiciones": {"robot_en_cocina"},  # El robot debe estar en la cocina.
        "añade": {"robot_en_sala"},             # El robot estará en la sala.
        "elimina": {"robot_en_cocina"}          # El robot ya no estará en la cocina.
    }
}

# -------------------------------------------------------
# Función para aplicar una acción al estado actual.
def aplicar_accion(accion, estado_actual):
    """
    Aplica una acción al estado actual si se cumplen las precondiciones.
    - accion: Nombre de la acción a aplicar.
    - estado_actual: Conjunto que representa el estado actual.
    """
    datos = acciones[accion]  # Obtiene los datos de la acción (precondiciones, añade, elimina).
    if datos["precondiciones"].issubset(estado_actual):  # Verifica si las precondiciones se cumplen.
        nuevo_estado = estado_actual.copy()  # Crea una copia del estado actual.
        nuevo_estado -= datos["elimina"]     # Elimina los elementos especificados en "elimina".
        nuevo_estado |= datos["añade"]       # Añade los elementos especificados en "añade".
        return nuevo_estado  # Devuelve el nuevo estado.
    return None  # Si no se cumplen las precondiciones, no se puede aplicar la acción.

# -------------------------------------------------------
# Función recursiva para planificar las acciones necesarias para alcanzar el objetivo.
def planificar_recursivo(estado_actual, meta, plan=[]):
    """
    Encuentra un plan (secuencia de acciones) para alcanzar el objetivo desde el estado actual.
    - estado_actual: Conjunto que representa el estado actual.
    - meta: Conjunto que representa el estado objetivo.
    - plan: Lista de acciones realizadas hasta el momento.
    """
    if meta.issubset(estado_actual):  # Si el estado actual cumple con el objetivo...
        return plan, estado_actual    # Devuelve el plan y el estado final.

    for accion in acciones:  # Itera sobre todas las acciones disponibles.
        nuevo_estado = aplicar_accion(accion, estado_actual)  # Intenta aplicar la acción.
        if nuevo_estado and accion not in plan:  # Si la acción es válida y no genera un ciclo...
            nuevo_plan = plan + [accion]  # Añade la acción al plan actual.
            resultado = planificar_recursivo(nuevo_estado, meta, nuevo_plan)  # Llama recursivamente.
            if resultado[0]:  # Si se encuentra un plan válido...
                return resultado  # Devuelve el plan y el estado final.

    return None, estado_actual  # Si no se encuentra un plan, devuelve None y el estado actual.

# -------------------------------------------------------
# Ejecutar planificación
print("Estado inicial:", estado)  # Muestra el estado inicial.
plan, estado_final = planificar_recursivo(estado, objetivo)  # Llama al planificador recursivo.

# Mostrar resultado
if plan:  # Si se encontró un plan...
    print("\nPlan encontrado:")
    for paso in plan:  # Muestra cada paso del plan.
        print(f" - {paso}")
    print("Estado final:", estado_final)  # Muestra el estado final alcanzado.
else:  # Si no se encontró un plan...
    print("\nNo se encontró un plan válido.")
