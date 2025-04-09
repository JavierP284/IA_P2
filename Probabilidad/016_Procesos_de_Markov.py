import numpy as np
import random

# ----------------------------
# Definimos los estados
# ----------------------------
estados = ['Casa', 'Trabajo', 'Restaurante']
indice_estados = {estado: i for i, estado in enumerate(estados)}

# ----------------------------
# Definimos la matriz de transición (basada en la Hipótesis de Markov)
# ----------------------------
# Cada fila representa las probabilidades de ir a otro estado desde el estado actual
# Por ejemplo: Desde 'Casa' → [Casa, Trabajo, Restaurante]
matriz_transicion = [
    [0.2, 0.6, 0.2],  # Desde 'Casa'
    [0.3, 0.4, 0.3],  # Desde 'Trabajo'
    [0.5, 0.2, 0.3]   # Desde 'Restaurante'
]

# Mostramos la matriz de transición
print("Matriz de transición:")
for i, fila in enumerate(matriz_transicion):
    print(f"Desde {estados[i]}: {fila}")

# ----------------------------
# Función que simula el proceso de Markov
# ----------------------------
def simular_proceso_markov(estado_inicial, pasos):
    """
    Simula un proceso de Markov dado un estado inicial y un número de pasos.

    Args:
        estado_inicial (str): El estado inicial del proceso.
        pasos (int): Número de pasos a simular.

    Returns:
        list: Secuencia de estados generada por el proceso de Markov.
    """
    if estado_inicial not in estados:
        raise ValueError(f"Estado inicial '{estado_inicial}' no es válido. Estados posibles: {estados}")
    if pasos <= 0:
        raise ValueError("El número de pasos debe ser un entero positivo.")

    estado_actual = estado_inicial
    secuencia = [estado_actual]

    for paso in range(pasos):
        i = indice_estados[estado_actual]
        siguiente_estado = random.choices(estados, weights=matriz_transicion[i])[0]
        secuencia.append(siguiente_estado)
        estado_actual = siguiente_estado

    return secuencia

# ----------------------------
# Función principal
# ----------------------------
def main():
    estado_inicial = 'Casa'
    num_pasos = 10

    print(f"\nEstado inicial: {estado_inicial}")
    print(f"Número de pasos: {num_pasos}\n")

    # Ejecutamos la simulación
    secuencia_resultado = simular_proceso_markov(estado_inicial, num_pasos)

    # Mostramos la secuencia generada
    print("Simulación de Proceso de Markov:")
    for i, estado in enumerate(secuencia_resultado):
        print(f"Paso {i}: {estado}")

    # Mostramos estadísticas finales
    print("\nEstadísticas de la simulación:")
    for estado in estados:
        frecuencia = secuencia_resultado.count(estado)
        print(f"{estado}: {frecuencia} veces ({(frecuencia / len(secuencia_resultado)) * 100:.2f}%)")

# ----------------------------
# Ejecutamos el programa
# ----------------------------
if __name__ == "__main__":
    main()
