import itertools  # Biblioteca para generar combinaciones de valores booleanos

# Expresiones lógicas precargadas (usa operadores válidos de Python: and, or, not)
expr1 = "(p and q) or r"  # Primera expresión lógica
expr2 = "(p or r) and (q or r)"  # Segunda expresión lógica

# Variables involucradas en las expresiones
variables = ['p', 'q', 'r']  # Lista de variables booleanas usadas en las expresiones

# Función para evaluar una expresión lógica con un conjunto de valores de variables
def evaluar(expresion, valores):
    """
    Evalúa una expresión lógica usando un contexto seguro.
    :param expresion: La expresión lógica como cadena.
    :param valores: Un diccionario con los valores de las variables (ej. {'p': True, 'q': False}).
    :return: El resultado booleano de evaluar la expresión.
    """
    return eval(expresion, {}, valores)  # Evalúa la expresión usando el diccionario 'valores'

# Función para generar y mostrar la tabla de verdad de una expresión lógica
def tabla_verdad(variables, expr):
    """
    Genera y muestra la tabla de verdad para una expresión lógica.
    :param variables: Lista de variables involucradas en la expresión.
    :param expr: La expresión lógica como cadena.
    :return: Una lista de tuplas con las combinaciones de valores y sus resultados.
    """
    print(f"\nTabla de verdad para: {expr}")
    # Encabezado de la tabla
    print(" | ".join(variables) + " | Resultado")
    print("-" * (len(variables) * 4 + 11))  # Línea separadora

    resultados = []  # Lista para almacenar los resultados de cada combinación
    # Genera todas las combinaciones posibles de valores booleanos para las variables
    for combinacion in itertools.product([False, True], repeat=len(variables)):
        # Crea un diccionario que asocia cada variable con su valor en la combinación actual
        valores = dict(zip(variables, combinacion))
        # Evalúa la expresión lógica con los valores actuales
        resultado = evaluar(expr, valores)
        # Convierte los valores booleanos a 1 (True) o 0 (False) para mostrarlos en la tabla
        valores_str = " | ".join(["1" if v else "0" for v in combinacion])
        # Imprime la fila de la tabla con los valores y el resultado
        print(f"{valores_str} |    {'1' if resultado else '0'}")
        # Almacena la combinación y el resultado en la lista de resultados
        resultados.append((valores, resultado))
    return resultados  # Devuelve la lista de resultados

# Mostrar las tablas de verdad para ambas expresiones
tabla1 = tabla_verdad(variables, expr1)  # Tabla de verdad para expr1
tabla2 = tabla_verdad(variables, expr2)  # Tabla de verdad para expr2

# Equivalencia: Compara los resultados de ambas tablas para verificar si son iguales
equivalentes = all(f1[1] == f2[1] for f1, f2 in zip(tabla1, tabla2))
print(f"\n¿Son equivalentes? {'Sí' if equivalentes else 'No'}")  # Muestra si son equivalentes

# Validez: Verifica si la expresión es siempre verdadera (válida)
valida_expr1 = all(f[1] for f in tabla1)  # Expr1 es válida si todos los resultados son True
valida_expr2 = all(f[1] for f in tabla2)  # Expr2 es válida si todos los resultados son True
print("\n¿Es válida cada expresión?")
print(f"- Expr1: {'Sí' if valida_expr1 else 'No'}")  # Muestra si expr1 es válida
print(f"- Expr2: {'Sí' if valida_expr2 else 'No'}")  # Muestra si expr2 es válida

# Satisfacibilidad: Verifica si al menos una combinación de valores hace verdadera la expresión
satisface_expr1 = any(f[1] for f in tabla1)  # Expr1 es satisfacible si algún resultado es True
satisface_expr2 = any(f[1] for f in tabla2)  # Expr2 es satisfacible si algún resultado es True
print("\n¿Es satisfacible cada expresión?")
print(f"- Expr1: {'Sí' if satisface_expr1 else 'No'}")  # Muestra si expr1 es satisfacible
print(f"- Expr2: {'Sí' if satisface_expr2 else 'No'}")  # Muestra si expr2 es satisfacible
