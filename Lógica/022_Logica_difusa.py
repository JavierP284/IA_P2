# -----------------------------------------------
# Sistema de lógica difusa mejorado para ventilador
# Basado en temperatura ambiente
# -----------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# Funciones de pertenencia difusa para la temperatura
def temperatura_baja(temp):
    """
    Calcula el grado de pertenencia de la temperatura al conjunto 'baja'.
    - Si la temperatura es <= 15, pertenece completamente al conjunto (grado 1.0).
    - Si la temperatura está entre 15 y 25, el grado disminuye linealmente.
    - Si la temperatura es > 25, no pertenece al conjunto (grado 0.0).
    """
    if temp <= 15:
        return 1.0
    elif 15 < temp < 25:
        return (25 - temp) / 10
    else:
        return 0.0

def temperatura_media(temp):
    """
    Calcula el grado de pertenencia de la temperatura al conjunto 'media'.
    - Forma de campana entre 20 y 30 grados.
    - Máxima pertenencia (grado 1.0) en 25 grados.
    - Fuera del rango 20-30, el grado es 0.0.
    """
    if 20 < temp < 25:
        return (temp - 20) / 5
    elif 25 <= temp <= 30:
        return (30 - temp) / 5
    else:
        return 0.0

def temperatura_alta(temp):
    """
    Calcula el grado de pertenencia de la temperatura al conjunto 'alta'.
    - Si la temperatura es <= 25, no pertenece al conjunto (grado 0.0).
    - Si la temperatura está entre 25 y 35, el grado aumenta linealmente.
    - Si la temperatura es > 35, pertenece completamente al conjunto (grado 1.0).
    """
    if temp <= 25:
        return 0.0
    elif 25 < temp < 35:
        return (temp - 25) / 10
    else:
        return 1.0

# Funciones de pertenencia difusa para la velocidad del ventilador (salida)
def velocidad_baja():
    """Devuelve la velocidad baja del ventilador."""
    return 2.0

def velocidad_media():
    """Devuelve la velocidad media del ventilador."""
    return 5.0

def velocidad_alta():
    """Devuelve la velocidad alta del ventilador."""
    return 8.0

# Visualización de funciones de pertenencia
def graficar_conjuntos():
    """
    Genera un gráfico que muestra las funciones de pertenencia para los conjuntos
    'baja', 'media' y 'alta' en el rango de temperaturas de 0 a 40 grados.
    """
    temperaturas = np.linspace(0, 40, 100)  # Rango de temperaturas
    bajas = [temperatura_baja(t) for t in temperaturas]
    medias = [temperatura_media(t) for t in temperaturas]
    altas = [temperatura_alta(t) for t in temperaturas]

    # Graficar las funciones de pertenencia
    plt.plot(temperaturas, bajas, label="Baja")
    plt.plot(temperaturas, medias, label="Media")
    plt.plot(temperaturas, altas, label="Alta")
    plt.title("Funciones de Pertenencia de Temperatura")
    plt.xlabel("Temperatura (°C)")
    plt.ylabel("Grado de Pertenencia")
    plt.legend()
    plt.grid()
    plt.show()

# Inferencia difusa tipo Mamdani
def inferencia_difusa(temp):
    """
    Realiza la inferencia difusa para determinar la velocidad del ventilador.
    - Calcula los grados de pertenencia de la temperatura a los conjuntos 'baja', 'media' y 'alta'.
    - Usa el método del centroide ponderado para defuzzificar y obtener un valor final.
    """
    if temp < 0 or temp > 50:
        raise ValueError("La temperatura debe estar entre 0 y 50°C.")

    # Obtener grados de pertenencia
    baja = temperatura_baja(temp)
    media = temperatura_media(temp)
    alta = temperatura_alta(temp)

    # Mostrar los grados de pertenencia
    print("\n--- Grados de Pertenencia ---")
    print(f"Temperatura baja: {baja:.2f}")
    print(f"Temperatura media: {media:.2f}")
    print(f"Temperatura alta: {alta:.2f}")

    # Defuzzificación usando centroide ponderado
    numerador = (baja * velocidad_baja()) + (media * velocidad_media()) + (alta * velocidad_alta())
    denominador = baja + media + alta

    if denominador == 0:
        print("\nNo se puede calcular la velocidad del ventilador (denominador = 0).")
        return 0.0  # Evitar división por cero

    velocidad_final = numerador / denominador
    print("\n--- Cálculo de Defuzzificación ---")
    print(f"Numerador: {numerador:.2f}")
    print(f"Denominador: {denominador:.2f}")
    print(f"Velocidad final (difusa): {velocidad_final:.2f}")
    return velocidad_final

# Reglas tipo CLIPS en Python simuladas con diccionarios
reglas_difusas = [
    {"condicion": lambda t: temperatura_baja(t) > 0.5, "accion": "ventilador_lento"},
    {"condicion": lambda t: temperatura_media(t) > 0.5, "accion": "ventilador_medio"},
    {"condicion": lambda t: temperatura_alta(t) > 0.5, "accion": "ventilador_rapido"},
    {"condicion": lambda t: temperatura_baja(t) > 0.3 and temperatura_media(t) > 0.3, "accion": "ventilador_medio_lento"},
]

def fuzzy_clips_simulado(temp):
    """
    Simula un sistema de reglas tipo CLIPS para determinar qué acción tomar
    en función de las condiciones difusas.
    """
    print("\n--- Reglas tipo CLIPS ---")
    for regla in reglas_difusas:
        if regla["condicion"](temp):
            print(f"✔️ Se activa regla: {regla['accion']}")

# --------------------------
# Ejemplo de uso
# --------------------------
if __name__ == "__main__":
    # Graficar funciones de pertenencia
    graficar_conjuntos()

    # Probar inferencia difusa
    temperatura_actual = 28  # Cambia este valor para probar diferentes casos
    print(f"\n--- Temperatura Actual: {temperatura_actual}°C ---")
    velocidad = inferencia_difusa(temperatura_actual)

    print(f"\n--- Resultado Final ---")
    print(f"Velocidad del ventilador: {round(velocidad, 2)}")

    # Ejecutar simulación CLIPS
    fuzzy_clips_simulado(temperatura_actual)
