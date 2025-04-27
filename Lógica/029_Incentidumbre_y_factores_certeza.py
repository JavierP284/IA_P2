# ----------------------------------------------
# Diagnóstico con Factores de Certeza
# ----------------------------------------------

# Función para calcular el factor de certeza del diagnóstico
def calcular_fc_diagnostico(sintomas_detectados, reglas_diagnostico):
    """
    Calcula el factor de certeza para cada enfermedad basada en los síntomas detectados
    y las reglas de diagnóstico.

    Args:
        sintomas_detectados (dict): Diccionario con síntomas y sus factores de certeza.
                                     Ejemplo: {"tos": 0.8, "fiebre": 0.6}
        reglas_diagnostico (dict): Diccionario con reglas de diagnóstico.
                                   Ejemplo:
                                   {
                                       "gripe": {
                                           "condiciones": ["tos", "fiebre"],
                                           "fc_regla": 0.9
                                       }
                                   }

    Returns:
        dict: Diagnósticos con sus factores de certeza.
              Ejemplo: {"gripe": 0.54, "resfriado": 0.56}
    """
    diagnosticos = {}  # Diccionario para almacenar los resultados de los diagnósticos

    # Iterar sobre cada enfermedad y sus reglas de diagnóstico
    for enfermedad, datos in reglas_diagnostico.items():
        condiciones = datos["condiciones"]  # Lista de síntomas necesarios para esta enfermedad
        fc_regla = datos["fc_regla"]        # Factor de certeza asociado a la regla

        # Obtener los factores de certeza de los síntomas detectados
        # Si un síntoma no está presente, se asigna un valor de 0
        fc_sintomas = [sintomas_detectados.get(s, 0) for s in condiciones]

        # Si falta algún síntoma (factor de certeza = 0), el diagnóstico no es válido
        if 0 in fc_sintomas:
            diagnosticos[enfermedad] = 0  # Factor de certeza del diagnóstico es 0
            continue  # Pasar a la siguiente enfermedad

        # Calcular el mínimo factor de certeza entre los síntomas involucrados
        fc_min_sintomas = min(fc_sintomas)

        # El factor final es el producto del factor de la regla y el mínimo FC de los síntomas
        fc_final = fc_regla * fc_min_sintomas

        # Guardar el resultado redondeado a 2 decimales
        diagnosticos[enfermedad] = round(fc_final, 2)

    return diagnosticos  # Retornar los diagnósticos con sus factores de certeza


# Función para mostrar los resultados de forma ordenada
def mostrar_resultados(diagnosticos):
    """
    Muestra los diagnósticos ordenados por el factor de certeza.

    Args:
        diagnosticos (dict): Diagnósticos con sus factores de certeza.
                             Ejemplo: {"gripe": 0.54, "resfriado": 0.56}
    """
    print("\nDiagnóstico generado:")
    # Ordenar los diagnósticos por el factor de certeza en orden descendente
    diagnosticos_ordenados = sorted(diagnosticos.items(), key=lambda x: x[1], reverse=True)

    # Mostrar cada diagnóstico con su factor de certeza
    for enfermedad, fc in diagnosticos_ordenados:
        if fc > 0:
            # Si el factor de certeza es mayor a 0, mostrar el diagnóstico
            print(f" - {enfermedad.capitalize()} con un factor de certeza de {fc}")
        else:
            # Si el factor de certeza es 0, indicar que no cumple con los síntomas necesarios
            print(f" - {enfermedad.capitalize()} no cumple con los síntomas necesarios.")


# ----------------------------------------------
# Datos de entrada: síntomas detectados y reglas de diagnóstico

# Diccionario con los síntomas detectados y sus factores de certeza
# Cada síntoma tiene un valor entre 0 y 1 que indica el nivel de certeza
sintomas_detectados = {
    "tos": 0.8,    # 80% seguro que tiene tos
    "fiebre": 0.6  # 60% seguro que tiene fiebre
}

# Diccionario con las reglas de diagnóstico para cada enfermedad
# Cada regla incluye los síntomas necesarios y un factor de certeza asociado
reglas_diagnostico = {
    "gripe": {
        "condiciones": ["tos", "fiebre"],  # Síntomas necesarios para diagnosticar gripe
        "fc_regla": 0.9  # Confianza del experto en la regla (90%)
    },
    "resfriado": {
        "condiciones": ["tos"],  # Síntomas necesarios para diagnosticar resfriado
        "fc_regla": 0.7  # Confianza del experto en la regla (70%)
    }
}

# ----------------------------------------------
# Ejecutar el diagnóstico

print("Calculando diagnóstico con incertidumbre...")
# Llamar a la función para calcular los diagnósticos
resultado = calcular_fc_diagnostico(sintomas_detectados, reglas_diagnostico)

# Mostrar los resultados del diagnóstico
mostrar_resultados(resultado)
