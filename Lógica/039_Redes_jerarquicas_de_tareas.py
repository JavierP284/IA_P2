# ----------------------------------------------------------
# Ejemplo HTN: Hacer una taza de té con tareas jerárquicas
# ----------------------------------------------------------

# Diccionario de métodos HTN
# Este diccionario define las tareas jerárquicas y cómo se descomponen en subtareas.
# Por ejemplo, "hacer_te" se descompone en las subtareas: "hervir_agua", "preparar_taza", "verter_agua" y "esperar".
metodos = {
    "hacer_te": ["hervir_agua", "preparar_taza", "verter_agua", "esperar"],
    "preparar_taza": ["poner_bolsa", "agregar_azucar"]  # "preparar_taza" se descompone en "poner_bolsa" y "agregar_azucar".
}

# Acciones primitivas (que no se descomponen)
# Este diccionario define las acciones básicas que no se pueden descomponer más.
# Cada acción está asociada a una función lambda que imprime un mensaje indicando que la acción se está ejecutando.
acciones_primitivas = {
    "hervir_agua": lambda: print("Hirviendo el agua..."),
    "poner_bolsa": lambda: print("Colocando la bolsa de té en la taza..."),
    "verter_agua": lambda: print("Vertiendo el agua caliente en la taza..."),
    "esperar": lambda: print("Esperando que el té se infusione..."),
    "agregar_azucar": lambda: print("Agregando azúcar a la taza...")
}

# ----------------------------------------------------------
# Planificador HTN recursivo
def planificar(tarea, progreso=None):
    """
    Descompone una tarea jerárquica en subtareas y ejecuta acciones primitivas.
    
    Parámetros:
    - tarea: La tarea que se desea planificar (puede ser jerárquica o una acción primitiva).
    - progreso: Lista que almacena las tareas completadas (se utiliza para rastrear el progreso).

    Retorna:
    - progreso: Lista actualizada con las tareas completadas.
    """
    if progreso is None:
        progreso = []  # Inicializa la lista de progreso si no se proporciona.

    # Caso 1: La tarea es una acción primitiva.
    if tarea in acciones_primitivas:
        print(f"Ejecutando acción: '{tarea}'")  # Muestra qué acción se está ejecutando.
        acciones_primitivas[tarea]()  # Ejecuta la acción primitiva.
        progreso.append(tarea)  # Registra la acción como completada.

    # Caso 2: La tarea es jerárquica (tiene subtareas).
    elif tarea in metodos:
        print(f"\nDescomponiendo tarea: '{tarea}'")  # Indica que la tarea se está descomponiendo.
        for subtarea in metodos[tarea]:  # Itera sobre las subtareas definidas en el diccionario de métodos.
            planificar(subtarea, progreso)  # Llama recursivamente a la función para cada subtarea.

    # Caso 3: La tarea no está definida en ninguno de los diccionarios.
    else:
        print(f"Error: Tarea '{tarea}' no definida.")  # Muestra un mensaje de error si la tarea no existe.

    return progreso  # Devuelve la lista de progreso actualizada.

# ----------------------------------------------------------
# Ejecutar planificador para hacer té
print("Iniciando tarea: hacer_te")  # Mensaje inicial indicando que se comienza la tarea principal.
progreso = planificar("hacer_te")  # Llama al planificador con la tarea principal "hacer_te".

# Mostrar progreso
print("\nTareas completadas:")  # Encabezado para la lista de tareas completadas.
for tarea in progreso:  # Itera sobre las tareas completadas.
    print(f"- {tarea}")  # Muestra cada tarea completada.
