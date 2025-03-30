import random

def busqueda_tabu(funcion_evaluacion, generar_vecinos, estado_inicial, max_iter=100, tamano_tabu=5):
    """
    Implementación de la Búsqueda Tabú.
    
    - funcion_evaluacion: Función que evalúa la calidad de una solución.
    - generar_vecinos: Función que genera estados vecinos.
    - estado_inicial: Estado de inicio.
    - max_iter: Máximo de iteraciones.
    - tamano_tabu: Cantidad máxima de elementos en la lista tabú.
    
    Retorna la mejor solución encontrada.
    """
    estado_actual = estado_inicial  # Se establece el estado inicial
    mejor_estado = estado_actual  # Se guarda la mejor solución encontrada
    mejor_valor = funcion_evaluacion(estado_actual)  # Se evalúa la solución inicial

    lista_tabu = []  # Lista tabú para evitar ciclos

    for _ in range(max_iter):  # Se itera hasta el máximo de iteraciones
        vecinos = generar_vecinos(estado_actual)  # Se generan vecinos del estado actual

        # Se filtran vecinos que no están en la lista tabú
        vecinos = [v for v in vecinos if v not in lista_tabu]

        if not vecinos:
            break  # Si no hay vecinos válidos, se detiene la búsqueda

        # Se selecciona el mejor vecino disponible
        estado_siguiente = max(vecinos, key=funcion_evaluacion)
        valor_siguiente = funcion_evaluacion(estado_siguiente)

        # Se actualiza la mejor solución encontrada
        if valor_siguiente > mejor_valor:
            mejor_estado = estado_siguiente
            mejor_valor = valor_siguiente

        # Se mueve al siguiente estado
        estado_actual = estado_siguiente

        # Se actualiza la lista tabú
        if estado_actual not in lista_tabu:  # Evitar duplicados
            lista_tabu.append(estado_actual)
        if len(lista_tabu) > tamano_tabu:  # Se mantiene un tamaño limitado
            lista_tabu.pop(0)

    return mejor_estado, mejor_valor  # Se retorna la mejor solución encontrada

# 🔹 Definimos la función de evaluación (Ejemplo: buscar el máximo de una parábola)
def funcion_evaluacion(x):
    return -(x - 3) ** 2 + 10  # Función con máximo en x = 3

# 🔹 Función para generar vecinos cercanos
def generar_vecinos(x):
    return [x - 0.1, x + 0.1]  # Pequeños cambios en x

# 🔹 Estado inicial aleatorio
estado_inicial = random.uniform(-10, 10)

# 🔹 Ejecutamos la Búsqueda Tabú
mejor_solucion, mejor_valor = busqueda_tabu(funcion_evaluacion, generar_vecinos, estado_inicial)

# 🔹 Mostramos los resultados
print(f"Mejor solución encontrada: x = {mejor_solucion}")
print(f"Valor óptimo: f(x) = {mejor_valor}")
