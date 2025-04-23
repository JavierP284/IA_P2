# -----------------------------------------------
# Lógica por Defecto en Python
# -----------------------------------------------

# Base de hechos: Representa el conocimiento inicial del sistema.
# Cada categoría (clave) contiene un conjunto de elementos (valores).
hechos = {
    "es_estudiante": {"pedro", "maria"},  # Personas que son estudiantes
    "esta_enfermo": {"pedro"}            # Personas que están enfermas
}

# Reglas por defecto: Lista de reglas que contienen:
# - Una condición principal (condicion): Define cuándo se aplica la regla.
# - Una excepción (excepcion): Define cuándo no se aplica la regla.
# - Una conclusión (conclusion): Define el resultado si la regla se aplica.
reglas_por_defecto = [
    {
        "condicion": lambda x: x in hechos.get("es_estudiante", set()),  # Es estudiante
        "excepcion": lambda x: x in hechos.get("esta_enfermo", set()),  # Pero está enfermo
        "conclusion": lambda x: f"{x} estudia por defecto"              # Conclusión si no está enfermo
    },
    {
        "condicion": lambda x: x in hechos.get("es_estudiante", set()),  # Es estudiante
        "excepcion": lambda x: x not in hechos.get("esta_enfermo", set()),  # Y no está enfermo
        "conclusion": lambda x: f"{x} puede asistir a clases"           # Conclusión si no hay excepción
    }
]

# Función que aplica lógica por defecto a un nombre dado
def aplica_logica_por_defecto(nombre):
    """
    Aplica las reglas por defecto a un nombre dado y retorna las conclusiones.
    - nombre: Nombre de la persona a evaluar.
    """
    conclusiones = []  # Lista para almacenar las conclusiones aplicadas

    # Iterar sobre cada regla en la lista de reglas por defecto
    for regla in reglas_por_defecto:
        # Verificar si la condición principal de la regla se cumple
        if regla["condicion"](nombre):
            # Verificar si la excepción de la regla se cumple
            if regla["excepcion"](nombre):
                # Si la excepción se cumple, la regla no se aplica
                print(f"Regla por defecto no se aplica: {nombre} cumple la excepción.")
            else:
                # Si la excepción no se cumple, aplicar la regla
                conclusion = regla["conclusion"](nombre)
                print(f"Regla por defecto aplicada: {conclusion}")
                conclusiones.append(conclusion)  # Agregar la conclusión a la lista

    # Si no se aplicaron reglas, informar al usuario
    if not conclusiones:
        print(f"No se aplicaron reglas por defecto para {nombre}.")
    return conclusiones  # Retornar las conclusiones aplicadas

# Función para agregar hechos dinámicamente
def agregar_hecho(categoria, nombre):
    """
    Agrega un hecho a la base de hechos.
    - categoria: Categoría del hecho (clave en el diccionario).
    - nombre: Elemento a agregar en la categoría.
    """
    if categoria not in hechos:  # Si la categoría no existe, crearla
        hechos[categoria] = set()
    hechos[categoria].add(nombre)  # Agregar el elemento a la categoría

# Función para eliminar hechos dinámicamente
def eliminar_hecho(categoria, nombre):
    """
    Elimina un hecho de la base de hechos.
    - categoria: Categoría del hecho (clave en el diccionario).
    - nombre: Elemento a eliminar de la categoría.
    """
    if categoria in hechos and nombre in hechos[categoria]:  # Verificar si el hecho existe
        hechos[categoria].remove(nombre)  # Eliminar el elemento de la categoría

# Probar el sistema con varios casos
print("Evaluando a Pedro:")
aplica_logica_por_defecto("pedro")  # Evaluar las reglas para Pedro

print("\nEvaluando a María:")
aplica_logica_por_defecto("maria")  # Evaluar las reglas para María

# Actualizar hechos dinámicamente
eliminar_hecho("esta_enfermo", "pedro")  # Eliminar el hecho de que Pedro está enfermo
print("\nActualización: Pedro ya no está enfermo.")

# Evaluar nuevamente a Pedro después de la actualización
print("Evaluando nuevamente a Pedro:")
aplica_logica_por_defecto("pedro")

# Agregar un nuevo hecho dinámicamente
agregar_hecho("es_estudiante", "juan")  # Agregar a Juan como estudiante
print("\nEvaluando a Juan:")
aplica_logica_por_defecto("juan")  # Evaluar las reglas para Juan
