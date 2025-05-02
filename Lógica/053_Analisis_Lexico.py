# Analizador léxico mejorado en Python

# Lista de palabras clave reservadas
# Estas son palabras que tienen un significado especial en el lenguaje que se está analizando.
keywords = {"if", "else", "while", "return", "int", "float"}

# Función para verificar si un carácter es una letra
# Esto incluye letras del alfabeto y el carácter de subrayado (_), que es común en identificadores.
def is_letter(char):
    return char.isalpha() or char == '_'

# Función para verificar si un carácter es un dígito
# Esto se utiliza para identificar números en el código fuente.
def is_digit(char):
    return char.isdigit()

# Función principal del analizador léxico
# Esta función toma una cadena de entrada (el código fuente) y la analiza para generar una lista de tokens.
def lexer(input_string):
    tokens = []     # Lista donde se almacenarán los tokens encontrados
    i = 0           # Índice para recorrer la cadena de entrada

    # Bucle principal para recorrer cada carácter de la cadena de entrada
    while i < len(input_string):
        char = input_string[i]  # Obtener el carácter actual

        # Ignorar espacios en blanco (como espacios, tabulaciones y saltos de línea)
        if char.isspace():
            i += 1
            continue

        # Ignorar comentarios de una línea (que comienzan con "//")
        if char == '/' and i + 1 < len(input_string) and input_string[i + 1] == '/':
            # Avanzar hasta el final de la línea o hasta que se termine la cadena
            while i < len(input_string) and input_string[i] != '\n':
                i += 1
            continue

        # Ignorar comentarios de múltiples líneas (que comienzan con "/*" y terminan con "*/")
        if char == '/' and i + 1 < len(input_string) and input_string[i + 1] == '*':
            i += 2  # Saltar los caracteres "/*"
            # Avanzar hasta encontrar el cierre del comentario "*/"
            while i < len(input_string) and not (input_string[i] == '*' and i + 1 < len(input_string) and input_string[i + 1] == '/'):
                i += 1
            i += 2  # Saltar los caracteres "*/"
            continue

        # Identificar palabras clave o identificadores
        # Una palabra clave es una palabra reservada, mientras que un identificador es un nombre definido por el usuario.
        if is_letter(char):
            start = i  # Marcar el inicio de la palabra
            # Continuar mientras el carácter sea una letra o un dígito
            while i < len(input_string) and (is_letter(input_string[i]) or is_digit(input_string[i])):
                i += 1
            word = input_string[start:i]  # Extraer la palabra completa
            # Verificar si la palabra es una palabra clave
            if word in keywords:
                tokens.append(("KEYWORD", word))  # Agregar como palabra clave
            else:
                tokens.append(("IDENTIFIER", word))  # Agregar como identificador

        # Identificar números
        elif is_digit(char):
            start = i  # Marcar el inicio del número
            # Continuar mientras el carácter sea un dígito
            while i < len(input_string) and is_digit(input_string[i]):
                i += 1
            number = input_string[start:i]  # Extraer el número completo
            tokens.append(("NUMBER", number))  # Agregar como número

        # Identificar operadores compuestos y simples
        elif char in "+-*/=<>":
            # Verificar si es un operador compuesto (como <=, >=, ==, !=)
            if i + 1 < len(input_string) and input_string[i:i+2] in {"<=", ">=", "==", "!="}:
                tokens.append(("OPERATOR", input_string[i:i+2]))  # Agregar como operador compuesto
                i += 2  # Saltar ambos caracteres
            else:
                tokens.append(("OPERATOR", char))  # Agregar como operador simple
                i += 1

        # Identificar cadenas de texto (delimitadas por comillas dobles)
        elif char == '"':
            start = i  # Marcar el inicio de la cadena
            i += 1  # Saltar la comilla inicial
            # Continuar hasta encontrar la comilla de cierre
            while i < len(input_string) and input_string[i] != '"':
                i += 1
            i += 1  # Incluir la comilla de cierre
            string = input_string[start:i]  # Extraer la cadena completa
            tokens.append(("STRING", string))  # Agregar como cadena de texto

        # Carácter no reconocido
        # Si el carácter no pertenece a ninguna categoría conocida, se marca como "UNKNOWN".
        else:
            tokens.append(("UNKNOWN", char))
            i += 1

    return tokens  # Devolver la lista de tokens encontrados

# Prueba del analizador léxico
# Este es un ejemplo de código fuente que se analizará.
code = """
int x = 10 + 20;
// Esto es un comentario
if (x >= 15) {
    x = x - 5;
    /* Comentario
       de múltiples líneas */
    return "Resultado";
}
"""

# Llamar a la función lexer para analizar el código de prueba
tokens = lexer(code)

# Mostrar los tokens encontrados en un formato tabular
print("{:<15} {:<15}".format("Tipo", "Valor"))
print("-" * 30)
for token in tokens:
    print("{:<15} {:<15}".format(token[0], token[1]))
