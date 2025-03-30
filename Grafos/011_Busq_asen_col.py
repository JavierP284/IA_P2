import random

def hill_climbing(funcion_evaluacion, vecinos, estado_actual, max_iteraciones=1000):
    """
    Algoritmo de Búsqueda de Ascensión de Colinas (Hill Climbing)
    - funcion_evaluacion: función que mide qué tan bueno es un estado
    - vecinos: función que genera estados vecinos
    - estado_actual: estado inicial de búsqueda
    - max_iteraciones: número máximo de iteraciones para evitar bucles infinitos
    """
    iteracion = 0
    while iteracion < max_iteraciones:
        # Obtener la evaluación del estado actual
        evaluacion_actual = funcion_evaluacion(estado_actual)

        # Generar todos los estados vecinos
        estados_vecinos = vecinos(estado_actual)

        # Evaluar los vecinos y elegir el mejor
        mejor_estado = estado_actual
        mejor_evaluacion = evaluacion_actual

        for estado in estados_vecinos:
            evaluacion = funcion_evaluacion(estado)

            # Si encontramos un mejor estado, lo actualizamos
            if evaluacion > mejor_evaluacion:
                mejor_estado = estado
                mejor_evaluacion = evaluacion

        # Si ningún vecino es mejor, terminamos la búsqueda
        if mejor_evaluacion == evaluacion_actual:
            return estado_actual  # Devolvemos la mejor solución encontrada

        # Continuamos desde el mejor estado encontrado
        estado_actual = mejor_estado
        iteracion += 1

    # Si se alcanza el límite de iteraciones, devolvemos el mejor estado encontrado
    return estado_actual


# Definir una función de evaluación (ejemplo: maximizar una función cuadrática)
def funcion_evaluacion(x):
    """Función de evaluación: f(x) = - (x - 3)^2 + 10 (máximo en x = 3)"""
    return - (x - 3) ** 2 + 10


# Generar vecinos cercanos al estado actual
def generar_vecinos(x):
    """Función que genera estados vecinos moviendo ligeramente x"""
    return [x - 0.1, x + 0.1]


# Definir un estado inicial aleatorio
estado_inicial = random.uniform(-10, 10)

# Ejecutar el algoritmo
resultado = hill_climbing(funcion_evaluacion, generar_vecinos, estado_inicial)

# Mostrar resultado
print(f"Máximo encontrado en x = {resultado:.4f}")
print(f"Valor de f(x) = {funcion_evaluacion(resultado):.4f}")
