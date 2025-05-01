# ---------------------------------------------------------
# K-DL: Lista de Decisión para evaluación de estudiantes
# ---------------------------------------------------------

# Constantes que definen los criterios mínimos para cada categoría
ASISTENCIA_MINIMA_APROBADO = 90  # Asistencia mínima para aprobar directamente
ASISTENCIA_MINIMA_OBSERVACION = 80  # Asistencia mínima para aprobar con observación
ASISTENCIA_MINIMA_REPROBADO = 70  # Asistencia mínima para no reprobar directamente
PROMEDIO_MINIMO_APROBADO = 8  # Promedio mínimo para aprobar directamente
PROMEDIO_MINIMO_OBSERVACION = 6  # Promedio mínimo para aprobar con observación

def evaluar_k_dl(asistencia, promedio):
    """
    Evalúa a un estudiante usando el método K-DL (Lista de Decisión).

    Parámetros:
        asistencia (int): Porcentaje de asistencia del estudiante (0-100).
        promedio (float): Promedio del estudiante (0-10).

    Retorna:
        str: Resultado de la evaluación:
            - "Aprueba": Si cumple con los criterios de asistencia y promedio para aprobar.
            - "Aprueba con observación": Si cumple con criterios mínimos pero no ideales.
            - "Reprueba": Si no cumple con los criterios mínimos.
            - "Caso especial": Si no encaja en ninguna de las categorías anteriores.
    """
    # Validación de rango de entrada
    if not (0 <= asistencia <= 100 and 0 <= promedio <= 10):
        return "Error: Valores fuera de rango."

    # Caso: Aprueba directamente
    if promedio >= PROMEDIO_MINIMO_APROBADO and asistencia >= ASISTENCIA_MINIMA_APROBADO:
        return "Aprueba"
    # Caso: Aprueba con observación
    elif promedio >= PROMEDIO_MINIMO_OBSERVACION and asistencia >= ASISTENCIA_MINIMA_OBSERVACION:
        return "Aprueba con observación"
    # Caso: Reprueba
    elif promedio < PROMEDIO_MINIMO_OBSERVACION or asistencia < ASISTENCIA_MINIMA_REPROBADO:
        return "Reprueba"
    # Caso especial (no debería ocurrir con las reglas actuales)
    else:
        return "Caso especial"

# ---------------------------------------------------------
# K-DT: Árbol de Decisión con condiciones k-conjuntivas
# ---------------------------------------------------------

def evaluar_k_dt(asistencia, promedio):
    """
    Evalúa a un estudiante usando el método K-DT (Árbol de Decisión).

    Parámetros:
        asistencia (int): Porcentaje de asistencia del estudiante (0-100).
        promedio (float): Promedio del estudiante (0-10).

    Retorna:
        str: Resultado de la evaluación:
            - "Aprueba": Si cumple con los criterios de asistencia y promedio para aprobar.
            - "Aprueba con observación": Si cumple con criterios mínimos pero no ideales.
            - "Reprueba directa por baja asistencia": Si la asistencia es demasiado baja.
            - "Reprueba": Si no cumple con los criterios mínimos.
    """
    # Validación de rango de entrada
    if not (0 <= asistencia <= 100 and 0 <= promedio <= 10):
        return "Error: Valores fuera de rango."

    # Árbol de decisión basado en asistencia
    if asistencia >= ASISTENCIA_MINIMA_APROBADO:
        # Subárbol: Asistencia suficiente para aprobar
        if promedio >= PROMEDIO_MINIMO_APROBADO:
            return "Aprueba"
        elif promedio >= PROMEDIO_MINIMO_OBSERVACION:
            return "Aprueba con observación"
        else:
            return "Reprueba"
    elif asistencia >= ASISTENCIA_MINIMA_OBSERVACION:
        # Subárbol: Asistencia suficiente para observación
        if promedio >= PROMEDIO_MINIMO_OBSERVACION:
            return "Aprueba con observación"
        else:
            return "Reprueba"
    else:
        # Caso: Asistencia demasiado baja
        return "Reprueba directa por baja asistencia"

# ---------------------------------------------------------
# Pruebas
# ---------------------------------------------------------

def pruebas():
    """
    Ejecuta pruebas para evaluar los métodos K-DL y K-DT.

    Se prueban diferentes combinaciones de asistencia y promedio para verificar
    que las funciones devuelvan los resultados esperados.
    """
    # Lista de casos de prueba con diferentes combinaciones de asistencia y promedio
    casos_prueba = [
        (92, 8.5),  # Caso: Aprueba
        (82, 6.5),  # Caso: Aprueba con observación
        (60, 7.0),  # Caso: Reprueba
        (90, 8.0),  # Caso límite: Aprueba
        (80, 6.0),  # Caso límite: Aprueba con observación
        (70, 5.9),  # Caso límite: Reprueba
        (50, 4.0),  # Caso: Reprueba directa por baja asistencia
        (110, 8.0), # Caso inválido: Asistencia fuera de rango
        (85, -1),   # Caso inválido: Promedio fuera de rango
    ]

    # Pruebas para el método K-DL
    print("\n--- Pruebas K-DL ---")
    for asistencia, promedio in casos_prueba:
        resultado = evaluar_k_dl(asistencia, promedio)
        print(f"Asistencia: {asistencia}%, Promedio: {promedio} -> Resultado: {resultado}")

    # Pruebas para el método K-DT
    print("\n--- Pruebas K-DT ---")
    for asistencia, promedio in casos_prueba:
        resultado = evaluar_k_dt(asistencia, promedio)
        print(f"Asistencia: {asistencia}%, Promedio: {promedio} -> Resultado: {resultado}")

# Ejecutar pruebas
pruebas()

