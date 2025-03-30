import random

def busqueda_haz_local(funcion_evaluacion, generar_vecinos, k=3, iteraciones=100):
    """
    Implementación de la Búsqueda de Haz Local.

    - funcion_evaluacion: Función que evalúa la calidad de una solución.
    - generar_vecinos: Función que genera un conjunto de vecinos a partir de un estado dado.
    - k: Número de soluciones que se mantienen en cada iteración.
    - iteraciones: Número máximo de iteraciones.

    Retorna la mejor solución encontrada.
    """
    
    # 🔹 Generamos k soluciones iniciales aleatorias
    haz_actual = [random.uniform(-10, 10) for _ in range(k)]
    
    for _ in range(iteraciones):
        # 🔹 Generamos todos los vecinos posibles a partir de las soluciones actuales
        vecinos = []
        for estado in haz_actual:
            vecinos.extend(generar_vecinos(estado))  # Expandimos cada estado en sus vecinos
        
        # 🔹 Evaluamos todas las soluciones (actuales y nuevas) y seleccionamos las k mejores
        haz_actual = sorted(vecinos + haz_actual, key=funcion_evaluacion, reverse=True)[:k]

    # 🔹 Retornamos la mejor solución encontrada
    mejor_solucion = max(haz_actual, key=funcion_evaluacion)
    return mejor_solucion, funcion_evaluacion(mejor_solucion)


# 🔹 Definimos la función de evaluación (Ejemplo: buscar el máximo de una parábola)
def funcion_evaluacion(x):
    return -(x - 3) ** 2 + 10  # Función con máximo en x = 3

# 🔹 Función para generar vecinos cercanos
def generar_vecinos(x):
    return [x + random.uniform(-1, 1) for _ in range(5)]  # Generamos 5 vecinos cercanos

# 🔹 Ejecutamos la Búsqueda de Haz Local con 3 soluciones iniciales
mejor_solucion, mejor_valor = busqueda_haz_local(funcion_evaluacion, generar_vecinos, k=3)

# 🔹 Mostramos los resultados
print(f"Mejor solución encontrada: x = {mejor_solucion}")
print(f"Valor óptimo: f(x) = {mejor_valor}")
