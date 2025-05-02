# Simulador que muestra ambigüedad al generar múltiples árboles sintácticos
# para una expresión usando la gramática:
# E → E + E | E - E | n

def parse_expression(tokens):
    """
    Función recursiva que genera todos los árboles sintácticos posibles
    para una lista de tokens.
    
    Parámetros:
    - tokens: Lista de tokens que representan una expresión (ejemplo: ['n', '+', 'n', '-', 'n']).
    
    Retorna:
    - Una lista de cadenas que representan todos los árboles sintácticos posibles.
    """
    trees = []  # Lista para almacenar los árboles sintácticos generados.

    # Caso base: si solo queda un token y es un número ('n'), devolvemos ese token.
    if len(tokens) == 1 and tokens[0] == 'n':
        return ['n']

    # Recorremos todos los posibles lugares para dividir la expresión.
    # Nos aseguramos de que el índice sea un operador (índices impares).
    for i in range(1, len(tokens) - 1, 2):
        operador = tokens[i]  # Obtenemos el operador actual ('+' o '-').

        # Verificamos si el token actual es un operador válido.
        if operador in ['+', '-']:
            # Dividimos la expresión en dos partes: izquierda y derecha.
            izquierda = tokens[:i]  # Tokens antes del operador.
            derecha = tokens[i+1:]  # Tokens después del operador.

            # Llamadas recursivas para generar árboles de las subexpresiones.
            arboles_izq = parse_expression(izquierda)  # Árboles para la parte izquierda.
            arboles_der = parse_expression(derecha)    # Árboles para la parte derecha.

            # Combinamos todos los árboles posibles de izquierda y derecha.
            for izq in arboles_izq:
                for der in arboles_der:
                    # Creamos un nuevo árbol combinando las subexpresiones con el operador.
                    trees.append(f'({izq} {operador} {der})')

    # Retornamos la lista de árboles generados.
    return trees

def main():
    """
    Función principal que ejecuta el simulador.
    """
    # Mensaje inicial explicando el propósito del programa.
    print("Simulador de Ambigüedad en Gramáticas")
    print("Gramática utilizada:")
    print("E → E + E | E - E | n\n")

    # Solicitar al usuario que ingrese una expresión en un formato específico.
    expresion = input("Ingrese una expresión en formato 'n operador n operador n' (ejemplo: n + n - n): ")
    tokens = expresion.split()  # Dividimos la entrada en tokens separados por espacios.

    # Validación de los tokens ingresados por el usuario.
    operadores_validos = {'+', '-'}  # Conjunto de operadores válidos.
    # Verificamos que:
    # - La cantidad de tokens sea impar (número, operador, número, ...).
    # - Los tokens en posiciones pares sean 'n'.
    # - Los tokens en posiciones impares sean operadores válidos.
    if len(tokens) % 2 == 0 or not all(
        token == 'n' if i % 2 == 0 else token in operadores_validos
        for i, token in enumerate(tokens)
    ):
        print("Error: La expresión ingresada no es válida.")  # Mensaje de error si la validación falla.
        return

    # Generar todos los árboles sintácticos posibles para la expresión ingresada.
    resultados = parse_expression(tokens)

    # Mostrar los resultados al usuario.
    print("\nÁrboles sintácticos posibles para la expresión ingresada:\n")
    for i, arbol in enumerate(resultados, 1):
        # Enumeramos y mostramos cada árbol generado.
        print(f"Árbol {i}: {arbol}")

# Punto de entrada del programa.
if __name__ == "__main__":
    main()