# Análisis Semántico básico: Verifica declaraciones y usos de variables

# Simula una tabla de símbolos (almacena las variables declaradas y sus tipos)
# La tabla de símbolos es un diccionario donde las claves son los nombres de las variables
# y los valores son los tipos de datos asociados a esas variables.
symbol_table = {}

# Lista de instrucciones simuladas (ya analizadas léxica y sintácticamente)
# Cada instrucción es una tupla con el formato:
# (tipo_de_instruccion, nombre_variable, valor_o_tipo)
instructions = [
    ("declare", "x", "int"),        # Declaración válida: se declara la variable 'x' como entero
    ("assign", "x", 10),            # Asignación válida: se asigna el valor 10 a 'x'
    ("assign", "y", 5),             # Error: 'y' no fue declarada previamente
    ("declare", "z", "int"),        # Declaración válida: se declara la variable 'z' como entero
    ("assign", "z", "hello"),       # Error: tipo incorrecto, se esperaba un entero para 'z'
    ("declare", "w", "string"),     # Declaración válida: se declara la variable 'w' como cadena
    ("assign", "w", "world"),       # Asignación válida: se asigna la cadena "world" a 'w'
    ("assign", "w", 123),           # Error: tipo incorrecto, se esperaba una cadena para 'w'
]

# Función para validar el tipo de valor asignado
# Esta función verifica si el valor proporcionado coincide con el tipo esperado.
def validate_type(expected_type, value):
    if expected_type == "int":
        # Verifica si el valor es un entero
        return isinstance(value, int)
    elif expected_type == "string":
        # Verifica si el valor es una cadena
        return isinstance(value, str)
    elif expected_type == "float":
        # Verifica si el valor es un número de punto flotante
        return isinstance(value, float)
    else:
        # Si el tipo esperado no es reconocido, retorna False
        return False

# Función que realiza el análisis semántico
# Esta función recorre las instrucciones y verifica que sean válidas semánticamente.
def semantic_analysis(instructions):
    errors = []  # Lista para acumular los errores encontrados durante el análisis

    # Itera sobre cada instrucción en la lista
    for instr in instructions:
        action = instr[0]  # Tipo de instrucción: "declare" o "assign"
        var = instr[1]     # Nombre de la variable involucrada

        if action == "declare":
            # Si la instrucción es "declare", se espera un tipo de dato como tercer elemento
            tipo = instr[2]
            if var in symbol_table:
                # Si la variable ya fue declarada, se agrega un error
                errors.append(f"Error: Variable '{var}' ya fue declarada.")
            else:
                # Si no fue declarada, se agrega a la tabla de símbolos con su tipo
                symbol_table[var] = tipo

        elif action == "assign":
            # Si la instrucción es "assign", se espera un valor como tercer elemento
            valor = instr[2]
            if var not in symbol_table:
                # Si la variable no está en la tabla de símbolos, se agrega un error
                errors.append(f"Error: Variable '{var}' no declarada.")
            else:
                # Si la variable está declarada, se verifica que el tipo del valor sea correcto
                tipo_esperado = symbol_table[var]
                if not validate_type(tipo_esperado, valor):
                    # Si el tipo no coincide, se agrega un error
                    errors.append(f"Error: Se esperaba un valor de tipo '{tipo_esperado}' para '{var}', pero se asignó {type(valor).__name__}.")

    # Mostrar los resultados del análisis
    if errors:
        # Si hay errores, se imprimen todos
        print("Se encontraron errores semánticos:")
        for error in errors:
            print("  -", error)
    else:
        # Si no hay errores, se indica que el análisis fue exitoso
        print("Análisis semántico exitoso. No hay errores.")

# Ejecutar el análisis semántico con la lista de instrucciones proporcionada
semantic_analysis(instructions)
