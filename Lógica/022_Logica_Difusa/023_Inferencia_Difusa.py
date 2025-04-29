# ----------------------------------------------------
# Inferencia Difusa: Control de ventilador por temperatura
# ----------------------------------------------------
# Este programa utiliza lógica difusa para determinar la velocidad de un ventilador
# en función de la temperatura. Se basa en funciones de pertenencia para clasificar
# la temperatura como baja, media o alta, y luego aplica reglas difusas para calcular
# una velocidad ponderada.

# Paso 1: Fuzzificación - funciones de pertenencia
def temp_baja(t):
    """
    Función de pertenencia para temperatura baja.
    Devuelve un grado de pertenencia entre 0 y 1.
    """
    if t <= 15:  # Si la temperatura es menor o igual a 15°C, pertenece completamente a "baja".
        return 1.0
    elif 15 < t < 25:  # Si está entre 15°C y 25°C, el grado de pertenencia disminuye linealmente.
        return (25 - t) / 10
    return 0.0  # Si es mayor o igual a 25°C, no pertenece a "baja".

def temp_media(t):
    """
    Función de pertenencia para temperatura media.
    Devuelve un grado de pertenencia entre 0 y 1.
    """
    if 20 < t < 30:  # Si está entre 20°C y 30°C, el grado de pertenencia aumenta linealmente.
        return (t - 20) / 10
    elif 30 <= t < 35:  # Si está entre 30°C y 35°C, el grado de pertenencia disminuye linealmente.
        return (35 - t) / 5
    return 0.0  # Fuera de este rango, no pertenece a "media".

def temp_alta(t):
    """
    Función de pertenencia para temperatura alta.
    Devuelve un grado de pertenencia entre 0 y 1.
    """
    if t <= 30:  # Si la temperatura es menor o igual a 30°C, no pertenece a "alta".
        return 0.0
    elif 30 < t < 40:  # Si está entre 30°C y 40°C, el grado de pertenencia aumenta linealmente.
        return (t - 30) / 10
    return 1.0  # Si es mayor o igual a 40°C, pertenece completamente a "alta".

# Paso 2: Inferencia - aplicar reglas difusas
def reglas_difusas(baja, media, alta):
    """
    Define las reglas difusas y calcula la velocidad ponderada del ventilador.
    Combina los grados de pertenencia de las temperaturas con velocidades asociadas.
    """
    # Velocidades asociadas a cada nivel de temperatura
    v_baja = 2   # Velocidad baja (por ejemplo, 2 RPM)
    v_media = 5  # Velocidad media (por ejemplo, 5 RPM)
    v_alta = 9   # Velocidad alta (por ejemplo, 9 RPM)

    # Defuzzificación - cálculo del centroide ponderado
    # Numerador: suma ponderada de las velocidades por sus grados de pertenencia
    numerador = (baja * v_baja) + (media * v_media) + (alta * v_alta)
    # Denominador: suma de los grados de pertenencia
    denominador = baja + media + alta

    if denominador == 0:  # Evitar división por cero si no hay pertenencia
        return 0.0

    # Resultado: velocidad ponderada
    return numerador / denominador

def inferir_velocidad(temp):
    """
    Calcula la velocidad del ventilador basada en la temperatura.
    Realiza los pasos de fuzzificación, inferencia y defuzzificación.
    """
    # Fuzzificación: calcular los grados de pertenencia para cada categoría
    baja = temp_baja(temp)
    media = temp_media(temp)
    alta = temp_alta(temp)

    # Mostrar los grados de pertenencia para la temperatura dada
    print(f"\nGrados de pertenencia (temperatura {temp}°C):")
    print(f" - Baja  : {round(baja, 2)}")
    print(f" - Media : {round(media, 2)}")
    print(f" - Alta  : {round(alta, 2)}")

    # Inferencia y defuzzificación: calcular la velocidad resultante
    velocidad_resultante = reglas_difusas(baja, media, alta)
    return round(velocidad_resultante, 2)  # Redondear el resultado a 2 decimales

# Paso 3: Visualización de resultados
def mostrar_resultados():
    """
    Prueba el sistema con distintas temperaturas y muestra los resultados.
    """
    # Lista de temperaturas de prueba
    temperaturas = [10, 22, 28, 33, 40]
    print("\nResultados del sistema difuso:")
    for t in temperaturas:
        # Calcular la velocidad del ventilador para cada temperatura
        velocidad = inferir_velocidad(t)
        print(f"Temperatura: {t}°C -> Velocidad del ventilador: {velocidad}")

# Ejecutar el sistema
if __name__ == "__main__":
    mostrar_resultados()
