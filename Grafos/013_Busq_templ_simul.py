import math
import random

def temple_simulado(funcion_evaluacion, generar_vecinos, estado_inicial, temperatura_inicial=100, enfriamiento=0.99, iteraciones=1000, umbral_temperatura=0.01):
    """
    Implementación del algoritmo de Búsqueda de Temple Simulado.

    - funcion_evaluacion: Función que evalúa la calidad de una solución.
    - generar_vecinos: Función que genera un estado vecino.
    - estado_inicial: Estado de inicio.
    - temperatura_inicial: Temperatura inicial para la aceptación de soluciones peores.
    - enfriamiento: Factor de reducción de la temperatura en cada iteración.
    - iteraciones: Número máximo de iteraciones.
    - umbral_temperatura: Umbral de temperatura para detener la búsqueda.

    Retorna la mejor solución encontrada.
    """
    estado_actual = estado_inicial  # Se establece el estado inicial
    mejor_estado = estado_actual  # Se guarda la mejor solución encontrada
    mejor_valor = funcion_evaluacion(estado_actual)  # Se evalúa la solución inicial

    temperatura = temperatura_inicial  # Se inicializa la temperatura

    for i in range(iteraciones):
        nuevo_estado = generar_vecinos(estado_actual)  # Se genera un nuevo estado vecino
        nuevo_valor = funcion_evaluacion(nuevo_estado)  # Se evalúa la nueva solución

        # Si la nueva solución es mejor, la aceptamos directamente
        if nuevo_valor > mejor_valor:
            mejor_estado = nuevo_estado
            mejor_valor = nuevo_valor
            estado_actual = nuevo_estado

        else:
            # Si la solución es peor, se acepta con probabilidad basada en la temperatura
            delta = nuevo_valor - mejor_valor  # Diferencia de calidad entre soluciones
            
            # Evitar división por cero en el cálculo de probabilidad
            if temperatura > 0:
                probabilidad = math.exp(delta / temperatura)
            else:
                probabilidad = 0

            if random.random() < probabilidad:
                estado_actual = nuevo_estado  # Se acepta la nueva solución peor

        # Reducimos la temperatura en cada iteración
        temperatura *= enfriamiento

        # Si la temperatura es demasiado baja, terminamos la búsqueda
        if temperatura < umbral_temperatura:
            break

    return mejor_estado, mejor_valor, temperatura, i + 1  # Se retorna la mejor solución encontrada

# 🔹 Definimos la función de evaluación (Ejemplo: buscar el máximo de una parábola)
def funcion_evaluacion(x):
    return -(x - 3) ** 2 + 10  # Función con máximo en x = 3

# 🔹 Función para generar vecinos cercanos
def generar_vecinos(x):
    return x + random.uniform(-0.5, 0.5)  # Se mueve aleatoriamente en un pequeño rango

# 🔹 Estado inicial aleatorio
estado_inicial = random.uniform(-10, 10)

# 🔹 Ejecutamos el algoritmo de Temple Simulado
mejor_solucion, mejor_valor, temperatura_final, iteraciones_realizadas = temple_simulado(funcion_evaluacion, generar_vecinos, estado_inicial)

# 🔹 Mostramos los resultados
print(f"Mejor solución encontrada: x = {mejor_solucion}")
print(f"Valor óptimo: f(x) = {mejor_valor}")
print(f"Temperatura final: {temperatura_final}")
print(f"Iteraciones realizadas: {iteraciones_realizadas}")
