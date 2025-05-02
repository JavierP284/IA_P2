# Simulador de una Gramática Causal Definida
# Gramática:
#   S → aSb | ε
# Esta gramática genera cadenas que comienzan con una cantidad igual de 'a' y terminan con la misma cantidad de 'b'.
# La producción ε (cadena vacía) permite terminar la recursión.

import random

# Reglas de producción de la gramática (definidas como un diccionario)
# Cada clave es un símbolo no terminal, y su valor es una lista de posibles producciones.
grammar = {
    "S": ["aSb", ""]  # El símbolo 'S' puede expandirse a "aSb" o a la cadena vacía (ε).
}

def set_random_seed(seed=None):
    """
    Establece una semilla para el generador aleatorio.
    Esto permite que los resultados sean reproducibles si se usa la misma semilla.
    
    Args:
        seed (int, opcional): Valor de la semilla. Si es None, no se establece ninguna semilla.
    """
    if seed is not None:
        random.seed(seed)  # Configura la semilla para el generador aleatorio.

def generate(symbol, depth=0):
    """
    Genera una cadena a partir de un símbolo no terminal de forma recursiva.
    
    Args:
        symbol (str): El símbolo no terminal que se desea expandir.
        depth (int): Nivel de profundidad de la recursión (usado para depuración y visualización).
    
    Returns:
        str: Cadena generada según las reglas de la gramática.
    """
    # Si el símbolo no está en la gramática, se asume que es un símbolo terminal.
    # Los símbolos terminales se devuelven directamente.
    if symbol not in grammar:
        return symbol

    # Elegimos aleatoriamente una de las producciones asociadas al símbolo no terminal.
    production = random.choice(grammar[symbol])

    # Mostrar el paso intermedio para depuración (indica qué producción se seleccionó).
    print(f"{'  ' * depth}Expandiendo '{symbol}' → '{production}'")

    # Inicializamos la cadena resultante.
    result = ""

    # Recorremos cada carácter de la producción seleccionada.
    # Si el carácter es un símbolo no terminal, se expande recursivamente.
    # Si es un símbolo terminal, se agrega directamente al resultado.
    for char in production:
        result += generate(char, depth + 1)  # Llamada recursiva para expandir el símbolo.

    return result  # Devolvemos la cadena generada.

def main():
    """
    Función principal para generar y mostrar cadenas válidas según la gramática.
    """
    print("Cadenas generadas a partir de la gramática S → aSb | ε:\n")

    # Opcional: establecer una semilla para que los resultados sean reproducibles.
    set_random_seed(42)

    # Número de cadenas que se generarán.
    num_cadenas = 5

    # Generar y mostrar las cadenas.
    for i in range(num_cadenas):
        cadena = generate("S")  # Generar una cadena a partir del símbolo inicial 'S'.
        print(f"Cadena {i+1}: '{cadena}'")  # Mostrar la cadena generada.

# Punto de entrada del programa.
if __name__ == "__main__":
    main()
