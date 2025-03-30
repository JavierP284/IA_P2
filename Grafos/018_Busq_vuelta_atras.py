def es_valido(tablero, fila, columna, n):
    """
    Verifica si es seguro colocar una reina en la posición (fila, columna) del tablero.
    """
    # Verificar la columna
    for i in range(fila):
        if tablero[i] == columna:
            return False
    
    # Verificar la diagonal izquierda
    for i, j in zip(range(fila - 1, -1, -1), range(columna - 1, -1, -1)):
        if tablero[i] == j:
            return False
    
    # Verificar la diagonal derecha
    for i, j in zip(range(fila - 1, -1, -1), range(columna + 1, n)):
        if tablero[i] == j:
            return False
    
    return True


def resolver_n_reinas(tablero, fila, n):
    """
    Algoritmo de vuelta atrás (Backtracking) para resolver el problema de las N reinas.
    """
    if fila == n:
        soluciones.append(tablero[:])  # Guardamos una copia de la solución encontrada
        return
    
    for columna in range(n):
        if es_valido(tablero, fila, columna, n):
            tablero[fila] = columna  # Colocamos la reina
            resolver_n_reinas(tablero, fila + 1, n)  # Llamada recursiva para la siguiente fila
            tablero[fila] = -1  # Retrocedemos (backtracking)


def imprimir_soluciones(soluciones, n):
    """
    Muestra todas las soluciones del problema de las N reinas en formato de tablero.
    """
    for sol in soluciones:
        print("Solución:")
        for i in range(n):
            fila = ["Q " if j == sol[i] else ". " for j in range(n)]
            print("".join(fila))
        print("\n")


def main():
    # Número de reinas
    n = 5  # Puedes cambiar el valor para resolver con más reinas
    global soluciones
    soluciones = []  # Lista para almacenar las soluciones
    resolver_n_reinas([-1] * n, 0, n)

    # Imprimir las soluciones encontradas
    imprimir_soluciones(soluciones, n)


if __name__ == "__main__":
    main()
