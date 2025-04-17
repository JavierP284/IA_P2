import random
import matplotlib.pyplot as plt
import numpy as np

# Definimos la función objetivo que queremos maximizar
# En este caso, es una parábola invertida: f(x) = -x^2 + 4
def funcion_objetivo(x):
    return -x**2 + 4

# Implementación del algoritmo de Ascenso de Colinas (Hill Climbing)
def hill_climbing(paso=0.1, iteraciones=1000, rango=(-10, 10)):
    """
    Algoritmo de Ascenso de Colinas para encontrar el máximo de una función.

    Parámetros:
    - paso: Tamaño máximo del cambio en cada iteración.
    - iteraciones: Número máximo de iteraciones.
    - rango: Rango de valores permitidos para x (mínimo, máximo).
    """
    # Seleccionamos un punto inicial aleatorio dentro del rango especificado
    x_actual = random.uniform(rango[0], rango[1])
    valor_actual = funcion_objetivo(x_actual)

    # Mostramos el punto inicial y su valor en la función objetivo
    print(f"Punto inicial: x = {x_actual:.4f}, f(x) = {valor_actual:.4f}")

    # Listas para almacenar el progreso del algoritmo (para graficar después)
    historial_x = [x_actual]
    historial_y = [valor_actual]

    # Iteramos hasta alcanzar el número máximo de iteraciones
    for i in range(iteraciones):
        # Generamos un nuevo punto vecino aleatorio dentro del rango permitido
        x_vecino = x_actual + random.uniform(-paso, paso)
        # Aseguramos que el nuevo punto vecino esté dentro del rango permitido
        x_vecino = max(min(x_vecino, rango[1]), rango[0])
        valor_vecino = funcion_objetivo(x_vecino)

        # Si el valor del vecino es mejor que el actual, nos movemos hacia él
        if valor_vecino > valor_actual:
            x_actual = x_vecino
            valor_actual = valor_vecino
            # Mostramos la mejora encontrada en esta iteración
            print(f"Mejora encontrada en iteración {i}: x = {x_actual:.4f}, f(x) = {valor_actual:.4f}")

        # Guardamos el progreso actual (para graficar después)
        historial_x.append(x_actual)
        historial_y.append(valor_actual)

    # Mostramos el máximo encontrado después de todas las iteraciones
    print(f"\nMáximo encontrado: x = {x_actual:.4f}, f(x) = {valor_actual:.4f}")

    # Graficamos la función objetivo y el progreso del algoritmo
    graficar_funcion(historial_x, historial_y, rango)

def graficar_funcion(historial_x, historial_y, rango):
    """
    Genera una gráfica de la función objetivo y el progreso del algoritmo.

    Parámetros:
    - historial_x: Lista de valores de x visitados por el algoritmo.
    - historial_y: Lista de valores de f(x) correspondientes a historial_x.
    - rango: Rango de valores para graficar la función objetivo.
    """
    # Generamos un conjunto de puntos para graficar la función objetivo
    x = np.linspace(rango[0], rango[1], 500)
    y = funcion_objetivo(x)

    # Configuramos la gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label="Función objetivo", color="blue")  # Línea de la función objetivo
    plt.scatter(historial_x, historial_y, color="red", label="Progreso del algoritmo")  # Puntos visitados
    plt.title("Algoritmo de Ascenso de Colinas")  # Título de la gráfica
    plt.xlabel("x")  # Etiqueta del eje x
    plt.ylabel("f(x)")  # Etiqueta del eje y
    plt.legend()  # Leyenda de la gráfica
    plt.grid()  # Cuadrícula para facilitar la lectura
    plt.show()  # Mostramos la gráfica

# Ejecutamos el algoritmo con parámetros configurables
# Parámetros:
# - paso: 0.1 (tamaño del cambio en cada iteración)
# - iteraciones: 100 (número máximo de iteraciones)
# - rango: (-5, 5) (rango de búsqueda para x)
hill_climbing(paso=0.1, iteraciones=100, rango=(-5, 5))
