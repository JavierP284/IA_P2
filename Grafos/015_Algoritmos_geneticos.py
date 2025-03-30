import random

# 🔹 Definimos la función de aptitud (Ejemplo: Maximizar f(x) = x^2)
def funcion_aptitud(x):
    return x ** 2

# 🔹 Creamos la población inicial aleatoria
def crear_poblacion(tamano, rango_min, rango_max):
    return [random.randint(rango_min, rango_max) for _ in range(tamano)]

# 🔹 Selección de padres (Ruleta)
def seleccion_ruleta(poblacion):
    total_aptitud = sum(funcion_aptitud(ind) for ind in poblacion)
    seleccion = random.uniform(0, total_aptitud)
    acumulado = 0
    for ind in poblacion:
        acumulado += funcion_aptitud(ind)
        if acumulado >= seleccion:
            return ind

# 🔹 Cruza de dos individuos (Promedio simple)
def cruzar(padre1, padre2):
    return (padre1 + padre2) // 2  # Se toma el promedio como descendencia

# 🔹 Mutación (Pequeño cambio aleatorio con validación de rango)
def mutar(individuo, prob_mutacion=0.1, rango_min=-10, rango_max=10):
    if random.random() < prob_mutacion:
        individuo += random.randint(-3, 3)  # Se modifica ligeramente
        # Validamos que el individuo esté dentro del rango permitido
        individuo = max(rango_min, min(individuo, rango_max))
    return individuo

# 🔹 Algoritmo Genético Principal (con parámetros ajustables)
def algoritmo_genetico(tamano_poblacion=10, generaciones=20, rango_min=-10, rango_max=10):
    poblacion = crear_poblacion(tamano_poblacion, rango_min, rango_max)  # Inicializamos
    
    for _ in range(generaciones):
        nueva_poblacion = []
        for _ in range(tamano_poblacion):
            padre1 = seleccion_ruleta(poblacion)
            padre2 = seleccion_ruleta(poblacion)
            hijo = cruzar(padre1, padre2)
            hijo = mutar(hijo, rango_min=rango_min, rango_max=rango_max)  # Aplicamos mutación
            nueva_poblacion.append(hijo)
        
        poblacion = nueva_poblacion  # Reemplazamos con la nueva generación

    mejor_solucion = max(poblacion, key=funcion_aptitud)  # Escogemos el mejor individuo
    return mejor_solucion, funcion_aptitud(mejor_solucion)

# 🔹 Ejecutamos el algoritmo genético
mejor_x, mejor_y = algoritmo_genetico()

# 🔹 Mostramos el resultado
print(f"Mejor solución encontrada: x = {mejor_x}")
print(f"Valor óptimo: f(x) = {mejor_y}")
