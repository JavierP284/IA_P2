# -------------------------------------------------------
# Simulación de Fuzzy CLIPS en Python: Sistema de riego
# -------------------------------------------------------

# Funciones de pertenencia para humedad
# Estas funciones calculan el grado de pertenencia de un valor de humedad
# a las categorías "baja", "media" y "alta".

def humedad_baja(h):
    """
    Grado de pertenencia para humedad baja.
    Si la humedad es menor o igual a 30%, pertenece completamente a "baja".
    Si está entre 30% y 50%, el grado de pertenencia disminuye linealmente.
    Si es mayor a 50%, no pertenece a "baja".
    """
    if h <= 30:
        return 1.0
    elif 30 < h <= 50:
        return (50 - h) / 20
    else:
        return 0.0

def humedad_media(h):
    """
    Grado de pertenencia para humedad media.
    Si la humedad está entre 30% y 50%, el grado de pertenencia aumenta linealmente.
    Si está entre 50% y 70%, el grado de pertenencia disminuye linealmente.
    Fuera de este rango, no pertenece a "media".
    """
    if 30 < h < 50:
        return (h - 30) / 20
    elif 50 <= h <= 70:
        return (70 - h) / 20
    else:
        return 0.0

def humedad_alta(h):
    """
    Grado de pertenencia para humedad alta.
    Si la humedad es menor o igual a 50%, no pertenece a "alta".
    Si está entre 50% y 80%, el grado de pertenencia aumenta linealmente.
    Si es mayor o igual a 80%, pertenece completamente a "alta".
    """
    if h <= 50:
        return 0.0
    elif 50 < h < 80:
        return (h - 50) / 30
    else:
        return 1.0

# Función para imprimir grados de pertenencia
def imprimir_grados(humedad, baja, media, alta):
    """
    Imprime los grados de pertenencia calculados para un valor de humedad.
    Esto ayuda a visualizar cómo se clasifica la humedad en las categorías
    "baja", "media" y "alta".
    """
    print(f"\nGrados de pertenencia (humedad {humedad}%):")
    print(f" - Baja  : {round(baja, 2)}")
    print(f" - Media : {round(media, 2)}")
    print(f" - Alta  : {round(alta, 2)}")

# Reglas borrosas tipo Fuzzy CLIPS
def reglas_fuzzy(humedad):
    """
    Calcula la cantidad de riego recomendada según las reglas difusas.
    Las reglas son:
    - Si la humedad es baja, se recomienda poco riego.
    - Si la humedad es media, se recomienda riego moderado.
    - Si la humedad es alta, no se recomienda riego.
    """
    # Fuzzificación: calcular grados de pertenencia
    baja = humedad_baja(humedad)  # Grado de pertenencia a "baja"
    media = humedad_media(humedad)  # Grado de pertenencia a "media"
    alta = humedad_alta(humedad)  # Grado de pertenencia a "alta"

    # Imprimir grados de pertenencia
    imprimir_grados(humedad, baja, media, alta)

    # Acciones propuestas según las reglas
    riego_poco = baja * 10       # Si humedad baja, poco riego (10 litros/m²)
    riego_moderado = media * 5   # Si humedad media, riego moderado (5 litros/m²)
    riego_nulo = alta * 0        # Si humedad alta, no riego (0 litros/m²)

    # Agregación de acciones: suma ponderada de las recomendaciones
    riego_total = riego_poco + riego_moderado + riego_nulo

    # Retornar el riego total redondeado a 2 decimales
    return round(riego_total, 2)

# Validación de entrada
def validar_humedad(humedad):
    """
    Valida que el valor de humedad esté en el rango 0-100.
    Si está fuera de este rango, se muestra un mensaje de error.
    """
    if 0 <= humedad <= 100:
        return True
    else:
        print(f"Error: La humedad {humedad}% está fuera del rango válido (0-100).")
        return False

# Probar el sistema de riego con distintas humedades
def probar_sistema(humedades_prueba):
    """
    Prueba el sistema de riego con una lista de valores de humedad.
    Para cada valor, valida la entrada y calcula la cantidad de riego recomendada.
    """
    for humedad in humedades_prueba:
        if validar_humedad(humedad):  # Validar que la humedad esté en el rango permitido
            riego = reglas_fuzzy(humedad)  # Calcular el riego recomendado
            print(f"Cantidad de riego recomendada: {riego} litros/m²")  # Mostrar resultado

# Lista de humedades de prueba
humedades_prueba = [20, 40, 60, 85, -10, 110]  # Valores de humedad para probar el sistema

# Ejecutar pruebas
probar_sistema(humedades_prueba)  # Llamar a la función para probar el sistema
