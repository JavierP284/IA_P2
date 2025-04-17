# Algoritmo de backtracking para resolver el problema de las N reinas

# Función para imprimir el tablero de manera visual
def imprimir_tablero(tablero):
    """
    Imprime el tablero de ajedrez con las posiciones de las reinas.
    Una 'Q' representa una reina, y un '.' representa una celda vacía.
    """
    for fila in tablero:
        # Convertir cada fila en una cadena con 'Q' para reinas y '.' para celdas vacías
        print(" ".join("Q" if celda else "." for celda in fila))
    # Imprimir una línea divisoria para separar soluciones
    print("-" * (len(tablero) * 2))

# Función para verificar si se puede colocar una reina en (fila, col)
def es_seguro(tablero, fila, col):
    """
    Verifica si es seguro colocar una reina en la posición (fila, col).
    Se revisan tres condiciones:
    1. Que no haya otra reina en la misma columna.
    2. Que no haya otra reina en la diagonal superior izquierda.
    3. Que no haya otra reina en la diagonal superior derecha.
    """
    # Verificar si hay una reina en la misma columna
    for i in range(fila):
        if tablero[i][col] == 1:
            return False

    # Verificar la diagonal superior izquierda
    i, j = fila - 1, col - 1
    while i >= 0 and j >= 0:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Verificar la diagonal superior derecha
    i, j = fila - 1, col + 1
    while i >= 0 and j < len(tablero):
        if tablero[i][j] == 1:
            return False
        i -= 1
        j += 1

    # Si pasa todas las verificaciones, es seguro colocar la reina
    return True

# Función recursiva que resuelve el problema usando backtracking
def resolver_reinas(tablero, fila, soluciones):
    """
    Resuelve el problema de las N reinas utilizando backtracking.
    Intenta colocar una reina en cada fila y retrocede si no es posible.
    """
    # Caso base: si todas las reinas han sido colocadas
    if fila == len(tablero):
        # Guardar una copia del tablero actual como solución
        soluciones.append([fila[:] for fila in tablero])
        # Imprimir la solución encontrada
        imprimir_tablero(tablero)
        return

    # Intentar colocar una reina en cada columna de la fila actual
    for col in range(len(tablero)):
        # Verificar si es seguro colocar una reina en (fila, col)
        if es_seguro(tablero, fila, col):
            # Colocar la reina en la posición (fila, col)
            tablero[fila][col] = 1
            # Llamada recursiva para intentar colocar la siguiente reina
            resolver_reinas(tablero, fila + 1, soluciones)
            # Retroceso: quitar la reina de la posición (fila, col)
            tablero[fila][col] = 0

# Función principal
def problema_reinas():
    """
    Función principal que solicita al usuario el tamaño del tablero,
    inicializa el tablero y encuentra todas las soluciones al problema
    de las N reinas.
    """
    # Solicitar al usuario el tamaño del tablero
    N = int(input("Ingrese el tamaño del tablero (N): "))
    # Crear un tablero vacío de tamaño NxN
    tablero_inicial = [[0 for _ in range(N)] for _ in range(N)]
    # Lista para almacenar todas las soluciones encontradas
    soluciones = []

    # Mensaje inicial
    print(f"\nBuscando soluciones para el problema de las {N} reinas...\n")
    # Llamar a la función recursiva para resolver el problema
    resolver_reinas(tablero_inicial, 0, soluciones)

    # Mostrar el resultado final
    if not soluciones:
        # Si no se encontraron soluciones
        print("No se encontró ninguna solución.")
    else:
        # Mostrar el número total de soluciones encontradas
        print(f"Se encontraron {len(soluciones)} soluciones.")

# Ejecutar el programa
if __name__ == "__main__":
    """
    Punto de entrada del programa. Llama a la función principal para resolver
    el problema de las N reinas.
    """
    problema_reinas()
