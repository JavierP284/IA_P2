# Analizador sintáctico mejorado para expresiones aritméticas con soporte para paréntesis y más operadores

# Clase para representar un token
class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo  # Tipo del token: NUMBER, OPERATOR o PARENTHESIS
        self.valor = valor  # Valor del token (por ejemplo, un número o un operador)

    def __repr__(self):
        # Representación legible del token para depuración
        return f"{self.tipo}:{self.valor}"

# Función léxica para dividir la entrada en tokens
def lexer(input_string):
    """
    Convierte una cadena de entrada en una lista de tokens.
    """
    tokens = []  # Lista para almacenar los tokens generados
    i = 0  # Índice actual en la cadena de entrada

    while i < len(input_string):
        char = input_string[i]  # Carácter actual

        if char.isspace():
            # Ignorar espacios en blanco
            i += 1
            continue

        if char.isdigit():
            # Detectar números
            num = ''
            while i < len(input_string) and input_string[i].isdigit():
                num += input_string[i]
                i += 1
            tokens.append(Token("NUMBER", int(num)))  # Agregar token de tipo NUMBER
        elif char in "+-*/":
            # Detectar operadores
            tokens.append(Token("OPERATOR", char))  # Agregar token de tipo OPERATOR
            i += 1
        elif char in "()":
            # Detectar paréntesis
            tokens.append(Token("PARENTHESIS", char))  # Agregar token de tipo PARENTHESIS
            i += 1
        else:
            # Manejar caracteres inválidos
            raise Exception(f"Carácter inválido: {char}")

    return tokens  # Retornar la lista de tokens

# Clase del analizador sintáctico
class Parser:
    def __init__(self, tokens):
        """
        Inicializa el analizador con una lista de tokens.
        """
        self.tokens = tokens  # Lista de tokens a analizar
        self.pos = 0  # Posición actual en la lista de tokens

    def current_token(self):
        """
        Retorna el token actual en la posición actual.
        """
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None  # Retorna None si no hay más tokens

    def advance(self):
        """
        Avanza al siguiente token en la lista.
        """
        self.pos += 1

    # Analiza una expresión completa
    def parse_expr(self):
        """
        Analiza una expresión completa, que puede incluir términos separados por operadores '+' o '-'.
        """
        if not self.parse_term():
            return False  # Si no se puede analizar un término, la expresión no es válida

        # Mientras haya operadores '+' o '-' después de un término
        while self.current_token() and self.current_token().tipo == "OPERATOR" and self.current_token().valor in "+-":
            self.advance()  # Avanzar al operador
            if not self.parse_term():
                return False  # Si no hay un término válido después del operador, error de sintaxis

        return True  # La expresión es válida

    # Analiza un término (maneja multiplicación y división)
    def parse_term(self):
        """
        Analiza un término, que puede incluir factores separados por operadores '*' o '/'.
        """
        if not self.parse_factor():
            return False  # Si no se puede analizar un factor, el término no es válido

        # Mientras haya operadores '*' o '/' después de un factor
        while self.current_token() and self.current_token().tipo == "OPERATOR" and self.current_token().valor in "*/":
            self.advance()  # Avanzar al operador
            if not self.parse_factor():
                return False  # Si no hay un factor válido después del operador, error de sintaxis

        return True  # El término es válido

    # Analiza un factor (maneja números y paréntesis)
    def parse_factor(self):
        """
        Analiza un factor, que puede ser un número o una expresión entre paréntesis.
        """
        token = self.current_token()  # Obtener el token actual

        if token and token.tipo == "NUMBER":
            # Si el token es un número, avanzar y retornar True
            self.advance()
            return True
        elif token and token.tipo == "PARENTHESIS" and token.valor == "(":
            # Si el token es un paréntesis de apertura, analizar la expresión dentro
            self.advance()  # Avanzar después del '('
            if not self.parse_expr():
                return False  # Si la expresión dentro no es válida, error de sintaxis
            if self.current_token() and self.current_token().tipo == "PARENTHESIS" and self.current_token().valor == ")":
                # Verificar que haya un paréntesis de cierre
                self.advance()  # Avanzar después del ')'
                return True
            else:
                raise Exception("Falta un paréntesis de cierre")  # Error si falta ')'
        return False  # Si no es un número ni un paréntesis, el factor no es válido

# Prueba del analizador
input_str = "(3 + 5) * 2 - 8 / 4"  # Cadena de entrada a analizar
tokens = lexer(input_str)  # Generar tokens a partir de la cadena

print("Tokens:", tokens)  # Mostrar los tokens generados

parser = Parser(tokens)  # Crear una instancia del analizador con los tokens

# Verificar si la expresión es válida sintácticamente
if parser.parse_expr():
    print("La expresión es sintácticamente válida.")
else:
    print("Error de sintaxis.")
