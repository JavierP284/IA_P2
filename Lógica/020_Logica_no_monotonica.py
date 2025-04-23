# ----------------------------------------------
# Lógica No Monotónica - Reglas por defecto
# ----------------------------------------------
# Este programa implementa un ejemplo de lógica no monotónica, donde las conclusiones
# pueden cambiar al modificar la base de hechos. Se utiliza un conjunto de reglas por
# defecto y excepciones para determinar si un animal puede volar.

# Base de hechos inicial
# Aquí se define la base de conocimiento inicial. Cada categoría (como "es_pajaro" o "es_pinguino")
# contiene un conjunto de elementos que cumplen con esa categoría.
hechos = {
    "es_pajaro": {"tweety"},  # Tweety es un pájaro
    "es_pinguino": {"tweety"},  # Tweety también es un pingüino
}

# Función que evalúa si un animal puede volar
def puede_volar(nombre):
    """
    Evalúa si un animal puede volar basado en las reglas por defecto y excepciones.
    Reglas:
    1. Si el animal es un pingüino, no puede volar (excepción específica).
    2. Si el animal es un pájaro, puede volar (regla por defecto).
    3. Si no hay información suficiente, no se puede determinar.
    """
    # Caso 1: Si el animal es un pingüino, no puede volar
    if nombre in hechos.get("es_pinguino", set()):
        print(f"{nombre} es un pingüino. No puede volar.")
        return False
    
    # Caso 2: Si el animal es un pájaro, puede volar
    if nombre in hechos.get("es_pajaro", set()):
        print(f"{nombre} es un pájaro. Por defecto, puede volar.")
        return True

    # Caso 3: Si no hay información suficiente, no se puede determinar
    print(f"No hay suficiente información sobre {nombre}.")
    return None

# Función para agregar un hecho
def agregar_hecho(categoria, nombre):
    """
    Agrega un hecho a la base de conocimiento.
    Parámetros:
    - categoria: La categoría a la que pertenece el hecho (por ejemplo, "es_pajaro").
    - nombre: El nombre del elemento que se agrega a la categoría.
    """
    # Si la categoría no existe en la base de hechos, se crea
    if categoria not in hechos:
        hechos[categoria] = set()
    # Se agrega el elemento a la categoría correspondiente
    hechos[categoria].add(nombre)
    print(f"Hecho agregado: {nombre} es {categoria}.")

# Función para eliminar un hecho
def eliminar_hecho(categoria, nombre):
    """
    Elimina un hecho de la base de conocimiento.
    Parámetros:
    - categoria: La categoría de la que se eliminará el hecho.
    - nombre: El nombre del elemento que se eliminará.
    """
    # Verifica si la categoría y el elemento existen en la base de hechos
    if categoria in hechos and nombre in hechos[categoria]:
        # Elimina el elemento de la categoría
        hechos[categoria].remove(nombre)
        print(f"Hecho eliminado: {nombre} ya no es {categoria}.")
    else:
        # Mensaje si el hecho no se encuentra
        print(f"No se encontró el hecho: {nombre} no es {categoria}.")

# Pruebas con el conocimiento inicial
# Aquí se evalúa si Tweety puede volar con la base de hechos inicial
print("¿Puede volar Tweety?:", puede_volar("tweety"))

# Actualización de hechos
# Se elimina el hecho de que Tweety es un pingüino
eliminar_hecho("es_pinguino", "tweety")
print("\nActualización: Tweety ya no es considerado pingüino.")

# Evaluamos nuevamente después de cambiar los hechos
# Ahora que Tweety ya no es un pingüino, se evalúa si puede volar
print("¿Puede volar Tweety ahora?:", puede_volar("tweety"))

# Agregar un nuevo hecho y probar
# Se agrega un nuevo pájaro llamado Robin y se evalúa si puede volar
agregar_hecho("es_pajaro", "robin")
print("\n¿Puede volar Robin?:", puede_volar("robin"))
