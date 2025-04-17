# ===========================
# Reglas del sistema
# ===========================
# Cada regla está definida como un diccionario con:
# - "antecedentes": un conjunto de hechos necesarios para aplicar la regla.
# - "consecuente": el hecho que se deduce si los antecedentes se cumplen.
rules = [
    {"antecedentes": {"A"}, "consecuente": "B"},  # Si "A" es verdadero, entonces "B" es verdadero.
    {"antecedentes": {"B", "C"}, "consecuente": "D"},  # Si "B" y "C" son verdaderos, entonces "D" es verdadero.
    {"antecedentes": {"D"}, "consecuente": "E"},  # Si "D" es verdadero, entonces "E" es verdadero.
    {"antecedentes": {"E"}, "consecuente": "F"},  # Si "E" es verdadero, entonces "F" es verdadero.
]

# ===========================
# Hechos conocidos
# ===========================
# Conjunto de hechos iniciales que se consideran verdaderos al inicio.
hechos_iniciales = {"A", "C"}  # Sabemos que "A" y "C" son verdaderos.

# ===========================
# Encadenamiento hacia adelante
# ===========================
def encadenamiento_hacia_adelante(rules, hechos):
    """
    Realiza el encadenamiento hacia adelante.
    Deduce nuevos hechos a partir de las reglas y los hechos iniciales.

    Args:
        rules (list): Lista de reglas del sistema.
        hechos (set): Conjunto de hechos iniciales.

    Returns:
        set: Conjunto de hechos deducidos.
    """
    # Copiamos los hechos iniciales para no modificarlos directamente.
    nuevos_hechos = hechos.copy()
    aplicado = True  # Variable para controlar si se aplicó alguna regla en cada iteración.

    print("\n=== Encadenamiento hacia adelante ===")
    print(f"Hechos iniciales: {nuevos_hechos}")

    # Mientras se sigan aplicando reglas, continuamos el proceso.
    while aplicado:
        aplicado = False  # Reiniciamos el indicador de aplicación de reglas.
        for regla in rules:
            # Verificamos si todos los antecedentes de la regla están en los hechos actuales
            # y si el consecuente aún no ha sido deducido.
            if regla["antecedentes"].issubset(nuevos_hechos) and regla["consecuente"] not in nuevos_hechos:
                print(f"Se aplica regla: {regla['antecedentes']} → {regla['consecuente']}")
                nuevos_hechos.add(regla["consecuente"])  # Agregamos el consecuente a los hechos deducidos.
                aplicado = True  # Indicamos que se aplicó una regla.

    print(f"\nHechos deducidos: {nuevos_hechos}")
    return nuevos_hechos

# ===========================
# Encadenamiento hacia atrás
# ===========================
def encadenamiento_hacia_atras(rules, hechos, meta, visitados=None):
    """
    Realiza el encadenamiento hacia atrás.
    Verifica si un hecho objetivo (meta) puede ser deducido a partir de las reglas y los hechos iniciales.

    Args:
        rules (list): Lista de reglas del sistema.
        hechos (set): Conjunto de hechos iniciales.
        meta (str): Hecho objetivo que queremos probar.
        visitados (set): Conjunto de hechos ya visitados para evitar ciclos.

    Returns:
        bool: True si el hecho objetivo puede ser deducido, False en caso contrario.
    """
    if visitados is None:
        visitados = set()  # Inicializamos el conjunto de visitados si no se proporciona.

    print(f"\nVerificando si se puede probar: {meta}")
    
    # Si el hecho objetivo ya está en los hechos iniciales, no necesitamos deducirlo.
    if meta in hechos:
        print(f"'{meta}' está en los hechos iniciales.")
        return True

    # Si ya visitamos este hecho, evitamos ciclos.
    if meta in visitados:
        print(f"'{meta}' ya fue visitado, evitando ciclos.")
        return False

    # Marcamos el hecho como visitado.
    visitados.add(meta)

    # Buscamos reglas cuyo consecuente sea el hecho objetivo.
    for regla in rules:
        if regla["consecuente"] == meta:
            print(f"Analizando regla para '{meta}': {regla['antecedentes']} → {meta}")
            # Verificamos si todos los antecedentes de la regla pueden ser probados.
            if all(encadenamiento_hacia_atras(rules, hechos, antecedente, visitados) for antecedente in regla["antecedentes"]):
                print(f"Todos los antecedentes para '{meta}' se cumplen.")
                return True

    # Si no encontramos una forma de deducir el hecho objetivo, devolvemos False.
    print(f"No se pudo probar: {meta}")
    return False

# ===========================
# Pruebas
# ===========================

# Encadenamiento hacia adelante
# Deducimos todos los hechos posibles a partir de los hechos iniciales.
hechos_finales = encadenamiento_hacia_adelante(rules, hechos_iniciales)
print("\n¿Se puede deducir 'F' con encadenamiento hacia adelante?")
print("Sí" if "F" in hechos_finales else "No")

# Encadenamiento hacia atrás
# Verificamos si el hecho "F" puede ser deducido a partir de los hechos iniciales.
print("\n=== Encadenamiento hacia atrás ===")
meta = "F"  # Hecho objetivo que queremos probar.
resultado = encadenamiento_hacia_atras(rules, hechos_iniciales, meta)
print(f"¿Se puede deducir '{meta}' con encadenamiento hacia atrás?")
print("Sí" if resultado else "No")
