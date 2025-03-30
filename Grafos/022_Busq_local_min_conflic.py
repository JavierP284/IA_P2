import random

def contar_conflictos(tablero, fila, columna):
    """
    Cuenta cuántas reinas atacan a la posición dada en el tablero.
    """
    conflictos = 0
    N = len(tablero)

    for i in range(N):
        if i == fila:
            continue  # No comparar con sí misma

        # Verificar si hay otra reina en la misma columna
        if tablero[i] == columna:
            conflictos += 1
        
        # Verificar diagonales
        if abs(i - fila) == abs(tablero[i] - columna):
            conflictos += 1
    
    return conflictos

def encontrar_menor_conflicto(tablero, fila):
    """
    Encuentra la columna con el menor número de conflictos para la fila dada.
    """
    N = len(tablero)
    min_conflictos = float('inf')
    mejores_columnas = []

    for columna in range(N):
        conflictos = contar_conflictos(tablero, fila, columna)
        
        if conflictos < min_conflictos:
            min_conflictos = conflictos
            mejores_columnas = [columna]
        elif conflictos == min_conflictos:
            mejores_columnas.append(columna)

    return random.choice(mejores_columnas)  # Elegir una aleatoria si hay empate

def minimos_conflictos(N, max_intentos=1000):
    """
    Algoritmo de búsqueda local por Mínimos-Conflictos para el problema de las N reinas.
    """
    # Paso 1: Generar una solución inicial aleatoria
    tablero = [random.randint(0, N - 1) for _ in range(N)]
    
    for _ in range(max_intentos):
        # Contar conflictos en cada fila
        conflictos = [contar_conflictos(tablero, fila, tablero[fila]) for fila in range(N)]

        # Si no hay conflictos, hemos encontrado la solución
        if sum(conflictos) == 0:
            return tablero

        # Seleccionar una reina con conflictos al azar
        filas_con_conflictos = [fila for fila in range(N) if conflictos[fila] > 0]
        fila_elegida = random.choice(filas_con_conflictos)

        # Mover la reina a la columna con menos conflictos
        tablero[fila_elegida] = encontrar_menor_conflicto(tablero, fila_elegida)

    return None  # No se encontró solución en el número de intentos

# Definir el tamaño del tablero
N = 8  # Puedes cambiar este valor para probar con otros tamaños de tablero

# Ejecutar el algoritmo
solucion = minimos_conflictos(N)

# Mostrar el resultado
if solucion:
    print("Solución encontrada:")
    for fila in range(N):
        print(" ".join("Q" if solucion[fila] == col else "." for col in range(N)))
else:
    print("No se encontró solución dentro del límite de intentos.")
